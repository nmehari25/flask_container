import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_quote():
    return "This is Sparta!"

if __name__ == '__main__':
    app.run(
    debug=True,
#      port=5000,
    host="0.0.0.0" # Listen for connections _to_ any server
    )
