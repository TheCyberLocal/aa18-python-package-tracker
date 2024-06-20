from flask import Flask, render_template, Blueprint, redirect
from .config import Config
from .shipping_form import ShippingForm
from flask_migrate import Migrate
from .models import db


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


bp = Blueprint('bp', __name__)


@bp.route('/new_package', methods=['GET', 'POST'])
def shipping_request():
    form = ShippingForm()

    if form.validate_on_submit():
        return redirect("/")

    return render_template('shipping_request.html', form=form)


app.register_blueprint(bp)
