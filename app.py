
import streamlit as st

from modulos.login import login
from modulos.VENTAS import mostrar_venta
from modulos.REPORTES import mostrar_reportes


# Inicializar variables de sesión
if "sesion_iniciada" not in st.session_state:
    st.session_state["sesion_iniciada"] = False

if "usuario" not in st.session_state:
    st.session_state["usuario"] = ""


# Verificar inicio de sesión
if st.session_state["sesion_iniciada"]:

    st.sidebar.title("MENU PRINCIPAL")

    st.sidebar.write(
        f"Usuario: {st.session_state['usuario']}"
    )

    opciones = [
        "Ventas",
        "Reportes de ventas",
        "Información"
    ]

    seleccion = st.sidebar.selectbox(
        "Seleccione una opción",
        opciones
    )

    # Módulo de ventas
    if seleccion == "Ventas":
        mostrar_venta()

    # Módulo de reportes
    elif seleccion == "Reportes de ventas":
        mostrar_reportes()

    # Módulo de información
    elif seleccion == "Información":

        st.title("Información del sistema")

        st.write(
            "Sistema de gestión desarrollado "
            "durante el Laboratorio de SGI."
        )

    # Cerrar sesión
    if st.sidebar.button("Cerrar sesión"):

        st.session_state["sesion_iniciada"] = False
        st.session_state["usuario"] = ""

        st.rerun()

else:

    login()
