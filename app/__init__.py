from flask import Flask, render_template, Blueprint, redirect
from .config import Config
from .shipping_form import ShippingForm
from flask_migrate import Migrate
from app.models import db, Package


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


bp = Blueprint('bp', __name__)


@bp.route('/new_package', methods=['GET', 'POST'])
def shipping_request():
    form = ShippingForm()

    if form.validate_on_submit():

        data = form.data
        new_package = Package(sender=data["sender_name"],
                              recipient=data["recipient_name"],
                              origin=data["origin"],
                              destination=data["destination"],
                              location=data["origin"])
        db.session.add(new_package)
        db.session.commit()
        return redirect("/")

    return render_template('shipping_request.html', form=form)


@bp.route("/")
def root_endpoint():
    packages = Package.query.all()
    print(packages)
    return render_template('package_status.html', packages=packages)


app.register_blueprint(bp)
