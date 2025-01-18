import requests
import streamlit as st
import time



st.title("Pokémon API App")



BASE_URL = "https://pokeapi.co/api/v2/"



def get_pokemon_info(name):
    url = f"{BASE_URL}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None




pokemon_name = st.text_input("Enter a Pokémon name:").strip().lower()

if st.button("Tips"):
    st.info("This site was made by Kabir Tiwari :)")
    time.sleep(2)
    st.info("Try inputting a Pokemon Name into the text box")



if pokemon_name:
    pokemon_info = get_pokemon_info(pokemon_name)
    if pokemon_info:
        st.write(f"Name: {pokemon_info.get('name').capitalize()}")
        st.write(f"Id: {pokemon_info['id']}")
        st.write(f"Height: {pokemon_info['height']}")
        st.write(f"Weight: {pokemon_info['weight']}")
        abilities = [a['ability']['name'] for a in pokemon_info['abilities']]
        types = [t['type']['name'] for t in pokemon_info['types']]
        st.write(f"Types: {', '.join(types)}")
        st.write(f"Abilities: {', '.join(abilities)}")
        image_url = pokemon_info['sprites']['front_default']
        st.image(image_url, caption=f"{pokemon_info.get('name').capitalize()}", width=250)
    else:
        st.write("Pokémon not found or failed to retrieve data.")

