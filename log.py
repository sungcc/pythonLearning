global x
x = 1
def main():
    global x
    choice = int(input("1.) Log a Person\n2.) Exit\n\nChoice (1-2):  "))
    if choice == 1:
        Log()
    elif choice == 2:
        x =0
    else:
        print('Invalid Choice!')

def Log():
    name = input("Name:  ")
    age = input("Age:  ")
    gender = input("Gender:  ")
    eye = input("Eye Color:  ")

    f = open("datafile.txt", "a")
    f.write("\n\n"+"-"*25+"\nName: "+name+"\nAge: "+age+"\nGender: "+gender+"\nEye Color: "+eye)
    f.close()
    print('Log Successful!\n\n')

while x == 1:
    main()