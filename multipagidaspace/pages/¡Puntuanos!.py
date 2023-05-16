import streamlit as st
st.sidebar.header("GOTY 💀💀💀")
def review_input():
    st.title("Ingresa tu review")

    # Recopilar la información de la review
    user = st.text_input("Usuario")
    calificacion = st.slider("Calificación (de 1 a 5)", 1, 5)
    review = st.text_area("Comentario")

    # Guardar la review en una variable de sesión
    if "reviews" in st.session_state:
        reviews = st.session_state.reviews
    if st.button("Enviar"):
        reviews={"user": user, "calificacion": calificacion, "review": review}
        st.experimental_set_query_params(**reviews)
        st.success("Gracias por tu review")
if __name__ == '__main__':
    review_input()
