from flask import Flask, jsonify, request, Blueprint
from src.handlers.getPokemonCardDataHandler import getPokemonDataHandler

tcgApiController = Blueprint('pkmn', __name__)

@tcgApiController.route("/card/<string:name>", methods=["GET"])
def getPokemonCardData(name):
    return getPokemonDataHandler(name)