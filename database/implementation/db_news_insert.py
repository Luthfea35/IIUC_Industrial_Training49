import os
import datetime
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_db_connection():
    
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            passwd=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )
        print("MySQL Database connection successful")
        return connection
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

def execute_query(connection, query, data=None):
    
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_category(connection, name, description):
    
    query = """
    INSERT INTO categories (name, description)
    VALUES (%s,%s)
    """
    data = (name,description)
    execute_query(connection, query, data)


def insert_author(connection, name, email):
    
    query = """
    INSERT INTO authors (name, email)
    VALUES (%s, %s)
    """
    data = (name, email)
    execute_query(connection, query, data)    

def insert_editor(connection, name, email):
    
    query = """
    INSERT INTO editors (name, email)
    VALUES (%s, %s)
    """
    data = (name, email)
    execute_query(connection, query, data)

def insert_news(connection, category_id, author_id, editor_id, datetime, title, body, link):
    
    query = """
    INSERT INTO news (category_id, author_id, editor_id, datetime, title, body, link)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    data = (category_id, author_id, editor_id, datetime, title, body, link)
    execute_query(connection, query, data)

def insert_image(connection, news_id, image_url):

    query = """
    INSERT INTO images (news_id, image_url)
    VALUES (%s, %s)
    """
    data = (news_id, image_url)
    execute_query(connection, query, data)
    
def insert_summary(connection, news_id, summary_text):
    
    query = """
    INSERT INTO summaries (news_id, summary_text)
    VALUES (%s, %s)
    """
    data = (news_id, summary_text)
    execute_query(connection, query, data)


if __name__ == "__main__":
    conn = create_db_connection()
    if conn is not None:
        #insert_category(conn, "International","All news related to World activities")
        #insert_author(conn, "Ahsanul Karim", "ahsan@gmail.com")  
        #insert_editor(conn, "Akib Mirja", "akibmirja38@gmail.com")
        """
        insert_news(conn, 2, 3, 2, "2024-03-4 17:45:00 ", "Bangladesh duo on the rise in T20 rankings",
                    A pair of experienced Bangladesh players 
                      have been rewarded for their good form against Zimbabwe by 
                      making giant strides on the latest ICC Mens T20I Player Rankings.,
                    "https://www.thedailystar.net/sports/cricket/news/bangladesh-duo-the-rise-t20-rankings-3604856")
        
        """
        #insert_image(conn, 4,"https://tds-images.thedailystar.net/sites/default/files/styles/big_202/public/images/2024/05/08/taskin-mahedi.jpg")
        
        insert_summary(conn, 4, """About T20 cup which made a big experiende of
                       Bangladeshi player""") 
        insert_summary(conn, 6, """China on Tuesday urged Israel to "stop attacking Rafah", 
                       after the Israeli army said it took "operational control" of the 
                       Palestinian side of the Rafah border crossing between Gaza and Egypt.""")
        
    