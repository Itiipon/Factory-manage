import datetime
from rest import app,db
from flask import request,jsonify
from model.schema import Workdetail as wd
from flask_login import current_user
from sqlalchemy import Date,String,Time,func

@app.route('/api/report',methods=['POST'])
def api_report():
    req = request.get_json()
    if req.get('start') and req.get('stop'):
        start = datetime.datetime.strptime(req.get('start'),'%Y-%m-%d')
        stop = datetime.datetime.strptime(req.get('stop'),'%Y-%m-%d')
        if start == stop:
            stop += datetime.timedelta(1)
        amount = wd.query.with_entities(func.sum(wd.amount)).filter_by(owner=current_user.employee_id)\
            .filter(wd.start >= start).filter(wd.stop <= stop).all()[0][0]
        minute = wd.query.with_entities(func.sum(wd.minute)).filter_by(owner=current_user.employee_id)\
            .filter(wd.start >= start).filter(wd.stop <= stop).all()[0][0]
        ot = wd.query.with_entities(func.sum(wd.ot_minute)).filter_by(owner=current_user.employee_id)\
            .filter(wd.start >= start).filter(wd.stop <= stop).all()[0][0]
    elif req.get('start'):
        start = datetime.datetime.strptime(req.get('start'),'%Y-%m-%d') 
        amount = wd.query.with_entities(func.sum(wd.amount)).filter_by(owner=current_user.employee_id)\
            .filter(wd.start >= start).all()[0][0]
        minute = wd.query.with_entities(func.sum(wd.minute)).filter_by(owner=current_user.employee_id)\
            .filter(wd.start >= start).all()[0][0]
        ot = wd.query.with_entities(func.sum(wd.ot_minute)).filter_by(owner=current_user.employee_id)\
            .filter(wd.start >= start).all()[0][0]
    else:
        stop = datetime.datetime.strptime(req.get('stop'),'%Y-%m-%d') 
        amount = wd.query.with_entities(func.sum(wd.amount)).filter_by(owner=current_user.employee_id)\
            .filter(wd.stop <= stop).all()[0][0]
        minute = wd.query.with_entities(func.sum(wd.minute)).filter_by(owner=current_user.employee_id)\
            .filter(wd.stop <= stop).all()[0][0]
        ot = wd.query.with_entities(func.sum(wd.ot_minute)).filter_by(owner=current_user.employee_id)\
            .filter(wd.stop <= stop).all()[0][0]
    amount = f'{amount:,.2f}' if amount else 0
    minute = f'{minute:,.2f}' if minute else 0 
    ot = f'{ot:,.2f}' if ot else 0
    return jsonify({'amount':amount,'minute':minute,'ot':ot})

