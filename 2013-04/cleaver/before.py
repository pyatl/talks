from flask import Flask

app = Flask(__name__)

template = """
    <form method="POST" action="/register">
        <button>Click Here, Dummy!</button>
    </form>
"""

@app.route("/")
def home():
    # Visiting / in a web browser will render a button
    return template

@app.route("/register", methods=['POST'])
def register():
    return "Thanks for Signing Up!"

if __name__ == '__main__':
    app.run(port=8080)
