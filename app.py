from flask import Flask, request

app = Flask(__name__)

hackathons = {
    "Bitcamp": {
        "start_date": "never"
    }
}

@app.route("/")
def hello_ghw():
    return "<p>Hello gang 404</p>"

@app.route('/hackathons', methods=['GET', 'POST'])
def getHackathons():
    if request.method == "POST":
        hackathons[request.json]
    else:
        return hackathons


if __name__ =="__main__":
    app.run(debug = True)