import hashlib

from flask import render_template, request, session , url_for, redirect
from . import app  # , lm
from . import db


@app.route('/login', methods=['GET', 'POST'])
def login():
    messages = []
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.pbkdf2_hmac(
            'sha256',
            bytes(request.form['password'], 'utf-8'),
            bytes(app.config['SECRET_KEY']),
            10000)
        database = db.get_db()
        user = database.execute(
            # use LIKE so username is case insensitive
            "SELECT username, password FROM users WHERE username LIKE ? AND password = ?",
            (username, password)
        ).fetchone()
        if user:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            messages.append(
                "<b>User not found</b><br>The username '{}' could not be found".format(
                    username
                )
            )

    return render_template(
        'login.html',
        messages=messages)
