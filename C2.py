# Input for hourly pay
Week_Rate = float(input("What is your hourly pay? "))
Sunday_Rate = Week_Rate * 1.5
Public_Rate = Week_Rate * 2.5

# The directions for the user
Week_Hours = float(input("How many hours did you work on weekdays and Saturday? "))
Sunday_Hours = float(input("How many hours did you work Sunday? "))
Public_Hours = float(input("How many hours did you work, if any on a public holiday? "))

# The pay calucations for each day
Week_Pay = Week_Hours * Week_Rate
Sunday_Pay = Sunday_Hours * Sunday_Rate
Public_Pay = Public_Hours * Public_Rate
Total_Pay = Sunday_Pay + Week_Pay + Public_Pay
Savings = Total_Pay / 4

# The earnings that are printed on the screen 
print ("You earned", Week_Pay ,"during the week and Saturday working", Week_Hours ,"hours.")
print ("You earned", Sunday_Pay ,"on Sunday working", Sunday_Hours ,"hours.")
print ("You earned", Public_Pay ,"on the the Public holiday working", Public_Hours ,"hours.")
print ("In total you earned", Total_Pay ,"this week.")
print("Since you earned", Total_Pay ,"you should save", Savings , "this week.")
