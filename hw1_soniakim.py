#Homework Assignment for HW1
#October 10, 2020 I am modifying this .py file through Terminal.
x = 0
n = 3
while n < 10:
	x = x + n
	print(x, end = " ") 

#Question 1
def compute_emi(rate, N, PV, FV):
   while(1):
       try:
           PV = int(input("Please enter your principal amount borrowed, in integers: "))
           FV = int(input("Please enter the future value you want to attain after the last payment is made, in integers: "))
       except:
           print("Not an integer! Try again")
       else: print(PV+FV/((1+0.04)^20))*(0.04*((1+0.04)^20)/((1+0.04)^20)-1)

    print (PV+FV/((1+rate)^N))*(rate*((1+rate)^N)/((1+rate)^N)-1)

return (PV+FV/((1+0.04)^20))*(0.04*((1+0.04)^20)/((1+0.04)^20)-1)

#Question 2
import os
os.chdir("/Users/sk4490/Documents/computing_bs/homework/hw1")

myfile = open('question2.txt')
for line in myfile:
    print(line, end=" ")
myfile.close()
