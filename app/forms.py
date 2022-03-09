from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PropertyForm(FlaskForm):
    property_title = StringField('Property Title', validators=[DataRequired()])
    property_desc = TextAreaField('Description', validators=[DataRequired()])
    no_rooms = StringField('No. of Rooms', validators=[DataRequired()])
    no_bathrooms = StringField('No. of Bathrooms', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    type = SelectField('Property Type', validators=[DataRequired()], choices=[('house', 'House'), ('apartment', 'Apartment')])
    file_upload = FileField('Photo',  validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])