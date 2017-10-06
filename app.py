# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import json



app = Flask(__name__, static_folder="/static")

id_array = []


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/do_pack", methods=["POST"])
def do_pack():
	# здесь доступен массив айдишников id_array

	# вернуть строкой коробку
	print(id_array)
	return "result"
	    
@app.route("/add_item", methods=["POST"])
def add_item():
	id = request.form["id"]
	id_array.append(id)

	return "1"

@app.route("/init_data", methods=["POST"])
def init_data():
	data  = open("data.json", "r", encoding="utf-8").read()
	print("data loaded")
	return data




if __name__ == "__main__":
    app.run()
