from flask import Flask,render_template,request
from ip_check import *
from nslookup import *
app = Flask(__name__)


@app.route('/',methods=('GET', 'POST'))
def hello_web():
    return render_template('index.html')
@app.route('/ping',methods=('GET', 'POST'))
def ping():
    if request.method == 'POST':
        ip = request.form['ip']
        result = ip_analyze(ip)
        return render_template('ping.html',data=result)
    if request.method == 'GET':
        return render_template('ping.html')

@app.route('/traceroute',methods=('GET', 'POST'))
def trace():
    if request.method == 'POST':
        ip = request.form['ip']
        result = traceroute(ip)
        return render_template('traceroute.html',data=result)
    if request.method == 'GET':
        return render_template('traceroute.html')

@app.route('/nslookup',methods=('GET', 'POST'))
def ns_look():
    if request.method == 'POST':
        ip = request.form['ip']
        result = ip_look(ip)
        print(result)
        return render_template('nslookup.html',data=result)
    if request.method == 'GET':
        return render_template('nslookup.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="5080",debug=True)