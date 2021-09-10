# Nmae:- Shubham Ingole
# Roll no:- 25

"""
Write a Python program to store marks scored in subject “Fundamental of Data 
Structure” by N students in the class. Write functions to compute following:
a) The average score of class 
b) Highest score and lowest score of class 
c) Count of students who were absent for the test
d) Display mark with highest frequency
"""
#input of marks 
Marks=[]
nos=int(input("enter the number of students in class:"))
for i in range(nos):
    x=input("enter the score of student: ")
    if (x!="ab"): #type(i)!=type(""): 
       Marks.append(int(x))
    else:
        Marks.append(x) 
print(Marks)

def main_menu():
    print("1. The Average score of class: ")
    print("2.Lowest and Higest scores of class: ")
    print("3. No of absent students of class: ")
    print("4.Higest frequency of marks: ")
    print("5.exit")

    ch=int(input("enter your choice: "))

    if ch==1:
        print("*------------------------------*")
        Avg_Score()
        print("*______________________________*", "\nEnter anather choice: ")
        main_menu()
    elif ch==2:
        print("*------------------------------*")
        High_Low_Marks()
        print("*______________________________*", "\nEnter anather choice: ")
        main_menu()

    elif ch==3:
        print("*------------------------------*")
        Absent_Students()
        print("*______________________________*", "\nEnter anather choice: ")
        main_menu()

    elif ch==4:
        print("*------------------------------*")
        Higest_Frequency_Marks()
        print("*______________________________*", "\nEnter anather choice: ")
        main_menu()

    elif ch==5:
        print("*------------------------------*", "\nSuccessfuly exited")
        exit (0)

    else:
        print("-----------------------------*")
        print("please enter valid option")
#average score calculation
def Avg_Score():
    cnt= 0
    sum= 0
    for i in Marks:
         if type(i)!=type(""):
            cnt= cnt+1 
            sum= sum+i
    #print("the sum is: " ,sum,"\nthe count of present students is :", cnt)
    avg = sum/cnt
    print("the average is :", avg)


#Max_Min
def High_Low_Marks():
    max= 0
    for i in Marks:
        if type(i)!=type(""):
            if i>max:
                max=i
    print("maximum score of class is:", max)

    min= 30
    for i  in Marks:
        if type(i)!=type(""):
            if i<min:
                min = i
    print("minimum score of class is:", min)

# two methods to find absent students in 
#Method 1
def Absent_Students():
    abs=0
    for i in Marks:
        if type(i)==type(""):
            abs=abs+1
    print("the absent students are:", abs ) #len(abs))

    #Method 2
    #abs=[]
    #for i in Marks:
    #    if type(i)==type(""):
    #        abs.append(i)
    #print("the no of absent students in exam is :", len(abs))


#now we want to find marks with higesht frequency
#to find the frequency of each marks
def Higest_Frequency_Marks():
    Count= []
    for i in range(31):
        cnt=0
        for j in Marks:
            if i==j:
                cnt=cnt+1
        Count.append(cnt)
    print(Count) 

    #the mark with maximum frequency 
    
    max= 0
    for i in range(31):
        if (Count[i]>max):
            max=Count[i]
            id=i
    if max==1:
        print("there is no such element")
        exit (0)
    for i in range(31):
        if max==Count[i]:
            print(i) 
main_menu()
