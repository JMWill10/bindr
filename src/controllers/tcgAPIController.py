from flask import Flask, jsonify, request

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/card/<str:name>", methods=["GET"])
def getPokemonCardData(name):
    return "Totodile is coolß"