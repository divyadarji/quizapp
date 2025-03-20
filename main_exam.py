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

def user_login():
    while True:
        print("1. Sign UP User")
        print("2. Sign IN User")
        print("3. Exist")
        x = int(input("Choose any one option (1-2) ::==>"))
        
        if x == 1:
            val = eval(input("Enter The Record into Format of name,username,password,email,phno in form of tuple()::=>"))
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
                server.login('preetmistry8524@gmail.com','pjyw pimq sssf hxnh')
                message = "Your Email Verification OTP is {}".format(otp)
                server.sendmail('preetmistry8524@gmail.com',val[3], message)
                while True:
                    input_otp = int(input("Enter the OTP::=>"))
                    if input_otp == otp:
                        print("OTP Verify")
                        list1 = list(val)
                        list1.append(True)
                        val = tuple(list1)            
                        mycursor.execute(sql,val)
                        mydb.commit()
                        print("{} Data Inserted into Database Sucessfully....".format(mycursor.rowcount))
                        student()
                        break
                    else:
                        print("Invalid OTP please enter valid OTP!")  
            
        elif x == 2:

            print("You Have to USER Login by Username & Password")
            a = input("Enter the Username ::==>")
            b = input("Enter the Password ::==>")
        
            sql = "SELECT * FROM user WHERE username = %s AND password = %s"

            mycursor.execute(sql,(a,b))
            user = mycursor.fetchone()    
            if user: 
                    print("Login Successfully...")
                    student()
            else :
                print("Something gone wrong...")
        else:
            break

def student():

    print("1.Sign Up For Student.")
    print("2.Sign In For Student.")
    exam = ()
    x = int(input("Choose any one option (1-2):==>"))
    if x == 1:
        val = eval(input("Enter The Record into Format of (name,rollno,schoolname,std,division,phno,email,username,password) in form of tuple()::=>"))
        
        sql = """INSERT INTO student (name,rollno,schoolname,std,division,phno,email,username,password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        mycursor.execute(sql,val)
        mydb.commit()
        print("inserted")
        student()
    else:
        print("You Have to STUDENT Sign In by Username & Password")
        stu_name = input("Enter the Username ::==>")
        stu_pass = input("Enter the Password ::==>")

        sql = "SELECT * FROM student WHERE username = %s AND password = %s"
        
        mycursor.execute(sql,(stu_name,stu_pass))
        user = mycursor.fetchone()    
        if user: 
            print("Login Successfully...")
            
            print("Quiz Competition.!!")
            print("There are 3 types of Quiz.")
            print("1. General Knowledge")
            print("2. Programming Language")
            print("3. General Language")
            category = int(input("Choose any one category (1-3) ::==>"))
            if category == 1 :
                    
                query = "SELECT * FROM quiz WHERE category='GK'"
                mycursor.execute(query)
                result = mycursor.fetchall()
                points = 0
                ques_ans = 0
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
                            ques_ans +=1
                        else:
                            print("This is wrong answer!!!", "Right answer is",correct_answer)
                            ques_ans +=1
                    except:
                        pass    
                        
                print("Your Score is ::=>",points)       
                print("No of attempts question ::=>",ques_ans)

            elif category == 2:
                print("There are 4 types of programming language")
                print("1. C Language.")
                print("2. C++ Language.")
                print("3. Java Language.")
                print("4. Python Language.")
                sub_category = int(input("Choose any one sub category (1-4) ::==>"))
                if sub_category == 1:
                    query = "SELECT * FROM quiz WHERE subcategory='c-language'"
                    mycursor.execute(query)
                    result = mycursor.fetchall()
                    points = 0
                    ques_ans = 0
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
                                ques_ans +=1
                            else:
                                print("This is wrong answer!!!", "Right answer is",correct_answer)
                                ques_ans +=1
                        except:
                            pass    
                    print("Your Score is ::=>",points)
                    print("No of attempts question ::=>",ques_ans)       
                            
                elif sub_category == 2:
                    query = "SELECT * FROM quiz WHERE subcategory='c++'"
                    mycursor.execute(query)
                    result = mycursor.fetchall()
                    points = 0
                    ques_ans = 0
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
                                ques_ans +=1
                            else:
                                print("This is wrong answer!!!", "Right answer is",correct_answer)
                                ques_ans +=1
                        except:
                            pass    
                    print("Your Score is ::=>",points)
                    print("No of attempts question ::=>",ques_ans)       
                        
                elif sub_category == 3:
                    query = "SELECT * FROM quiz WHERE subcategory='java'"
                    mycursor.execute(query)
                    result = mycursor.fetchall()
                    points = 0
                    ques_ans = 0
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
                                ques_ans +=1
                            else:
                                print("This is wrong answer!!!", "Right answer is",correct_answer)
                                ques_ans +=1
                        except:
                            pass    
                    print("Your Score is ::=>",points)                       
                    print("No of attempts question ::=>",ques_ans)

                else:
                    query = "SELECT * FROM quiz WHERE subcategory='python'"
                    mycursor.execute(query)
                    result = mycursor.fetchall()
                    points = 0
                    ques_ans = 0
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
                                ques_ans +=1
                            else:
                                print("This is wrong answer!!!", "Right answer is",correct_answer)
                                ques_ans +=1
                        except:
                            pass    
                    print("Your Score is ::=>",points)       
                    print("No of attempts question ::=>",ques_ans)

            else:
                print("There are 3 types of general language")
                print("1. English Language.")
                print("2. Hindi Language.")
                print("3. Gujarati Language.")
                sub_category = int(input("Choose any one sub category (1-3) ::==>"))
                if sub_category == 1:
                    query = "SELECT * FROM quiz WHERE subcategory='eng'"
                    mycursor.execute(query)
                    result = mycursor.fetchall()
                    points = 0
                    ques_ans = 0
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
                                ques_ans +=1
                            else:
                                print("This is wrong answer!!!", "Right answer is",correct_answer)
                                ques_ans +=1
                        except:
                            pass    
                    print("Your Score is ::=>",points)             
                    print("No of attempts question ::=>",ques_ans)

                elif sub_category == 2:
                    query = "SELECT * FROM quiz WHERE subcategory='hindi'"
                    mycursor.execute(query)
                    result = mycursor.fetchall()
                    points = 0
                    ques_ans = 0
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
                                ques_ans +=1
                            else:
                                print("This is wrong answer!!!", "Right answer is",correct_answer)
                                ques_ans +=1
                        except:
                            pass    
                    print("Your Score is ::=>",points)
                    print("No of attempts question ::=>",ques_ans)

                else:
                    query = "SELECT * FROM quiz WHERE subcategory='guj'"
                    mycursor.execute(query)
                    result = mycursor.fetchall()
                    points = 0
                    ques_ans = 0
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
                                ques_ans +=1
                            else:
                                print("This is wrong answer!!!", "Right answer is",correct_answer)
                                ques_ans +=1
                        except:
                            pass    
                    print("Your Score is ::=>",points)        
                    print("No of attempts question ::=>",ques_ans)

            
            # print(val)
        sql = "SELECT name,std,division,rollno FROM student WHERE username = %s " 

        mycursor.execute(sql,(stu_name,))
        student_data = mycursor.fetchone()
        if student_data :
            name,std,division,rollno = student_data
            category_name = ""
            subcategory_name = ""
            
            if category == 1:
                category_name = "GK"
                subcategory_name = "none"  
            elif category == 2:
                category_name = "PL"
                subcategory_map = {1: "C Language", 2: "C++", 3: "Java", 4: "Python"}
                subcategory_name = subcategory_map.get(sub_category, "Unknown")
            elif category == 3:
                category_name = "GL"
                subcategory_map = {1: "English", 2: "Hindi", 3: "Gujarati"}
                subcategory_name = subcategory_map.get(sub_category, "Unknown")
            
            exam = (name,std,division,rollno,category_name,subcategory_name,ques_ans,points,ques_ans-points)
            sql = "INSERT INTO evaluation (name,std,division,rollno,category,subcategory,noofattempt,rightans,wrongans) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            
            mycursor.execute(sql,exam)
            mydb.commit()
            print(mycursor.rowcount,"inserted")
            print(tuple(exam))
            

choice = int(input("Enter 1 for Sign In or Registration for User ::=>"))

if choice == 1:
    user_login()
# elif choice == 2:
    # student()