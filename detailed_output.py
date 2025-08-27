##########################################################
#                                                        #
#   Code up a PythonProgram that uses a function         #
#   to create a detailed output message to the user      #
#   after finding the largest of three numbers. The      #
#   detailed output statement should look something      #
#   like this:                                           #
#                                                        #
#   Message to User: You entered three numbers, 32,      #
#   57, and 99. The first whole number you entered       #
#   was assigned to a variable named num1, the           #
#   second to (57) to num2, and finally the third (99)   #
#   was assigned to num3. Your inout was processed and   #
#   the largest number you entered was 99, which         #
#   belonged to an integer variable named num3.          #
#                                                        #
#   This is a little advanced and will required more     #
#   coding to keep track of the variablke name that      #
#   contained the largest of three.                      #
#                                                        #
##########################################################

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

def num_assign(b1, b2, b3, lgnum):
    nlarge = ''
    if lgnum == b1:
        nlarge = 'num1'
    elif lgnum == b2:
        nlarge = 'num2'
    else:
        nlarge = 'num3'
    return nlarge

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
nlarge = num_assign(n1, n2, n3, lgnum)

print(f"""You entered 3 numbers, {n1}, {n2}, and {n3}. The first whole number you entered was assigned to a variable
      num1, the second ({n2}) to num2, and finally the third ({n3}) was assigned to num3. Your input was processed
      and the largest number you entered was {lgnum} which was assigned to an interger variable named {nlarge}""")