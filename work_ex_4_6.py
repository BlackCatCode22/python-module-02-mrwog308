########################################################
#                                                      #
#   Watch the video and code up a program that uses    #
#   a function named comput_pay (Worked Exercise 4.6)  #
#                                                      #
########################################################

def compute_pay(hours, rate):
    # print ('In compute_pay', hours, rate)
    regular_pay = 0
    overtime_pay = 0
    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        pay = regular_pay + overtime_pay
    else:
        pay = hours * rate
    return pay, overtime_pay, regular_pay

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
    fh = float(hours)
    fr = float(rate)
except:
    print('ERROR!, Please enter numeric input')
    quit()

pay, overtime_pay, regular_pay = compute_pay(fh, fr)

print('Straight Pay: $',regular_pay if fh > 40 else pay)
print('Overtime Pay: $', overtime_pay if fh > 40 else 0)
print('Total Pay: $', pay)
print('Straight Time hours:', float(40) if fh > 40 else fh)
print('Overtime hours:', fh - 40 if fh > 40 else 0)