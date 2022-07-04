from flask import Flask
from flask import render_template, redirect, request
from werkzeug.serving import run_simple


app=Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/products')
def products():
	return render_template('product.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')



if __name__=="__main__":

	run_simple('127.0.0.1', 8000, app, use_reloader=False)
