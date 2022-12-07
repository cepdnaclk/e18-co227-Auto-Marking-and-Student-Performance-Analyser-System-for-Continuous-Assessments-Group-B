#marks as a line chart

from http import client
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creads=ServiceAccountCredentials.from_json_keyfile_name("creads.json",scope)

client1=gspread.authorize(creads)


sheet1=client1.open("Testing").get_worksheet(0)

student_marks_line=[]
data = sheet1.get_all_records()

num=1
for student in data:
    if student['submission_timestamp']!='':
        mark=student['points_awarded']
        student_marks_line.append([num,mark])
        num+=1




print(student_marks_line)
