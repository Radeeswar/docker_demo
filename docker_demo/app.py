from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "getting started docker new changed by zeeshan!!"



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=4000)
