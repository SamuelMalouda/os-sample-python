from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Ta grand mere la pute OS"

if __name__ == "__main__":
    application.run()
