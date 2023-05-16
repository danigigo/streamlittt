# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:11:33 2023

@author: camac
"""

import streamlit as st
import webbrowser
import matplotlib.pyplot as plt
import pandas as pd # Importacion estandar de la libreria Pandas
import numpy  as np # Importacion estandar de la libreria NumPy


st.set_page_config(
    page_title="PROYECTO INTEGRADOR",
    page_icon="👋",
)

st.write("# :red[Conoce acerca de Space Scape]🚀 ")

st.sidebar.success("DANIEL SANTIAGO CAMACHO CALVO \n SANTIAGO JOSE HERRERA TORRES")

st.markdown(
    """
    Los videojuegos pueden proporcionar una forma de estimulación mental mejorando
    la creatividad y la imaginación. Al jugar videojuegos, las personas pueden mantener 
    su mente activa y comprometida.
    
    El objetivo de nuestro proyecto es el desarrollo de un videojuego en Unity que pueda 
    **brindar una experiencia atractiva e inmersiva a los jugadores.** Sin embargo, en el proceso 
    de desarrollo del juego nos enfrentamos a diferentes problemas a resolver. Uno de
    los principales desafíos que identificamos fue la necesidad de crear un diseño de 
    juego interesante y equilibrado que pudiera mantener a los jugadores comprometidos
    y motivados a seguir jugando
    
    ### Nuestros objetivos
    - PLANEAR
    - DISEÑAR
    - ASEGURAR CALIDAD

"""
)
url = 'https://www.canva.com/design/DAFh6JsOnuw/dA69ZHOLgPihR0HQ91bjaA/edit?utm_content=DAFh6JsOnuw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton'


if st.button('VER NUESTRA PRESENTACION'):
    webbrowser.open_new_tab(url)

st.title("¿Qué opina la gente?")
# Obtener las revisiones enviadas desde la página 1 a través de la variable de sesión


def main():
    st.title("Página de Visualización de Reviews y Gráfica")

    # Obtener los datos enviados desde la página anterior
    params = st.experimental_get_query_params()
    review = params.get("review", [""])[0]
    calificacion = params.get("calificacion", [""])[0]
    user=params.get("user", [""])[0]
    # Obtener todas las reviews y calificaciones enviadas
    reviews = st.session_state.get("reviews", [])
    if review and calificacion and user:
        reviews.append({"user": user, "calificacion": calificacion, "review": review})
        st.session_state["reviews"] = reviews
        st.table(reviews)
    # Mostrar la lista de opiniones
    if reviews:
        st.header("Opiniones:")
        for item in reviews:
            st.write(f"user: {item['user']}")
            st.write(f"Calificacion: {item['calificacion']}")
            st.write(f"Review: {item['review']}")
            st.write("---------")

        # Mostrar la gráfica de distribución de calificaciones
        calificaciones = [int(item['calificacion']) for item in reviews]
        puntuaciones = [1, 2, 3, 4, 5]
        repeticiones = [calificaciones.count(p) for p in puntuaciones]

        # Crear la gráfica
        fig, ax = plt.subplots()
        ax.bar(puntuaciones, repeticiones)

        # Configurar etiquetas y título
        ax.set_xlabel('Calificacion')
        ax.set_ylabel('Repeticiones')
        ax.set_title('Distribución de calificaciones')

        # Mostrar la gráfica en Streamlit
        st.pyplot(fig)

if __name__ == '__main__':
    main()