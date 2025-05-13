import streamlit as st 
import pandas as pd
import plotly.express as px

from scripts.datos_kaggle import df_costo_educacion


df = df_costo_educacion()


st.title("Visualizaciones")




### Barra de Filtros 
with st.sidebar: 
    st.header("Filtros")
    
    opciones_pais = sorted(df["Country"].unique())
    pais = st.selectbox("Pais", opciones_pais , index= None, placeholder="Elige un pais")
    
    if pais:
        opciones_ciudad = sorted(df["City"][ df["Country"] == pais ].unique())
        ciudad = st.selectbox("Ciudad",  opciones_ciudad, index=None )
        
        if ciudad:
            opciones_carreras = sorted(df["Program"][ df["City"] == ciudad].unique())
            carreras = st.selectbox("Carrera", opciones_carreras, index=None)
    
    
# contenido filtrado

df_filtrado = df[
    (df["Country"] == pais)
    ]


def tabla_completa():
    tab1, tab2, tab3, tab4 = st.tabs([ "Universidades" ,"Paises" , "Carreras" ,"Datos"]) 
    
    with tab1:
        df_universidad_paises = df["Country"].value_counts().reset_index()
        fig_histo = px.histogram(df_universidad_paises, x="Country", y="count" ,title="Cantidad por pais")
        st.plotly_chart(fig_histo,use_container_width=True)
        
        fig = px.box(df ,x="University", y="Costo Carrera Final", color="Country")
        st.plotly_chart(fig, use_container_width=True)

    
    with tab2:
        fig = px.sunburst(df,path= ["Country"] ,values="Costo Carrera Final" , title="Costo Final por paises")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:   
        df_carreras = df["Program"].value_counts().reset_index()
        fig_histo_carreras = px.histogram(df_carreras, x="Program", y="count")
        fig_histo_carreras.update_layout(title="Histograma de Carreras", xaxis_title="Carreras", yaxis_title="Cantidad")
        st.plotly_chart(fig_histo_carreras)
        
        fig = px.box(df, x="Country", y="Costo Carrera Final", color="Program", title="Costo de carrera por paises")
        st.plotly_chart(fig, use_container_width=True)
        
    with tab4:
        st.write("## Tabla completa")
        st.write(df)
    


def costo_por_pais():
    
    st.write(f"## Costo de Vida de {pais}")
    df_costo_vida_ciudad = (
        df.loc[ df["Country"] == pais] 
               .groupby("City")["Living_Cost_Index"].mean().round().sort_values()
               )

    col1, col2 = st.columns([1,1.5], vertical_alignment="center")
    with col1:
        st.write(df_costo_vida_ciudad)
        
    with col2:
        fig_bar = px.bar(df_costo_vida_ciudad)
        st.plotly_chart(fig_bar, use_container_width=True)
        
    st.write(f"## Carreras en {pais}")
    df_carreras_pais = df.loc[ df["Country"] == pais, "Program" ]
    st.write(df_carreras_pais)
        
    
    if ciudad: 
        st.divider()
        st.write(f"## Carreras en {ciudad}")
        df_carreras_ciudad = df[ df["City"] == ciudad ]
        df_carreras_ciudad = df_carreras_ciudad.groupby("Program")["Costo Carrera Final"].mean().round().sort_values()
        st.write(df_carreras_ciudad)
    


if pais:
    st.write(df_filtrado)
    costo_por_pais()
    
else:
    tabla_completa()