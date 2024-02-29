import os
import json
def mainmenu():
    print("1. Report")
    print("2. Admin")
    print("3. Exit")
    a = int(input("Enter choice(1-3): "))
    if a == 1:
        Report()
    elif a == 2:
        AdminMenu()
    elif a == 3:
        print("Exit-ed")
    else:
        print("Invalid option, xin hãy chọn lại")
        mainmenu()
###########################################################################
        
def AdminMenu():
    print("ADMIN MENU")
    print("1. CREATE PUPIL RECORD")
    print("2. DISPLAY ALL PUPILS RECORDS")
    print("3. SEARCH PUPIL RECORD")
    print("4. MODIFY PUPIL RECORD")
    print("5. DELETE PUPIL RECORD")
    print("6. BACK TO MAIN MENU")    
    a = int(input("Enter choice(1-6): "))
    if a == 1:
        CreatePupilRecord()
    elif a ==2:
        DisplayAllPupilsRecords()
    elif a ==3:
        SearchPupilRecord()
    elif a ==4:
        ModifyPupilRecord()
    elif a == 5:
        DeleteRecord()
    elif a ==6:
        mainmenu()
    else: 
        print("Invalid option, xin hãy chọn lại")
        AdminMenu()
        
#########################################################
def CreatePupilRecord():
    a1 = int(input("Enter roll number: "))
    try:   
        b = "Rollnumber"+str(a1)+".json"  
        with open(str(b),"x") as a:
            with open(str(b), "w") as a:
                a2 = str(input("Enter name: "))
                a3 = float(input("Enter Marks in English: "))
                a4 = float(input("Enter Marks in Maths: "))
                a5 = float(input("Enter Marks in Physics: "))
                a6 = float(input("Enter Marks in Chemistry: "))
                a7 = float(input("Enter Marks in CS: "))
                globals()["Rollno"+ str(a1)] = {"Rollno":a1,"Name":a2,"EnMark":a3,"MaMark":a4,"PhyMark":a5,"CheMark":a6,"CSMark":a7}
                json.dump(globals()["Rollno"+str(a1)],a)
            c = str(input("Wants to enter more record (y/n)?: "))
            if c == "y":
                CreatePupilRecord()
            else:
                mainmenu()
    except FileExistsError:
        print("Roll Number đã tồn tại")
        mainmenu()
########################################################     
def DisplayAllPupilsRecords():
    path = os.path.dirname(os.path.abspath(__file__))
    DataStorage = [a for a in os.listdir(path)if a.endswith('.json')]   #lấy directory của py(file py vs json chung folder)
    print("\nPUPIL DETAILS..")
    for a in DataStorage:
        with open(str(a),"r") as b:
            data = json.load(b)
            print(f"Roll Number: {data['Rollno']}")
            print(f"Name: {data['Name']}")
            print(f"English: {data['EnMark']}")
            print(f"Maths: {data['MaMark']}")
            print(f"Physics: {data['PhyMark']}")
            print(f"Chemistry: {data['CheMark']}")
            print(f"CS: {data['CSMark']}")
            print("\n")
    mainmenu()
########################################################
def SearchPupilRecord():
    num = int(input("Enter the rollno you want to search: "))
    c = "Rollnumber" + str(num) + ".json"
    if os.path.isfile(c):
        with open(str(c),"r") as a:
            data = json.load(a)
            print("\nPUPIL DETAILS..")
            print(f"Roll Number: {data['Rollno']}")
            print(f"Name: {data['Name']}")
            print(f"English: {data['EnMark']}")
            print(f"Maths: {data['MaMark']}")
            print(f"Physics: {data['PhyMark']}")
            print(f"Chemistry: {data['CheMark']}")
            print(f"CS: {data['CSMark']}")
    else:
        print("Roll Number không tồn tại")
    mainmenu()
##############################################################
def changedata(tenfile, key, val):
    with open(tenfile,'r') as a:
        data = json.load(a)
        data[key] = val
    with open(tenfile, "w") as a:
        json.dump(data, a)

def ModifyPupilRecord(): 
    print("\nMODIFY RECORD")
    num = int(input("Enter roll number: "))
    c = "Rollnumber" + str(num) + ".json"
    if os.path.isfile(c):
        with open(str(c),"r") as a:
            data = json.load(a)
                     
            print(f"Name: {data['Name']}")
            d = str(input("Wants to edit(y/n)? "))
            if d == "y":
                a = str(input("Enter the name "))
                changedata(str(c),"Name",a)
                   
            print(f"English: {data['EnMark']}")
            d = str(input("Wants to edit(y/n)? "))
            if d == "y":
                a = float(input("English marks: "))
                changedata(str(c),"EnMark",a)
            
            print(f"Maths: {data['MaMark']}")
            d = str(input("Wants to edit(y/n)? "))
            if d == "y":
                a = float(input("Maths marks: "))
                changedata(str(c),"MaMark",a)
            
            print(f"Physics: {data['PhyMark']}")
            d = str(input("Wants to edit(y/n)? "))
            if d == "y":
                a = float(input("Physics marks: "))
                changedata(str(c),"PhyMark",a)
            
            print(f"Chemistry: {data['CheMark']}")
            d = str(input("Wants to edit(y/n)? "))
            if d == "y":
                a = float(input("Chemistry marks: "))
                changedata(str(c),"CheMark",a)
                
            print(f"CS: {data['CSMark']}")
            d = str(input("Wants to edit(y/n)? "))
            if d == "y":
                a = float(input("CS marks: "))
                changedata(str(c),"CSMark",a)
                
        with open(str(c),"r") as a:
            data = json.load(a)
            print("\nPUPIL DETAILS..")
            print(f"Roll Number: {data['Rollno']}")
            print(f"Name: {data['Name']}")
            print(f"English: {data['EnMark']}")
            print(f"Maths: {data['MaMark']}")
            print(f"Physics: {data['PhyMark']}")
            print(f"Chemistry: {data['CheMark']}")
            print(f"CS: {data['CSMark']}")
    mainmenu()    
###############################################################
            
    
def DeleteRecord():
    print("\nDELETE RECORD")
    num = int(input("Enter roll number: "))
    c = "Rollnumber" + str(num) + ".json"
    if os.path.isfile(c):
        with open(str(c),"r") as a:
            data = json.load(a)
            print("\nPUPIL DETAILS..")
            print(f"Roll Number: {data['Rollno']}")
            print(f"Name: {data['Name']}")
            print(f"English: {data['EnMark']}")
            print(f"Maths: {data['MaMark']}")
            print(f"Physics: {data['PhyMark']}")
            print(f"Chemistry: {data['CheMark']}")
            print(f"CS: {data['CSMark']}")
    os.remove(str(c))
    print("record found and deleted")
    mainmenu()
def Report():
    print("1. CLASS RESULT")
    print("2. PUPIL REPORT CARD")
    print("3. BACK TO MAIN MENU")
    a = int(input("Enter choice(1-3): "))
    if a == 1:
        ClassResult()
    elif a == 2:
        SearchPupilRecord()
    elif a == 3:
        mainmenu()
    else:
        print("Invalid option, xin hãy chọn lại")
        Report()
def ClassResult():
    path = os.path.dirname(os.path.abspath(__file__))
    DataStorage = [a for a in os.listdir(path)if a.endswith('.json')]
    blankspace=" "*7
    print(f"Rollno{blankspace}Name{blankspace}English{blankspace}Maths{blankspace}Physics{blankspace}Chemistry{blankspace}CS")
    for a in DataStorage:
        with open(str(a),"r") as b:
            data = json.load(b)
            print(f"{data['Rollno']}{blankspace}{data['Name']}{blankspace}{data['EnMark']}{blankspace}{data['MaMark']}{blankspace}{data['PhyMark']}{blankspace}{data['CheMark']}{blankspace}{data['CSMark']}")
    print("\n")
    mainmenu()

mainmenu()