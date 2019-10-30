from flask import Flask
app = Flask(__name__)

@app.route("/")
id = 1
def id_generator():
    id = int(id) + 1
    return str(id)

if __name__ == "__main__":
    app.run()