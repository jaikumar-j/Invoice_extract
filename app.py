import streamlit as st
from PIL import Image
import pytesseract
from googletrans import Translator

translator = Translator()

st.set_page_config(page_title="Multilanguage Invoice Extractor")

st.title("Multilanguage Invoice Extractor")

uploaded_file = st.file_uploader("Upload an invoice (Image/PDF)", type=["jpg", "jpeg", "png", "pdf"])

target_language = st.text_input("Enter language code", "en")

if st.button("Extract and Translate"):
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Invoice", use_column_width=True)

        extracted_text = pytesseract.image_to_string(image)
        st.subheader("Extracted Text:")
        st.write(extracted_text)

        translated_text = translator.translate(extracted_text, dest=target_language).text
        st.subheader(f"Translated Text ({target_language}):")
        st.write(translated_text)
    else:
        st.write("Please upload an invoice.")
