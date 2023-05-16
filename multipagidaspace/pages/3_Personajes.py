# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:39:10 2023

@author: camac
"""

import streamlit as st
from PIL import Image




st.set_page_config(page_title="PERSONAJES 👩‍🚀", page_icon="🤖")

st.markdown("# :blue[PERSONAJES] 👩‍🚀 ")
st.sidebar.header("💀💀💀")
st.write(
    """ """
)

image = Image.open('ellencita.png')

# Dividir la pantalla en dos columnas
col1, col2 = st.columns(2)

# Mostrar la imagen en la primera columna
with col1:
    st.image(image, width=300)

# Mostrar la descripción en la segunda columna
with col2:
    st.write(
        """
        
        Ellen era una exploradora del universo apasionada y aventurera. Desde joven, se fascinaba con 
        las historias sobre los descubrimientos de los grandes exploradores del pasado y soñaba con ser 
        como ellos. Después de años de estudio y entrenamiento, finalmente obtuvo una posición en la flota 
        estelar y comenzó su carrera como exploradora.
        Durante su primera misión, Ellen se unió a una tripulación de una nave espacial que se dirigía a una 
        galaxia desconocida en los confines del universo.
      """, text_align='justify'
    )
st.write(
        """ A medida que se adentraban en el espacio profundo,
            Ellen se enfrentó a desafíos increíbles, como tormentas espaciales peligrosas, cuerpos celestes
            desconocidos y peligrosos, y criaturas alienígenas hostiles. Sin embargo, su valentía, habilidades 
            y perseverancia la ayudaron a superar todos estos obstáculos.
            Con el tiempo, Ellen se convirtió en una de las exploradoras más respetadas y exitosas de la flota.
            Descubrió nuevas galaxias, planetas y formas de vida alienígenas. Además, se destacó por su capacidad
            para resolver problemas, liderar equipos y tomar decisiones críticas en momentos de crisis.
            A pesar de todas las dificultades y peligros, Ellen nunca se rindió. Siempre buscaba nuevos desafíos
            y aventuras emocionantes. Su dedicación y pasión por la exploración del universo inspiró a muchos 
            otros a seguir sus pasos y se convirtió en una leyenda en la historia de la exploración espacial
      """, text_align='justify'
    )

st.markdown("# :red[ENEMIGOS] 👽")

image1 = Image.open('enemigo2.png')
image2 = Image.open('zyro.png')

# Colocar las imágenes en una lista
images = [image1, image2]

# Mostrar las imágenes en una disposición en mosaico
st.image(images, width=300, caption=["Flork", "El guardian de la roca"])
st.write(".")
