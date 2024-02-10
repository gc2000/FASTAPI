from fastapi import FastAPI, Response, HTTPException, status
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2, time
from psycopg2.extras import RealDictCursor

class Post (BaseModel):
    title: str
    content: str
    author: str

while True:
    try: 
        conn = psycopg2.connect(host="postgres", dbname="db1", port="5432",user="postgres", password="postgres", cursor_factory=RealDictCursor)
        cur = conn.cursor()
        print("Database connection was successful!")
        break
    except Exception as error:
        print ("Conntion failed")
        print ("Error:", error)
        time.sleep(2)


app = FastAPI()


@app.get("/posts")
def get_posts():
        cur.execute("SELECT * FROM posts")
        posts = cur.fetchall()
        return (posts)
    
@app.get("/posts/{id}")
def get_posts_by_id(id: int):
    try:
        cur.execute("""SELECT * FROM posts where id=%s """, (str(id),))
        fetched_post = cur.fetchone()
    
        if fetched_post is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")

        return {"data": fetched_post}
    
    except (psycopg2.Error) as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

@app.post("/posts")
def insert_posts(post: Post):
    try:
        postgres_insert_query = """INSERT INTO posts (title, content, author) VALUES (%s,%s,%s) RETURNING * """
        record_to_insert = (post.title, post.content, post.author,)
        cur.execute(postgres_insert_query, record_to_insert)
        conn.commit()
        
        new_post = cur.fetchone()
        return {"message": new_post}
    except (psycopg2.Error) as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.put("/posts/{id}", status_code = status.HTTP_201_CREATED)
def update_posts_by_id(id: int, updated_data: dict):
    try:
        update_statement = "UPDATE Posts SET "
        update_statement += ", ".join([f"{key} = %s" for key in updated_data.keys()])
        update_statement += " WHERE id = %s RETURNING *"

        # Extract values from updated_data and create tuple for parameters
        values = list(updated_data.values())
        values.append(id)
        
        # Execute the update statement with the parameters
        cur.execute(update_statement, tuple(values))
        # Commit the transaction
        conn.commit()
        updated_post = cur.fetchone()
    
        return {"message": updated_post}
    
    except (psycopg2.Error) as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts_by_id(id: int):
    try:
        cur.execute("""DELETE FROM posts where id=%s RETURNING * """, (str(id),))
        deleted_post = cur.fetchone()
        conn.commit()
        if deleted_post is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except (psycopg2.Error) as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")