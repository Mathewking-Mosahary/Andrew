import os
class student:
    print("""\n*********WELCOME TO PATKIJULI UNIVERSITY
    DETAILS OF UNIVERSITY:\n
    UNDER GUWAHATI UNIVERSITY
    ADDRESS: PATKIJULI,BAKSA,ASSAM,781360
    DIRECTOR: ANDREW MOSAHARY
    ESTABLISH: 2005""")
    
    
    def __init__(self):
        self.a=""
        self.b=""
        self.c=""
        self.p=""

    def reg(self):
        

        self.a=input("Enter your name: ")
        
        entry=open(self.a+".txt",'a')
        entry.write("Name:" )
        entry.write(self.a)
        entry.write("\n")

        cache=open("mathew.txt",'a')
        cache.write(self.a)
        cache.write("\n")
        
        self.b=input("Enter your address: ")
        entry1=open(self.a+".txt",'a')
        entry.write("Address:")
        entry.write(self.b)
        entry.write("\n")
        self.c=input("Enter your phone number: ")
        entry=open(self.a+".txt",'a')
        entry.write("Phone number:")
        entry.write(self.c)
        entry.write("\n")
        student.course(self)
        
        
    def course(self):
        print ("Select a course:-\n")
        print ("1.  COMPUTER SCIENCE AND ENGINEERING")
        print ("2.  CIVIL ENGINEERING")
        print ("3.  MECHANICAL ENGINEERING")
        print ("4.  ELECTRICAL ENGINEERING\n")
        x=int(input("Enter Your Choice Please: "))
        if(x==1):
            cse="COMPUTER SCIENCE AND ENGINEERING\n"
            entry=open(self.a+".txt",'a')
            entry.write("course:" )
            entry.write(cse)
            entry.write("\n")
            
            print (cse)
            print("""Select the subject combinations:-\n
                     1.Maths,C language,English,Environment
                     2.Maths,C++ language,Humanities,Environment
                     3.Maths,Java,English,Environment""")
            y=int(input("Enter the option: \n"))
            if(y==1):
                print("Maths,C language,English,Environment")
            elif(y==2):
                print("Maths,C++ language,Humanities,Environment")
            elif(y==3):
                print("Maths,Java,English,Environment")
            else:
                print("Not available")
        if (x==2):
            civil="CIVIL ENGINEERING"
            entry=open(self.a+".txt",'a')
            entry.write("course:" )
            entry.write(civil)
            entry.write("\n")
            print ("CIVIL ENGINEERING\n")
            print("""Select the subject combinations:-\n
                     1.Maths,C language,English,Environment
                     2.Maths,C++ language,Humanities,Environment
                     3.Maths,Java,English,Environment""")
            y=int(input("Enter the option: \n"))
            if(y==1):
                print("Maths,C language,English,Environment\n")
            elif(y==2):
                print("Maths,C++ language,Humanities,Environment\n")
            elif(y==3):
                print("Maths,Java,English,Environment\n")
            else:
                print("Not available\n")
        if (x==3):
            mech="MECHANICAL ENGINEERING"
            entry=open(self.a+".txt",'a')
            entry.write("course:" )
            entry.write(mech)
            entry.write("\n")
            print ("MECHANICAL ENGINEERING\n")
            print("""Select the subject combinations:-\n
                     1.Maths,C language,English,Environment
                     2.Maths,C++ language,Humanities,Environment
                     3.Maths,Java,English,Environment""")
            y=int(input("Enter the option: \n"))
            if(y==1):
                print("Maths,C language,English,Environment\n")
            elif(y==2):
                print("Maths,C++ language,Humanities,Environment\n")
            elif(y==3):
                print("Maths,Java,English,Environment\n")
            else:
                print("Not available")
        if (x==4):
            entry=open(self.a+".txt",'a')
            entry.write("course:" )
            entry.write("ELECTRICAL ENGINEERING")
            entry.write("\n")
            print ("ELECTRICAL ENGINEERING\n")
            print("""Select the subject combinations:-\n
                     1.Maths,C language,English,Environment
                     2.Maths,C++ language,Humanities,Environment
                     3.Maths,Java,English,Environment""")
            y=int(input("Enter the option: \n"))
            if(y==1):
                print("Maths,C language,English,Environment\n")
            elif(y==2):
                print("Maths,C++ language,Humanities,Environment\n")
            elif(y==3):
                print("Maths,Java,English,Environment\n")
            else:
                print("Not available")

        student.eligible(self)


    def eligible(self):

        print("""ELIGIBILITY TO GET ADMISSION IN THIS COLLEGE

        1. His/Her mark should be above 60% in H.S examination
        2. He/She should in Indian citizen\n""")

        print("Enter your percentage in H.S: ")
        z=int(input())
        if(z<60):
            print("NOT ELIGIBLE\n")
        elif(z>=60):
            print("Eligible\n")
        student.bill(self)
        
        

    def bill(self):
        print ("******Admission bill*******")

        print ("""
               1. Admission fee-->Rs6000
               2. Examination fee-->Rs1000
               3. Library fee-->Rs700
               4. Grade card fee---->Rs100
               5. Labratory fee--->Rs5000\n""")
        self.p=6000+1000+700+100+5000
        self.p1="Rs 12800"
        entry=open(self.a+".txt",'a')
        entry.write("Total bill:" )
        entry.write(self.p1)
        entry.write("\n")
        print ("Total  Bill=Rs",self.p,"\n")

    def display(self):
        print("*****LIST OF STUDENTS******")
        E=open("mathew.txt","r")
        print(E.read())
        E.close()
        
    def searching(self):
        search=input("Enter the name to search: ")
        if os.path.exists(search + ".txt"):
            fin = open(search + ".txt","r")
            print("Student Details:")
            print(fin.read())
            fin.close()
        else:
            print("not found")

    def start(self):
        while (1):
            print("\n1.Registration")
            print("2.Display student details")
            print("3.Searching")
            print("4.EXIT")

            b=int(input("\nEnter your choice:"))
            if (b==1):
                student.reg(self)

            if (b==2):

                student.display(self)
            
            if (b==3):

                student.searching(self)

            if (b==4):

                quit()
o = student()
o.start()


