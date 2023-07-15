import flask

# Create a simple flask app that calles index.html
app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=False)
