# the below code submits, provided details in employee.html to database
# the github, helped me and youtube channel to write the below code.

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#Mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Raghava10'
app.config['MYSQL_DB'] = 'wk6pay'
mysql = MySQL(app)

#the below line I copied from https://stackoverflow.com/questions/34902378/where-do-i-get-a-secret-key-for-flask/34903502
app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

@app.route('/')
def home_template():
    return render_template('employee.html')

@app.route('/add/', methods=['POST'])
def Index():
    return render_template('index.html')

def addDetails():
    if request.method == 'POST':
        name = request.form['fullname']
        departname = request.form['depart']
        email = request.form['email']
        print(departname)
        cur = mysql.connection.cursor()
        if departname == 'Accounts':
            cur.execute('INSERT INTO employee (name, email,department_id) VALUES (%s, %s,%s)', (name, email, 10))
        elif departname == 'HR':
            cur.execute('INSERT INTO employee (name, email,department_id) VALUES (%s, %s,%s)', (name, email, 20))
        elif departname == 'Computer':
            cur.execute('INSERT INTO employee (name, email,department_id) VALUES (%s, %s,%s)', (name, email, 30))
        else:
            cur.execute('INSERT INTO employee (name, email,department_id) VALUES (%s, %s,%s)', (name, email, 40))
            
        mysql.connection.commit()
        flash("employee details added successfully!")
        return redirect(url_for('Index'))
        #return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)