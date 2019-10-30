from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    id_file = open("id.txt", "r")
    id = id_file.read()
    id_file.close()
    new_id = int(id) + 1
    id_file = open("id.txt", "w")
    id_file.write(str(id))
    return id

if __name__ == "__main__":
    application.run()
