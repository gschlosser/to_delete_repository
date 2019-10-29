from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
@app.route('/hello/<name>')
def newHello(name):
    return f'hello {name}'

@app.route('/number/<int:inputnum>')
def usernumber(inputnum):
    return f'you have {inputnum} and '


@app.route('/makevari/<vari>')
def makevari(vari):
    print('u did it')
    return f"{vari}"


if __name__ == "__main__":
    app.run()