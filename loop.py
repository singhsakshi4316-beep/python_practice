#loop with using range ()function
#for variable in range (start,stop,step):
#start:indexing 0 start beginning of the loop
#stop:do not include the stop value
#step:gap between the values
# %%
for i in range(1, 11):
    print(i)
# %%
# %%
# WAP to calculate the average in a list
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print("Average:", average)
# %%
#while loop syntax
#while condition:
i = 1
while i <= 5:
    print(i)
    i += 1

    #wap to print odd and even numbers from 1 to 20 using for loop and conditional statements
for num in range(1, 20):
    if num % 2 == 0:
        print(num, "is even" ,end=", ")
    else:
        print(num, "is odd" ,end=", ")

#continue statement
#for i in range(start,stop,step):
  #  if condition:
   #     continue
    #remaining code

    for i in range(1, 6):
        if i == 4:
            continue
        print(i)

        #wP ONLY PRINT ODD NUMBERS
        for num in range(1, 20, 2):
            print(num, end=" , ")
            continue
        print("\n")
        #list 
lst=[10,20,30,40]
        
#function with parameters 
def add(a,b):
     result= a+b
     print(result)

def sub(a,b):
    result= a-b
    print(result)
 #function calling

 add(50,40)
 sub(10,20) 


def check_odd(num):
    if num % 2!=0:
        return"odd"
     else:
        return"even"
 n=int(input("Enter a number:"))   

result=check_odd(n)
print(result)

#wap to check whether a number is prime or not
 def check_prime(num):
    if num < 2:
        return Falsealse
    for i in range(2,num):
        if num%i == 0:
            return False
    return True
#Take user input
n=int(input("Enter a number:"))
if check_prime(n):
print(n,"is a prime number")

#loop using print pattern with rule

#step 1:
#step 2:

#wap to print triangle pattern
# *
# * *
# * * *
# * * * *

rows = int(input("Enter row:"))
#outer loop

for i in range(1,6):
    for j in range(1,i+1):
        print("*", end="")
    print()

    # reverse pattern
for i in range()
    for j in range()
        print("*", end="")

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
    
    

# %%
