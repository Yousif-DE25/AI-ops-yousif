import requests
import streamlit as st
# from api import 

def layout():
    st.markdown("# PydanticAI")

    st.selectbox("Select what to display", options=["Movies", "Actors", "Directors"])
    movies = requests.get("http://localhost:8000/movies").json()
    st.dataframe(movies)

if __name__ == "__main__":
    layout()
