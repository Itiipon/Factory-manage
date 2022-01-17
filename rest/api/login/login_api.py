from flask.templating import render_template
from rest import app
from model.schema import (
    Employee as ey)
from flask import request,redirect,url_for,flash
from flask_login import login_user

@app.route('/api/login',methods=['POST'])
def api_login():
    employee_id = request.form.get('employee_id')
    password = request.form.get('password')
    employee = ey.query.filter_by(employee_id=employee_id).filter(ey.password== password).first()
    if employee:
        login_user(employee)
        return redirect(url_for('home'))
    else :
        flash('กรุณาตรวจสอบรหัสพนักงานหรือรหัสผ่านอีกครั้ง',category='danger')
        return render_template('loginpage.html')
    