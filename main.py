import streamlit as st
from alize.core.agent import AlizeCore

st.set_page_config(
    page_title="Chat..",
    page_icon="🤖"
)

# Initialize Agent
if "agent" not in st.session_state:
    st.session_state.agent = AlizeCore()

# Initialize session states
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []
if "input" not in st.session_state:
    st.session_state["input"] = ""
if "stored_session" not in st.session_state:
    st.session_state["stored_session"] = []

# Define function to get user input
def get_text():
    """
    Get the user input text.
    Returns:
        (str): The text entered by the user
    """
    input_text = st.text_input("You: ", st.session_state["input"], key="input",
                            placeholder="Your AI assistant here! Ask me anything ...", 
                            label_visibility='hidden')
    return input_text

# Define function to start a new chat
def new_chat(model_name):
    """
    Clears session state and starts a new chat.
    """
    st.session_state.agent.update_model(model_name)
    save = []
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        save.append("User:" + st.session_state["past"][i])
        save.append("Bot:" + st.session_state["generated"][i])        
    st.session_state["stored_session"].append(save)
    st.session_state["generated"] = []
    st.session_state["past"] = []
    st.session_state["input"] = ""
    st.session_state.agent.reset_chat_hist()

# Define function to update model knowledge
def update_knowledge(keyword):
    st.session_state.agent.update_knowledge(keyword)

st.sidebar.text("Configuration Area")

# # Set up sidebar with various options
# with st.sidebar.expander("Select Base Model", expanded=False):
#     MODEL = st.selectbox(label='Model', options=['gpt-3.5-turbo','text-davinci-003','text-davinci-002','code-davinci-002'])

with st.sidebar.expander("Start a new chat", expanded=True):
    st.session_state.model_name = st.selectbox(
            label='Model',
            options=['gpt-3.5-turbo','text-davinci-003','text-davinci-002','code-davinci-002']
        )
    # Add a button to start a new chat
    st.button("New Chat", on_click = new_chat, args=(st.session_state.model_name,), type='primary')
    

with st.sidebar.expander("Update Knowledge", expanded=False):
    NEW_KNOWLEDGE = st.text_input("ADD KEYWORD KNOWLEDGE")
    start_btn = st.button("Update and Start Chat", on_click=update_knowledge, args=(NEW_KNOWLEDGE,),type='primary')
    if start_btn:
        update_knowledge(NEW_KNOWLEDGE)
    
# Set up the Streamlit app layout
st.title("🤖 Chat with Alize")
st.subheader("Your personal Assistant chatbot..")


# Get the user input
user_input = get_text()

# Generate the output using the ConversationChain object and the user input, and add the input/output to the session
if user_input:
    output = st.session_state.agent.predict(user_input)  
    st.session_state.past.append(user_input)  
    st.session_state.generated.append(output) 

# Allow to download as well
download_str = []
# Display the conversation history using an expander, and allow the user to download it
with st.expander("Conversation", expanded=True):
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        st.info(st.session_state["past"][i],icon="🧐")
        st.success(st.session_state["generated"][i], icon="🤖")
        download_str.append(st.session_state["past"][i])
        download_str.append(st.session_state["generated"][i])
    
    # Can throw error - requires fix
    download_str = '\n'.join(download_str)
    if download_str:
        st.download_button('Download',download_str)


# Display stored conversation sessions in the sidebar
for i, sublist in enumerate(st.session_state.stored_session):
        with st.sidebar.expander(label= f"Conversation-Session:{i}"):
            st.write(sublist)

# Allow the user to clear all stored conversation sessions
if st.session_state.stored_session:   
    if st.sidebar.checkbox("Clear-all"):
        st.session_state["stored_session"] = []