from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'brunello'
app.config['MYSQL_DATABASE_PASSWORD'] = 'bonanni'
app.config['MYSQL_DATABASE_DB'] = 'sampledb'
app.config['MYSQL_DATABASE_HOST'] = 'mysql-myproject.192.168.202.24.nip.io'
mysql.init_app(app)
