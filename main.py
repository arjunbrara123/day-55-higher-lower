from flask import Flask
from random import randint

LOW_GIF = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
HIGH_GIF = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
CORRECT_GIF = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

rand_int = randint(1, 10)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<int:num>')
def check_num(num):
    if rand_int == num:
        html_text = f'Correct!<br><img src="{CORRECT_GIF}"></img>'
    elif rand_int > num:
        html_text = f'Too low, try again!<br><img src="{LOW_GIF}"></img>'
    elif rand_int < num:
        html_text = f'Too high, try again!<br><img src="{HIGH_GIF}"></img>'
    return html_text

app.run(debug=True)

