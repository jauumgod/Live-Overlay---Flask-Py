from flask import Flask, render_template, url_for, redirect
import datetime

app = Flask(__name__)
app.config['SECRET_KEY']=False

@app.route("/")
def overlay():
    horarios = {'Segunda':"offline", 'Terça':"19:00",'Quarta':"19:00"
                ,'Quinta': "offline", 'Sexta': "19:00"}
    return render_template('overlay.html', horarios=horarios)

@app.route("/time")
def get_current_time():
    time = datetime.datetime.now().strftime('%H:%M:%S')
    return {'time': time}

@app.route("/audio")
def soundclound():
    return 0



if __name__ == '__main__':
    app.run(debug=True)
