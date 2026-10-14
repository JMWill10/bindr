# from handlers.getPokemonCardDataHandler import *ß
from flask import Flask
from src.controllers.tcgAPIController import tcgApiController

app = Flask(__name__)

app.register_blueprint(tcgApiController, url_prefix='/view')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
# pokemonName = ""
# while True:
#     print('Hello, Welcome to Bindr!')
#     pokemonName = input('Please choose a pokemon to look up that card data (input end to terminate): \n')
    
#     if pokemonName.lower() == "end":
#         print("Come again!!")
#         break

#     pokemonData = getData(pokemonName)

#     print('Here is your pokemon!\n')
#     print(pokemonData)

