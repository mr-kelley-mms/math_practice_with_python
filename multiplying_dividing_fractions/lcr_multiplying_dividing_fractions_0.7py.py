#Luke R, Multiplying and Dviding Fractions, 5/06/19, version 0.7

print("Hello, my name is Fraction-Bot9000. I will multiply and divide fractions for you.\n")
user_name = input("What is your name? [Type your name and press ENTER.]\n")
print("Hello, ",user_name," how are you today?")

print("For this program, I need to know the numerator and the denominator for both fractions. \n")

# Variables for fraction 0.
numerator0 =0
denominator0 =0
print("The first fraction is", numerator0,"/",denominator0,".\n")

# Variables for fraction 1.
numerator1 =0
denominator1 =0
print("The second fraction is", numerator1,"/",denominator1,".\n")

print("When multiplying fractions you multiply the two numerators together.\n")
print("Then you will multiply the two denominators together.\n")

numerator0 = int(input("Type the first numerator and press enter.\n")) 
numerator1 = int(input("Type the second numerator and press enter.\n"))

denominator0 = int(input("Type the first denominator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))

print("The first fraction is", numerator0,"/",denominator0,".\n")
print("The second fraction is", numerator1,"/",denominator1,".\n")

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("The new fraction is", new_numerator,"/",new_denominator,".\n")

# This is where the division of the fractions will start.

print("To divide a fraction you will muiliply using the reciprocal or inverse of the second fraction. \n")

numerator2 = int(input("Type the first numerator and press enter.\n")) 
numerator3 = int(input("Type the second numerator and press enter.\n"))

denominator2 = int(input("Type the first denominator and press enter.\n"))
denominator3 = int(input("Type the second denominator and press enter.\n"))

print("The first fraction is", numerator2,"/",denominator2,".\n")
print("The second fraction is", numerator3,"/",denominator3,".\n")

new_numerator1 = numerator2 * denominator3
new_denominator1 = numerator3 * denominator2

print("The new fraction is", new_numerator1,"/",new_denominator1,".\n")