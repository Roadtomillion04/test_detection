import pyrebase
import streamlit as st

if __name__ == "__main__":
    st.title("This is tile")
    image = st.file_uploader("Upload an image file")
    if image is None:
        st.write("Or Capture live images")
        image = st.camera_input("")

config = {
    "apiKey": "AIzaSyDGIQ_IqRiQAp__05dq40nDAVYMONmx4Qw",
    "authDomain": "warm-actor-387103.firebaseapp.com",
    'databaseURL': "https://warm-actor-387103-default-rtdb.firebaseio.com",
    'projectId': "warm-actor-387103",
    'storageBucket': "warm-actor-387103.appspot.com",
    'messagingSenderId': "235656772589",
    'appId': "1:235656772589:web:b8e246814d2dc8659585e4",
    'measurementId': "G-Z234WKZ420",
    'databaseURL':'https://warm-actor-387103-default-rtdb.firebaseio.com'
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

storage.child("Elephant").child("Image1").put("tiger and elephhant.jpg")
