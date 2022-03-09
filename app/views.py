"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from crypt import methods
import os
from app import app
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from .forms import PropertyForm
from app.models import Property
from app import db
from werkzeug.utils import secure_filename


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route("/properties/create", methods=["GET", "POST"])
def create_property():
    form = PropertyForm()

    if request.method == "POST":
        if form.validate_on_submit():
            property_title = request.form["property_title"]
            property_desc = request.form["property_desc"]
            no_rooms = request.form["no_rooms"]
            no_bathrooms = request.form["no_bathrooms"]
            price = request.form["price"]
            location = request.form["location"]
            type = request.form["type"]

            file = form.file_upload.data
            file_name = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], file_name))


            property = Property(property_title, property_desc, no_rooms, no_bathrooms, price, location, type, file_name)
            db.session.add(property)
            db.session.commit()
            flash('Property was successfully created', 'success')

            return redirect(url_for('display_properties'))

    return render_template('form.html', form=form)

def  get_uploaded_images():
    path = os.path.join(os.getcwd(),app.config["UPLOAD_FOLDER"] )
    return [file for subdir, dirs, files in os.walk(path) for file in files]

@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

@app.route('/properties')
def display_properties():
    properties = db.session.query(Property).all()
    return render_template('properties.html', properties=properties)

@app.route('/properties/<propertyid>')
def display_property(propertyid):
    property = Property.query.get(propertyid)
    return render_template('property.html', property=property)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
