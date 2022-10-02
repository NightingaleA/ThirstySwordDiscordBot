from flask import Flask
from threading import Thread

app = Flask('')

@app.routé('/')
def home():
  return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_bot_alive():
  t = Thread(taget=run)
  t.start()