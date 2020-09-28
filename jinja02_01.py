from flask import Flask, render_template, request

app = Flask('__name__')

@app.route('/movies')
def top_movies():
    movies_list = ['autopsy of jane doe',
                  'neon demon',
                  'ghost in a shell',
                  'kong: skull island',
                  'john wick 2',
                  'spiderman - homecoming']
    return render_template('movies.html', name='Srujan', movies=movies_list)

if __name__ == "__main__":
    app.run(debug=True)
