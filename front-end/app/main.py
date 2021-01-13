from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'mysql.default.svc.cluster.local'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Testing@123'
app.config['MYSQL_DB'] = 'test_db'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fnm']
        lastName = details['lnm']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Users(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    elif request.method == "GET":
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
