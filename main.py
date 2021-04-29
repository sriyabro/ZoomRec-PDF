from __future__ import unicode_literals
import tkinter as tk
import datetime

root = tk.Tk()  # Window object
root.title("Zoom Classes")

canvas = tk.Canvas(root, height=450, width=800)

lbl1 = tk.Label(root, text="Date")
lbl1.grid(column=0, row=0)
date = tk.Entry(root, width=50, fg="#0000FF", )
today = datetime.date.today()
date.insert(tk.END, today.strftime("%d/%m/%Y"))
date.grid(column=1, row=0)

lbl2 = tk.Label(root, text="Time")
lbl2.grid(column=0, row=1)
now = datetime.datetime.now()
time = tk.Entry(root, width=50, fg="#0000FF")
time.insert(tk.END, now.strftime("%H:%M %p"))
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
link_time.insert(tk.END, now.strftime("%H:%M %p"))
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

btn_text = tk.StringVar()
btn = tk.Button(root, textvariable=btn_text, command=lambda: stud())
btn_text.set("Enter student names")
btn.grid(column=2, row=10)

students = []


def stud():
    for i in range(int(no_stu.get())):
        lbl12 = tk.Label(root, text="Student " + str(i + 1))
        lbl12.grid(column=0, row=11 + i)
        stu = tk.Entry(root, width=50, fg="#0000FF")
        stu.grid(column=1, row=11 + i)
        students.append(stu)

    btn_pdf = tk.Button(root, text="Generate Output", command=lambda: doc_out(i))
    btn_pdf.grid(column=2, row=12 + i)


def doc_out(i):
    txt = tk.Text(root)
    txt.grid(columnspan=3, row=13 + i)
    text_temp = "Date: " + str(date.get()) + "\nTime: " + str(time.get()) + "\nSubject: " + str(subject.get()) + "\nGrade: " + str(grade.get()) + "\nZoom meeting link: " + str(link.get()) + "\nTime which the link was sent to the student group: " + str(link_time.get()) + "\nUnit: " + str(unit.get()) + "\nSubject content covered: " + str(content.get()) + "\nActivities: " + str(activities.get()) + "\nHomework: " + str(homework.get()) + "\nStudents participated: \n"
    students_txt = ""
    for j in students:
        students_txt = students_txt + "\t" +str(j.get()) + "\n"
    txt.insert(tk.END, text_temp + students_txt)

root.mainloop()  # End Window object
