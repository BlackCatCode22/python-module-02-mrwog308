########################################################
#                                                      #
#   Write a Python program that uses nested if         #
#   statements (nested decisions) to get three         #
#   integers from the user and outputs the largest     #
#   of the three.                                      #
#                                                      #
########################################################

def largest_of_3(a, b, c):
    if a >= b:
        if a >= c:
            lgnum = a
        else:
            lgnum = c
    else:
        if b >= c:
            lgnum = b
        else:
            lgnum = c
    return lgnum

def check_numeric(n1, n2, n3):
    try:
        n1 = int(num1)
        n2 = int(num2)
        n3 = int(num3)
    except:
        print('ERROR!, Please enter numeric input')
        quit()
    return n1, n2, n3

num1 = input("Enter First Number: ")
num2 = input("Enter Second Number: ")
num3 = input("Enter Third Number: ")

n1,n2,n3 = check_numeric(num1, num2, num3)
lgnum = largest_of_3(n1, n2, n3)
print("The largest number is:", lgnum)