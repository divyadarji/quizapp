# Quiz Application

## Overview
This is a backend-driven quiz application that supports multiple quiz categories, including General Knowledge (GK), Programming Languages, and General Languages. The project is designed to handle user authentication, quiz management, and question retrieval from a MySQL database.

## Features
- User & Student Authentication (Sign Up & Sign In)
- Multiple Quiz Categories
- Question Retrieval from MySQL Database
- CSV-based Question Import
- Score Calculation
- Flask Web Application (Upcoming)

## Technologies Used
- Python
- Flask (Upcoming for UI)
- MySQL
- Pandas (for CSV Handling)

## Folder Structure
```
quiz_question/
│── exam.py
│── guj.csv
│── main_exam.py
│── query.sql
│── student.py
│── table.py
│── test2.py
│__ app.py
│── C_language_MCQs.csv
│── c++.csv
│── eng.csv
│── GK.csv
│── hindi_mcq.csv
│── java_mcq_questions.csv
│── python_mcq.csv
```

## Installation & Setup
### **1. Clone the Repository**
```sh
git clone https://github.com/yourusername/quiz_application.git
cd quiz_application
```

### **2. Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Configure Database**
- Create a MySQL database named `quiz_db`.
- Update `table.py` and other scripts with your MySQL credentials.
- Run the following command to create tables and insert data:
```sh
python table.py
```

### **5. Run the Quiz Application**
```sh
python app.py
```

## Upcoming Features
- Flask-based UI for a better user experience.
- Admin panel for managing questions.
- API endpoints for quiz management.

## Contributing
Feel free to fork this repository, make changes, and submit a pull request.

## License
MIT License. See `LICENSE` for details.

