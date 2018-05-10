#boss

import csv
import os

csvpath = ("employee_data1.csv"  and "employee_data1.csv")

employee_id = []
first_name = []
last_name = []
DOB = []
SSN = []
State = []

us_state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
    'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN',
    'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
    'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
    'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX',
    'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
    'Wisconsin': 'WI', 'Wyoming': 'WY',
}

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)

    for row in csvreader:
        employee_id.append(row[0])
        name = row[1].split(" ") 
        first_name.append(name[0]) 
        last_name.append(name[1])

        bdate = row[2].split("-") 
        new_db = bdate[1] + "/" + bdate[2] + "/" + bdate[0] 
        DOB.append(new_db)


        SSN_split = row[3].split("-") 
        new_SSN = "***-**-" +SSN_split[2] 
        SSN.append(new_SSN)
     

        State.append(us_state_abbrev[row[4]])


employees = zip(employee_id, first_name, last_name, DOB, SSN, State)

output_file = ('employee_data_clean_1.csv')

with open(output_file, 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')

    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    for employee in employees:
        writer.writerow(Employee)
