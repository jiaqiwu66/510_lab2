import streamlit as st
import pandas as pd
import seaborn as sns

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
    sepal_length_slider = st.slider(
        "Sepal Length (mm)",
        min(df["sepal_length"]),
        max(df["sepal_length"]),
    )


    species_filter = st.multiselect("Species", df["species"].unique())

# Filter data

if species_filter:
    df = df[df["species"].isin(species_filter)]
df = df[df["sepal_length"] > sepal_length_slider]


# Filter data
with st.expander("RAW Data"):
    st.write(df)


# st.write(df)