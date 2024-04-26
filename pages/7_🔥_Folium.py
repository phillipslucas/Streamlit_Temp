import streamlit as st
import thebeans.foliummap as thebeans

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/phillipslucas/Streamlit_Temp>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://raw.githubusercontent.com/phillipslucas/Streamlit_Temp/main/data/RiverFire_AIlogo.jpg"
st.sidebar.image(logo)

st.title("Burn Scars")

with st.expander("See source code"):
    with st.echo():
        m = thebeans.Map()
        m.add_basemap("OpenTopoMap")
        

m.to_streamlit(width = 1000, height=700)
