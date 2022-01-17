from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__,template_folder='../frontend/templates',static_folder='../frontend',static_url_path='')
app.secret_key = 'alksdfjlkjasldkfjlksadf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

import rest.page
import rest.api.login.login_api
import rest.api.logout.logout_api
import rest.api.checkin_out.checkin_checkout_api
import rest.api.report.report
import rest.api.admin.api_admin


