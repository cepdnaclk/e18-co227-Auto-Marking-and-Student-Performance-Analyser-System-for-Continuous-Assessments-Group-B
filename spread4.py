#dispalying the students with their enum,marks and assignment submission status

from http import client
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask,render_template





scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creads=ServiceAccountCredentials.from_json_keyfile_name("creads.json",scope)

client1=gspread.authorize(creads)

assignments_avg=[]
assignments_individual_dict={}
assignments_individual=[]
assignments_avg.append(['Assigment Name','Average Marks'])
assignments_individual.append(['Marks'])

number=1
flag=True


enums=client1.open("Testing").get_worksheet(0).col_values(1)


while flag:
    try:
        sheet=client1.open("Testing").get_worksheet(number)
        data=sheet.get_all_records()
        #Getting Avg Marks for all assignments
        assignment_name=data[0]['assignment_name']
        assignments_individual[0].append(assignment_name)

        tot_marks=0
        for student in data:
            tot_marks=(((student['points_awarded']*1.0)/student['points_available'])*100)+tot_marks

        avg_mark=tot_marks/len(data)
        assignments_avg.append([assignment_name,avg_mark])
        number+=1

        

    except Exception as e:
        print("All sheets done")
        flag=False

print("Number of sheets: ",number)





for enum in enums:
    empty=[]
    for val in range(number-1):
        empty.append(0)
    assignments_individual_dict[enum]=empty


flag=True
sheet_number=1

while flag:
    try:
        sheet=client1.open("Testing").get_worksheet(sheet_number)
        data=sheet.get_all_records()


        for student in data:
            stud_enum=student['roster_identifier']
            stud_mark=((student['points_awarded']*1.0)/student['points_available'])*100
            assignments_individual_dict[stud_enum][sheet_number-1]=stud_mark


        sheet_number+=1

    except Exception as e:
        print("All sheets done")
        flag=False




for enum in enums:
    lis=[enum]
    for mark in assignments_individual_dict[enum]:
        lis.append(mark)

    assignments_individual.append(lis)

print(assignments_individual)
print("\n\n\n")
print(assignments_avg)


