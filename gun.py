from flask import Flask
gun = Flask(__name__)

@gun.route('/')
def hello_world():
    return 'Hello Prats!'