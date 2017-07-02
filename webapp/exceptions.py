student={
    "name":"Mark",
    "student_id":15163,
    "feedback":None
}

try:
    lastname=student["lastname"]
except KeyError:
    print("Error finding last name")

print("This code executes!")