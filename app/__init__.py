from flask import Flask, render_template, Blueprint, redirect
from .config import Config
from .shipping_form import ShippingForm


app = Flask(__name__)
app.config.from_object(Config)


bp = Blueprint('bp', __name__)


@bp.route('/new_package', methods=['GET', 'POST'])
def shipping_request():
    form = ShippingForm()

    if form.validate_on_submit():
        return redirect("/")

    return render_template('shipping_request.html', form=form)


app.register_blueprint(bp)
