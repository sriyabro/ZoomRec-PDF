from __future__ import unicode_literals
import tkinter as tk
from tkinter import filedialog as fd
import pdfkit as pdf
import datetime
import os
import sys

config = pdf.configuration(wkhtmltopdf="bin\wkhtmltopdf.exe")
options = {
    'page-size': 'A4',
    'margin-top': '1.0in',
    'margin-right': '1.0in',
    'margin-bottom': '1.0in',
    'margin-left': '1.0in',
    'encoding': "UTF-8",
    'no-outline': None
}

root = tk.Tk()  # Window object
root.title("Zoom Class Records - PDF")

canvas = tk.Canvas(root, height=450, width=800)

lbl1 = tk.Label(root, text="Date")
lbl1.grid(column=0, row=0)
date = tk.Entry(root, width=50, fg="#0000FF")
today = datetime.date.today()
date.insert(tk.END, today.strftime("%d/%m/%Y"))
date.grid(column=1, row=0)

lbl2 = tk.Label(root, text="Time")
lbl2.grid(column=0, row=1)
now = datetime.datetime.now()
time = tk.Entry(root, width=50, fg="#0000FF")
time.insert(tk.END, now.strftime("%I:%M %p"))
time.grid(column=1, row=1)

lbl3 = tk.Label(root, text="Subject")
lbl3.grid(column=0, row=2)
subject = tk.Entry(root, width=50, fg="#0000FF")
subject.grid(column=1, row=2)

lbl4 = tk.Label(root, text="Grade")
lbl4.grid(column=0, row=3)
grade = tk.Entry(root, width=50, fg="#0000FF")
grade.grid(column=1, row=3)

lbl5 = tk.Label(root, text="Link")
lbl5.grid(column=0, row=4)
link = tk.Entry(root, width=50, fg="#0000FF")
link.grid(column=1, row=4)

lbl6 = tk.Label(root, text="Time which the link was sent to the student group")
lbl6.grid(column=0, row=5)
link_time = tk.Entry(root, width=50, fg="#0000FF")
link_time.insert(tk.END, now.strftime("%I:%M %p"))
link_time.grid(column=1, row=5)

lbl7 = tk.Label(root, text="Unit")
lbl7.grid(column=0, row=6)
unit = tk.Entry(root, width=50, fg="#0000FF")
unit.grid(column=1, row=6)

lbl8 = tk.Label(root, text="Subject content covered")
lbl8.grid(column=0, row=7)
content = tk.Entry(root, width=50, fg="#0000FF")
content.grid(column=1, row=7)

lbl9 = tk.Label(root, text="Activities")
lbl9.grid(column=0, row=8)
activities = tk.Entry(root, width=50, fg="#0000FF")
activities.grid(column=1, row=8)

lbl10 = tk.Label(root, text="Homework")
lbl10.grid(column=0, row=9)
homework = tk.Entry(root, width=50, fg="#0000FF")
homework.grid(column=1, row=9)

lbl11 = tk.Label(root, text="No of students participated")
lbl11.grid(column=0, row=10)
no_stu = tk.Entry(root, width=50, fg="#0000FF")
no_stu.grid(column=1, row=10)


btn = tk.Button(root, text="Enter student names", command=lambda: stud())
btn.grid(column=2, row=10)

students = []

#generates text boxes acc. to no. of students
def stud():
    try:
        for i in range(int(no_stu.get())):
            lbl12 = tk.Label(root, text="Student " + str(i + 1))
            lbl12.grid(column=0, row=11 + i)
            stu = tk.Entry(root, width=50, fg="#0000FF")
            stu.grid(column=1, row=11 + i)
            students.append(stu)
            
    except:
        no_stu.delete(0, tk.END)
        no_stu.insert(tk.END, "Please enter an Integer")
        no_stu.select_range(0, tk.END)


    lbl13 = tk.Label(root, text="").grid(columnspan=3, row=12+i) #seperator

    #sets file name as grade-subject-date
    out_name = "Grade " + str(grade.get()) + "-" + str(subject.get()) + "-" + now.strftime("%d-%m-%Y")

    lbl_save = tk.Label(root, text="Save file as")
    lbl_save.grid(column=0, row=13+i)

    txt_out_name = tk.Entry(root, width=50, fg="#0000FF")
    txt_out_name.insert(tk.END, out_name)
    txt_out_name.grid(column=1, row=13+i)

    btn_save_path = tk.Button(root, text="   Browse   ", command=lambda: save_path(i, txt_out_name, out_name))
    btn_save_path.grid(column=2, row=13+i)



#opens explorer to select save path
def save_path(i, txt_out_name, out_name):
    out_name = fd.asksaveasfilename(initialdir="%USERPROFILE%/Desktop", initialfile=out_name, filetypes=[("PDF files", ".pdf")])
    txt_out_name.delete(0, tk.END)
    txt_out_name.insert(0, out_name)

    message = tk.StringVar()

    btn_pdf = tk.Button(root, text="Generate PDF", command=lambda: pdf_out(out_name, message,i))
    btn_pdf.grid(column=2, row=14 + i)

    lbl12 = tk.Label(root, textvariable=message, height=4)
    lbl12.grid(columnspan=3, row=15+i)


#generates pdf
def pdf_out(out_name, message,i):
    html_text = '''
            <html>
            <head>
            <style>
            body {font-family: Arial, Helvetica, sans-serif;}
            p {font-size: 18;}
            </style>
            </head>
            <body>
                <h2 style="text-align: center;">HARVARD MEDHA INTERNATIONAL SCHOOL</h2>
                <h3 style="text-align: center;">ONLINE CLASSES CONDUCTED VIA ZOOM</h3>
                </br>
                <p><b>Date: </b>''' + str(date.get()) + '''</p>
                <p><b>Time: </b>''' + str(time.get()) + '''</p>
                <p><b>Subject: </b>''' + str(subject.get()) + '''</p>
                <p><b>Grade: </b>''' + str(grade.get()) + '''</p>
                <p><b>Meeting invitaion: </b>''' + str(link.get()) + '''</p>
                <p><b>Time which the link was sent to the student group: </b>''' + str(link_time.get()) + '''</p>
                <p><b>Unit: </b>''' + str(unit.get()) + '''</p>
                <p><b>Subject content covered: </b>''' + str(content.get()) + '''</p>'''
    
    if str(activities.get()) != "":
        html_text+= '''<p><b>Activities: </b>''' + str(activities.get()) + '''</p>'''

    if str(homework.get()) != "":
        html_text+= '''<p><b>Homework: </b>''' + str(homework.get()) + '''</p>'''
    

    student_names = ""

    for j in students: #format students names as html string
        student_names = student_names + "<li>" + str(j.get()) + "</li>"

    html_text+='''
            <p><b>Students participated: </b><ol>''' + student_names + '''</ol></p>
        </body>
        </html>'''

    message.set("Generating PDF...")
 
    #generate pdf
    try:
        pdf.from_string(html_text, str(out_name)+".pdf", configuration=config, options=options)
    
    except:
        message.set("Some error occured !! Try again")


    else:
        message.set("PDF created successfully !")
        
    tk.Button(root, text="  Reset  ", command=restart_program).grid(column=2, row=15 + i)
    
    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

## raw print on text area
# def doc_out(i):
#     txt = tk.Text(root)
#     txt.grid(columnspan=3, row=13 + i)
#     text_temp = "Date: " + str(date.get()) + "\nTime: " + str(time.get()) + "\nSubject: " + str(subject.get()) + "\nGrade: " + str(grade.get()) + "\nZoom meeting link: " + str(link.get()) + "\nTime which the link was sent to the student group: " + str(link_time.get()) + "\nUnit: " + str(unit.get()) + "\nSubject content covered: " + str(content.get()) + "\nActivities: " + str(activities.get()) + "\nHomework: " + str(homework.get()) + "\nStudents participated: \n"
#     students_txt = ""
#     for j in students:
#         students_txt = students_txt + "\t" + str(j.get()) + "\n"
#     txt.insert(tk.END, text_temp + students_txt)


root.mainloop()  # End Window object
