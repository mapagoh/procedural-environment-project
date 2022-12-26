from dotenv import load_dotenv
load_dotenv()
import os
import MySQLdb
import mysql.connector

connection = mysql.connector.connect(
  host= os.getenv("HOST"),
  user=os.getenv("USERNAME"),
  passwd= os.getenv("PASSWORD"),
  db= os.getenv("DATABASE"),
  
)

cursor=connection.cursor()
cursor.execute("/queries/create/main.sql")

connection.close()
