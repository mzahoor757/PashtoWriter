import streamlit as st
from backend import roman_to_pashto
import pyperclip

st.set_page_config(page_title="Roman Pashto to Proper Pashto Converter", layout="centered")

st.image("peshawar.jpg", use_container_width=True)

st.title("📝 Roman Pashto ➝ Proper Pashto Converter")

# User input
roman_text = st.text_area("Enter Roman Pashto text:", placeholder="Sanga ye?")

if "converted_text" not in st.session_state:
    st.session_state.converted_text = ""

if st.button("Convert"):
    if roman_text.strip():
        with st.spinner("Converting... Tamasha Kawa Janana xD 😜"):
            pashto_text = roman_to_pashto(roman_text)
            st.session_state.converted_text = pashto_text  # Store result in session state
        st.success("✅ Converted Text:")
    else:
        st.warning("⚠️ Please enter some text to convert.")

# Display converted text
if st.session_state.converted_text:
    st.markdown(f"<p style='font-size:30px;'>{st.session_state.converted_text}</p>", unsafe_allow_html=True)

    # Copy button functionality (without refreshing)
    if st.button("📋 Copy Text"):
        pyperclip.copy(st.session_state.converted_text)
        st.success("✅ Text copied to clipboard!")

st.markdown("Built with **Langchain + OpenAI API + Streamlit** by **_Hassaan Yousafzai_**")
