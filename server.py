from flask import Flask
import random
app=Flask(__name__)

@app.route("/")
def hello():
    return ("<h1>guess a number between 0 and 9</h1>"
            "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzd4OXR4Z3JubzVkNDkxOTM0ZngyeXp6ZTdkeTBlYm91b3ZzcXAwcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JdFEeta1hLNnO/giphy.gif'>")

choice=random.randint(0,9)

@app.route("/<int:num>")
def choices(num):
    if num<choice:

        return (f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
                f"<h1 style='color:blue'>{num} is too low</h1>")
    elif num>choice:
        return (f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
                f"<h1 style='color:red'>{num} is too high")
    else :
        return (f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
                f"<h1 style='color:green'>HEhe</h1>")





if __name__=="__main__":
    app.run(debug=True)
