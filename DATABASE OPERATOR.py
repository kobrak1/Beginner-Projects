import mysql.connector
import time

    
def select():
        
        
    

        
            
    while True:


        connection=mysql.connector.connect (
            name='ahmet',
            host='localhost',
            user='root',
            password='98Karhan98klmn',
            database='schooldb'
        )

        cursor=connection.cursor()
        print('1-Data Insert\n2-Delete Data\n3-Search\n4-Exit')
        choice=input('Choice:')
            

        if choice== '3':

            NAME= input('Name: ')
            SURNAME=input('Surname: ')
            cursor.execute(f'SELECT*FROM student Where Name LIKE "%{NAME}%" or Surname LIKE "%{SURNAME}%"')

            result=  cursor.fetchall()

            for i in result:
                print(i)
            print('Do you wanna search more? y/n')
            a=input()
            if a == 'y' or a=='Y':
                continue
            else:
                break
            
        elif choice == '1':
                
            STUDENT_NUMBER=input('Student Number:')
            NAME=input('Name:')
            SURNAME=input('Surname:')
            BIRTH_DATE=input('Birth Date:')
            GENDER=input('Gender:')
            sql='INSERT INTO student(StudentNumber,Name,SurName,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)'
            values=[STUDENT_NUMBER,NAME,SURNAME,BIRTH_DATE,GENDER]
            cursor.execute(sql,values)
            connection.commit()
            print('Data saved to database successfully..')
            time.sleep(2)
            print('Continue? y/n')
            b=input()
            if b=='y' or b=='Y':
                continue
            else:
                break
            
        elif choice=='2':
            name=input('Name:')
            surname=input('Surname:')
            cursor.execute(f'DELETE FROM student Where Name="{name}" or Surname="{surname}"')
            connection.commit()
            print(f'{name} {surname} person deleted from database successfully..')
            print('You wanna continue? y/n')
            x=input()
            if x=='y'or x=='Y':
                continue
            else:
                break

        elif choice == '4':
            break
        else:
            print('Please enter a valid character(Etc. 4).')
            continue



select()