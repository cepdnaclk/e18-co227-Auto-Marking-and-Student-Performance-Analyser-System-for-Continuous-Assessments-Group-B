#pie chart showing students who have accepted and not accepted the assignment
#Student acception of the assignment
from http import client
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask,render_template

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creads=ServiceAccountCredentials.from_json_keyfile_name("creads.json",scope)

client1=gspread.authorize(creads)

app=Flask(__name__)
@app.route('/')
def google_pie_chart():
    return render_template("index.html",data=submission_status)

sheet2=client1.open("Testing").get_worksheet(1)
sheet1=client1.open("Testing").get_worksheet(0)


submission_status=[['Status','Number']]
data = sheet1.col_values(5)
all_e_num=sheet2.col_values(1)


submission_status.append(['Accepted',len(data)-1])
submission_status.append(['Not Accepted',len(all_e_num)-len(data)+1])
 


print(submission_status)
