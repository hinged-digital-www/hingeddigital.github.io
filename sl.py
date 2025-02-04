import streamlit as st

# Initialize Ollama
llm = Ollama(model="codellama")

# Create a conversation chain with memory
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

# Set up Streamlit app
st.title("AI Chatbot")
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Get user input
if prompt := st.chat_input("Enter your message"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response from LLM
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        response = conversation.run(prompt, callbacks=[st_callback])
        st.write(response)
     
    # Add assistant message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
