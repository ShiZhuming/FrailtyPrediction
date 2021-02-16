from flask import Flask , render_template, request, redirect, make_response
app = Flask(__name__)

@app.route('/')
def base():
    return redirect('/index')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['GET'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html',result=request.args.get('age'))
    else:
        return 'submit error'

if __name__ == '__main__':
    app.run(debug=True)
