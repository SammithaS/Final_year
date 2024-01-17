## Seat Allotment

### Objective:

This project aims to simulate the admission process of a Engineering College. Students can apply for a degree program at an engineering college using this system. It's a complete merit-based allotment system. Students are admitted taking in consideration their Common Entrance Test (CET) marks / University Exam Marks and course preferences.

### Eliminating Inequities in College Admissions

This project tackles a crucial issue in educational access: ensuring a fair and transparent college admissions process. It simulates the scenario of an engineering college admission system based solely on merit, removing potential biases introduced by factors like caste or personal connections.
Students applying to the program provide their Common Entrance Test (CET) marks or University Exam results, along with their preferred course choices. The system then uses a pre-defined, transparent algorithm to rank candidates based solely on their academic merit. This ranking determines seat allocation, prioritizing deserving students regardless of background or influence.

#### Features

The code is divided into different classes: menu, database, allotment_mechanism. Each file contains a class which has the related data members and functions defined in it. The functionality is divided mainly into 2 parts: For Admin and Student. There are different functionalities available to the user depending upon whether he/she is an Admin or a Student. Validations are added for all inputs to ensure an error free experience. The system carries out seat allocation efficiently for 500+ student records currently present in the database. Passwords are encrypted with a simple caesar-cipher algorithm before saving in the datasheet.

<hr>

> **Functions available for Students:**

 **Sign Up** :  
A new Student has to register and set his username and password before he can log into the application and access more features. 
The password can be changed later by logging into the account.
- **Login for Students** : 
Student has to log into the application with his username and password.
- **Fill Application details** : 
Students can update their application with their perosnal details (gender, email-id), marks, and course preferences. Students can reset their course preferences any number of times before the allotment process is done. 
(This functionality is available only till the allotment process is executed by Admin)
- **View seat matrix** : 
Students can view the number of available seats of all courses offered by the college.
- **Check application status** : 
Students can view their saved application details and check the allotment status: application incomplete / allotment pending / allotment result.
- **Withdraw application** : 
Student can choose to withdraw his/her application which will delete all the saved details and the student gets logged out of his account automatically.
(This functionality is available only till the allotment process is executed by Admin)
- **View cutoff marks** : 
Students can view the cut off marks of various Engineering Courses that the college offers. (This functionality is available only *after* the Admin has run the allotment process)
- **Get vacancy data** : 
Students can view the vacancies left after allotment is done, for each course offered by the college.

<hr>

> **Functions available for Admin:**

- Admin can **Run the allotment** process after which the students are admitted to a course of their preference. Admin can also **reset** the allotments if needed.
- Admin can **view the details** of any Student who has applied to the college.
- Admin can **view the full allotment result**, where all the applicants are listed with their alloted course name.
- Admin can **get course wise allotment list** of students.
- Admin can **get the count and list** of students who **haven't been alloted** any seat.
- Admin can **view the data of vacancies** left after allotment process.

---

**Programming Language:**  

- Python </br>
- **Data Structures used:**  Dictionary, List, List of dictionaries, List of lists (2D Array) </br>
- **Libraries used:** </br>
- pandas (for handling of csv data)
- csv  (for reading and writing to csv file)
- pywebio (for GUI)
- Flask (for deployment of the web app)

---

### Steps to run the Project

- Clone the repo

  ```
  https://github.com/Final-Year-Project-Team-3-CSE/Seat-Allotment.git
  ```
  
- Change the directory to the working directory

  ```
  cd Seat-Allotment
  ```

- Create a virtual environment and activate it

  ```
  pip install virtualenv
  ```

  ```
  virtualenv env
  env/Scripts/activate
  ```

- Install all the requirements

  ```
  pip install -r requirements.txt
  ```

- Run the Flask Web Server

  ```
  flask run
  ```

A development server will be started and then navigate to the URL `http://127.0.0.1:5000/tool`

- You can now either log in as admin or student

> [!NOTE]
>
> Admin Password: `secretadmin`




