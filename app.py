from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

import random

app = Flask(__name__)
Bootstrap(app)


nav = Nav(app)

# registers the "top" menubar
nav.register_element('top', Navbar(
    View('Plus', 'my_form'),
    View('Minus', 'my_form_minus')
))



@ app.route('/')
def my_form():
    a = random.randrange(0, 9)
    b = random.randrange(0, 49)
    return render_template('plus.html', a=a, b=b)


@ app.route('/', methods=['POST'])
def my_form_post():
    svar = request.form['svar']
    svar_int = int(svar)
    a = request.form.get('a')
    b = request.form.get('b')
    summa = int(a) + int(b)
    return render_template('plus.html', a=a, b=b, svar=svar, summa=summa)
   # if summa == svar_int:
   #     text = f"{svar} rätt"
   #     return render_template('svar.html', text=text)
   # else:
   #     text = f"{svar} är fel rätt ska vara {summa}"
   #     return render_template('svar.html', text=text)



@ app.route('/minus')
def my_form_minus():
    a = random.randrange(0, 10)
    b = random.randrange(0, 10)
    return render_template('minus.html', a=a, b=b)


@ app.route('/minus', methods=['POST'])
def my_form_post_minus():
    svar = request.form['svar']
    svar_int = int(svar)
    a = request.form.get('a')
    b = request.form.get('b')
    summa = int(a) - int(b)
    if summa == svar_int:
        text = f"{svar} rätt"
        return render_template('svar.html', text=text)
    else:
        text = f"{svar} är fel rätt ska vara {summa}"
        return render_template('svar.html', text=text)


if __name__ == "__main__":
    app.run()
    
