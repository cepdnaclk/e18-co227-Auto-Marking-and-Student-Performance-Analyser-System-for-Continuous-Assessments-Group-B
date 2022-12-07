#app.py
#pie chart showing students who have accepted and not accepted the assignment
#Student acception of the assignment
from http import client
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template



scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creads=ServiceAccountCredentials.from_json_keyfile_name("creads.json",scope)

client1=gspread.authorize(creads)

sheet2=client1.open("Testing").get_worksheet(0)
sheet1=client1.open("Testing").get_worksheet(1)

#pie chart showing students who have accepted and not accepted the assignment
#Student acception of the assignment

submission_status={'Status':'Number'}

data = sheet1.col_values(5)
all_e_num=sheet2.col_values(1)


submission_status['Accepted']=len(data)-1

submission_status['Not Accepted']=len(all_e_num)-len(data)+1
 


print(submission_status)

#dispalying the students with their enum,marks and assignment submission status

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
        ind_stu.append("Yes")
    else:
        ind_stu.append(0)
        ind_stu.append("No")

    student_performance.append(ind_stu)

print(student_performance)
 

#For Part2 ----------------------------------------------------------------------------------------

assignments_avg=[] #column chart showing average marks for an assignment
assignments_individual_dict={}
assignments_individual=[] #bar chart showing individual marks
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

app = Flask(__name__)

print(assignments_individual)
   
@app.route('/')
def google_pie_chart():
    return render_template('com.html',data=submission_status, student_data=student_performance, data_3=assignments_individual, data_4=assignments_avg)
 
if __name__ == "__main__":
    app.run()