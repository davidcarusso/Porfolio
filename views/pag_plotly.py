import streamlit as st 
import pandas as pd
import plotly.express as px

from scripts.datos_ejemplo import generar_datos



st.title("Dashboard de ventas")


def cargar_datos():
    data = generar_datos()
    df = pd.DataFrame(data)
    return df

df = cargar_datos()
df["Mes"] = df["Fecha"].dt.month_name(locale="es")
df["Year"] = df["Fecha"].dt.year


# 2. Widgets interactivos en sidebar
with st.sidebar:
    st.header("Filtros")
    categorias_seleccionada = st.multiselect("Categorias", options=df["Categoria"].unique(), default=df["Categoria"].unique())
    
    #filtro de fechas
    year = st.selectbox("year", options= sorted( df["Year"].unique() ), index=None )
    mes = st.selectbox("Mes", options= sorted (df["Mes"].unique() ), index=None)
    rango_fechas = st.date_input("Rango de Fechas", min_value=df["Fecha"].min(), max_value=df["Fecha"].max() , value=[df["Fecha"].min(), df["Fecha"].max()], format="DD/MM/YYYY" )
    

# 3. Filtrar datos
df_filtrado = df[
    (df["Categoria"].isin(categorias_seleccionada) ) &
    (df["Fecha"].between(pd.to_datetime(rango_fechas[0]), pd.to_datetime(rango_fechas[1]) ) ) &
    (df["Mes"] == (mes) )
]

# 4. Gráficos interactivos
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Series Temporales", "Geográfico", "Relaciones", "Distribución", "Otros Graficos"]) 

with tab1:
    # Gráfico de línea con Plotly
    fig_line = px.line(
        df_filtrado.groupby("Fecha")["Ventas"].sum().reset_index(),
        x="Fecha",
        y="Ventas",
        title="Tendencias de Ventas Diarias"
    )
    st.plotly_chart(fig_line, use_container_width=True)

with tab2:
    # Mapa interactivo
    fig_map = px.scatter_geo(
        df_filtrado,
        lat="Latitud",
        lon="Longitud",
        color="Region",
        size="Ventas",
        hover_name="Categoria",
        projection="natural earth"
    )
    st.plotly_chart(fig_map, use_container_width=True)


with tab3:
    # Scatter plot con selección de ejes
    col1, col2 = st.columns(2)
    with col1:
        eje_x = st.selectbox("Eje x", options=["Ventas", "Beneficio", "Rating"])
    with col2:
        eje_y = st.selectbox("Eje y", options=["Beneficio", "Rating", "Ventas"])
    
    fig_scatter = px.scatter(
        df_filtrado,
        x=eje_x,
        y=eje_y,
        color="Categoria",
        trendline="lowess"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
with tab4:
    # histograma dinamico
    bins = st.slider("Numero de bins:", min_value=5, max_value = 50, value = 20, step=5)
    fig_hist = px.histogram(
        df_filtrado, 
        x="Ventas",
        nbins=bins,
        color="Region",
        barmode="overlay"
    )
    st.plotly_chart(fig_hist)

with tab5:
    #Otros graficos

    # Usando el dataset de práctica anterior
    fig = px.choropleth(
    df,
    locations="Region",  # Columna con nombres de países/regiones
    locationmode="country names",
    color="Ventas",
    hover_name="Categoria",
    animation_frame=df["Fecha"].dt.month,  # Animación por mes 
    projection="natural earth",
    title="Ventas Globales por Mes"
    )
    fig.update_layout(height=600)
    st.plotly_chart(fig)

    st.divider()
    df_radar = df_filtrado.groupby("Categoria")[["Ventas", "Beneficio", "Rating"]].mean().reset_index()
    fig = px.line_polar(
    df_radar,
    title="Grafico Radar con Filtro",
    r="Ventas",
    theta="Categoria",
    line_close=True,
    color="Beneficio"
    ,template="plotly_dark"
    )
    st.plotly_chart(fig)

    st.divider()
    tipo_grafico = st.selectbox("Elige el Grafico:", ["Box", "Violin", "Sunburst"])

    match tipo_grafico:

        case "Box":
            st.write("Box")
            fig = px.box(df_filtrado, 
            x="Region", 
            y="Ventas", 
            color="Categoria")

        case "Violin":
            st.write("Violin")
            fig = px.violin(df_filtrado, 
            x="Region", 
            y="Beneficio", 
            color="Region" ,
            box=True)

        case "Sunburst":
            st.write("Sunburst")
            fig = px.sunburst(
            df_filtrado, 
            path=["Region", "Categoria"] , 
            values="Ventas")

    st.plotly_chart(fig)
        


with st.expander("Datos Filtrados"):
    st.dataframe(df_filtrado, height=200)


    
