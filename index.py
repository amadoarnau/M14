from flask import render_template
from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello_world():
    return '<a href="calendari">Calendari</a></br><a href="sudoku">Sudoku</a>'

@app.route('/calendari/')
@app.route('/calendari/<name>')
def calendari(name=None):
    return render_template('calendari.html', date=name, mes=name)

@app.route('/sudoku/')
def sudoku():
    return render_template('sudoku.html')

if __name__ == "__main__":
    app.run()
