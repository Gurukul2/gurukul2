import os
from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from werkzeug.utils import secure_filename
from forms import RegistrationForm
from config import Config


app = Flask(__name__)

app.config.from_object(Config)  # Load configuration from Config

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/database')
def database():
    from Shared.DatabaseConnectionString import pullFromDatabase
    data = pullFromDatabase()
    print(data)
    return render_template("table.html", data=data)


@app.route('/forms_example', methods=['GET', 'POST'])
def index():
    greeting = ''
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            greeting = f'Hello, Good Morning, {name}!'
    return render_template('form_example.html', greeting=greeting)


@app.route('/ajax_example', methods=['GET'])
def ajax_example():
    return render_template('ajax_example.html')


@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name')
    if name:
        greeting = f'Hello, {name}!'
        return jsonify({'greeting': greeting})
    else:
        return jsonify({'greeting': 'Hello, Stranger!'}), 400


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/flask_form', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Process form data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        gender = form.gender.data
        hobbies = form.hobbies.data
        country = form.country.data
        agree = form.agree.data

        # Handle file upload
        file = form.profile_picture.data
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
        else:
            flash('Invalid file type.', 'danger')
            return redirect(request.url)

        # For demonstration, we'll just pass data to the success page
        user_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'gender': gender,
            'hobbies': hobbies,
            'country': country,
            'profile_picture': filename
        }

        flash('Registration successful!', 'success')
        return redirect(url_for('success', **user_data))
    return render_template('FLAST_WTF_Session/register.html', form=form)


@app.route('/flask_form_success')
def success():
    # Extract query parameters
    user_data = {
        'first_name': request.args.get('first_name'),
        'last_name': request.args.get('last_name'),
        'email': request.args.get('email'),
        'gender': request.args.get('gender'),
        'hobbies': request.args.getlist('hobbies'),
        'country': request.args.get('country'),
        'profile_picture': request.args.get('profile_picture')
    }
    return render_template('FLAST_WTF_Session/success.html', user=user_data)

if __name__ == '__main__':
    app.run(debug=True)
