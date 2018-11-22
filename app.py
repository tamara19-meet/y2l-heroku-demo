from flask import Flask 
import render_template
app = Flask(__name__)

@app.route('/NEW')
def hello_world():
    return render_template('NEW.html')

if __name__ == '__main__':
    app.run(debug=True)

