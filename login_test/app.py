from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/loginResponse')
def res():
    data = request.get_json()
    print(data)

if __name__ == '__main__':
    app.run(host='localhost', port=8887, debug=True)