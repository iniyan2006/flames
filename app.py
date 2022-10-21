from flask import Flask, request, render_template, redirect
from flamesFinder.flames import flames
app = Flask(__name__)
app.config['SECRET_KEY']="ThisIsMe"
first_name = ""
second_name = ""
@app.route('/', methods = ["GET", "POST"]) 
def index():
    if request.method == "POST":
        first_name = request.form.get("fname").lower() 
        second_name = request.form.get("sname").lower()
        if first_name == 'admin' and second_name == 'admin':
            return redirect('/admin')
        else:
            status = flames(first_name, second_name)
            emoji = status.split(" ")
            status = emoji[0]
            with open('./info.txt','a') as f:
                f.write(f"\n  first name : {first_name} second_name : {second_name}  result : {status[0]}")
            return render_template('result.html',status=status, emoji=emoji[1], first_name=first_name, second_name=second_name) 
    return render_template('index.html')
@app.route('/admin')
def admin():
    file = './info.txt'
    with open(file, 'r') as f:
        file = f.readlines()
    return render_template('admin.html', file = file) 
app.run(debug = True, host = "0.0.0.0")
