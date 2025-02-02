import streamlit as st
import json
from groq import Groq

client = Groq(
    api_key="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",     
)

# Load website content
with open("bmsit_data.json", "r") as file:
    website_data = json.load(file)

# Initialize chatbot memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chatbot function
def chatbot_response(question, memory):
    question_input = {"role": "user", "content": question}
    
    # Append question to the memory
    memory.append(question_input)
    
    # Check if the question is about the principal
    if:
        # Use Groq for general responses
        llm_response = client.chat.completions.create(
            messages=[
                question_input
            ],
            model="llama3-8b-8192",
        )
        response = llm_response.choices[0].message.content
    
    # Append bot response to memory
    memory.append({"role": "assistant", "content": response})
    return response

# Streamlit interface
st.title("BMSIT Chatbot")
st.write("Ask me anything about BMSIT!")

user_input = st.text_input("Your question:")

if user_input:
    response = chatbot_response(user_input + " of bms institute of technology and management bengaluru", st.session_state.messages)
    st.text_area(
        "Chat History",
        value=f"{st.session_state.messages[-1]['role'].capitalize()}: {st.session_state.messages[-1]['content']}",
        height=300
    )
