from flask import Flask, request

app = Flask(__name__)

#simple get request
@app.route('/')
def hello_flask():
    return 'Hello Flask!'

# get method 2
@app.route('/index')
def hello_flask_slash():
    return 'Hello Srujan Alikanti'

#get method 3
@app.route('/new/')
def query_string():
    query_val = request.args.get('greeting')
    return '<h1>The greeting is : {0} </h1>'.format(query_val)

#get with default answer
@app.route('/default')
def default_query(default='Diagonal Matrix'):
    def_query = request.args.get('default', default)
    return '<h1>Welcome to {0} </h1>'.format(def_query)

#default answer method 2
@app.route('/user')
@app.route('/user/<name>')
def query_user(name='Mina'):
    return '<h1>Hello {0}, Welcome to Diagonal Matrix</h1>'.format(name)

# String
@app.route('/text/<string:name>')
def working_with_string(name):
    return '<h1> Here is the string '+name+'</h1>'

# Integers
@app.route('/text/<int:num>')
def working_with_numbers(num):
    return '<h1> This is integer: '+str(num)+'</h1>'

# add numbers
@app.route('/text/<int:num1>/<int:num2>')
def adding_integers(num1, num2):
    return '<h1>This is Integer: {}'.format(num1 + num2)+'</h1>'

# float
@app.route('/text/<float:num1>/<float:num2>')
def product_two_numbers(num1, num2):
    return '<h1>This is a flot: {}'.format(num1 * num2)+'</h1>'

if __name__ == '__main__':
    app.run(debug=True)
