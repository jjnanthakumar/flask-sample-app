import pandas as pd
import random
departments = ['IT', 'DEVELOPMENT', 'HR']
Roles = ['Junior Software Developer', 'Senior Software Developer', 'IT Admin','Project Manager','Project Lead', 'Lead Analyst']
df = pd.read_csv('employees.csv')
df.insert(0, 'Id', [i for i in range(1, df.shape[0]+1)])
df.insert(1, 'Code', [i for i in range(10190, df.shape[0]+10190)])
df.insert(2, 'Department', [departments[random.randint(0, len(departments)-1)]
          for i in range(1, df.shape[0]+1)])
df.insert(3, 'Role', [Roles[random.randint(0, len(Roles)-1)]
          for i in range(1, df.shape[0]+1)])
df.rename(columns={'First Name': 'Name'}, inplace=True)

df.to_csv('employees.csv', index= False)