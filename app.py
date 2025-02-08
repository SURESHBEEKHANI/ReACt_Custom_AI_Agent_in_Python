import streamlit as st
import requests

# Configure Streamlit page
st.set_page_config(
    page_title="ReACt Custom AI Agent",
    page_icon="🤖",
    initial_sidebar_state="expanded"
)

# Page title and description
st.title("🤖 ReACt Custom AI Agent")
st.caption("🔍 AI-Powered Assistance with Custom ReACt  AI Agent ")

# Sidebar with features
with st.sidebar:
    st.divider()
    st.markdown("### AI Agent Features")
    st.markdown(
        """
        - 🧠 Reasoning and Action-based AI
        - 🔍 Advanced Query Processing
        - 📑 Context-Aware Responses
        - 📝 Document Analysis & Insights
        """
    )
    st.divider()
    st.markdown("Built with ReACt | Python | Streamlit")

# Backend API URL
API_URL = "http://127.0.0.1:9999/chat"

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Hello! How can I assist you today?"}
    ]

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capture user input
user_query = st.chat_input("Enter your query")

if user_query:
    # Append user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_query})
    
    # Send request to backend API
    with st.spinner("🧠 Reasoning"):
        response = requests.post(API_URL, json={"messages": [user_query]})
    
    # Handle response
    if response.status_code == 200:
        agent_response = response.json().get("response", "No response received.")
        st.session_state.chat_history.append({"role": "assistant", "content": agent_response})
    else:
        st.error("Failed to get a response from the server.")
    
    # Rerun the app to update chat history
    st.rerun()