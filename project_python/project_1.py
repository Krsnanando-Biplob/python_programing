
import streamlit as st

st.header("Ms: Konika Roy",divider=True, anchor=False)

st.title(":orange[**Hello Biplob**]", anchor=False)

st.markdown("my name is biplob")

name = st.text_input("enter your name")
st.write("your name:",name)
age = st.number_input("enter your age",value= None)
st.write("your age:", age)

passa = st.button("enter to confrim")

if passa:
    st.write(f"your name {name} your age {age}")