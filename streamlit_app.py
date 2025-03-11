import streamlit as st
import base64
import os
from pathlib import Path

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

# Function to read and display HTML content
def get_html_content(file_path, start_tag, end_tag):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            start_index = content.find(start_tag)
            end_index = content.find(end_tag, start_index)
            if start_index != -1 and end_index != -1:
                return content[start_index + len(start_tag):end_index].strip()
            else:
                return "Content not found in file."
    except FileNotFoundError:
        return f"File {file_path} not found."

# Main app layout
def main():
    # Header
    st.markdown('<div class="header"><h1>Moon Mission Documentation</h1><p>Comprehensive Planning and Implementation Guide</p></div>', unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Select a page:",
        ["Home", "Mission Overview", "Timeline & Visualization", "Technical Specifications", 
         "Crew Training", "Scientific Objectives", "Risk Assessment", "Budget & Resources",
         "Mission Audio"]
    )
    
    # Home page
    if page == "Home":
        st.markdown('<h2>Welcome to the Moon Mission Documentation</h2>', unsafe_allow_html=True)
        
        # Mission cards in a 2-column layout
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<h3>Mission Overview</h3>', unsafe_allow_html=True)
            st.markdown("""
            <p>High-level mission description, objectives, phases, and key components.</p>
            <ul>
                <li>Mission objectives</li>
                <li>Mission phases</li>
                <li>Key components</li>
                <li>Crew requirements</li>
            </ul>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<h3>Technical Specifications</h3>', unsafe_allow_html=True)
            st.markdown("""
            <p>Detailed technical requirements and specifications for all mission systems.</p>
            <ul>
                <li>Launch vehicle specs</li>
                <li>Crew module details</li>
                <li>Life support systems</li>
                <li>Communication systems</li>
            </ul>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<h3>Scientific Objectives</h3>', unsafe_allow_html=True)
            st.markdown("""
            <p>Research goals, experiments, and data collection protocols.</p>
            <ul>
                <li>Research objectives</li>
                <li>Experimental packages</li>
                <li>Sample collection</li>
                <li>Data management</li>
            </ul>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<h3>Budget & Resources</h3>', unsafe_allow_html=True)
            st.markdown("""
            <p>Financial planning and resource allocation details.</p>
            <ul>
                <li>Cost breakdown</li>
                <li>Resource allocation</li>
                <li>Funding sources</li>
                <li>Budget tracking</li>
            </ul>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<h3>Timeline & 3D Visualization</h3>', unsafe_allow_html=True)
            st.markdown("""
            <p>Detailed mission timeline with interactive 3D visualization of mission phases.</p>
            <ul>
                <li>Complete mission timeline</li>
                <li>Interactive 3D illustration</li>
                <li>Key milestones</li>
                <li>Project management details</li>
            </ul>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<h3>Crew Training</h3>', unsafe_allow_html=True)
            st.markdown("""
            <p>Comprehensive training protocols and requirements for mission personnel.</p>
            <ul>
                <li>Selection criteria</li>
                <li>Training programs</li>
                <li>Physical conditioning</li>
                <li>Technical training</li>
            </ul>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<h3>Risk Assessment</h3>', unsafe_allow_html=True)
            st.markdown("""
            <p>Comprehensive analysis of mission risks and mitigation strategies.</p>
            <ul>
                <li>Launch risks</li>
                <li>System risks</li>
                <li>Crew safety</li>
                <li>Emergency protocols</li>
            </ul>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<h3>Mission Audio</h3>', unsafe_allow_html=True)
            st.markdown("""
            <p>Audio recordings from different mission phases.</p>
            <ul>
                <li>Launch audio</li>
                <li>Orbit communications</li>
                <li>Lunar landing</li>
                <li>Ascent and return</li>
            </ul>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Timeline section
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h2>Mission Timeline</h2>', unsafe_allow_html=True)
        
        st.markdown('<div class="phase">', unsafe_allow_html=True)
        st.markdown('<h3>Phase 1: Project Initiation (90 days)</h3>', unsafe_allow_html=True)
        st.markdown('<p>Team formation, initial design reviews, requirements definition</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="phase">', unsafe_allow_html=True)
        st.markdown('<h3>Phase 2: Preliminary Design (180 days)</h3>', unsafe_allow_html=True)
        st.markdown('<p>Component specifications, vendor selection, initial testing plans</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="phase">', unsafe_allow_html=True)
        st.markdown('<h3>Phase 3: Detailed Design (270 days)</h3>', unsafe_allow_html=True)
        st.markdown('<p>Complete system design, prototype development, test planning</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="phase">', unsafe_allow_html=True)
        st.markdown('<h3>Phase 4: Manufacturing & Integration (365 days)</h3>', unsafe_allow_html=True)
        st.markdown('<p>Hardware production, system assembly, initial testing</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="phase">', unsafe_allow_html=True)
        st.markdown('<h3>Phase 5: Testing & Validation (180 days)</h3>', unsafe_allow_html=True)
        st.markdown('<p>Full system testing, crew training, mission simulations</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="phase">', unsafe_allow_html=True)
        st.markdown('<h3>Phase 6: Launch Preparation (90 days)</h3>', unsafe_allow_html=True)
        st.markdown('<p>Final checks, launch site preparation, mission readiness review</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="phase">', unsafe_allow_html=True)
        st.markdown('<h3>Phase 7: Mission Execution (38 days)</h3>', unsafe_allow_html=True)
        st.markdown('<p>Launch, transit to Moon, lunar operations, return journey</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="phase">', unsafe_allow_html=True)
        st.markdown('<h3>Phase 8: Post-Mission Analysis (180 days)</h3>', unsafe_allow_html=True)
        st.markdown('<p>Data analysis, mission report, future planning</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Footer
        st.markdown('<div class="footer">', unsafe_allow_html=True)
        st.markdown('<p>Total Mission Duration: 1,393 days (approximately 3.8 years)</p>', unsafe_allow_html=True)
        st.markdown('<p>For detailed information, please refer to the individual documentation sections.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Mission Audio page
    elif page == "Mission Audio":
        st.markdown('<h2>Mission Audio Files</h2>', unsafe_allow_html=True)
        st.markdown('<p>Listen to audio recordings from different phases of the mission.</p>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3>Launch Phase</h3>', unsafe_allow_html=True)
        st.markdown('<p>Audio recording of the launch sequence and initial ascent.</p>', unsafe_allow_html=True)
        display_audio("launch.wav")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3>Orbit Phase</h3>', unsafe_allow_html=True)
        st.markdown('<p>Communications during orbital operations.</p>', unsafe_allow_html=True)
        display_audio("orbit.wav")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3>Lunar Landing</h3>', unsafe_allow_html=True)
        st.markdown('<p>Audio from the lunar landing sequence.</p>', unsafe_allow_html=True)
        display_audio("landing.wav")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3>Ascent Phase</h3>', unsafe_allow_html=True)
        st.markdown('<p>Audio from the lunar ascent and return journey.</p>', unsafe_allow_html=True)
        display_audio("ascent.wav")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3>Mission Complete</h3>', unsafe_allow_html=True)
        st.markdown('<p>Final communications and mission completion.</p>', unsafe_allow_html=True)
        display_audio("complete.wav")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Other content pages
    elif page == "Mission Overview":
        st.markdown('<h2>Mission Overview</h2>', unsafe_allow_html=True)
        st.markdown('<p>High-level mission description, objectives, phases, and key components.</p>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3>Mission Objectives</h3>', unsafe_allow_html=True)
        st.markdown("""
        <ul>
            <li>Establish a sustainable human presence on the lunar surface</li>
            <li>Conduct scientific research on lunar geology and potential resources</li>
            <li>Test technologies for future Mars missions</li>
            <li>Demonstrate international cooperation in space exploration</li>
            <li>Inspire the next generation of scientists and engineers</li>
        </ul>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3>Key Components</h3>', unsafe_allow_html=True)
        st.markdown("""
        <ul>
            <li>Heavy-lift launch vehicle</li>
            <li>Crew transport module</li>
            <li>Lunar landing module</li>
            <li>Lunar habitat</li>
            <li>Scientific equipment and rovers</li>
            <li>Life support and power systems</li>
        </ul>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    elif page == "Timeline & Visualization":
        st.markdown('<h2>Timeline & 3D Visualization</h2>', unsafe_allow_html=True)
        st.markdown('<p>Detailed mission timeline with visualization of mission phases.</p>', unsafe_allow_html=True)
        
        # Timeline visualization using Streamlit
        import plotly.express as px
        import pandas as pd
        
        # Sample timeline data
        timeline_data = {
            'Phase': ['Project Initiation', 'Preliminary Design', 'Detailed Design', 
                     'Manufacturing & Integration', 'Testing & Validation', 
                     'Launch Preparation', 'Mission Execution', 'Post-Mission Analysis'],
            'Start': [0, 90, 270, 540, 905, 1085, 1175, 1213],
            'Duration': [90, 180, 270, 365, 180, 90, 38, 180]
        }
        
        df = pd.DataFrame(timeline_data)
        df['End'] = df['Start'] + df['Duration']
        
        fig = px.timeline(df, x_start='Start', x_end='End', y='Phase', 
                         color='Phase', title='Mission Timeline (Days)')
        fig.update_layout(xaxis_title='Days from Project Start')
        st.plotly_chart(fig, use_container_width=True)
        
        # 3D visualization placeholder
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3>3D Mission Visualization</h3>', unsafe_allow_html=True)
        st.markdown('<p>Interactive 3D visualization would be displayed here.</p>', unsafe_allow_html=True)
        st.image("https://via.placeholder.com/800x400?text=3D+Mission+Visualization", caption="3D Mission Visualization")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Add other content pages as needed...
    elif page == "Technical Specifications":
        st.markdown('<h2>Technical Specifications</h2>', unsafe_allow_html=True)
        st.markdown('<p>Detailed technical requirements and specifications for all mission systems.</p>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3>Launch Vehicle</h3>', unsafe_allow_html=True)
        st.markdown("""
        <ul>
            <li>Height: 111 meters</li>
            <li>Diameter: 10.1 meters</li>
            <li>Mass: 2,970 metric tons</li>
            <li>Payload capacity to LEO: 130 metric tons</li>
            <li>Payload capacity to TLI: 45 metric tons</li>
            <li>First stage engines: 4 liquid-fueled engines</li>
            <li>Second stage engines: 2 vacuum-optimized engines</li>
        </ul>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3>Crew Module</h3>', unsafe_allow_html=True)
        st.markdown("""
        <ul>
            <li>Capacity: 4 astronauts</li>
            <li>Habitable volume: 16 cubic meters</li>
            <li>Mission duration capability: 21 days</li>
            <li>Life support: Closed-loop system with 30-day redundancy</li>
            <li>Power: Solar arrays with battery backup</li>
            <li>Thermal control: Active fluid loop system</li>
            <li>Communications: S-band and Ka-band systems</li>
        </ul>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Add other content pages as needed...

# Run the app
if __name__ == "__main__":
    main() 