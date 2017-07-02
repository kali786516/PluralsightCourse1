students=[]

def get_student_title_case():
    student_titlecase=[]
    for student in students:
        student_titlecase.append(student["name"].title())
        return student_titlecase

def print_student_title_case():
    student_title_case=get_student_title_case()
    print(student_title_case)


def add_student(name,student_id=332):
    student={"name":name,"student_id":student_id}
    students.append(student)


def save_file(student):
    try:
        f=open("students.txt","a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f=open("students.txt","r")
        for student in f.readlines():
            add_student(student)
            f.close()
    except Exception:
        print("Cound not read file")


read_file()
print_student_title_case()

student_name=input("Enter student name:- ")
student_id=input("Enter student id:- ")

add_student(student_name,student_id)
save_file(student_name)


# just for demo
'''
def var_args(names,**kwargs):
    print(names)
    print(kwargs["studentid"],kwargs["address"])
'''

'''
add_student("Sri")
add_student("kali","786")
'''

'''
var_args("Sri",studentid="786",address="402 foulk road")
'''




