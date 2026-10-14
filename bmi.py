
import streamlit as st

st.title("BMI Calculator")
st.write("This application is used to calculate BMI")

weight = st.number_input("Enter your Weight (in kg)")
height = st.number_input("Enter your height (in m)")

if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            st.write("You are underweight")

        elif bmi >= 18.5 and bmi < 25:
            st.success("BMI lies in the normal range")

        elif bmi >= 25 and bmi < 30:
            st.write("BMI lies in the overweight range")

        else:
            st.write("You are obese")

        st.success(f"Your BMI is {bmi:.2f}")

    else:
        st.warning("Please enter a valid weight and height")
