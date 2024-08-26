import os
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

def execute_query(connection, query):
    
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
   
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        return []
    

def create_tables(connection):
       
    create_categories_table = """
    CREATE TABLE IF NOT EXISTS categories (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description TEXT
    );
    """
    execute_query(connection, create_categories_table)
    
    create_authors_table = """
    CREATE TABLE IF NOT EXISTS authors (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL
    );
    """
    execute_query(connection, create_authors_table)
    
    create_editors_table = """
    CREATE TABLE IF NOT EXISTS editors (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL
    );
    """
    execute_query(connection, create_editors_table)
    
    create_news_table = """
    CREATE TABLE IF NOT EXISTS news (
        id INT AUTO_INCREMENT PRIMARY KEY,
        category_id INT,
        author_id INT,
        editor_id INT,
        datetime DATETIME,
        title VARCHAR(255) NOT NULL,
        body TEXT,
        link VARCHAR(255),
        FOREIGN KEY (category_id) REFERENCES categories (id),
        FOREIGN KEY (author_id) REFERENCES authors (id),
        FOREIGN KEY (editor_id) REFERENCES editors (id)
    );
    """
    execute_query(connection, create_news_table)
    
    create_images_table = """
    CREATE TABLE IF NOT EXISTS images (
        id INT AUTO_INCREMENT PRIMARY KEY,
        news_id INT,
        image_url VARCHAR(255),
        FOREIGN KEY (news_id) REFERENCES news (id)
    );
    """
    execute_query(connection, create_images_table)
    
    create_summaries_table = """
    CREATE TABLE IF NOT EXISTS summaries (
        id INT AUTO_INCREMENT PRIMARY KEY,
        news_id INT,
        summary_text TEXT,
        FOREIGN KEY (news_id) REFERENCES news (id)
    );
    """
    execute_query(connection, create_summaries_table)

    
if __name__ == "__main__":
    conn = create_db_connection()
    if conn is not None:
        create_tables(conn)
        read_categories_query = "SELECT * FROM categories"
        news_categories = execute_read_query(conn, read_categories_query)
        print(news_categories)
        
        read_authors_query = "SELECT * FROM authors"
        news_authors = execute_read_query(conn, read_authors_query)
        print(news_authors)
        
        read_editors_query = "SELECT * FROM editors"
        news_editors = execute_read_query(conn, read_editors_query)
        print(news_editors)
        
        read_news_query = "SELECT * FROM news"
        news_news = execute_read_query(conn, read_news_query)
        print(news_news)
        
        read_images_query = "SELECT * FROM images"
        news_images = execute_read_query(conn, read_images_query)
        print(news_images)
        
        read_summaries_query = "SELECT * FROM summaries"
        news_summaries = execute_read_query(conn, read_summaries_query)
        print(news_summaries)
