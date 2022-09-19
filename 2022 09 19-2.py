from tkinter import W


def calculate(name):
    name = name.lower()
    if name == "rectangle":
        l = int(input("Enter the rectangle's length: "))
        w = int(input("Enter the rectangle's width: "))

        rec_area = l*w

        print("The area of the rectangle is: "+str(rec_area))

    elif name == "square":

        s = int(input("Enter the square's side length: "))

        sq_area = s*s

        print("The area of the square is: "+str(sq_area))

    elif name == "triangle":
        l = int(input("Enter the triangle's length: "))
        w = int(input("Enter the triangle's width: "))

        tri_area = 0.5*w*l

        print("The area of the triangle is: "+str(tri_area))

    elif name == "circle":
        r = int(input("Enter the circle's radius length: "))
        pi = 3.14

        circle_area = r*r*pi

        print("The area of the circle is: "+str(circle_area))
    else:
        print("Sorry! This shape is not available!")

################################################################

def get_grades(name):
    marks = {"James" : 90, "Jule":60, "Bob":75, "Katy":90}
    
    for student in marks:
        if student == name:
            print(marks[student])
            break
    else:
        print("No entry with that name found.")


if __name__ == "__main__":
    print("maths test result")
    student_name = input("Type student's name: ")
    get_grades(student_name)
