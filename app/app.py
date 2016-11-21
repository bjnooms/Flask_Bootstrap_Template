########## Flask Web Application Template ##########

## FLask specific imports
from flask import Flask, render_template, redirect, \
    url_for, request, session, flash, g, make_response, send_file

## My imports




## Instantiate Flask object as app
app = Flask(__name__)

## Define app routes

# Home/Landing page
@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)
    
# //TODO - Add more pages below this




## Actually run the app
if __name__ == "__main__":
    app.run()