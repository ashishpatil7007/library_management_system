from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def login():
   return render_template("login.html")

@app.route('/add_student')
def add_student():
   return render_template("add_student.html")

@app.route('/add_teacher')
def add_teacher():
   return render_template("add_teacher.html")

@app.route('/add_class')
def add_class():
   return render_template("add_class.html")

@app.route('/attendance_sheet')
def attendance_sheet():
   return render_template("attendance.html")

@app.route('/reports')
def reports():
   return render_template("reports.html")

@app.route('/api/save_student',methods=['post'])
def save_student():
   student_name = request.form.get('student_name')  # access the data inside
   phone_number = request.form.get('phone_number')
   address = request.form.get('address')
   parent_phone_number = request.form.get('parent_phone_number')
   print(student_name)
   print(phone_number)
   print(address)
   print(parent_phone_number)
   from database.student import insert_student
   insert_student(student_name,phone_number,address,parent_phone_number)
   return render_template("add_student.html")

@app.route('/api/save_teacher',methods=['post'])
def save_teacher():
   teacher_name = request.form.get('teacher_name')  # access the data inside
   phone_number = request.form.get('phone_number')
   address = request.form.get('address')
   teacher_education = request.form.get('teacher_education')
   print(teacher_name)
   print(phone_number)
   print(address)
   print(teacher_education)
   from database.teacher import insert_teacher
   insert_teacher(teacher_name,phone_number,address,teacher_education)
   return render_template("add_teacher.html")

if __name__ == '__main__':
   app.run(debug=True)