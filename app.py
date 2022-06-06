from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    colors = ['Red', 'Blue', 'Green', 'Black', 'Purple']
    title = 'Main page'
    return render_template('index.html', colors=colors, title=title)
    # return redirect(url_for('about'))


@app.route('/about')
def about():
    title = 'About page'
    return render_template('about.html', title=title)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')

