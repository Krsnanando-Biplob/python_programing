import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("input frist number",value=None,placeholder="Enter your number...")
num2 = st.number_input("input secand number", value=None, placeholder="Enter your number")

# অপারেশন নির্বাচন
operation = st.selectbox(
    "chose options",
    ("+", "-", "*", "/")
)

# button
if st.button("Calculate"):

    if operation == "+":
        result = num1 + num2

    elif operation == "-":
        result = num1 - num2

    elif operation == "*":
        result = num1 * num2

    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("you can't divite by zero")
            result = None

    if result is not None:
        st.success(f"Result: {result}")