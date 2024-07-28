import streamlit as st

# Title of the app
st.title('BMI Calculator')

# Input: User's height in centimeters
height = st.number_input('Enter your height (cm)', min_value=0.0, value=170.0)

# Input: User's weight in kilograms
weight = st.number_input('Enter your weight (kg)', min_value=0.0, value=70.0)

# Calculate BMI
if height > 0 and weight > 0:
    height_m = height / 100  # Convert height to meters
    bmi = weight / (height_m ** 2)  # Calculate BMI
    st.write(f'Your BMI is {bmi:.2f}')
    # Display BMI category
    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")
else:
    st.write('Please enter valid height and weight')
