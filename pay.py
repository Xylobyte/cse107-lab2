employee = int(input("Enter the type of employee::\n(1: Manager; 2: Hourly worker; 3: Commission Worker; 4: Pieceworker): "))
if employee == 1:
    pay = float(input("Enter weekly salary: "))
    print("The manager's pay is " + str(format(pay, ".2f")))
elif employee == 2:
    salary = float(input("Enter the hourly salary: "))
    hours = float(input("Enter the total hours worked: "))
    pay = 0.00
    if(hours > 40):
        pay = (salary * 40) + ((salary * 1.5) * (hours - 40))
    else:
        pay = salary * hours
    print("The worker's pay is " + str(format(pay, ".2f")))
elif employee == 3:
    sales = int(input("Enter gross weekly sales: "))
    pay = 250 + (sales * 0.057)
    print("The commision worker's pay is " + str(format(pay, ".2f")))
elif employee == 4:
    pieces = int(input("Enter number of pieces made: "))
    ppp = float(input("Enter the wage per piece: "))
    pay = pieces * ppp
    print("The peiceworker's pay is " + str(format(pay, ".2f")))
else:
    print("Error; the given employee code is not valid.\nValid codes are:\n1: Manager; 2: Hourly worker; 3: Commission Worker; 4: Pieceworker")