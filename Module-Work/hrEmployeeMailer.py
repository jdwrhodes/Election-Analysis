#%%
import os
import csv

#%%
filePath = os.path.join('.', 'newEmployees.csv')

#%%


# %%
class NewEmployees():
    def __init__(self, fName, lName, ssn):
        self.first_name = fName
        self.last_name = lName
        self.ssn: str = ssn
        self.valid_ssn = False

    def checkSSN(self):
        ssn_int = self.ssn.replace('-', '')
        if len(ssn_int) == 9:
            self.valid_ssn = True
        else:
            self.valid_ssn = False 
# %%
welcomeEmailList = []
invalidSSNEmailList = []

#%%
with open(file = filePath, mode='r') as employees:
    file_object = csv.reader(employees, delimiter = ',')
    print(file_object)
    for row in file_object:
        print(row)
        aNewEmployee = NewEmployees(fName=row[0], lName=row[1], ssn=row[2])
        aNewEmployee.checkSSN()
        if aNewEmployee.valid_ssn:
            welcomeEmailList.append(aNewEmployee)
        else:
            invalidSSNEmailList.append(aNewEmployee)

# %%
welcomeEmailList
# %%
for employee in welcomeEmailList:
    welcomeMessage = f'Hi {employee.first_name}, {employee.last_name}'
    print(welcomeMessage)

for employee in invalidSSNEmailList:
    invalidSSNMessage = f'Hi {employee.first_name}, {employee.last_name}. Your SSN doesn''t seem to be valid. Please try again or email HR.'
    print(invalidSSNMessage)
# %%
