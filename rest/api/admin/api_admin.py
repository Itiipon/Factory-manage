from flask import request,jsonify
from rest import app
from model.schema import Employee as em 

@app.route('/api/employee',methods=['POST'])
def api_employee():
    draw = request.form.get('draw')
    row = request.form.get('start')
    search = request.form.get('search[value]')
    totalRecord = em.query.count()
    if search == '':
        result = em.query.with_entities(em.employee_id,em.name,em.phone,em.role)\
            .all()
    else:
        result = em.query.with_entities(em.employee_id,em.name,em.phone,em.role)\
            .filter(
            (em.employee_id.contains(search)) |\
            (em.name.contains(search)) |\
            (em.phone.contains(search)) |\
            (em.role.contains(search)) 
        ).all()
    totalRecordWithfilter = len(result)
    response = {
        'draw':draw,
        'iTotalRecords':int(totalRecord),
        'iTotalDisplayRecords':totalRecordWithfilter,
        'data':result[int(row):10+int(row)]
    }
    return jsonify(response)