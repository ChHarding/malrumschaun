import streamlit as st


st.title("Stremlit Test")
st.subheader("This is a subheader")
st.write("This is very fine.")  
st.markdown("[Streamlit](https://www.streamlit.io)") 
html_page = """
<div style="background-color:blue;padding:50px">
<p style="color:yellow;font-size:50px">Enjoy Streamlit!</p>
</div>
"""
st.markdown(html_page, unsafe_allow_html=True)
st.success("Success!")
if st.button("Play"):
      st.text("Hello world!")
if st.checkbox("Checkbox"):
      st.text("Checkbox selected") 
city = st.selectbox("Your City", ["Napoli", "Palermo", "Catania"])
occupation = st.multiselect("Your Occupation", ["Programmer", "Data Scientist", "IT Consultant", "DBA"])
select_val = st.slider("Select a Value", 1, 10)