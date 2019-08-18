from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'brunello'
app.config['MYSQL_DATABASE_PASSWORD'] = 'bonanni'
app.config['MYSQL_DATABASE_DB'] = 'sampledb'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.13'
mysql.init_app(app)
