from flask import Flask, render_template

app = Flask('__name__')

@app.route('/movie_table')
def movies_plus():
    movies_dict = {'autopsy of jane doe': 02.14,
                   'neon demon': 3.20,
                   'ghost in a shell': 1.50,
                   'kong: skull island': 3.50,
                   'john wick 2': 02.52,
                   'spiderman - homecoming': 1.48}
    return render_template('table_data.html', name='Srujan', movies=movies_dict)

if __name__ == '__main__':
    app.run(debug=True)
