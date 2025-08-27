########################################################
#                                                      #
#   Watch the video and code up the Payroll Program    #  
#   with Overtime (Worked Exercise 3.1)                #
#                                                      #
########################################################

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
fh = float(hours)
fr = float(rate)
if fh > 40:
    regular_pay = 40 * fr
    overtime_pay = (fh - 40) * (fr * 1.5)
    pay = regular_pay + overtime_pay
else:
    pay = fh * fr

print('Straight Pay: $',regular_pay if fh > 40 else pay)
print('Overtime Pay: $', overtime_pay if fh > 40 else 0)
print('Total Pay: $', pay)
print('Straight Time hours:', float(40) if fh > 40 else fh)
print('Overtime hours:', fh - 40 if fh > 40 else 0)
