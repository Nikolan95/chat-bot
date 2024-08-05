from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
  return "Programm is running"

@app.route('/twilio/receiveMessage')
def receiveMessage():
  return "Message received"
