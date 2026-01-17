import os
import streamlit as st
from utils.data_loader import load_data

def page():
    # Custom CSS for enhanced styling
    st.markdown("""
        <style>
        /* Main container */
        .main {
            padding: 1rem 2rem;
        }
        
        /* Hero section */
        .hero-section {
            background: linear-gradient(135deg, #0891b2 0%, #06b6d4 50%, #14b8a6 100%);
            padding: 3rem 2rem;
            border-radius: 20px;
            margin-bottom: 2rem;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
            text-align: center;
        }
        
        .hero-title {
            color: white;
            font-size: 2.8rem;
            font-weight: 800;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }
        
        .hero-subtitle {
            color: rgba(255, 255, 255, 0.95);
            font-size: 1.2rem;
            line-height: 1.8;
            max-width: 800px;
            margin: 0 auto;
        }
        
        /* Info card styling */
        .info-card {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            border-left: 5px solid #0891b2;
            margin-bottom: 1.5rem;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        
        .info-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
        }
        
        .card-title {
            color: #0891b2;
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .card-content {
            color: #334155;
            font-size: 1rem;
            line-height: 1.8;
        }
        
        /* Team member card */
        .team-card {
            background: linear-gradient(135deg, #f0fdfa 0%, #ccfbf1 100%);
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.08);
            transition: transform 0.3s, box-shadow 0.3s;
            height: 100%;
        }
        
        .team-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
        }
        
        .team-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .team-name {
            color: #0f172a;
            font-size: 1.3rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        
        .team-role {
            color: #0891b2;
            font-size: 0.95rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        
        /* Metric card enhancement */
        .metric-container {
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.08);
            text-align: center;
            border-top: 4px solid #0891b2;
            transition: transform 0.3s;
        }
        
        .metric-container:hover {
            transform: scale(1.05);
        }
        
        /* Feature highlight box */
        .feature-box {
            background: linear-gradient(135deg, #ecfeff 0%, #cffafe 100%);
            border-left: 5px solid #06b6d4;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1.5rem 0;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        }
        
        .feature-title {
            color: #0891b2;
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        
        .feature-text {
            color: #334155;
            font-size: 0.95rem;
            line-height: 1.6;
        }
        
        /* Badge styling */
        .badge {
            display: inline-block;
            background: #0891b2;
            color: white;
            padding: 0.4rem 1rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            margin: 0.2rem;
        }
        
        /* Section divider */
        .section-divider {
            height: 3px;
            background: linear-gradient(90deg, transparent, #0891b2, transparent);
            margin: 2rem 0;
            border: none;
        }
        </style>
    """, unsafe_allow_html=True)
    
    df = load_data()

    # =======================
    # TOP LOGO (HEADER BRANDING)
    # =======================
# # =======================
#     # TOP LOGO (HEADER BRANDING)
#     # =======================
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     LOGO_PATH = os.path.join(BASE_DIR, "assets", "Hackathon.jpg")

#     if os.path.exists(LOGO_PATH):
#         st.image(LOGO_PATH, use_container_width=True)

#     st.markdown("<br>", unsafe_allow_html=True)

    # =======================
    # HERO SECTION
    # =======================
    st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title" style="color: black;">UIDAI Hackathon</h1>
            <h2 style="color: white; font-size: 2rem; margin-bottom: 1.5rem;">
                Aadhaar Enrolment Analytics Dashboard
            </h2>
            <p class="hero-subtitle">
                A comprehensive data-driven platform built to analyze pan-India Aadhaar 
                enrolment trends at State → District → Pincode → Date level, enabling 
                data-driven insights for policymakers and administrators.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # =======================
    # HACKATHON DETAILS
    # =======================
    st.markdown("""
        <div class="info-card">
            <h2 class="card-title">🏆 Hackathon Details</h2>
            <div class="card-content">
                <p style="margin-bottom: 1rem;">
                    <strong>Hackathon Name:</strong> UIDAI Hackathon<br>
                    <strong>Theme:</strong> Aadhaar Data Analytics & Governance<br>
                    <strong>Team Size:</strong> 3 Members
                </p>
                <div style="margin-top: 1rem;">
                    <span class="badge">Data Analytics</span>
                    <span class="badge">Governance</span>
                    <span class="badge">Policy Insights</span>
                    <span class="badge">Interactive Dashboard</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Objective section
    st.markdown("""
        <div class="feature-box">
            <div class="feature-title">🎯 Project Objective</div>
            <div class="feature-text">
                Build an interactive analytics platform to explore Aadhaar enrolment 
                patterns across India and enable data-driven insights for policymakers 
                and administrators. The dashboard provides multi-dimensional analysis 
                capabilities including temporal trends, geographic distributions, 
                demographic breakdowns, and performance metrics.
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # =======================
    # TEAM MEMBERS SECTION
    # =======================
    st.markdown("""
        <div class="info-card">
            <h2 class="card-title">👥 Meet Our Team</h2>
        </div>
    """, unsafe_allow_html=True)

    t1, t2, t3 = st.columns(3)

    with t1:
        st.markdown("""
            <div class="team-card">
                <div class="team-icon">👨‍💻</div>
                <div class="team-name">Jatin Agrawal</div>
                <div class="team-role">3rd Year Student (LNMIIT)</div>
                <a href="https://www.linkedin.com/in/jatin-agrawal-b80092367/" 
                   style="color: #0891b2; text-decoration: none; font-weight: 600;">
                    🔗 LinkedIn Profile
                </a>
            </div>
        """, unsafe_allow_html=True)

    with t2:
        st.markdown("""
            <div class="team-card">
                <div class="team-icon">⚙️</div>
                <div class="team-name">Priyansh Gupta</div>
                <div class="team-role">3rd Year Student (LNMIIT)</div>
                <a href="https://www.linkedin.com/in/priyansh123/" 
                   style="color: #0891b2; text-decoration: none; font-weight: 600;">
                    🔗 LinkedIn Profile
                </a>
            </div>
        """, unsafe_allow_html=True)

    with t3:
        st.markdown("""
            <div class="team-card">
                <div class="team-icon">🎨</div>
                <div class="team-name">Naman Agrawal</div>
                <div class="team-role">3rd Year Student (LNMIIT)</div>
                <a href="https://www.linkedin.com/in/naman-agrawal-8671aa27b/" 
                   style="color: #0891b2; text-decoration: none; font-weight: 600;">
                    🔗 LinkedIn Profile
                </a>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # =======================
    # DATA OVERVIEW METRICS
    # =======================
    st.markdown("""
        <div class="info-card">
            <h2 class="card-title">📊 Dataset Overview</h2>
            <p class="card-content">
                Comprehensive analysis of Aadhaar enrolment data across multiple dimensions
            </p>
        </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4, c5 = st.columns(5)

    metrics = [
        ("📋", "Total Records", f"{df.shape[0]:,}"),
        ("🗺️", "States Covered", f"{df['state'].nunique()}"),
        ("🏙️", "Districts", f"{df['district'].nunique()}"),
        ("📍", "Pincodes", f"{df['pincode'].nunique()}"),
        ("📅", "Reported Days", f"{df['date'].nunique()}")
    ]

    for col, (icon, label, value) in zip([c1, c2, c3, c4, c5], metrics):
        with col:
            st.markdown(f"""
                <div class="metric-container">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
                    <div style="color: #64748b; font-size: 0.85rem; margin-bottom: 0.5rem;">{label}</div>
                    <div style="color: #0f172a; font-size: 1.8rem; font-weight: 700;">{value}</div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =======================
    # FEATURES HIGHLIGHT
    # =======================
    st.markdown("""
        <div class="feature-box">
            <div class="feature-title">✨ Key Features of This Dashboard</div>
            <div class="feature-text">
                <strong>📍 Navigation Guide:</strong> Use the sidebar to explore various analytical views:
                <ul style="margin-top: 0.5rem; padding-left: 1.5rem;">
                    <li><strong>Nationwide Analysis:</strong> Pan-India trends and geographic distributions</li>
                    <li><strong>State-wise Insights:</strong> Detailed state-level performance metrics</li>
                    <li><strong>District Analysis:</strong> Granular district-level breakdowns</li>
                    <li><strong>Pincode Explorer:</strong> Hyperlocal enrolment patterns</li>
                    <li><strong>Demographics:</strong> Age and gender composition analysis</li>
                    <li><strong>Temporal Trends:</strong> Time-series analysis and seasonality patterns</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <div style="text-align: center; margin-top: 3rem; padding: 2rem; 
                    background: linear-gradient(135deg, #f0fdfa 0%, #ccfbf1 100%); 
                    border-radius: 15px;">
            <p style="color: #0891b2; font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem;">
                🚀 Ready to Explore?
            </p>
            <p style="color: #64748b; font-size: 0.95rem;">
                Select a page from the sidebar to begin your analysis journey
            </p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    page()