import streamlit as st
from src.PS import PinGenerator, RandomPassword, MemorablePasswordGenerator

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXszccTOxAaRRS7_73BE4pFtb2jwOmfTdD9w&s', width=400)
st.title(':coffee: Password Generator')

option = st.radio(
    "select your option:",
    ('Pin code', 'Random pass', 'Memorable pass')
)

if option == 'Pin code':
    length = st.slider('select the length of your pin code:', 8, 20)
    generator = PinGenerator(length)
    password = generator.generate()

elif option == 'Random pass':
    length = st.slider('select the length of your password:', 8, 20)
    include_symbol = st.toggle('include symbol')
    include_numb = st.toggle('include number')
    generator = RandomPassword(length,
                               include_numb,
                               include_symbol)
    password = generator.generate()

elif option == 'Memorable pass':
    nf = st.slider('select number of words:', 4, 14)
    seprator = st.text_input('Seperator', value='_')
    capitalization = st.toggle('Capitalization')
    vocab = ["lantern", "breeze", "mosaic", "clutch", "orbit",
             "thistle", "gravel", "whistle", "drift", "velvet"]
    generator = MemorablePasswordGenerator(number_of_words=nf,
                                           seprator=seprator,
                                           cap=capitalization,
                                           vocab=vocab)
    password = generator.generate()


st.write(fr"Your pass is ```{password}``` ")
