import streamlit as st
import requests
url = "http://127.0.0.1:8000"
st.title("Patient Management System")
st.header("Patient Details")
pid = st.text_input("Enter Patient ID")
name = st.text_input("Enter Patient Name")
height = st.number_input("Enter Height")
weight = st.number_input("Enter weight")
gender = st.selectbox(
    " Select Gender",["male", "female"]
)





if st.button("Add Patient"):

    patient_data = {
        "pid": pid,
        "name": name,
        "height": height,
        "weight": weight,
        "gender": gender
    }

    response = requests.post(
        "http://127.0.0.1:8000/create",
        json=patient_data
    )

    if response.status_code == 200 or response.status_code == 201:
        st.success("Patient added successfully")
        st.write(response.json())

    elif response.status_code == 422:
        st.error("Invalid patient data")

    else:
        st.error("Something went wrong")
        st.write(response.json())
st.subheader("Patient Details")

if st.button("Display Patients"):
    response = requests.get(f"{url}/view")
    if response.status_code == 200:
        patients = response.json()
        st.dataframe(patients)
    else:
        st.error("Unable to get patient data")
