from datetime import datetime
from rest import app,db
from flask_login import current_user
from model.schema import Workdetail
from flask import jsonify

@app.route('/api/checkinStart',methods=['GET'])
def checkiStart():
    process = Workdetail(
        owner = current_user.employee_id,
        start = datetime.today()
    )
    db.session.add(process)
    db.session.commit()
    return jsonify({'status':True})

@app.route('/api/checkinStop')
def checkinStop():
    stop_process = Workdetail.query.filter_by(owner=current_user.employee_id)\
        .filter(Workdetail.stop == None).order_by(Workdetail.id.desc()).first()
    now = datetime.today()
    stop_process.stop = now
    start_time = stop_process.start
    work_seconds = (now - start_time).seconds
    work_minute = work_seconds / 60
    stop_process.minute = f'{work_minute:.2f}'
    stop_process.amount = round(work_minute * 5,2)
    db.session.commit()
    return jsonify({'status':True})

@app.route('/api/checkTime')
def checkTime():
    start_process = Workdetail.query.filter_by(owner=current_user.employee_id)\
        .filter(Workdetail.stop == None).order_by(Workdetail.id.desc()).first()
    if start_process:
        now = datetime.today()
        start_time = start_process.start
        work_seconds = (now - start_time).seconds
        minute = work_seconds // 60
        seconds = work_seconds % 60
        return jsonify({'minute':str(minute).zfill(2),'seconds':str(seconds).zfill(2)})
    else:
        return jsonify({'minute':'00','seconds':'00'})
        
    