import csv 

with open('names.csv',mode='w') as csvfile:
    fieldnames = ["first name","last name"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"first name":"satyam", "last name":"soni"})
    writer.writerow({"first name":"ankit", "last name":"jawre"})
    writer.writerow({"first name":"nilesh", "last name":"barasia"})