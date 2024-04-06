import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import numpy as np



st.set_page_config(
    page_title="Iris Explorer",
    page_icon="🌷",
    layout="centered", # centered, wide 
    initial_sidebar_state="auto", 
    menu_items=None
)

st.title("🌷 Iris Explorer")

df = pd.read_csv('https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv')

with st.sidebar:
    # Input filter options
    st.subheader("Iris Data Screening")
    st.caption("This dataset contains data on three species of iris leaves, including the length and width of the sepals and petals. Use the provided filters to explore the relationships between species, sepal, and petal!")
    sepal_length_slider = st.slider(
        "Sepal Length (mm)",
        min(df["sepal_length"]),
        max(df["sepal_length"]),
    )
    sepal_width_slider = st.slider(
        "Sepal Width (mm)",
        min(df["sepal_width"]),
        max(df["sepal_width"]),
    )


    species_filter = st.multiselect("Species", df["species"].unique())

    option = st.selectbox(
   "Petal length's range",
   ("< 5mm", "5 - 6mm", "> 6mm"),
   index=None,
   placeholder="Select petal length range...",
)

st.write('Petal length range:', option)

# Filter data

if species_filter:
    df = df[df["species"].isin(species_filter)]

df = df[df["sepal_length"] > sepal_length_slider]
df = df[df["sepal_width"] > sepal_width_slider]

if option == "< 5mm":
    df = df[df["petal_length"] < 5.0]
elif option == "5 - 6mm":
    df = df[(df["petal_length"] >= 5.0) & (df["petal_length"] <= 6.0)]
elif option == '> 6mm':
    df = df[df["petal_length"] > 6.0]
 
with st.expander("RAW Data"):
    st.markdown("Iris leaves'length and width of the sepals and petals in three species." )
    st.write(df)




fig = px.histogram(
    df, 
    x="sepal_length"
)
st.subheader("Length distribution of Iris sepal")
st.plotly_chart(fig)

fig2 = px.histogram(
    df, 
    x="species",
    color="species"
)
st.subheader("Count of Iris in different species")
st.plotly_chart(fig2)


fig3 = px.scatter(
    df, 
    x="sepal_length", 
    y="petal_length",
    color="species"
)

st.subheader("Rerlationship of Iris's sepal length and petal length")
st.plotly_chart(fig3)


fig4 = px.scatter(
    df,
    x = "sepal_length",
    y = "sepal_width",
    color="species"
)
st.subheader("Relationship of Iris's sepal length and sepal width")
st.plotly_chart(fig4)

