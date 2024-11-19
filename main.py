import datetime

from flask import Flask, request, render_template, url_for, redirect, flash
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('FLASK_KEY')


def get_year():
    acc_date = datetime.datetime.now()
    return acc_date.year


@app.route('/')
def home():

    return render_template('index.html', year=get_year())


@app.route('/products')
def products():

    return render_template('products.html', year=get_year())


@app.route('/contact')
def contact_me():

    return render_template('contactme.html', year=get_year())


if __name__ == "__main__":
    app.run(debug=False)
