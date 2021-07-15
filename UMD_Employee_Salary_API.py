import requests

#Connects with the Diamondback news API and gets the information in JSON format.
r = requests.get("https://api.dbknews.com/salary/year/2021?search=&sortby=salary&order=desc&page=1").json()

#Gets the employee's name, salary and their title.
print("Employee with the highest salary in UMD:")
print("\tName: " + r.get('data')[0].get('Employee') + "\n\tSalary: " + r.get('data')[0].get('Salary') + "\n\tPosition: " + r.get('data')[0].get("Title"))
