import streamlit as st
from PIL import Image
from FakeNewsModel import FakeNewsModel

st.set_page_config(page_title="Fake News Classifier",page_icon="fake.png",layout="wide")

col1,col2 = st.columns((2,1))

img1 = Image.open('fake.png')
img2 = Image.open('fk.png')

st.sidebar.image(img1)

col2.image(img2)
col2.image(img2)
col2.image(img2)

col1.write("""
# Fake News Classifier App
* A type of yellow journalism, fake news encapsulates pieces of news that may be hoaxes and is generally spread through social media and other online media.
* This is often done to further or impose certain ideas and is often achieved with political agendas. Such news items may contain false and/or exaggerated claims,\
and may end up being viralized by algorithms, and users may end up in a filter bubble.
""")
col1.write("---")

st.sidebar.title("User Input Parameter")
demo_data = "For a long time in American politics, we\'ve been trapped in a cycle of ever-escalating political polarization. As measured by voting patterns in the US Congress, the two parties have pulled apart to distances we\'ve never seen before. As measured by consistent partisan positioning among voters, the split in the electorate has reached a historic level of divisiveness."
test_data = st.sidebar.text_area("Enter News",demo_data,height=250)

col1.subheader("User Input News")
col1.write(test_data)
col1.write("---")

# Predicting News is Fake Or Real
ob = FakeNewsModel()
output = ob.predict([test_data])

if col1.button("Predict News (Fake/Real)"):
    col1.subheader("Input News is : {}".format(output))
    col1.write("---")

st.sidebar.markdown("<br><hr><center>Created by <strong>Palak Raghuwanshi</strong></center><hr>", unsafe_allow_html=True)





