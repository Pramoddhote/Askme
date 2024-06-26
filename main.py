from langchain.llms import GooglePalm
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")

llm = GooglePalm(google_api_key=API_KEY, temperature=0.5)
import streamlit as st


# Streamlit App

def main():
    st.title("Ask Me Anything!")
    st.markdown("###### developed by Pramod!")

    # Input field for the question
    question = st.text_input("Ask a question : ", key="input_field")

    # JavaScript to trigger button click on "Enter" key press
    js_script = """
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const inputField = document.getElementById('input_field');
            inputField.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    document.getElementById('get_answer_button').click();
                }
            });
        });
    </script>
    """
    st.markdown(js_script, unsafe_allow_html=True)


    if st.button("Get Answer", key="get_answer_button"):
        if question:
            # Generate and display the answer
            answer = llm(question)
            st.write("Answer : ", answer)
        else:
            st.write("Please enter a question.")

if __name__ == "__main__":
    main()
