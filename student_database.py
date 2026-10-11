#student database management system
#data structure used: hash table

students={}
def add_student():
    roll_no=input("enter roll number:")

    if roll_no in students:
        print("student allready exists!")
        return
    name=input("enter student name:")
    marks=float(input("enter marks:"))

    students[roll_no]={
        "name":name,
        "marks":marks
    }

    print("student added successfully!")

def search_student():
    roll_no=input("enter roll number to search:")

    if roll_no in students:
        print("student found!")
        print("roll number:",roll_no)
        print("name:",students[roll_no]["name"])
        print("marks:",students[roll_no]["marks"])
    else:
        print("student not found!")
def display_students():
            if not students:
                print("no student recorda available.")
                return
            print("\n---student records---")
            for roll_no,details in students.items():
                print("roll number:",roll_no)
                print("name:",details["name"])
                print("marks:",details["marks"])
                print("-------------")
def delete_student():
            roll_no=input("enter roll no to delete:")
            if roll_no in students:
                del students[roll_no]
                print("student deleted successfully!")
            else:
                print("student not found")
while True:
    print("1. add student")
    print("2.search student")
    print("3.display students")
    print("4. delete student")
    print("5.exit")

    choice=input("enter your choice:")
    if choice=="1":
       add_student()
    elif choice=="2":
        search_student()
    elif choice=="3":
        display_students()
    elif choice=="4":
        delete_student()
    elif choice=="5":
        print("thank you!")
        break
    else:
       print("invalid choice!try again.")
                        

