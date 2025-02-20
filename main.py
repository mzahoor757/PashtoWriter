import streamlit as st
from backend import roman_to_pashto

st.set_page_config(page_title="Roman Pashto to Proper Pashto Converter", layout="centered")

st.title("📝 Roman Pashto ➝ Proper Pashto Converter")

# User input
roman_text = st.text_area("Enter Roman Pashto text:", placeholder="Sanga ye?")

if st.button("Convert"):
    if roman_text.strip():
        with st.spinner("Converting... Please wait ⏳"):
            pashto_text = roman_to_pashto(roman_text)
            st.session_state.converted_text = pashto_text  # Store in session
        st.success("✅ Converted Text:")

        # Display Converted Text with Increased Font Size
        st.markdown(f'<pre style="font-size: 20px;">{st.session_state.converted_text}</pre>', unsafe_allow_html=True)

        # Copy Button using JavaScript
        st.markdown(
            f"""
            <button onclick="copyToClipboard()" style="
                padding: 10px 15px; 
                font-size: 16px; 
                border-radius: 5px;
                background-color: #007bff; 
                color: white; 
                border: none;
                cursor: pointer;
                margin-top: 10px;
            ">📋 Copy Text</button>
            <script>
            function copyToClipboard() {{
                navigator.clipboard.writeText("{st.session_state.converted_text}");
                alert("Copied to clipboard!");
            }}
            </script>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("⚠️ Please enter some text to convert.")

st.markdown("Built with **Langchain + OpenAI API + Streamlit** by **_Hassaan Yousafzai_**")
