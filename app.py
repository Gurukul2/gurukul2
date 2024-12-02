from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
