from flask import render_template
from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
@app.route('/<mes>')
def cal(mes=None):
	
	
    return render_template('calendari.html', mes=mes, cal=range(5))
    
    


if __name__ == "__main__":
    app.run()

