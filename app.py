import flask
 
app = flask.Flask(__name__)

#Set app.debug=true to enable tracebacks on Beanstalk log output. 
#Make sure to remove this line before deploying to production.
app.debug=True
 
@app.route('/')
def hello_world():
    return "Hello world!"

@app.route('/<name>')
def name(name):
    return "<h1>Hello %s,</h1><p>Welcome here!</p>" % name
 
@app.route('/Dan')
def Dan():
    return "<h2>Dan is a meat!! :)</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)