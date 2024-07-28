import streamlit as st

# Title and description
st.title("BMI Calculator")
st.write("Enter your height and weight to calculate your BMI.")

# Input fields for height and weight
height = st.number_input("Height (cm)", min_value=0.0, format="%.2f")
weight = st.number_input("Weight (kg)", min_value=0.0, format="%.2f")

# Calculate BMI
if height > 0 and weight > 0:
    bmi = weight / ((height / 100) ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

    # Categorize BMI
    if bmi < 18.5:
        st.write("Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        st.write("Category: Normal weight")
    elif 25 <= bmi < 29.9:
        st.write("Category: Overweight")
    else:
        st.write("Category: Obesity")

    # Visualization
    import matplotlib.pyplot as plt

    categories = ["Underweight", "Normal weight", "Overweight", "Obesity"]
    values = [18.5, 24.9, 29.9, bmi] if bmi > 29.9 else [bmi, 18.5, 24.9, 29.9]

    fig, ax = plt.subplots()
    ax.barh(categories, values, color=['blue', 'green', 'orange', 'red'])
    ax.axvline(x=bmi, color='black', linestyle='--')
    plt.xlabel('BMI Value')
    plt.title('BMI Categories')

    st.pyplot(fig)
else:
    st.write("Please enter valid height and weight.")
