                            #Question 1(To check 'is' operator on float and string)
#checking for float
m=3.339
n=3.339
bool = m is n  
print(bool) #The bool variable will be true thereby indicating that m and n variabe are pointing to same memory object

#checking for string
m="ajay"
n="ajay"
bool = m is n  
print(bool) #The bool variable will be true thereby indicating that m and n variabe are pointing to same memory object

                            #Question 2(To solve precedence)
bool = 1>3>4 
print(bool)
#The bool variable will be false since the associativity of precedence will be from left to right due to 1 being less than 3



                            #Question 3(To demonstrate the use of int,float and str functions)
#The int function will convert the entered string into an integer
age =int(input("enter the age"))
print(age,type(age))


#The float function will convert the integer 12 into a floating point number
float_number = float(12)
print(float_number,type(float_number))

#The string function will convert the integer number 139 into a string value
number = 139
string1 = str(number)
print(string1,type(string1))
