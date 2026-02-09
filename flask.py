from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello this is lo"

if __name__ == "__main__":
    app.run(debug=True)
