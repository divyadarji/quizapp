import random
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Divya99403@",
    database = "test"
)

mycursor = mydb.cursor()
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS student (
        name VARCHAR(255),
        rollno VARCHAR(255),
        schoolname VARCHAR(255),
        class VARCHAR(255),
        division VARCHAR(255),
        phno VARCHAR(255),
        email VARCHAR(255),
        username VARCHAR(255),
        password VARCHAR(255)
    )
""")
mydb.commit()

print("1.Sign Up For Student.")
print("2.Sign In For Student.")
x = int(input("Choose any one option (1-2):==>"))
if x == 1:

    mycursor.execute("""CREATE TABLE IF NOT EXISTS evaluation(
                        name VARCHAR(255),
                        std VARCHAR(255),
                        division VARCHAR(255),  # Renamed `div` to `division`
                        rollno VARCHAR(255),
                        category VARCHAR(255),
                        subcategory VARCHAR(255),
                        noofattempt VARCHAR(255),
                        rightans VARCHAR(255),
                        wrongans VARCHAR(255),
                        totalmarks VARCHAR(255)
                        )""")

    val = eval(input("Enter The Record into Format of (name,rollno,schoolname,class,division,phno,email,username,password) in form of tuple()::=>"))
    
    sql = """INSERT INTO student (name,rollno,schoolname,class,division,phno,email,username,password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    # check = "SELECT * FROM student WHERE username = %s OR email = %s"
    mycursor.execute(sql,val)
    mydb.commit()
    print("inserted")
    # data = mycursor.fetchone()

else:
    print("You Have to Sign In by Username & Password")
    a = input("Enter the Username ::==>")
    b = input("Enter the Password ::==>")

    sql = "SELECT * FROM student WHERE username = %s AND password = %s"
    mycursor.execute(sql,(a,b))
    user = mycursor.fetchone()    
    if user: 
        print("Login Successfully...")
    
        print("Quiz Competition.!!")
        print("There are 3 types of Quiz.")
        print("1. General Knowledge")
        print("2. Programming Language")
        print("3. General Language")
        x = int(input("Choose any one category (1-3) ::==>"))
        if x == 1:
                
            query = "SELECT * FROM quiz WHERE category='GK'"
            mycursor.execute(query)
            result = mycursor.fetchall()

            if not result:
                print("No questions available in the database for General Knowledge.")
            else:
                data = random.choice(result)

            points = 0
            ques_no = 0
            ques = []
            for i in range(1, 11):
                data = random.choice(result)
                while data[0] in ques:
                    data = random.choice(result)
                ques.append(data[0])
                question = data[0]
                options = data[1].split("|")  
                correct_answer = data[2]  
            
                print(f"\nQuestion {i}: {question}")
                print(f"Option : {options}")
                try:
                    user_ans = input("Enter your answer(A-D) ::=>")
                      
                    if user_ans.upper() == correct_answer:
                        print("This is right answer!!!" )
                        points +=1
                        ques_no +=1
                    else:
                        print("This is wrong answer!!!", "Right answer is",correct_answer)
                        ques_no +=1
                except:
                    pass    
                    
            print("Your Score is :",points)
            print("No of attempts question :",ques_no)       
               
        elif x == 2:
            print("There are 4 types of programming language")
            print("1. C Language.")
            print("2. C++ Language.")
            print("3. Java Language.")
            print("4. Python Language.")
            a = int(input("Choose any one sub category (1-4) ::==>"))
            if a == 1:
                query = "SELECT * FROM quiz WHERE subcategory='c-language'"
                mycursor.execute(query)
                result = mycursor.fetchall()
                points = 0
                ques = []
                for i in range(1, 11):
                    data = random.choice(result)
                    while data[0] in ques:
                        data = random.choice(result)
                    ques.append(data[0])
                    question = data[0]
                    options = data[1].split("|")  
                    correct_answer = data[2]  
                
                    print(f"\nQuestion {i}: {question}")
                    print(f"Option : {options}")
                    try:
                        user_ans = input("Enter your answer(A-D) ::=>")
                           
                        if user_ans.upper() == correct_answer:
                            print("This is right answer!!!" )
                            points +=1
                        else:
                            print("This is wrong answer!!!", "Right answer is",correct_answer)
                    except:
                        pass    
                print("Your Score is :",points)       
                         
            elif a == 2:
                query = "SELECT * FROM quiz WHERE subcategory='c++'"
                mycursor.execute(query)
                result = mycursor.fetchall()
                points = 0
                ques = []
                for i in range(1, 11):
                    data = random.choice(result)
                    while data[0] in ques:
                        data = random.choice(result)
                    ques.append(data[0])
                    question = data[0]
                    options = data[1].split("|")  
                    correct_answer = data[2]  
                
                    print(f"\nQuestion {i}: {question}")
                    print(f"Option : {options}")
                    try:
                        user_ans = input("Enter your answer(A-D) ::=>")
                            
                        if user_ans.upper() == correct_answer:
                            print("This is right answer!!!" )
                            points +=1
                        else:
                            print("This is wrong answer!!!", "Right answer is",correct_answer)
                    except:
                        pass    
                print("Your Score is :",points)       
                    
            elif a == 3:
                query = "SELECT * FROM quiz WHERE subcategory='java'"
                mycursor.execute(query)
                result = mycursor.fetchall()
                points = 0
                ques =[]
                for i in range(1, 11):
                    data = random.choice(result)
                    while data[0] in ques:
                        data = random.choice(result)
                    ques.append(data[0])
                    question = data[0]
                    options = data[1].split("|")  
                    correct_answer = data[2]  
                
                    print(f"\nQuestion {i}: {question}")
                    print(f"Option : {options}")
                    try:
                        user_ans = input("Enter your answer(A-D) ::=>")
                            
                        if user_ans.upper() == correct_answer:
                            print("This is right answer!!!" )
                            points +=1
                        else:
                            print("This is wrong answer!!!", "Right answer is",correct_answer)
                    except:
                        pass    
                print("Your Score is :",points)                       
                
            else:
                query = "SELECT * FROM quiz WHERE subcategory='python'"
                mycursor.execute(query)
                result = mycursor.fetchall()
                points = 0
                ques =[]
                for i in range(1, 11):
                    data = random.choice(result)
                    while data[0] in ques:
                        data = random.choice(result)
                    ques.append(data[0])
                    question = data[0]
                    options = data[1].split("|")  
                    correct_answer = data[2]  
                
                    print(f"\nQuestion {i}: {question}")
                    print(f"Option : {options}")
                    try:
                        user_ans = input("Enter your answer(A-D) ::=>")
                        
                        if user_ans.upper() == correct_answer:
                            print("This is right answer!!!" )
                            points +=1
                        else:
                            print("This is wrong answer!!!", "Right answer is",correct_answer)
                    except:
                        pass    
                print("Your Score is :",points)       
            
        else:
            print("There are 3 types of general language")
            print("1. English Language.")
            print("2. Hindi Language.")
            print("3. Gujarati Language.")
            b = int(input("Choose any one sub category (1-3) ::==>"))
            if b == 1:
                query = "SELECT * FROM quiz WHERE subcategory='eng'"
                mycursor.execute(query)
                result = mycursor.fetchall()
                points = 0
                ques =[]
                for i in range(1, 11):
                    data = random.choice(result)
                    while data[0] in ques:
                        data = random.choice(result)
                    ques.append(data[0])
                    question = data[0]
                    options = data[1].split("|")  
                    correct_answer = data[2]  
                    
                    print(f"\nQuestion {i}: {question}")
                    print(f"Option : {options}")
                    try:
                        user_ans = input("Enter your answer(A-D) ::=>")
                        
                        if user_ans.upper() == correct_answer:
                            print("This is right answer!!!" )
                            points +=1
                        else:
                            print("This is wrong answer!!!", "Right answer is",correct_answer)
                    except:
                        pass    
                print("Your Score is :",points)             
                
            elif b == 2:
                query = "SELECT * FROM quiz WHERE subcategory='hindi'"
                mycursor.execute(query)
                result = mycursor.fetchall()
                points = 0
                ques =[]
                for i in range(1, 11):
                    data = random.choice(result)
                    while data[0] in ques:
                        data = random.choice(result)
                    ques.append(data[0])
                    question = data[0]
                    options = data[1].split("|")  
                    correct_answer = data[2]  
                
                    print(f"\nQuestion {i}: {question}")
                    print(f"Option : {options}")
                    try:
                        user_ans = input("Enter your answer(A-D) ::=>")
                            
                        if user_ans.upper() == correct_answer:
                            print("This is right answer!!!" )
                            points +=1
                        else:
                            print("This is wrong answer!!!", "Right answer is",correct_answer)
                    except:
                        pass    
                print("Your Score is :",points)        
            else:
                query = "SELECT * FROM quiz WHERE subcategory='guj'"
                mycursor.execute(query)
                result = mycursor.fetchall()
                points = 0
                ques =[]
                for i in range(1, 11):
                    data = random.choice(result)
                    while data[0] in ques:
                        data = random.choice(result)
                    ques.append(data[0])
                    question = data[0]
                    options = data[1].split("|")  
                    correct_answer = data[2]  
                
                    print(f"\nQuestion {i}: {question}")
                    print(f"Option : {options}")
                    try:
                        user_ans = input("Enter your answer(A-D) ::=>")
                            
                        if user_ans.upper() == correct_answer:
                            print("This is right answer!!!" )
                            points +=1
                        else:
                            print("This is wrong answer!!!", "Right answer is",correct_answer)
                    except:
                        pass    
                print("Your Score is :",points)        

    else:
        print("Something gone wrong...")
