from flask import Flask, request
from cleaver import SplitMiddleware
from cleaver.backend.db import SQLAlchemyBackend

app = Flask(__name__)
app.wsgi_app = SplitMiddleware(
    app.wsgi_app,
    lambda environ: environ['HTTP_USER_AGENT'],  # Track by browser
    SQLAlchemyBackend('sqlite:///experiment.data')
)

template = """
    <form method="POST" action="/register">
        <button>%s</button>
    </form>
"""

@app.route("/")
def home():
    # Visiting / in a web browser will render a button
    return template % (
        request.environ['cleaver'](
            'call-to-action',
            ('control', 'Click Here, Dummy!'),
            ('test', 'Free Puppies!')
        )
    )

@app.route("/register", methods=['POST'])
def register():
    # Submitting the form will go to /register to display a thank-you
    request.environ['cleaver'].score('call-to-action')
    return "Thanks for Signing Up!"

if __name__ == '__main__':
    app.run(port=8080)
