from rest import app 
from flask_login import logout_user,current_user
from flask import redirect,url_for

@app.route('/api/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))