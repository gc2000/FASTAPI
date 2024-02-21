1. Install pip, virtualenv, postgres
sudo apt update -y
sudo apt upgrade -y

python --version
pip --version
sudo apt install python3-pip
sudo apt install virtualenv
sudo apt install postgresql postgresql-contrib -y
psql --version

2. Configure postgres users, password
whoami
sudo cat /etc/passwd
sudo su - postgres
psql -U postgres

postgres=# \password
Enter new password for user "postgres":
Enter it again:


3. Configure pg_hba.conf and  postgresql.conf 
/etc/postgresql/14/main

postgresql.conf:
listen_addresses = '*'

pg_hba.conf:
local   all             postgres                                md5
# TYPE  DATABASE        USER            ADDRESS                 METHOD
# "local" is for Unix domain socket connections only
local   all             all                                     md5
# IPv4 local connections:
host    all             all             0.0.0.0/0               md5
# IPv6 local connections:
host    all             all             ::/0                    md5


Restart postgresql:
sudo systemctl restart postgresql

4. Make sure the firewall is open. for Linux1, Iptables is used for all incoming ports. 5432 is blocked by default.
Apply the following:
sudo iptables -I INPUT -p tcp --dport 8890 -j ACCEPT

5. Test the connection
telnet xxx.xxx.xxx.xxx 5432
pgAdmin