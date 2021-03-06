from flask import Flask, render_template, request, redirect, url_for, abort, session
from ESA import app

@app.route('/')
def home():
    return render_template('index.html')
    # return "Hello there" + data
    # return app.config['ENV']

@app.route('/signup', methods=['POST'])
def signup():
    session['username'] = request.form['username']
    session['message'] = request.form['message']
    return redirect(url_for('message'))

@app.route('/message')
def message():
    if not username in session:
        return abort(403)
    return render_template('message.html', username=session['username'], 
                                           message=session['message'])

if __name__ == '__main__':
    app.run()