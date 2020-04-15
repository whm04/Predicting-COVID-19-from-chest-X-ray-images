
from flask import Flask, render_template, request
app = Flask(__name__)




@app.route('/')
def homepage():
    

    return render_template('index.html', title = "Welcome", paragraph = 'Lorem ipsum dolor sit amet')
 

if __name__ == '__main__':
    app.run(debug=True)
