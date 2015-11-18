from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/button')
def button():
    return render_template('Buttons.html')

@app.route('/forms')
def forms():
    return render_template('forms.html')

#print("we're making a website")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
