from flask import Flask, render_template, Blueprint
from .config import Config


app = Flask(__name__)
app.config.from_object(Config)


bp_shipping_request = Blueprint('bp_shipping_request', __name__)


@bp_shipping_request.route('/new_package', methods=['GET', 'LIST'])
def bp_shipping_request():
    return render_template('shipping_request.html')
