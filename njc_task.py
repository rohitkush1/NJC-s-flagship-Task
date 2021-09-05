import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "MoviesData"
)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Creating a Database 
cursor.execute("CREATE DATABASE IF NOT EXISTS MoviesData ")


#Executing an MYSQL function using the execute() method and Creating Table 
sql = """CREATE TABLE IF NOT EXISTS MOVIES(
    ID int AUTO_INCREMENT PRIMARY KEY, 
    MOVIES_NAME CHAR(20) NOT NULL, 
    DIRECTOR_NAME CHAR(20), 
    LEAD_ACTOR_NAME CHAR(20),  
    ACTRESS_NAME CHAR(200),  
    RELESE_YEAR YEAR(4)
    )"""
cursor.execute(sql)

#Inserting Data into Table
insert_stmt = """INSERT INTO MOVIES (
        MOVIES_NAME, DIRECTOR_NAME, LEAD_ACTOR_NAME, ACTRESS_NAME, RELESE_YEAR)
        VALUES (%s, %s, %s, %s, %s)"""

val = [
    ('shershaah', 'Vishnu Varadhan', 'Sidharth Malhotra', 'Kiara Advani, Nora Fatehi, Pranitha Subhas', 2021), 
    ('Bhuj : the pride of india', 'Abhishek Dudhaiya', ' Ajay Devgn', 'Sonakshi Sinha, Nora Fatehi, Pranitha Subhas', 2021), 
    ('Bellbottom ', 'Ranjit Tiwari', 'Akshay Kumar', 'Vaani Kapoor, Huma Qureshi', 2021), 
    ('Sadak 2 ', 'Mahesh Bhatt', 'Aditya Roy Kapur', 'Alia Bhatt', 2020), 
    ('Mimi ', 'Laxman Utekar', 'Pankaj Tripathi', 'Kriti Sanon, Sai Tamhanka Shama', 2021), 
    ('Haseen Dillruba', 'Vinil Mathew', 'Vikrant Massey', 'aapsee Pannu,, ', 2021), 
    ('Toofaan', 'Rakeysh Omprakash Mehra', 'Farhan Akhtar', 'Mrunal Thakur, ', 2021), 
    ('Jungle Cruise ', 'Jaume Collet-Serra', 'Dwayne Johnson', 'Isabelle Fuhrman Emily Blunt, ', 2021), 
    ('The King`s Man ', 'Matthew Vaughn', 'Dwayne Johnson', 'Stanley Tucci, Gemma Arterton', 2021), 
    ('Black Widow ', 'Cate Shortland', ' David Harbour', 'Scarlett Johansson F, ', 2021), 

   ]

# Executing the SQL command
cursor.executemany(insert_stmt, val)

# Commit your changes in the database
conn.commit()

print(cursor.rowcount, "Record Inerted Successfully")

#empty print for line break
print()

#Retrieving  records.  WE Can use any mysql command like- like, delete, update, where etc in this execution
cursor.execute("SELECT * FROM MOVIES")

#SELECT * FROM MOVIES WHERE LEAD_ACTOR_NAME LIKE 'Sidharth Malhotra' ORDER BY ACTRESS_NAME ASC
result = cursor.fetchall()

#ForLoop for retrieving data in manner
for i in result:
    print(i)

# Closing the connection
conn.close()
