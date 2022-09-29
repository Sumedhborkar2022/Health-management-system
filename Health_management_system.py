import datetime
try:
    def gettime():
        return datetime.datetime.now()
    def take(k):
        if k == 1:
            c = int(input("Enter 1 for exercise and 2 for food:"))
            if(c == 1):
                Value = input("type here\n")
                with open("harry-exercise.txt","a") as op:
                    op.write(str([str(gettime())])+": " + Value + "\n")
                print("Sucessfully written")    
            elif(c == 2):
                Value = input("type here\n")
                with open("harry-food.txt","a") as op:
                    op.write(str([str(gettime())])+": " + Value + "\n")
                print("Sucessfully written") 
        elif k == 2:
            c = int(input("Enter 1 for exercise and 2 for food:"))
            if(c == 1):
                Value = input("type here\n")
                with open("rohan-exercise.txt","a") as op:
                    op.write(str([str(gettime())])+": " + Value + "\n")
                print("Sucessfully written")    
            elif(c == 2):
                Value = input("type here\n")
                with open("rohan-food.txt","a") as op:
                    op.write(str([str(gettime())])+": " + Value + "\n")
                print("Sucessfully written")                  
        elif k == 3:
            c = int(input("Enter 1 for exercise and 2 for food:"))
            if(c == 1):
                Value = input("type here\n")
                with open("hammad-exercise.txt","a") as op:
                    op.write(str([str(gettime())])+": " + Value + "\n")
                print("Sucessfully written")    
            elif(c == 2):
                Value = input("type here\n")
                with open("hammad-food.txt","a") as op:
                    op.write(str([str(gettime())])+": " + Value + "\n")
                print("Sucessfully written")                 
        else:
            print("Plz enter between given numbers,(harry - 1,rohan - 2, hammad - 3)")

    def retrieve(k):
        if k == 1:
            c = int(input("Enter 1 for exercise and 2 for food:"))        
            if (c == 1):
                with open("harry-exercise.txt") as op:
                    for i in op:
                        print(i,end="")
            elif(c==2):
                with open("harry-food.txt") as op:
                    for i in op:
                        print(i,end="")                        
        elif k == 2:
            c = int(input("Enter 1 for exercise and 2 for food:"))        
            if (c == 1):
                with open("rohan-exercise.txt") as op:
                    for i in op:
                        print(i,end="")
            elif(c==2):
                with open("rohan-food.txt") as op:
                    for i in op:
                        print(i,end="")
        elif k == 3:                 
            c = int(input("Enter 1 for exercise and 2 for food:"))        
            if (c == 1):
                with open("hammad-exercise.txt") as op:
                    for i in op:
                        print(i,end="")
            elif(c==2):
                with open("hammad-food.txt") as op:
                    for i in op:
                        print(i,end="")
        else:
            ("Please, enter valid value")                                                     
    print("Health managment system")
    a = int(input("Enter 1 for log and 2 for retrieve:"))

    if a == 1:
        b = int(input("Press harry - 1,rohan - 2, hammad - 3:")) 
        take(b)
    else:
        b = int(input("Press harry - 1,rohan - 2, hammad - 3:")) 
        retrieve(b)
except Exception as e:
    print(e)        
