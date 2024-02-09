from fastapi import FastAPI, Response, status, HTTPException
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
        cur.execute("""SELECT * FROM posts where id=%s""", (id,))
        post = cur.fetchone()
    
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")

        return {"id": post[0], "title": post[1], "content": post[2]}
    
    except (psycopg2.Error, Exception) as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

@app.post("/posts")
def insert_posts(post: Post):
    try:
        postgres_insert_query = """INSERT INTO posts (title, content, author) VALUES (%s,%s,%s)"""
        record_to_insert = (post.title, post.content, post.author,)
        cur.execute(postgres_insert_query, record_to_insert)
        conn.commit()
        return {"message": "Record inserted successfully"}
    except (psycopg2.Error, Exception) as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
