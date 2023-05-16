# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:32:07 2023

@author: camac
"""
import streamlit as st
from PIL import Image
import json
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="HISTORIA ", page_icon="🌍")
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



st.markdown("# HISTORIA 🪐")
st.sidebar.header("💀💀💀")
st.write(
    """Después de años de exploración espacial en equipo, Ellen decidió tener una aventura en solitario para 
    desafiar sus límites y descubrir nuevos horizontes. Se embarcó en su nave espacial personal y se dirigió 
    hacia una región inexplorada del espacio profundo. Sin embargo, durante el viaje, su nave sufrió un fallo técnico y se estrelló en un planeta desconocido para ella.
    Ellen quedó aturdida y confundida por el impacto, pero rápidamente se recuperó y evaluó la situación. 
    Descubrió que estaba atrapada en un planeta hostil y desolado, sin comunicación con la nave ni con la 
    flota estelar. A pesar de esto, decidió que no se daría por vencida y que haría todo lo posible por 
    sobrevivir y encontrar una manera de salir del planeta
  """
)

image = Image.open('ellen.png')

st.image(image, caption='ellen')
lottie_load = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_ypej3gd9.json")

st_lottie(
        lottie_load,
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
         # canvas
        height=300,
        width=300,
        key=None,
    )