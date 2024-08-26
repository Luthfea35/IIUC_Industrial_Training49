# **Project Title: News Scraping and Summarization**
# **Table of Contents**

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Requirements](#requirements)
- [Installation and Setup](#installation-and-setup)
- [Screenshots](#screenshots)

## **1. Project Overview**
This project is designed to scrape news articles from specified websites, store the data in a MySQL database, generate concise summaries using a Large Language Model (LLM), and provide a user-friendly interface via Streamlit. It aims to make news consumption easier by summarizing articles and presenting them in a simple, digestible format.

## **2. Features**
- **Web Scraping:** Collect news articles from various websites using FastAPI.
- **Database Management:** Store and manage news articles in a MySQL database.
- **Summary Generation:** Use an LLM to generate concise summaries of the articles.
- **User Interface:** Provide a simple UI for viewing news and summaries using Streamlit.
- **Real-Time Updates:** Periodically update the news database with the latest articles.

## **3. Tech Stack**

- **Backend:**
  - FastAPI: For creating the RESTful API.
  - MySQL: For storing news articles.
- **Machine Learning:**
  - LLM Model: For generating summaries of the articles.
- **Frontend:**
  - Streamlit: For creating the user interface.
  - Python: For scripting and automation.

## **4. Requirements**

### **Software:**
- Python 3.8 or higher
- MySQL Server
- Docker (optional, for containerization)

### **Python Packages:**
- `fastapi`
- `uvicorn`
- `mysql-connector-python`
- `sqlalchemy`
- `groq` (depending on the LLM)
- `streamlit`
- `requests`
- `pydantic`

### **System:**
- OS: Windows
- Hardware: Minimum 8 GB RAM, 4 CPU cores

## **Installation and Setup**

Follow the steps below to set up the project on your local machine:

### **Step 1: Create the Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### **Step 2: Install Dependencies**

```bash
pip install -r requirements.txt
```
### **Step 3: Set Up MySQL Database**
Install MySQL Server and create a database.
Create a .env file in the root directory with your MySQL credentials:

```bash
DB_HOST=localhost
DB_USER=youruser
DB_PASSWORD=yourpassword
DB_NAME=newsdb
```
### **Step 4: Run the Application**
Backend (FastAPI)

```bash
run main.py
```
Frontend (Streamlit)

```bash
streamlit run Home.py
```
### **Step 5: Access the Application**
Open your browser and navigate to http://localhost:8501 to view the Streamlit UI.

## **6. Screenshots**
### Homepage: Display the news feed and summaries.

![Home](https://github.com/user-attachments/assets/fcac2034-e6c4-419c-b35a-06f8e83eae5f)

### Scraping Status: Show the current scraping process.

![scrapping](https://github.com/user-attachments/assets/54d91f03-b936-4bcd-96bf-3d1e03014728)

### Database View: Overview of stored articles.

![database](https://github.com/user-attachments/assets/9df8018c-e976-4d37-a399-9c94b0a5b4dd)

