import streamlit as st
import os

def show_welcome_page():
    """
    Show the welcome page with the main interface
    """
    # Set page to use full width
    st.set_page_config(layout="wide")
    
    # Remove default padding and margins
    st.markdown("""
    <style>
        .main > div {
            max-width: 100%;
            padding: 0;
        }
        .stApp {
            padding: 0 !important;
        }
        .stButton > button {
            width: 200px;
            margin: 20px auto;
            display: block;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Read the HTML file
    html_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'index.html')
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Hide the HTML button since we'll use Streamlit's button
        html_content = html_content.replace('id="startButton"', 'style="display: none;"')
        
        # Display the HTML content in full width
        st.components.v1.html(html_content, height=800, scrolling=False)
        
        # Add a single centered button below the HTML content
        if st.button("Get Started", key="get_started_btn"):
            st.session_state['current_page'] = 'onboarding'
            st.rerun()
                
    except Exception as e:
        st.error(f"Error loading welcome page: {str(e)}")
        st.markdown("""
        <div style='text-align: center; padding: 20px;'>
            <h1>Welcome to AfriDesk</h1>
            <p>Your one-stop platform for accessing government services across Africa.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Get Started"):
            st.session_state['current_page'] = 'onboarding'
            st.rerun()
