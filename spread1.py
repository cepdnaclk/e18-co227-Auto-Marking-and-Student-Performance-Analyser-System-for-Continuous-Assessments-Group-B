#dispalying the students with their enum,marks and assignment submission status

from http import client
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask,render_template





scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creads=ServiceAccountCredentials.from_json_keyfile_name("creads.json",scope)

client1=gspread.authorize(creads)

sheet2=client1.open("Testing").get_worksheet(1)
sheet1=client1.open("Testing").get_worksheet(0)

student_performance=[]
student_marks={}
data = sheet1.get_all_records()
all_e_num=sheet2.col_values(1)

for student in data:
    if student['submission_timestamp']!='':
        num=student['roster_identifier'].split(',')[0]
        student_marks[num]=student['points_awarded']




for enum in all_e_num:
    ind_stu=[enum]
    if enum in student_marks.keys():
        ind_stu.append(student_marks[enum])
        ind_stu.append(True)
    else:
        ind_stu.append(0)
        ind_stu.append(False)

    student_performance.append(ind_stu)

print(student_performance)
