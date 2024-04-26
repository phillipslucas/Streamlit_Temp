import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/phillipslucas/Streamlit_Temp>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = r"C:\Users\phill\Downloads\RiverFire_AIlogo.jpg"
st.sidebar.image(logo)

st.title("2023 Libya Floods")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        m.split_map(
            left_layer="https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-07-01.tif", 
            right_layer="https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-09-13.tif"
        )
        

m.to_streamlit(height=700)
