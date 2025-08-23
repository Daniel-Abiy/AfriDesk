import os
import streamlit as st
from afridesk import services, response, locations, welcome, onboarding
from streamlit_card import card
from dotenv import load_dotenv

# Create aliases for backward compatibility
services_list = services.services_list
display_response = response.display_response
government_offices = locations.government_offices
show_welcome_page = welcome.show_welcome_page
onboarding_questionnaire = onboarding.onboarding_questionnaire

# Load environment variables
load_dotenv()


def main():
    # Set page config for wide mode with dark theme
    st.set_page_config(
        page_title="AfriDesk",
        page_icon="🌍",
        menu_items={
            "About": "AfriDesk is an AI-powered platform that helps African citizens navigate government services with ease. Get clear information about government procedures, office locations, required documents, and more.",
            "Get help": None,
            "Report a Bug": None
        },
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Apply custom CSS with light theme
    st.markdown("""
    <style>
        /* Main background - Solid light gray */
        .stApp, body {
            background-color: #f8f9fa;
            color: #1e293b;
        }
        
        /* Text color for better contrast */
        .stApp, .stText, .stMarkdown, .stMarkdown p {
            color: #212529 !important;
        }
        
        /* Sidebar */
        .css-1d391kg, .css-1d391kg > * {
            background-color: #f8f9fa !important;
            color: #1e293b !important;
            border-right: 1px solid #dee2e6;
        }
        
        /* Headers - Darker for better contrast */
        h1, h2, h3, h4, h5, h6 {
            color: #0f172a !important;  /* slate-900 */
            font-weight: 700;
        }
        
        /* Text */
        .stMarkdown, .stText, .stTextInput > div > div > input, .stTextArea > div > div > textarea {
            color: #e2e8f0 !important;
        }
        
        /* Buttons */
        .stButton > button {
            background-color: #4f46e5;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            background-color: #4338ca;
            transform: translateY(-2px);
        }
        
        /* Input fields */
        .stTextInput > div > div > input, .stTextArea > div > div > textarea {
            background-color: #1e293b;
            border: 1px solid #334155;
            border-radius: 8px;
            padding: 0.5rem;
        }
        
        /* Select boxes */
        .stSelectbox > div > div {
            background-color: #1e293b;
            border: 1px solid #334155;
            border-radius: 8px;
        }
        
        /* Cards and containers */
        .stTabs > div > div > div > div > div {
            background-color: #1e293b;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            border: 1px solid #334155;
        }
        
        /* Chat messages */
        .stChatMessage {
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            max-width: 85%;
        }
        
        .stChatMessage[data-testid="stChatMessage"] {
            background-color: #4f46e5;
            color: white;
            margin-left: auto;
        }
        
        .stChatMessage[data-testid="stChatMessage"]:not([data-message-author="user"]) {
            background-color: #1e293b;
            color: #e2e8f0;
            border: 1px solid #334155;
            margin-right: auto;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize session state for navigation
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'welcome'

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style.css")

    # Sidebar navigation
    with st.sidebar:
        st.markdown("# AfriDesk 🌍")
        st.markdown("## Navigation")
        st.button("Home", on_click=lambda: setattr(st.session_state, 'current_page', 'welcome'))
        st.button("Government Services", on_click=lambda: setattr(st.session_state, 'current_page', 'services'))
        st.button("Office Locations", on_click=lambda: setattr(st.session_state, 'current_page', 'locations'))
        st.button("Ask Questions", on_click=lambda: setattr(st.session_state, 'current_page', 'chat'))

        # Try to get API key from environment first, then from input
        gemini_api_key = os.getenv('GEMINI_API_KEY')
        if not gemini_api_key:
            gemini_api_key = st.text_input("Gemini API Key", key="gemini_api_key", type="password")
            st.markdown("[Get a Gemini API key](https://ai.google.dev/)")
    
    st.session_state.gemini_api_key = gemini_api_key

    # Handle page navigation
    if st.session_state['current_page'] == 'welcome':
        show_welcome_page()  # Using the welcome page
    elif st.session_state['current_page'] == 'onboarding':
        onboarding_questionnaire()
    elif st.session_state['current_page'] == 'services':
        if st.session_state.get('onboarding_complete', False):
            services_list()
        else:
            st.warning("Please complete the onboarding process first.")
            st.session_state['current_page'] = 'welcome'
            st.rerun()
    elif st.session_state['current_page'] == 'locations':
        if 'onboarding_complete' in st.session_state and st.session_state.onboarding_complete:
            government_offices()
        else:
            st.session_state['current_page'] = 'welcome'
            st.rerun()
    elif st.session_state['current_page'] == 'chat':
        if 'onboarding_complete' in st.session_state and st.session_state.onboarding_complete:
            if 'gemini_api_key' in st.session_state and st.session_state.gemini_api_key:
                display_response(api_key=st.session_state.gemini_api_key)
            else:
                st.warning("Please enter your Gemini API key in the sidebar to use the chat feature.")
        else:
            st.session_state['current_page'] = 'welcome'
            st.rerun()

def welcome_page():
    st.title("Welcome to AfriDesk 🌍")
    st.markdown("### Your Guide to Government Services in Africa")

    # Hero section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ## Navigating Government Services Made Simple
        
        AfriDesk helps you:
        - 📋 Understand government procedures and requirements
        - 📍 Find government offices near you
        - ⚖️ Get clear explanations of laws and regulations
        - 🕒 Check office hours and required documents
        - 🌐 Access services across multiple African countries
        
        Get started by selecting a service or asking a question!
        """)
    with col2:
        # Using a placeholder image from a free image service
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Africa_map_blank.svg/1200px-Africa_map_blank.svg.png", 
                use_column_width=True, 
                caption="African Countries Map")

    # Quick access cards
    st.markdown("## Quick Access")
    
    # Create a row of cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        card(
            title="Popular Services",
            text="Passport, ID, Business Registration",
            styles={
                "card": {
                    "width": "100%",
                    "padding": "20px",
                    "border-radius": "10px",
                    "box-shadow": "0 4px 6px rgba(0,0,0,0.1)",
                    "margin-bottom": "20px"
                }
            }
        )
    
    with col2:
        card(
            title="Find Offices",
            text="Locate government offices near you",
            styles={
                "card": {
                    "width": "100%",
                    "padding": "20px",
                    "border-radius": "10px",
                    "box-shadow": "0 4px 6px rgba(0,0,0,0.1)",
                    "margin-bottom": "20px"
                }
            }
        )
    
    with col3:
        card(
            title="Ask Questions",
            text="Get help with government procedures",
            styles={
                "card": {
                    "width": "100%",
                    "padding": "20px",
                    "border-radius": "10px",
                    "box-shadow": "0 4px 6px rgba(0,0,0,0.1)",
                    "margin-bottom": "20px"
                }
            }
        )


    # Additional information section
    st.markdown("---")
    st.markdown("## About AfriDesk")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        ### Our Mission
        To make government services more accessible and understandable for all African citizens, 
        providing clear guidance and support through our AfriDesk platform.
        """)
    
    with col2:
        st.info("""
        ### Our Vision
        A future where every African citizen can easily access and navigate government services 
        with confidence and clarity, regardless of their background or location.
        """)
    
    # Call to action
    st.markdown("---")
    st.markdown("## Ready to Get Started?")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Browse Services"):
            st.session_state['current_page'] = 'services'
    with col2:
        if st.button("Find Offices"):
            st.session_state['current_page'] = 'locations'
    with col3:
        if st.button("Ask a Question"):
            st.session_state['current_page'] = 'chat'
        

if __name__ == "__main__":
    main()

