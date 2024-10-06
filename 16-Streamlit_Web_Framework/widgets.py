import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")


name=st.text_input("Enter your name:")
#slider
age = st.slider("Select your age: ",0,100,25)

st.write(f"Your age is : {age}")

#options/selectbox
options = ["Python","Java","C++","JavaScript"]
choice = st.selectbox("Choose your favorite language:",options)
st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello, {name}")

# dataframe
data = {
    "Name":["John","Jane","Jake","Jill"],
    "Age":[28,24,35,40],
    "City":["New York","Loss Angeles","Chicago","Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

## Upload 
uploaded_file = st.file_uploader("Choose a CSV File",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)