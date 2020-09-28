from flask import Flask, render_template, request

app = Flask(__name__)

# String
@app.route('/text/<string:name>')
def working_with_string(name):
    return '<h1> here is the string: '+name+'</h1>'

if __name__ == '__main__':
    app.run(debug=True)
