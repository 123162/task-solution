import streamlit as st
import requests

st.set_page_config(page_title="Medical Semantic Search", layout="centered")

st.title("🩺 Medical Semantic Search")
print("✅ Streamlit UI loaded")

query = st.text_input("Enter your symptom, diagnosis or medical question:")

if st.button("Search"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        with st.spinner("Searching..."):
            response = requests.post("http://medical-backend:8000/search", json={"query": query})
            if response.status_code == 200:
                results = response.json().get("results", [])
                if not results:
                    st.info("No relevant answers found.")
                else:
                    for i, item in enumerate(results, 1):
                        st.markdown(f"### {i}. ❓ {item['question'] or 'No question'}")
                        st.markdown(f"**💡 Answer:** {item['answer'] or 'N/A'}")
                        st.markdown(f"📚 Source: `{item['source']}`\n---")
            else:
                st.error("Something went wrong. Check your FastAPI server.")
