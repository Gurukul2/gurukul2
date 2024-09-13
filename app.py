from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/database')
def database():
    from Shared.DatabaseConnectionString import pullFromDatabase
    data = pullFromDatabase()
    print(data)
    return render_template("table.html", data = data)

if __name__ == '__main__':
    app.run(debug=True)
