from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/form')
def my_app():
    return render_template('myform.html')

@app.route('/signup', methods=['POST'])
def signup():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    print(firstname, lastname)
    return render_template('otherform.html', firstname=firstname, lastname=lastname)



# @app.route('/goto')
# def gotorickandmorty():

#     return 

if __name__ == "__main__":
    app.run()