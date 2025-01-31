import streamlit as st

def calculator_body():
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        num1 = st.number_input(label='Enter the first number', step=1)
    with col2:
        num2 = st.number_input(label='Enter the second number', step=1)
    with col3:
        operation = st.selectbox(label='Select the operation', options=['+', '-', '*', '/'])

    if st.button("Click here to calculate"):
        if num2 == 0 and operation == "/":
            st.error("Cannot divide by zero")
        else:
            calculator_function(num1, num2, operation)

def calculator_function(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        st.error("Invalid operation")
        return

    st.success(f"The result of {num1} {operation} {num2} is **{result}**")
