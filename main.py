import mysql.connector

config = {
    "host": "localhost",
    "user": "interuser",
    "password": "#Mypss1234",
    "database": "pycruddb"
}


conn = mysql.connector.connect(**config)
cursor = conn.cursor()


roll_number = int(input("Enter Roll Number: "))
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
subject = input("Enter Subject: ")
marks = float(input("Enter Marks: "))


select_query = "SELECT * FROM student_info WHERE roll_number = %s"
cursor.execute(select_query, (roll_number,))
existing_student = cursor.fetchone()

if existing_student:
    update_query = "UPDATE student_info SET first_name = %s, last_name = %s, subject = %s, marks = %s WHERE roll_number = %s"
    cursor.execute(update_query, (first_name, last_name, subject, marks, roll_number))
    print("Student information updated.")
else:
    insert_query = "INSERT INTO student_info (roll_number, first_name, last_name, subject, marks) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (roll_number, first_name, last_name, subject, marks))
    print("New student inserted.")

conn.commit()

select_query = "SELECT * FROM student_info"
cursor.execute(select_query)
student_records = cursor.fetchall()

for record in student_records:
    print("Roll Number:", record[0])
    print("First Name:", record[1])
    print("Last Name:", record[2])
    print("Subject:", record[3])
    print("Marks:", record[4])
    print()
    

cursor.close()
conn.close()





