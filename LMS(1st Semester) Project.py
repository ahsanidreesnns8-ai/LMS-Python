#LMS SYSTEM 
#2025-CYS-112
#AHSAN IDREES
import time
class LMS:
    def __init__(self, name, reg_no, username, password, token_number, degree_title, fee):
        self.name = name
        self.reg_no = reg_no
        self.classes = 16
        self.username = username
        self.password = password
        self.semester = '1'
        self.token_no = int(token_number)
        self.degree = degree_title
        self.fee = fee

    def Student_Course(self):
        for i in range(20):
            print('=',end='=')
            time.sleep(0.1)
        print()
        print('\n----Welcome to UET LMS----')
        print()
        username_input=input("Enter your username: ")
        password_input=input("Enter your password: ")
        if username_input!=self.username and password_input!=self.password:
            print("Wrong username and password.")
            print('Access Denied')
        elif username_input==self.username and password_input==self.password:
            print('Access Available.')
            print('Loading...')
            for i in range(101):
                print(f'\r{i}',end=" ")
                time.sleep(0.1)
        print()
        print('Student Details:')
        print(f'Student name: {self.name}')
        print(f'Student registration Number: {self.reg_no}')
        print(f'Student LMS ID: {self.username}')
        print(f'Student enrolled in semester: {self.semester}')
        print(f'Student enrolled in: {self.degree}')
        print()
        dic={}
        subject_no=int(input("Enter the number of sujects: "))
        for i in range(1,subject_no+1):
            subject_course={}
            name=input("Enter subject name: ")
            for i in range(1,17):
                course=input(f'Enter content course of {name} for Semester {self.semester} Week {i}: ')
                subject_course[f'Course Cotent Week {i}']=course
            marks=int(input(f"Enter the total marks of {name}: "))
            dic[f'{name}']=marks
            count=0
            for i in range(1,self.classes+1):
                user_input=input(f"Is student attend class {i} of {name} (Y/N): ").upper()
                if user_input=='Y':
                    count+=1
                elif user_input=='N':
                    count+=0
            for j in range(subject_no):
                mid_marks=int(input('Enter the marks of Mid: '))
                final_marks=int(input('Enter the marks of Final: '))
                no_quizes=int(input("Enter the number of Quizes taken: "))
                marks_one_quiz=int(input("Enter the marks of one quiz(eitehr 0): "))
                total_marks_quiz=f'{no_quizes*marks_one_quiz}'
                no_of_assignment=int(input('Enter the number of assignments(either 0): '))
                marks_of_one_assignment=int(input('Enter the number of one assignment(eitehr 0): '))
                total_marks_assignment=f'{no_of_assignment*marks_of_one_assignment}'
                no_of_presentation=int(input('Enter the number of presentation(either 0): '))
                marks_of_one_presentation=int(input('Enter the number of one presentation(either 0):'))
                total_marks_presentation=f'{no_of_presentation*marks_of_one_presentation}'
                marks_attendance=int(input('Enter the marks of attendance(either 0): '))
                no_of_viva=int(input('Enter the number of viva(either 0): ')) 
                marks_of_viva=int(input('Enter marks of one viva(either 0): '))
                total_marks_viva=f'{no_of_viva*marks_of_viva}'
                marks_of_project=int(input('Enter the marks of Project(either 0): '))
                total_marks_subject=int(mid_marks)+int(final_marks)+int(total_marks_quiz)+int(total_marks_presentation)+int(total_marks_assignment)+int(marks_attendance)+int(total_marks_viva)+int(marks_of_project)
                if total_marks_subject<100:
                    remaining_marks=100-total_marks_subject
                d={}
                for i,(j,k) in enumerate(subject_course.items(),1):
                    print(f'{i}. {j}:{k}')
                    time.sleep(1)
                print(f'Total Marks of {name}: 100')
                print("Marks Distribution is here")
                print()
                print('=='*20)
                d['Quiz Marks']= f'{total_marks_quiz}'
                d['Mid Marks']=f'{mid_marks}'
                d['Final Marks']=f'{final_marks}'
                d['Assignment Marks']=f'{total_marks_assignment}'
                d['Attendance Marks']=f'{marks_attendance}'
                d['Presentation Marks']=f'{total_marks_presentation}'
                d['Project number']=f'{marks_of_project}'
                d['Viva Marks']=f'{no_of_viva*marks_of_viva}'
                d['Other Marks']=f'{remaining_marks}'
                d['Class attended by student']=f'{count}'
                for i,(j,k) in enumerate(d.items(),1):
                    print(f'{i}. {j}:{k}')
                    time.sleep(1)
                total_obtain_marks=0
                marks_in_quizes=int(input("Enter marks in Quizes(either 0): "))
                marks_in_mid=int(input("Enter marks in Mid-Exam(either 0): "))
                if count<((16*75)/100):
                    print("You are not allowed to sit in  Final exam.")
                    print(f'You Attend {count} classes which is less than 75%.So,it is not acceptable.')
                    break
                else:
                    marks_in_final=int(input("Enter marks in Final-Exam(either 0): "))
                    marks_in_presentation=int(input("Enter marks in presentation(either 0): "))
                    marks_in_attendance=int(input("Enter marks of attendance(either 0): "))
                    marks_in_assignment=int(input("Enter marks in Assignments(either 0): "))
                    marks_in_project=int(input('Enter marks in Project(either 0): '))
                    marks_in_viva=int(input('Enter the marks in viav(either 0): '))
                    total_obtain_marks=marks_in_quizes+marks_in_mid+marks_in_final+marks_in_attendance+marks_in_assignment+marks_in_presentation+marks_in_project+marks_in_viva
                    print(f'Obtain Marks in {name} (out of 100): {total_obtain_marks}')
                    print(f'Percentage in marks: {total_obtain_marks}%')
                    break
               
    def Hostel_Information(self, Hall, Room):
        try: 
            student_hostellite=input('Is a student a hostellite(Y/N): ').upper()
            student_name=input('Enter student name: ').upper()
            if student_hostellite=='Y':
                if student_name=='M. AHSAN IDREES':
                  fee_update=input('Whether student pay Hostel Fee(Y/N): ').upper()
                  if fee_update=='Y':
                      while True:
                         count=0
                         pin_input=int(input('Enter student Token number: '))
                         count+=1
                         if pin_input==int(self.token_no):
                             print('Searching')
                             for i in range(101):
                                 print(f'\r{i}',end=' ')
                                 time.sleep(0.25)
                             print('Done')
                             print()
                             print('---Hostel Information---')
                             print(f'Student name: {student_name}')
                             print(f'Student Rgistration number: {self.reg_no}')
                             print(f'Student Enrolled in semester: {self.semester}st')
                             print(f'Student Enrolled in : {self.degree}')
                             print(f'Hall: {Hall}')
                             print(f'Room no: {Room}')
                             print('Fee status: OK')
                             break
                         elif pin_input!=int(self.token_no):
                             print('Inavalid token number')
                             if count==3:
                                break
                  elif fee_update=='N':
                      print('Student need first to pay fee challan')
                elif student_name!='M. AHSAN IDREES':
                    print('Searching...')
                    for i in range(101):
                        print(f'\r{i}',end=' ')
                        time.sleep(0.1)
                    print()
                    print(f'Student Name {student_name} is not found.Please try again Later.')
            elif student_hostellite=='N':
                print('Day Scholar...')
                print('Student is not a resident of Hostel')
            else:
                print('Invalid...')
        except:
            print('Something went wrong...')
            
    def fee_status(self):
        category=input('Enter the category of student(A1/A2): ').upper()
        if category=='A1':
            student_fee=input('Is student pay fee Challan 1(Y/N): ').upper()
            if student_fee=='Y':
                while True:
                    count=0
                    token_no_student=int(input('Enter correct token number: '))
                    if token_no_student==self.token_no:
                        print('Searching...')
                        for i in range(101):
                            print(f'\r{i}',end='')
                            time.sleep(0.1)
                        print()
                        print('-'*10)
                        print('\nFee Structure')
                        print('\nChallan Title: BSc. Session Fall 2025')
                        print(f'\nChallan ID: {self.token_no}')
                        print(f'\nSemester: {self.semester}')
                        print('\nChallan type')
                        print(f'\nSemester fee(Admission+Tution+Other): {self.fee}')
                        print(f'\nAdmission Category: {category}')
                        print('\nFee status: OK')
                        break
                    elif token_no_student!=self.token_no:
                        print('Please enter correct Token number')
                        count+=1
                        continue
                    break
            elif student_fee=='N':
                print('Student need to pay their fee challan first.')
            else:
                print('Something went wrong...')
        elif category=='A2':
            student_fee_1=input('Is student pay fee 1st Challan (Y/N): ').upper()
            student_fee_2=input('Is student pay fee 2nd Challan (Y/N): ').upper()
            if student_fee_1=='Y' and student_fee_2=='Y':
                while True:
                    token_no_student=int(input('Enter correct token number: '))
                    if token_no_student==self.token_no:
                        print('Searching...')
                        for i in range(101):
                            print(f'\r{i}',end='')
                            time.sleep(0.1)
                        print('-'*10)
                        print('\nFee Structure')
                        print('\nChallan Title: BSc. Session Fall 2025')
                        print(f'\nChallan ID: {self.token_no}')
                        print(f'\nSemester: {self.semester}')
                        print('\nChallan type')
                        print(f'\nSemester fee(Admission+Tution+Other): {self.fee}')
                        print('\nSemester fee: 1000')
                        print(f'\nAdmission Category: {category}')
                        print('\nFee status')
                        print('\nChallan 1st: OK')
                        print('\nChallan 2nd: OK')
                        break
                    elif token_no_student!=self.token_no:
                        print('Please enter correct Token number')
                        continue
                    break
            elif student_fee_1=='Y' and student_fee_2=='N':
                print('\nStudent is not allowed to sit in Final Exam')
                print('\nFirst Pay fee Challan no. 2')
                print('\nFee status')
                print('\nChallan 1st: OK')
                print('\nChallan 2nd: No')
            elif student_fee_1=='N' and student_fee_2=='N':
                print('Student need to pay first fee challan immediately.Otherwise admission will be canceleld and set will be given to desired one')
                print('\nFee status')
                print('Challan 1st: No')
                print('Challan 2nd: No')
    
    def GPA(self):
        print("Welcome to GPA Calculator...")
        print("Let's start...")
        grades={
             "A+": 4.0, 
             "A": 3.9, 
             "A-": 3.7, 
             "B+": 3.3, 
             "B": 3.0, 
             "B-": 2.7, 
             "C+": 2.3, 
             "C": 2.0, 
             "C-": 1.7, 
             "D+": 1.3, 
             "D": 1.0, 
             "D-": 0.7, 
             "F": 0.0
        }
        for keys,values in grades.items():
            print(f'{keys} : {values}')
            time.sleep(0.2)
        total_credit_hours=16
        subjects=int(input("How many subject are you studied in UNI: ")) #lab will be considered as one subject so total probabaly is 8.
        Credit_hour_3=int(input("Enter number of subjects of 3 credit hours: "))
        Credit_hour_2=int(input("Enter number of subjects of 2 credit hours: "))
        Credit_hour_1=int(input("Enter number of subjects of 1 credit hours: "))
        credit_hour=[]
        while True:
            try:
                for i in range(1,Credit_hour_3+1):
                    name_3_credit_hour=input(f"Enter name of subject {i} (3 credit hour): ")
                    gpa_subject=input(f"Enter grade of that subject {i}: ")
                    credit_hour.append(grades[gpa_subject]*3)
                for j in range(1,Credit_hour_2+1):
                    name_2_credit_hour=input(f"Enter name of subject {j} (2 credit hour): ")
                    gpa_subject=input(f"Enter grade of that subject {j}: ")
                    credit_hour.append(grades[gpa_subject]*2)
                for k in range(1,Credit_hour_1+1):
                    name_1_credit_hour=input(f"Enter name of subject {k} (1 credit hour): ")
                    gpa_subject=input(f"Enter grade of that subject {k}: ")
                    credit_hour.append(grades[gpa_subject]*1)
                break
            except ValueError:
                raise 'Invalid name given.'
        sum_points=0
        
        for l in credit_hour:
            sum_points+=l
        gpa=sum_points/total_credit_hours
        print(f'\nYou have studied {subjects} in UNI...')
        print('\nStudent Details:')
        print(f'\nStudent name: {self.name}')
        print(f'\nStudent registration Number: {self.reg_no}')
        print(f'\nStudent LMS ID: {self.username}')
        print(f'\nStudent enrolled in semester: {self.semester}')
        print(f'\nStudent enrolled in: {self.degree}')
        print(f"\nYour GPA is: {gpa:.2f}.")
        print("\nCongratulations...")
       
Student1=LMS('M. Ahsan Idrees','2025-CYS-112', '2025CYS112@student.uet.edu.pk', 't-oZ6URm','535455','Cybersecurity',153457)
# Student1.Student_Course()
Student1.Hostel_Information('Mumtaz Hall',87)
Student1.fee_status()
Student1.GPA()
#%%
