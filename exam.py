import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Divya99403@",
    database = "test"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
mycursor.execute("""CREATE TABLE IF NOT EXISTS evaluation(name VARCHAR(255),
                    std VARCHAR(255),
                    divsion VARCHAR(255),
                    rollno VARCHAR(255),
                    category VARCHAR(255),
                    subcategory VARCHAR(255),
                    noofattempt VARCHAR(255),
                    rightans VARCHAR(255),
                    wrongans VARCHAR(255),
                    totalmarks VARCHAR(255)
                    )""")

sql = """
INSERT INTO evaluation(name,std,division,rollno)
SELECT name,class,division.rollno FROM student
"""
