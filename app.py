import os
from flask import Flask, flash, request, redirect, render_template

app = Flask(__name__)
app.secret_key = "lol"
app.config['MAX_CONTENT_LENGTH'] = float("inf")


@app.route('/')
def upload_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':

        if 'clipboard' not in request.form:
            flash('No text entered.')
            return redirect(request.url)

        if 'password' not in request.form:
            flash('No password entered.')
            return redirect(request.url)

        password = request.form['password']
        clipboard = request.form['clipboard']

        if password == "password":
            os.system(f"echo {clipboard} | xclip -selection clipboard")
            flash("Great success")
        else:
            flash("fucking retard")

        return redirect('/')


if __name__ == "__main__":
    app.run()
