 # Your Name
 # Date
  # Assignment Name
  # A brief description of the project
#request employee information
name = input("Enter employee's name or \"Done\" to terminate: ")
# create accumulator variables for overtime pay, reg pay, gross pay, and one to count number of employees entered
overTime_total = 0.0
regPay_total = 0.0
gross_total = 0.0
Employee_count = 0.0
while name !="Done":
    #add one to Employee_count var
    Employee_count = +1
    #ask for employee information
    hoursWorked = float(input("How many hours did "+name+" work? "))
    payRate = float(input("What is "+name+"'s pay rate? "))
    #evaluate overtime
    if hoursWorked >40 :
        print("regular pay")

    else:
        print("over time pay")


    #Display output
    print("\nEmployee's name:  ",name,"\n")
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime":<12}{"Overtime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
    print('-'*87)
    #print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime":<12}{"Overtime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
    print()
    #ask user for another employee name
    name = input("Enter employee's name or \"Done\" to terminate: ")
#Display final results
#display overtime total, regular pay total, gross pay total, and number of employees entered
print("\nTotal number of employees entered: ", Employee_count, sep="")
print("Total amount paid for overtime: $", format(overTime_total,".2f"), sep="")
print("Total amount paid for regular hours: $", format(regPay_total,".2f"), sep="")
print("Total amount paid in gross: $", format(gross_total,".2f"), sep="")








