from flask import Flask
app = Flask(__name__)

@app.route("/")
def id_generator():
    id1 = 25
    return str(id1)

if __name__ == "__main__":
    app.run()