from sys import argv
name_script, prod, hourly_rate, prize = argv

salary = float(prod) * float(hourly_rate) + float(prize)
print(f"The salary is {salary}")
