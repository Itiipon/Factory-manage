from rest import app
from flask import render_template
from flask_login import login_required,current_user
from sqlalchemy import Date,String,Time
from model.schema import Employee as em

@app.route('/',methods=['GET'])
def login():
    return render_template('loginpage.html')

@app.route('/home',methods=['GET'])
@login_required
def home():
    return render_template('homepage.html')

@app.route('/report',methods=['GET'])
@login_required
def report():
    return render_template('report.html')

@app.route('/profile',methods=['GET'])
@login_required
def profile():
    return render_template('profile.html')

@app.route('/checkin',methods=['GET'])
@login_required
def checkin():
    return render_template('checkinpage.html')

@app.route('/admin')
@login_required
def admin():
    work_detail =  em.query.with_entities(em.employee_id,em.name,em.phone,em.role)\
            .all()
    return render_template('admin.html',work_detail=work_detail)