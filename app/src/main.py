import streamlit as st
import os
from dotenv import load_dotenv
from logic import trigger_n8n_webhook

# Page configuration
# TODO: Update the page title and icon for your specific project
st.set_page_config(
    page_title="n8n Automation Hub",
    page_icon="🤖",
    layout="centered"
)

# Load environment variables
load_dotenv()

def login():
    """Simple login screen."""
    st.title("🔐 Client Login")
    
    # Sidebar navigation placeholder
    # TODO: Add your custom branding/logo here
    st.sidebar.markdown("### [Client Logo]")
    st.sidebar.divider()
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        
        if submit:
            if username == os.getenv("APP_USERNAME") and password == os.getenv("APP_PASSWORD"):
                st.session_state["authenticated"] = True
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password.")

def main_app():
    """Main dashboard after login."""
    # TODO: Update the dashboard title
    st.title("🤖 n8n Automation Hub")
    
    # Sidebar navigation
    # TODO: Add more sidebar options or info
    st.sidebar.markdown("### [Client Logo]")
    st.sidebar.divider()
    st.sidebar.write(f"Welcome, **{os.getenv('APP_USERNAME')}**")
    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()

    # Dashboard logic
    st.header("Trigger Automation")
    st.write("Click the button below to start the automation workflow.")
    
    # Example Input for the workflow
    # TODO: Replace or add more inputs needed for your automation
    task_name = st.text_input("Task Name", placeholder="Enter a name for this run...")
    
    if st.button("🚀 Start Automation"):
        if not task_name:
            st.warning("Please provide a task name.")
        else:
            with st.spinner("Running automation... Please wait."):
                # TODO: Update the payload structure to match your n8n workflow
                payload = {"task": task_name, "triggered_by": "streamlit_ui"}
                result = trigger_n8n_webhook(payload)
                
                if "error" in result:
                    st.error(result["error"])
                    if st.button("Retry"):
                        st.rerun()
                else:
                    st.success("Automation completed successfully!")
                    st.json(result)

# Session state management
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    main_app()

# TODO: Add more tabs or pages using st.tabs() or streamlit multipage feature
