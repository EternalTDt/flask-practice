from flask import Flask, render_template, request, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)
Bootstrap(app)

# DB conf

db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)


@app.route('/')
def index():
    # cursor.execute("DELETE FROM users WHERE username='J'")
    # mysql.connection.commit()

    # res = cursor.execute("SELECT * FROM users")
    # if res > 0:
    #     users = cursor.fetchall()
    #     return str(users)
    cursor = mysql.connection.cursor()
    if cursor.execute("INSERT INTO users(username) VALUES ('Peter')"):
        mysql.connection.commit()
        return 'Success!', 201
    return render_template('index.html')
    # return redirect(url_for('about'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return request.form['password']
    return render_template('reg.html')


@app.errorhandler(404)
def page_not_found(e):
    return 'Oops! Page was not found :('


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')

