import smtplib
import random
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Divya99403@",
    database = "test"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE test")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

print("1. Sign UP")
print("2. Sign IN")
x = int(input("Choose any one option (1-2) ::==>"))

if x == 1:
    mycursor.execute("""CREATE TABLE IF NOT EXISTS user(
                      name VARCHAR(255),
                      username VARCHAR(255), 
                      password VARCHAR(255),
                      email VARCHAR(255),
                      phno VARCHAR(255),
                      isverified BOOLEAN DEFAULT FALSE
                     )
                    """)
    import ast
    val = ast.literal_eval(input("Enter The Record as name,username,pass,email,phno. tuple():=>"))

    
    check = "SELECT * FROM user WHERE  username = %s OR email = %s" 
    mycursor.execute(check, (val[1],val[3]))
    existing_data = mycursor.fetchone()

    if existing_data :
        print("This Data Already Inserted In The Table...")        
    else:
        sql = "INSERT INTO user(name,username,password,email,phno,isverified) VALUES(%s,%s,%s,%s,%s,%s)"
        otp = random.randint(1000,9999)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('darjidivya256@gmail.com','sxla wxtw ykjc obei')
        message = "Your Email Verification OTP is {}".format(otp)
        server.sendmail('darjidivya256@gmail.com',val[3], message)
        while True:
            input_otp = int(input("Enter the OTP::=>"))
            if input_otp == otp:
                print("OTP Verify")
                list1 = list(val)
                list1.append(True)
                val = tuple(list1)
                # sql = "DELETE FROM user WHERE name = 'Smeet'"            
                mycursor.execute(sql,val)
                mydb.commit()
                print("{} Data Inserted into Database Sucessfully....".format(mycursor.rowcount))
                break
            else:
                print("Invalid OTP please enter valid OTP!")  
    
else:

    print("You Have to Login by Username & Password")
    a = input("Enter the Username ::==>")
    b = input("Enter the Password ::==>")
 
    sql = "SELECT * FROM user WHERE username = %s AND password = %s"

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


            # mycursor.execute("""CREATE TABLE quiz(
            #            question VARCHAR(255),
            #            option VARCHAR(255), 
            #            answer VARCHAR(255),
            #            category VARCHAR(255),
            #            sub category VARCHAR(255)
            #            )
            #            """)
    else:
        print("Nope Something Wrong")
        