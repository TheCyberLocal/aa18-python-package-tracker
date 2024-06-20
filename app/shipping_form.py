from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired
from map.map import map


class ShippingForm(FlaskForm):
    sender_name = StringField("Sender Name", validators=[DataRequired()])
    recipient_name = StringField("Recipient Name",validators=[DataRequired()])
    origin = SelectField("Origin", choices =map.keys(), validators=[DataRequired()])
    destination = SelectField("Destination", choices=map.keys(), validators=[DataRequired()])
    express = BooleanField("Express", validators=[DataRequired()])
    submit = SubmitField("Submit")