from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    my_variable = "Welcome to My Flask App!"
    return render_template('index.html', variable=my_variable)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
