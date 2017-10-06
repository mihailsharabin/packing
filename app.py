from flask import Flask, render_template
import json



app = Flask(__name__, static_folder="/static")


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/do_pack", methods=["POST"])
def do_pack():
	# вернуть строкой номер коробки
	return "1"
	    





if __name__ == "__main__":
    app.run()


