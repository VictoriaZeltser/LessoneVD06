from flask import render_template, request
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        hobby = request.form['hobby']
        age = request.form['age']
        return render_template('blog.html', name=name, city=city, hobby=hobby, age=age)
    return render_template('blog.html')
