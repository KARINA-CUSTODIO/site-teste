# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13Y0V7h7VOCSMQT2UvbTUMcSeoTx_wZ26
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
   return "Olá, mundo!"

import os
