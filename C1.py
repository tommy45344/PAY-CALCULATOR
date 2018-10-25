import sys

def Pay_Calculator():
    while True:
        Week_Rate = 17.70
        Public_Rate = Week_Rate * 2.5
        Sunday_Rate = Week_Rate * 1.5

        while True:
            Week_Hours = (input("How many hours did you work on weekdays and Saturday? "))
            if Week_Hours.isdigit():
                break
            else:
                print('Invalid input.')

        while True:
            Sunday_Hours = (input("How many hours did you work Sunday? "))
            if Sunday_Hours.isdigit():
                break
            else:
                print('Invalid input.')

        while True:
            Public_Hours = (input("How many hours did you work, if any on a public holiday? "))
            if Public_Hours.isdigit():
                break
            else:
                print('Invalid input.')

        Week_Hours = int(Week_Hours)
        Sunday_Hours = int(Sunday_Hours)
        Public_Hours = int(Public_Hours)

        Week_Pay = Week_Hours * Week_Rate
        Sunday_Pay = Sunday_Hours * Sunday_Rate
        Public_Pay = Public_Hours * Public_Rate
        Total_Pay = Sunday_Pay + Week_Pay + Public_Pay
        Bank_Pay = Total_Pay * .25

        Week_Pay = format(Week_Pay, '.2f')
        Sunday_Pay = format(Sunday_Pay, '.2f')
        Public_Pay = format(Public_Pay, '.2f')
        Total_Pay = format(Total_Pay, '.2f')
        Bank_Pay = format(Bank_Pay, '.2f')

        print ("You earned", '${}'.format(Week_Pay),"during the week and Saturday working", Week_Hours ,"hours.")
        print ("You earned", '${}'.format(Sunday_Pay) ,"on Sunday working", Sunday_Hours ,"hours.")
        print ("You earned", '${}'.format(Public_Pay) ,"on the the Public holiday working", Public_Hours ,"hours.")
        print ("In total you earned", '${}'.format(Total_Pay) ,"this week.")
        print ("Since you earned", '${}'.format(Total_Pay), "you should bank", '${}'.format(Bank_Pay))

        while True:
            Restart_Program = input("Do you want to restart the program? ")
            if Restart_Program in ('yes', 'YES', 'Yes'):
                break
            else:
                sys.exit()
