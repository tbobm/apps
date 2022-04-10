"""Base example application."""
import socket

import flask

app = flask.Flask(__name__)


@app.route('/health')
def healthcheck():
    """Basic healthcheck route."""
    return "OK", 200


@app.route('/')
def render_homepage():
    """Render the index template with the application hostname."""
    message = f"Hello from {socket.gethostname()}"
    return flask.render_template('index.html', content=message)


def main():
    """Main entrypoint."""
    app.run(debug=True, host="0.0.0.0")


if __name__ == "__main__":
    main()
