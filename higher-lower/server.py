from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)

@app.route('/')
def hello_world():
    return '<center><h1>Guess a number between 0 and 9</h1></center>' \
           '<center><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></center>' \
           '<img src="https://notasdemascotas.com/wp-content/uploads/2017/07/Perros-Chihuahua.jpg" width=200>'


@app.route('/<int:guess>')
def check_answer(guess):

    if guess > random_number:
        return '<center><h1 style="color: purple">Too high!</h1></center>' \
               '<center><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"></center>'
    elif guess < random_number:
        return '<center><h1 style="color: red">Too low!</h1></center>' \
               '<center><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"></center>'
    else:
        return '<center><h1 style="color: green">Correct!</h1></center>' \
                '<center><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"></center>'


if __name__ == "__main__":
    app.run(debug=True)
