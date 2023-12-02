import psycopg2

conn = psycopg2.connect(database="flask_crud_db", host="localhost",user="postgres",password="postgres",port="5432")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS courses (id serial PRIMARY KEY, name varchar(100),fees integer,duration integer)""")
cur.execute("""INSERT INTO courses (name,fees,duration) VALUES ('python',6500,60)""")

conn.commit()
cur.close()
conn.close()