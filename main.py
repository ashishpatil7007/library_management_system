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

@app.route('/add_user')
def user():
   return render_template("add_user.html")

@app.route('/reports')
def reports():
   from database.attendance import view_attendance
   attendance_dict=view_attendance()
   print(attendance_dict)
   return render_template("reports.html",attendance_dict=attendance_dict)

@app.route('/student_reports')
def student_reports():
   from database.student import view_student
   student_dict=view_student()
   print(student_dict)
   return render_template("student_reports.html",student_dict=student_dict)

@app.route('/teacher_reports')
def teacher_reports():
   from database.teacher import view_teacher
   teacher_dict=view_teacher()
   print(teacher_dict)
   return render_template("teacher_reports.html",teacher_dict=teacher_dict)

@app.route('/class_reports')
def class_reports():
   from database.add_class import view_class
   class_dict=view_class()
   print(class_dict)
   return render_template("class_reports.html",class_dict=class_dict)

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

@app.route('/api/save_class',methods=['post'])
def save_class():
   class_name = request.form.get('class_name')  # access the data inside
   room_number = request.form.get('room_number')
   floor_number = request.form.get('floor_number')
   print(class_name)
   print(room_number)
   print(floor_number)
   from database.add_class import insert_class
   insert_class(class_name,room_number,floor_number)
   return render_template("add_class.html")

@app.route('/api/save_attendance',methods=['post'])
def save_attendance():
   student_name = request.form.get('student_name')  # access the data inside
   class_name = request.form.get('class_name')
   present_or_absent= request.form.get('present_or_absent')
   date = request.form.get('date')
   print(student_name)
   print(class_name)
   print(present_or_absent)
   print(date)
   from database.attendance import insert_attendance
   insert_attendance(student_name,class_name,present_or_absent,date)
   return render_template("attendance.html")

@app.route('/api/save_user',methods=['post'])
def save_user():
   username = request.form.get('username')  # access the data inside
   password = request.form.get('password')
   print(username)
   print(password)
   from database.add_user import insert_user
   insert_user(username,password)
   return render_template("add_user.html")

if __name__ == '__main__':
      app.run(debug=False,host="0.0.0.0",port=5000)