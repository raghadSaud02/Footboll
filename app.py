import streamlit as st
import requests
import json

st.image("image.png")
st.title('Players Values Prediction ')
#st.write('')
#url ="https://deplument-usecase7.onrender.com/"

params = {
          "age": 21.0,
          "appearance": 34,
          "minutes_played": 2758,
          "highest_value": 2000000
 }

# User inputs with text input for keyboard input
age = st.text_input("Insert age", value="", placeholder="Type a number...")
appearance = st.text_input("Insert appearance", value="", placeholder="Type a number...")
minutes_played = st.text_input("Insert minutes played", value="", placeholder="Type a number...")
highest_value = st.text_input("Insert highest value", value="", placeholder="Type a number...")

# Convert text inputs to integers if they are not empty
try:
    age = int(age) if age else 0
except ValueError:
    st.error("Please enter a valid number for age")

try:
    appearance = int(appearance) if appearance else 0
except ValueError:
    st.error("Please enter a valid number for appearance")

try:
    minutes_played = int(minutes_played) if minutes_played else 0
except ValueError:
    st.error("Please enter a valid number for minutes played")

try:
    highest_value = int(highest_value) if highest_value else 0
except ValueError:
    st.error("Please enter a valid number for highest value")

# Display the inputs
#st.write(f"Age: {age}")
#st.write(f"Appearance: {appearance}")
#st.write(f"Minutes Played: {minutes_played}")
#st.write(f"Highest Value: {highest_value}")

# Converting the inputs into a JSON format
inputs = {
    "age": age,
    "appearance": appearance,
    "minutes_played": minutes_played,
    "highest_value": highest_value,
    }

# When the user clicks on the button, it will fetch the API
if st.button('Get Prediction'):
    try:
        res = requests.post(
            url="https://deplument-usecase7.onrender.com/predict",
            headers={"Content-Type": "application/json"},
            data=json.dumps(inputs)
        )
        res.raise_for_status()  # Check for HTTP request errors
        st.subheader(f"Prediction Result  = {res.json()}")

    except requests.exceptions.RequestException as e:
        st.error(f"HTTP Request failed: {e}")
    except ValueError as e:
        st.error(f"Failed to parse JSON response:{e}")
