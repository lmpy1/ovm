#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/service')
def service():
    return render_template('service.html')


@app.route('/products')
def products():
    return render_template('products.html')


@app.route('/products/guarantee')
def product_guarantee():
    return render_template('product_guarantee.html')


@app.route('/products/guarantee/demo')
def demo_index():
    return render_template('demo/index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
