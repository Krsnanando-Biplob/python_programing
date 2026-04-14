
import streamlit as st

st.header("Ms: Konika Roy",divider=True, anchor=False)

st.title(":orange[**Hello Biplob**]", anchor=False)

st.markdown("my name is biplob")

name = st.text_input("enter your name", placeholder="write your name...")
# st.write("your name:",name)
age = st.number_input("enter your age",value= None, placeholder="write your age...")
# st.write("your age:", age)
pas = st.text_input("enter your password",type="password",placeholder="write your password...")

passa = st.button("enter to confrim",type="primary")

if passa:
    st.write(f"your name {name} your age {age}")
    
seletedd = st.selectbox("your select profation ",
                        ("student","teacher","jobholder"),
                        index = None,
                        accept_new_options =True
                        )


st.write("selection :",seletedd)

print(type(seletedd))


imag = st.file_uploader("enter your img", type=["jpg",'jpeg',"png"],
                        accept_multiple_files = True)
print(type(imag))

if imag:
    col = st.columns(len(imag))
    for i, img in enumerate(imag):
        col[i].image(img)


