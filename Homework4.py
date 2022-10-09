def hanyados(a,b):
    try:
        c=a/b
        print(c)
    except ZeroDivisionError:
        print("Division by 0 not allowed!")
    finally:
        print("Out of try except blocks")

if __name__ == "__main__":
    while True:
        a=int(input("Enter 'a' value:" ))
        b=int(input("Enter 'b' value:" ))
        hanyados(a,b)