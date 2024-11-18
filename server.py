from flask import Flask, request, render_template, url_for, redirect, flash
from dotenv import load_dotenv
# from flask_bootstrap import Bootstrap5
import os
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def home():

    return render_template('index.html')

@app.route('/products')
def products():

    return render_template('products.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
