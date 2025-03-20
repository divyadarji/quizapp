# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
import random
import smtplib
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Database configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Divya99403@",
    "database": "test"
}

# Helper function to get database connection
def get_db_connection():
    conn = mysql.connector.connect(**DB_CONFIG)
    return conn, conn.cursor()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

# User authentication routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn, cursor = get_db_connection()
        cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
        user = cursor.fetchone()
        
        if user and user[2] == password:  # Index 2 is password in your DB
            session['user_id'] = user[0]
            session['username'] = user[1]
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
        
        conn.close()
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        
        conn, cursor = get_db_connection()
        
        # Check if username or email already exists
        cursor.execute("SELECT * FROM user WHERE username = %s OR email = %s", (username, email))
        existing_user = cursor.fetchone()
        
        if existing_user:
            flash('Username or email already exists', 'danger')
            conn.close()
            return render_template('signup.html')
        
        # Generate OTP
        otp = random.randint(1000, 9999)
        session['otp'] = otp
        session['signup_data'] = {
            'name': name,
            'username': username,
            'password': password,
            'email': email,
            'phone': phone
        }
        
        # Send OTP via email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('preetmistry8524@gmail.com', 'pjyw pimq sssf hxnh')
            message = f"Your Email Verification OTP is {otp}"
            server.sendmail('preetmistry8524@gmail.com', email, message)
            server.quit()
            flash('OTP sent to your email', 'info')
            return redirect(url_for('verify_otp'))
        except Exception as e:
            flash(f'Error sending OTP: {str(e)}', 'danger')
        
        conn.close()
    return render_template('signup.html')

@app.route('/verify-otp', methods=['GET', 'POST'])
def verify_otp():
    if 'otp' not in session or 'signup_data' not in session:
        flash('Session expired. Please sign up again.', 'danger')
        return redirect(url_for('signup'))
    
    if request.method == 'POST':
        user_otp = request.form['otp']
        if int(user_otp) == session['otp']:
            data = session['signup_data']
            
            conn, cursor = get_db_connection()
            cursor.execute(
                "INSERT INTO user (name, username, password, email, phno, isverified) VALUES (%s, %s, %s, %s, %s, %s)",
                (data['name'], data['username'], data['password'], data['email'], data['phone'], 1)
            )
            conn.commit()
            conn.close()
            
            flash('Registration successful! Please login.', 'success')
            
            # Clear session data
            session.pop('otp', None)
            session.pop('signup_data', None)
            
            return redirect(url_for('login'))
        else:
            flash('Invalid OTP. Please try again.', 'danger')
    
    return render_template('verify_otp.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

# Student routes
@app.route('/student-login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn, cursor = get_db_connection()
        cursor.execute("SELECT * FROM student WHERE username = %s AND password = %s", (username, password))
        student = cursor.fetchone()
        conn.close()
        
        if student:
            session['student_id'] = student[1]  # rollno
            session['student_name'] = student[0]  # name
            session['student_class'] = student[3]  # class
            session['student_division'] = student[4]  # division
            flash('Login successful!', 'success')
            return redirect(url_for('student_dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('student_login.html')

@app.route('/student-signup', methods=['GET', 'POST'])
def student_signup():
    if request.method == 'POST':
        name = request.form['name']
        rollno = request.form['rollno']
        school = request.form['school']
        std = request.form['std']
        division = request.form['division']
        phone = request.form['phone']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        
        conn, cursor = get_db_connection()
        cursor.execute(
            "INSERT INTO student (name, rollno, schoolname, class, division, phno, email, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (name, rollno, school, std, division, phone, email, username, password)
        )
        conn.commit()
        conn.close()
        
        flash('Student registration successful!', 'success')
        return redirect(url_for('student_login'))
    
    return render_template('student_signup.html')

@app.route('/student-dashboard')
def student_dashboard():
    if 'student_id' not in session:
        flash('Please login first', 'danger')
        return redirect(url_for('student_login'))
    
    # Get student details
    conn, cursor = get_db_connection()
    cursor.execute("SELECT * FROM student WHERE rollno = %s", (session['student_id'],))
    student = cursor.fetchone()
    
    # Get past quiz results
    cursor.execute(
        "SELECT * FROM evaluation WHERE rollno = %s ORDER BY category, subcategory",
        (session['student_id'],)
    )
    results_raw = cursor.fetchall()
    conn.close()
    
    # Convert string values to integers
    results = []
    for result in results_raw:
        processed_result = list(result)
        # Convert string values to integers for columns 7, 8, and 9
        processed_result[7] = int(processed_result[7]) if processed_result[7] else 0
        processed_result[8] = int(processed_result[8]) if processed_result[8] else 0
        processed_result[9] = int(processed_result[9]) if processed_result[9] else 0
        results.append(processed_result)
    
    return render_template('student_dashboard.html', student=student, results=results)
# Quiz routes
@app.route('/quiz-categories')
def quiz_categories():
    if 'student_id' not in session:
        flash('Please login first', 'danger')
        return redirect(url_for('student_login'))
    
    return render_template('quiz_categories.html')

@app.route('/quiz-subcategories/<category>')
def quiz_subcategories(category):
    if 'student_id' not in session:
        flash('Please login first', 'danger')
        return redirect(url_for('student_login'))
    
    subcategories = []
    
    if category == 'gk':
        subcategories = [{'id': 'gk', 'name': 'General Knowledge'}]
    elif category == 'pl':
        subcategories = [
            {'id': 'c-language', 'name': 'C Language'},
            {'id': 'c++', 'name': 'C++'},
            {'id': 'java', 'name': 'Java'},
            {'id': 'python', 'name': 'Python'}
        ]
    elif category == 'gl':
        subcategories = [
            {'id': 'eng', 'name': 'English'},
            {'id': 'hindi', 'name': 'Hindi'},
            {'id': 'guj', 'name': 'Gujarati'}
        ]
    
    return render_template('quiz_subcategories.html', category=category, subcategories=subcategories)

# Add this helper function at the top level of your app.py file
def debug_quiz_data(question_data, user_answer=None):
    """Helper function to debug quiz question data"""
    print("\n==== QUIZ DATA DEBUG ====")
    print(f"Question: {question_data['question']}")
    print("Options:")
    for i, opt in enumerate(question_data['options']):
        print(f"  {i}: '{opt}'")
    print(f"Stored correct answer: '{question_data['answer']}'")
    if user_answer:
        print(f"User provided answer: '{user_answer}'")
    print("========================\n")

# Replace both start_quiz and quiz_question functions

@app.route('/start-quiz/<category>/<subcategory>')
def start_quiz(category, subcategory):
    if 'student_id' not in session:
        flash('Please login first', 'danger')
        return redirect(url_for('student_login'))
    
    conn, cursor = get_db_connection()
    
    # Map category and subcategory to DB values
    db_category = 'GK' if category == 'gk' else ('PL' if category == 'pl' else 'GL')
    db_subcategory = subcategory
    
    # Get questions for the selected category/subcategory
    if category == 'gk':
        cursor.execute("SELECT * FROM quiz WHERE category = 'GK'")
    else:
        cursor.execute("SELECT * FROM quiz WHERE subcategory = %s", (subcategory,))
    
    all_questions = cursor.fetchall()
    conn.close()
    
    if not all_questions:
        flash('No questions found for this category', 'warning')
        return redirect(url_for('quiz_categories'))
    
    # Select 10 random questions or all available if less than 10
    selected_questions = random.sample(all_questions, min(10, len(all_questions)))
    
    # Store questions in session with a completely different approach
    processed_questions = []
    
    for i, q in enumerate(selected_questions):
        # Get raw data from database record
        question_text = q[0] if q[0] else "No question text"
        options_text = q[1] if q[1] else ""
        correct_answer_text = q[2] if q[2] else ""
        
        # Process options list
        options = [opt.strip() for opt in options_text.split(',')]
        
        # Instead of text comparison, store the correct answer as an index (0-based)
        correct_index = None
        
        # First try exact matching
        for idx, option in enumerate(options):
            if option == correct_answer_text:
                correct_index = idx
                break
        
        # If exact matching failed, try normalized comparison
        if correct_index is None:
            for idx, option in enumerate(options):
                if option.lower().strip() == correct_answer_text.lower().strip():
                    correct_index = idx
                    break
        
        # If still no match, set a default (first option)
        if correct_index is None:
            correct_index = 0
            print(f"WARNING: Could not find '{correct_answer_text}' in options - using first option as default")
        
        # Store processed question
        processed_questions.append({
            'id': i,
            'question': question_text,
            'options': options,
            'correct_index': correct_index,  # Store as index instead of text
            'answer': correct_answer_text    # Keep original for display purposes
        })
        
        # Debug output
        debug_quiz_data(processed_questions[-1])
    
    # Store processed questions in session
    session['quiz_questions'] = processed_questions
    session['quiz_category'] = category
    session['quiz_subcategory'] = subcategory
    session['quiz_db_category'] = db_category
    session['quiz_db_subcategory'] = db_subcategory
    session['current_question'] = 0
    session['correct_answers'] = 0
    session['attempted_questions'] = 0
    
    return redirect(url_for('quiz_question'))

@app.route('/quiz-question', methods=['GET', 'POST'])
def quiz_question():
    if 'student_id' not in session or 'quiz_questions' not in session:
        flash('Please start a quiz first', 'danger')
        return redirect(url_for('quiz_categories'))
    
    questions = session['quiz_questions']
    current_index = session['current_question']
    
    if current_index >= len(questions):
        return redirect(url_for('quiz_result'))
    
    question = questions[current_index]
    
    if request.method == 'POST':
        # Get user's answer - expecting the index of the selected option
        user_answer_index = -1
        try:
            # Get the option that the user selected
            user_answer = request.form.get('answer', '')
            
            # Find which index this answer corresponds to
            for i, option in enumerate(question['options']):
                if option == user_answer:
                    user_answer_index = i
                    break
                    
            # If not found, try normalized comparison
            if user_answer_index == -1:
                for i, option in enumerate(question['options']):
                    if option.lower().strip() == user_answer.lower().strip():
                        user_answer_index = i
                        break
        except Exception as e:
            print(f"Error processing user answer: {str(e)}")
            user_answer_index = -1
        
        # Debug output
        print("\n==== ANSWER COMPARISON ====")
        print(f"User selected option text: '{user_answer}'")
        print(f"User selected option index: {user_answer_index}")
        print(f"Correct option index: {question['correct_index']}")
        print(f"Correct option text: '{question['options'][question['correct_index']] if question['correct_index'] < len(question['options']) else 'INVALID'}'")
        print("==========================\n")
        
        # Compare by index
        if user_answer_index == question['correct_index']:
            session['correct_answers'] += 1
            flash('Correct answer!', 'success')
        else:
            correct_text = question['options'][question['correct_index']] if question['correct_index'] < len(question['options']) else question['answer']
            flash(f'Wrong answer. The correct answer is: {correct_text}', 'danger')
        
        session['attempted_questions'] += 1
        session['current_question'] += 1
        
        if session['current_question'] >= len(questions):
            return redirect(url_for('quiz_result'))
        
        return redirect(url_for('quiz_question'))
    
    return render_template('quiz_question.html', question=question, question_num=current_index+1, total_questions=len(questions))
@app.route('/quiz-result')
def quiz_result():
    if 'student_id' not in session or 'quiz_questions' not in session:
        flash('Please start a quiz first', 'danger')
        return redirect(url_for('quiz_categories'))
    
    # Get quiz results
    correct_answers = session['correct_answers']
    total_questions = len(session['quiz_questions'])
    attempted_questions = session['attempted_questions']
    
    # Save results to database
    conn, cursor = get_db_connection()
    cursor.execute(
        "INSERT INTO evaluation (name, std, division, rollno, category, subcategory, noofattempt, rightans, wrongans) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (
            session['student_name'],
            session['student_class'],
            session['student_division'],
            session['student_id'],
            session['quiz_db_category'],
            session['quiz_db_subcategory'],
            attempted_questions,
            correct_answers,
            attempted_questions - correct_answers
        )
    )
    conn.commit()
    conn.close()
    
    # Clear quiz session data
    quiz_data = {
        'questions': session['quiz_questions'],
        'category': session['quiz_category'],
        'subcategory': session['quiz_subcategory'],
        'correct_answers': correct_answers,
        'attempted_questions': attempted_questions
    }
    
    session.pop('quiz_questions', None)
    session.pop('quiz_category', None)
    session.pop('quiz_subcategory', None)
    session.pop('quiz_db_category', None)
    session.pop('quiz_db_subcategory', None)
    session.pop('current_question', None)
    session.pop('correct_answers', None)
    session.pop('attempted_questions', None)
    
    return render_template('quiz_result.html', 
                          correct=correct_answers, 
                          total=total_questions, 
                          attempted=attempted_questions,
                          category=quiz_data['category'],
                          subcategory=quiz_data['subcategory'])

# Dashboard routes
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please login first', 'danger')
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', username=session['username'])

if __name__ == '__main__':
    app.run(debug=True)