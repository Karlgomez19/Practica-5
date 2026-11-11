
import streamlit as st
from config.conexion import obtener_conexion


def mostrar_reportes():

    st.title("Reportes de ventas")

    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()

        if conexion is None:
            return

        cursor = conexion.cursor()

        # Consultar total de ventas y unidades
        consulta = """
        SELECT
            COUNT(*),
            COALESCE(SUM(Cantidad), 0)
        FROM VENTAS
        """

        cursor.execute(consulta)
        resultado = cursor.fetchone()

        total_ventas = resultado[0]
        total_unidades = resultado[1]

        # Mostrar indicadores
        col1, col2 = st.columns(2)

        col1.metric("Total de ventas", total_ventas)
        col2.metric("Unidades vendidas", total_unidades)

        st.divider()

        st.subheader("Historial de ventas")

        # Consultar historial
        consulta = """
        SELECT Id_Venta, Producto, Cantidad
        FROM VENTAS
        ORDER BY Id_Venta DESC
        """

        cursor.execute(consulta)
        registros = cursor.fetchall()

        if registros:

            st.dataframe(
                registros,
                column_config={
                    0: "ID Venta",
                    1: "Producto",
                    2: "Cantidad"
                },
                use_container_width=True
            )

        else:
            st.info("No hay ventas registradas.")

    except Exception as error:
        st.error(f"Error al generar el reporte: {error}")

    finally:
        if cursor is not None:
            cursor.close()

        if conexion is not None and conexion.is_connected():
            conexion.close()
