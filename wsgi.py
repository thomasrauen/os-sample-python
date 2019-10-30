from flask import Flask
app = Flask(__name__)

@app.route("/")
def id_generator():
    return "Hello World!"

if __name__ == "__main__":
    app.run()