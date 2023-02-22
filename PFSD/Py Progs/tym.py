import flask
appp=flask.Flask(__name__)

@appp.route("/")
def sam():
    return "Hello World"

if __name__=="__main__":
    appp.run()