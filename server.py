import flask
from two1.wallet import Wallet
from two1.bitserv.flask import Payment
app = flask.Flask(__name__)
payment = Payment(app, Wallet())

@app.route('/hello')
@payment.required(5000)
def hello():
    return 'Hello, Bitcoin!'
            