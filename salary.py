days=int(input("How many days do you work in a month?\n"))
hours=float(input("How many hours do you work in a day?\n"))
rate=float(input("What is your hourly rate?\n"))

salary = (days*hours*rate)
print(f"Your monthly salary is : {salary}")