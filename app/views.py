from flask import render_template, request, redirect, url_for, session
from app import app


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        logged_in = True
    else:
        username = 'Anonymous user'
        logged_in = False
    return render_template(
        'home.html',
        user=username,
        logged_in=logged_in)


@app.route('/redirect')
def redirect_view():
    if "to" in request.args:
        return redirect(request.args['to'])
    else:
        return redirect(url_for('.err', error='This page was not found.'))


@app.route('/error')
def err():
    if "error" in request.args:
        messages = ["<b>Error!</b> {}".format(request.args["error"])]
    else:
        messages = ["<b>Error!</b> No error message found."]
    return render_template('home.html', messages=messages)
