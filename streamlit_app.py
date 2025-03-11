import streamlit as st
import base64
import os
from pathlib import Path
import re
from bs4 import BeautifulSoup

# Set page configuration
st.set_page_config(
    page_title="Moon Mission Documentation",
    page_icon="🌕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to style the app similar to the HTML version
st.markdown("""
<style>
    .main {
        background-color: #f0f0f0;
    }
    h1, h2, h3 {
        color: #1a237e;
    }
    .stButton button {
        background-color: #1a237e;
        color: white;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .header {
        background-color: #1a237e;
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 30px;
        text-align: center;
    }
    .phase {
        margin-bottom: 15px;
        padding-left: 20px;
        border-left: 3px solid #1a237e;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        background-color: #1a237e;
        color: white;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Function to display audio player if file exists
def display_audio(audio_file):
    if os.path.exists(audio_file):
        audio_bytes = open(audio_file, 'rb').read()
        st.audio(audio_bytes, format='audio/wav')
    else:
        st.warning(f"Audio file {audio_file} not found.")

# Function to read HTML file and extract content
def read_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"<p>File {file_path} not found.</p>"

# Function to render HTML content from file
def render_html_content(html_content, section=None):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # If a specific section is requested, try to find it
    if section:
        section_content = soup.find(id=section) or soup.find(class_=section)
        if section_content:
            return str(section_content)
    
    # Extract the body content
    body_content = soup.body
    if body_content:
        # Remove any script tags
        for script in body_content.find_all('script'):
            script.decompose()
        return str(body_content)
    
    return html_content

# Function to extract document cards from index.html
def extract_document_cards(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    document_grid = soup.find(class_='document-grid')
    if document_grid:
        return document_grid.find_all(class_='document-card')
    return []

# Function to extract timeline from index.html
def extract_timeline(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    timeline = soup.find(class_='timeline')
    if timeline:
        return timeline
    return None

# Function to extract footer from index.html
def extract_footer(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    footer = soup.find(class_='footer')
    if footer:
        return footer
    return None

# Main app layout
def main():
    # Read the index.html file
    index_html = read_html_file('index.html')
    
    # Extract header content
    soup = BeautifulSoup(index_html, 'html.parser')
    header = soup.find(class_='header')
    if header:
        st.markdown(f'<div class="header">{header.decode_contents()}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="header"><h1>Moon Mission Documentation</h1><p>Comprehensive Planning and Implementation Guide</p></div>', unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    pages = ["Home", "Mission Overview", "Timeline & Visualization", "Technical Specifications", 
             "Crew Training", "Scientific Objectives", "Risk Assessment", "Budget & Resources",
             "Mission Audio"]
    
    # Extract document cards to get actual page names
    document_cards = extract_document_cards(index_html)
    if document_cards:
        pages = ["Home"]
        for card in document_cards:
            link = card.find('a')
            if link and link.get('href') and link.text:
                page_name = link.text
                if page_name not in pages:
                    pages.append(page_name)
        pages.append("Mission Audio")
    
    page = st.sidebar.radio("Select a page:", pages)
    
    # Home page
    if page == "Home":
        st.markdown('<h2>Welcome to the Moon Mission Documentation</h2>', unsafe_allow_html=True)
        
        # Extract and display document cards in a 2-column layout
        document_cards = extract_document_cards(index_html)
        if document_cards:
            # Split cards into two columns
            mid_point = len(document_cards) // 2
            col1, col2 = st.columns(2)
            
            with col1:
                for card in document_cards[:mid_point]:
                    st.markdown(f'<div class="card">{card.decode_contents()}</div>', unsafe_allow_html=True)
            
            with col2:
                for card in document_cards[mid_point:]:
                    st.markdown(f'<div class="card">{card.decode_contents()}</div>', unsafe_allow_html=True)
                
                # Add Mission Audio card if not already in the document cards
                if not any("Mission Audio" in card.text for card in document_cards):
                    st.markdown('''
                    <div class="card">
                        <h3>Mission Audio</h3>
                        <p>Audio recordings from different mission phases.</p>
                        <ul>
                            <li>Launch audio</li>
                            <li>Orbit communications</li>
                            <li>Lunar landing</li>
                            <li>Ascent and return</li>
                        </ul>
                    </div>
                    ''', unsafe_allow_html=True)
        else:
            # Fallback if document cards can't be extracted
            st.warning("Could not extract document cards from index.html. Displaying default content.")
            # Default content would go here...
        
        # Extract and display timeline
        timeline = extract_timeline(index_html)
        if timeline:
            st.markdown(f'<div class="card">{timeline.decode_contents()}</div>', unsafe_allow_html=True)
        
        # Extract and display footer
        footer = extract_footer(index_html)
        if footer:
            st.markdown(f'<div class="footer">{footer.decode_contents()}</div>', unsafe_allow_html=True)
    
    # Mission Audio page
    elif page == "Mission Audio":
        st.markdown('<h2>Mission Audio Files</h2>', unsafe_allow_html=True)
        st.markdown('<p>Listen to audio recordings from different phases of the mission.</p>', unsafe_allow_html=True)
        
        audio_files = [
            ("Launch Phase", "launch.wav", "Audio recording of the launch sequence and initial ascent."),
            ("Orbit Phase", "orbit.wav", "Communications during orbital operations."),
            ("Lunar Landing", "landing.wav", "Audio from the lunar landing sequence."),
            ("Ascent Phase", "ascent.wav", "Audio from the lunar ascent and return journey."),
            ("Mission Complete", "complete.wav", "Final communications and mission completion.")
        ]
        
        for title, file, description in audio_files:
            st.markdown(f'<div class="card"><h3>{title}</h3><p>{description}</p></div>', unsafe_allow_html=True)
            display_audio(file)
    
    # Other content pages - load from corresponding HTML files
    else:
        # Map page names to HTML files
        page_to_file = {}
        for card in document_cards:
            link = card.find('a')
            if link and link.get('href') and link.text:
                page_to_file[link.text] = link.get('href')
        
        if page in page_to_file:
            html_file = page_to_file[page]
            html_content = read_html_file(html_file)
            
            # Extract the main content
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Display the title
            st.markdown(f'<h2>{page}</h2>', unsafe_allow_html=True)
            
            # Find and display content sections
            content_container = soup.find(class_='content-container')
            if content_container:
                sections = content_container.find_all(class_='section')
                for section in sections:
                    st.markdown(f'<div class="card">{section.decode_contents()}</div>', unsafe_allow_html=True)
            else:
                # If no sections found, display the whole body content
                body = soup.body
                if body:
                    # Remove header and back button if present
                    header = body.find(class_='header')
                    if header:
                        header.decompose()
                    
                    back_button = body.find(class_='back-button')
                    if back_button:
                        back_button.decompose()
                    
                    st.markdown(f'<div class="card">{body.decode_contents()}</div>', unsafe_allow_html=True)
                else:
                    st.warning(f"Could not extract content from {html_file}")
        else:
            st.warning(f"No HTML file found for {page}")

# Run the app
if __name__ == "__main__":
    main() 