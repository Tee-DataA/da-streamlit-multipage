import streamlit as st
from app_pages.multi_page import MultiPage  # Import the multi_page module from the specified package
from app_pages.page_calculator import calculator_body  # Import the calculator_body function from the page_calculator module

# Create an instance of the MultiPage class with the app name "calculator"
app = MultiPage(app_name="calculator")

# Add a page to the app with the title "Calculator" and the content from calculator_body
app.add_page("Calculator", calculator_body)

# Run the app
app.run()
