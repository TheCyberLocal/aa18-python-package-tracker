from flask import Flask, render_template, Blueprint, redirect
from .config import Config
from .shipping_form import ShippingForm



app = Flask(__name__)
app.config.from_object(Config)


bp_shipping_request = Blueprint('bp_shipping_request', __name__)


@bp_shipping_request.route('/new_package', methods=['GET', 'LIST'])
def bp_shipping_request():
    form = ShippingForm()
    if form.validate_on_submit():


        return redirect("/")

    return render_template('shipping_request.html')
