import requests
import streamlit as st




base_url = "https://pokeapi.co/api/v2/"



def get_pokemon_info(name):
    # Initiates Response / Adapt to request
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
       pokemon_data = response.json()
       return pokemon_data
    else:
        st.write(f"Failed to retrieve data or Pokemon doesn't exist. Response code: {response.status_code}")


pokemon_name = st.text_input("Enter a pokemon name here: ").lower()

pokemon_info = get_pokemon_info(pokemon_name)


if pokemon_info:
    # All Requests
    st.write(f"Name: {pokemon_info['name']}")
    st.write(f"Id: {pokemon_info['id']}")
    st.write(f"Height: {pokemon_info['height']}")
    st.write(f"Weight: {pokemon_info['weight']}")
    
    
    # Multiple Response 
    abilities = [a['ability']['name'] for a in pokemon_info['abilities']]
    types = [t['type']['name'] for t in pokemon_info['types']]
    st.write(f"Types: {', '.join(types)}")
    st.write(f"Abilities: {', '.join(abilities)}")


    

