from handlers.getPokemonCardDataHandler import *

pokemonName = ""
while True:
    print('Hello, Welcome to Bindr!')
    pokemonName = input('Please choose a pokemon to look up that card data (input end to terminate): \n')
    
    if pokemonName.lower() == "end":
        print("Come again!!")
        break

    pokemonData = getData(pokemonName)

    print('Here is your pokemon!\n')
    print(pokemonData)