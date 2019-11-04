from flask import Flask

from controllers.calc_controller import calculator


app = Flask(__name__)

app.register_blueprint(calculator, url_prefix='/calculator')

if __name__ == '__main__':
    app.run()