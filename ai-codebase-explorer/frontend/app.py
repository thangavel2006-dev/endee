import streamlit as st
import requests

st.set_page_config(page_title="Endee Explorer", layout="wide")

st.title("📂 AI Codebase Explorer (Endee + RAG)")

query = st.text_input("Ask about the codebase:")

if st.button("Analyze"):
    with st.spinner("Thinking..."):
        try:
            response = requests.get(f"http://localhost:8000/ask?query={query}")

            if response.status_code != 200:
                st.error("Backend error. Check terminal.")
            else:
                res = response.json()

                st.subheader("🧠 AI Answer")
                st.write(res.get("answer", "No answer"))

                with st.expander("📁 Sources"):
                    for s in set(res.get("sources", [])):
                        st.code(s)

        except Exception as e:
            st.error(f"Error: {e}")