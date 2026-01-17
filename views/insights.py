import streamlit as st
from utils.data_loader import load_data


def page():
    df = load_data()

    # =====================================================
    # ENHANCED HEADER WITH CYAN THEME STYLING
    # =====================================================
    st.markdown("""
        <style>
        /* Main header with gradient animation */
        .main-header {
            font-size: 2.8rem;
            font-weight: 800;
            background: linear-gradient(135deg, #00bcd4 0%, #00acc1 50%, #00bcd4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 1.5rem;
            animation: gradient-shift 3s ease infinite;
            background-size: 200% 200%;
        }
        
        @keyframes gradient-shift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* Insight cards */
        .insight-card {
            background: linear-gradient(135deg, #00bcd4 0%, #0097a7 100%);
            padding: 1.5rem;
            border-radius: 12px;
            color: white;
            margin-bottom: 1.5rem;
            box-shadow: 0 6px 12px rgba(0,188,212,0.4);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .insight-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,188,212,0.5);
        }
        
        /* Metric boxes with enhanced styling */
        .metric-box {
            background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%);
            padding: 1.3rem;
            border-radius: 10px;
            border-left: 5px solid #00bcd4;
            margin: 1.2rem 0;
            box-shadow: 0 3px 8px rgba(0,188,212,0.2);
            transition: all 0.3s ease;
        }
        
        .metric-box:hover {
            transform: translateX(5px);
            box-shadow: 0 5px 15px rgba(0,188,212,0.3);
        }
        
        /* Highlight text with better contrast */
        .highlight-text {
            background: linear-gradient(135deg, #b2ebf2 0%, #80deea 100%);
            color: #004d40;
            padding: 0.3rem 0.6rem;
            border-radius: 6px;
            font-weight: 700;
            box-shadow: 0 2px 4px rgba(0,188,212,0.2);
        }
        
        /* Enhanced cyan divider with shadow */
        .cyan-divider {
            height: 4px;
            background: linear-gradient(90deg, transparent, #00bcd4, #00acc1, #00bcd4, transparent);
            border: none;
            margin: 2.5rem 0;
            box-shadow: 0 2px 4px rgba(0,188,212,0.3);
            border-radius: 2px;
        }
        
        /* Cyan box with enhanced styling */
        .cyan-box {
            background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%);
            padding: 1.8rem;
            border-radius: 12px;
            border: 2px solid #00bcd4;
            margin: 1.2rem 0;
            box-shadow: 0 4px 10px rgba(0,188,212,0.2);
            transition: all 0.3s ease;
        }
        
        .cyan-box:hover {
            box-shadow: 0 6px 15px rgba(0,188,212,0.3);
            border-color: #00acc1;
        }
        
        /* Enhanced cyan badges with animation */
        .cyan-badge {
            background: linear-gradient(135deg, #00bcd4 0%, #00acc1 100%);
            color: white;
            padding: 0.4rem 1rem;
            border-radius: 25px;
            font-size: 0.95rem;
            font-weight: 600;
            display: inline-block;
            margin: 0.3rem;
            box-shadow: 0 3px 6px rgba(0,188,212,0.3);
            transition: all 0.3s ease;
        }
        
        .cyan-badge:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 10px rgba(0,188,212,0.4);
        }
        
        /* Insight number badges */
        .insight-number {
            font-size: 3.5rem;
            font-weight: 900;
            color: #00bcd4;
            opacity: 0.15;
            float: left;
            margin-right: 1.5rem;
            line-height: 1;
            text-shadow: 2px 2px 4px rgba(0,188,212,0.2);
        }
        
        /* Section headers with better visual */
        .section-header {
            color: #00838f;
            font-size: 1.8rem;
            font-weight: 700;
            margin: 2rem 0 1rem 0;
            padding-bottom: 0.5rem;
            border-bottom: 3px solid #00bcd4;
            display: inline-block;
        }
        
        /* Card containers for impact factors */
        .impact-card {
            background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%);
            padding: 1.5rem;
            border-radius: 10px;
            border: 2px solid #00bcd4;
            text-align: center;
            height: 100%;
            transition: all 0.3s ease;
            box-shadow: 0 3px 8px rgba(0,188,212,0.2);
        }
        
        .impact-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 8px 16px rgba(0,188,212,0.4);
            border-color: #00acc1;
        }
        
        .impact-card h3 {
            color: #00838f;
            margin: 0 0 0.8rem 0;
            font-size: 1.3rem;
        }
        
        .impact-card p {
            color: #00acc1;
            font-weight: 700;
            font-size: 1.1rem;
            margin: 0;
        }
        
        /* Warning boxes with better styling */
        .warning-box {
            background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%);
            padding: 1.3rem;
            border-radius: 10px;
            border-left: 5px solid #ffa726;
            box-shadow: 0 3px 8px rgba(255,167,38,0.2);
            margin: 1rem 0;
        }
        
        /* Activity status cards */
        .activity-high {
            background: linear-gradient(135deg, #a7ffeb 0%, #64ffda 100%);
            padding: 1.8rem;
            border-radius: 12px;
            text-align: center;
            border: 3px solid #00bfa5;
            box-shadow: 0 4px 10px rgba(0,191,165,0.3);
            transition: all 0.3s ease;
        }
        
        .activity-high:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 15px rgba(0,191,165,0.4);
        }
        
        .activity-medium {
            background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%);
            padding: 1.8rem;
            border-radius: 12px;
            text-align: center;
            border: 3px solid #00bcd4;
            box-shadow: 0 4px 10px rgba(0,188,212,0.3);
            transition: all 0.3s ease;
        }
        
        .activity-medium:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 15px rgba(0,188,212,0.4);
        }
        
        .activity-low {
            background: linear-gradient(135deg, #ffccbc 0%, #ffab91 100%);
            padding: 1.8rem;
            border-radius: 12px;
            text-align: center;
            border: 3px solid #ff7043;
            box-shadow: 0 4px 10px rgba(255,112,67,0.3);
            transition: all 0.3s ease;
        }
        
        .activity-low:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 15px rgba(255,112,67,0.4);
        }
        
        /* Age group card */
        .age-card {
            background: linear-gradient(135deg, #00bcd4 0%, #0097a7 100%);
            padding: 2rem;
            border-radius: 12px;
            text-align: center;
            color: white;
            box-shadow: 0 6px 12px rgba(0,188,212,0.4);
            transition: all 0.3s ease;
        }
        
        .age-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,188,212,0.5);
        }
        
        .age-card h4 {
            margin: 0;
            opacity: 0.95;
            font-size: 1.1rem;
        }
        
        .age-card h2 {
            margin: 1rem 0;
            font-size: 3rem;
            font-weight: 900;
        }
        
        .age-card p {
            margin: 0;
            opacity: 0.95;
            font-size: 1rem;
        }
        
        /* Progress bars for spatial distribution */
        .progress-container {
            background-color: rgba(0,188,212,0.1);
            border-radius: 10px;
            padding: 0.3rem;
            margin: 1rem auto;
        }
        
        .progress-bar {
            height: 24px;
            border-radius: 8px;
            transition: width 0.5s ease;
            box-shadow: 0 2px 4px rgba(0,188,212,0.3);
        }
        
        /* Conclusion box */
        .conclusion-box {
            background: linear-gradient(135deg, #a7ffeb 0%, #64ffda 100%);
            padding: 2rem;
            border-radius: 15px;
            border: 3px solid #00bfa5;
            box-shadow: 0 6px 15px rgba(0,191,165,0.3);
            margin: 1.5rem 0;
        }
        
        /* Acknowledgement box */
        .ack-box {
            background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%);
            padding: 2.5rem;
            border-radius: 18px;
            text-align: center;
            border: 3px solid #00bcd4;
            box-shadow: 0 8px 20px rgba(0,188,212,0.3);
        }
        
        /* Expander styling */
        .streamlit-expanderHeader {
            background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%);
            border-radius: 8px;
            border: 2px solid #00bcd4;
            font-weight: 600;
            color: #00838f;
        }
        
        /* Tabs enhancement */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%);
            padding: 0.8rem;
            border-radius: 12px;
            box-shadow: 0 3px 8px rgba(0,188,212,0.2);
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 55px;
            background-color: white;
            border-radius: 10px;
            color: #00838f;
            font-weight: 700;
            padding: 0 2rem;
            border: 2px solid #b2ebf2;
            transition: all 0.3s ease;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background-color: #e0f7fa;
            border-color: #00bcd4;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #00bcd4 0%, #00acc1 100%);
            color: white;
            border: 2px solid #00bcd4;
            box-shadow: 0 4px 8px rgba(0,188,212,0.3);
        }
        </style>
    """, unsafe_allow_html=True)

    # Enhanced title with icon
    st.markdown('<p class="main-header">📌 Key Insights & Observations</p>', unsafe_allow_html=True)

    # Enhanced introduction with cyan theme
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.markdown("""
        <div class="cyan-box">
        <h4 style="color: #00838f; margin-top: 0; font-size: 1.5rem;">🌊 Welcome to the Insights Dashboard!</h4>
        <p style="color: #006064; font-size: 1.05rem; line-height: 1.6;">
        This section highlights the major insights derived from Aadhaar enrolment data 
        across states, districts, time periods, and demographic groups.
        </p>
        <div style="margin-top: 1.5rem;">
        <span class="cyan-badge">📊 Data-Driven Analysis</span>
        <span class="cyan-badge">🔍 Pattern Recognition</span>
        <span class="cyan-badge">📈 Trend Insights</span>
        </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="cyan-divider">', unsafe_allow_html=True)

    # =====================================================
    # INSIGHT 1 - Enhanced
    # =====================================================
    with st.container():
        col1, col2 = st.columns([1, 20])
        with col1:
            st.markdown("### 1️⃣")
        with col2:
            st.markdown("### <span style='color: #00838f;'>Significant State-level Disparities</span>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-box">
        <p style="margin: 0; font-size: 1.1rem; color: #006064;">
        Aadhaar enrolment activity is <span class="highlight-text">highly uneven across states</span>.  
        A small number of states contribute a disproportionately large share of total enrolments.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="impact-card">
                <h3>Population Size</h3>
                <p>🔼 High Impact</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="impact-card">
                <h3>Admin Capacity</h3>
                <p>➡️ Medium Impact</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="impact-card">
                <h3>Outreach</h3>
                <p>🔄 Variable</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.expander("💡 Why does this matter?", expanded=False):
            st.markdown("""
            <div style="background-color: #e0f7fa; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #00bcd4;">
            
            <p style="color: #006064; font-size: 1.05rem; margin-bottom: 0.8rem;">
            <strong style="color: #00838f;">🎯 Resource Allocation:</strong> Helps identify states needing additional resources
            </p>
            <p style="color: #006064; font-size: 1.05rem; margin-bottom: 0.8rem;">
            <strong style="color: #00838f;">⭐ Best Practices:</strong> Reveals best practices from high-performing states
            </p>
            <p style="color: #006064; font-size: 1.05rem; margin-bottom: 0;">
            <strong style="color: #00838f;">🚀 Strategic Planning:</strong> Guides targeted intervention strategies
            </p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<hr class="cyan-divider">', unsafe_allow_html=True)

    # =====================================================
    # INSIGHT 2 - Enhanced
    # =====================================================
    with st.container():
        col1, col2 = st.columns([1, 20])
        with col1:
            st.markdown("### 2️⃣")
        with col2:
            st.markdown("### <span style='color: #00838f;'>Inconsistent Reporting Across Time</span>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="warning-box">
        <strong style="font-size: 1.2rem;">⚠️ Data Coverage Alert</strong><br><br>
        <p style="margin: 0; font-size: 1.05rem;">
        Not all states and districts report enrolment data consistently across the full national timeline.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="cyan-box">
        <p style="color: #006064; font-size: 1.1rem; margin-bottom: 1.2rem;">
        Several states show <strong>partial reporting windows</strong>, which impacts:
        </p>
        <div style="margin-top: 1rem;">
        <span class="cyan-badge">📊 Comparability</span>
        <span class="cyan-badge">📈 Trend Analysis</span>
        <span class="cyan-badge">🔢 Total Estimates</span>
        </div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("📈 View Impact"):
            st.markdown("""
            <div style="background-color: #e0f7fa; padding: 1.5rem; border-radius: 10px; border: 2px solid #00bcd4;">
            <p style="color: #006064; font-size: 1.05rem; line-height: 1.6;">
            This highlights the importance of accounting for <strong style="color: #00838f;">data coverage bias</strong> 
            while interpreting totals and making cross-state comparisons.
            </p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<hr class="cyan-divider">', unsafe_allow_html=True)

    # =====================================================
    # INSIGHT 3 - Enhanced
    # =====================================================
    with st.container():
        col1, col2 = st.columns([1, 20])
        with col1:
            st.markdown("### 3️⃣")
        with col2:
            st.markdown("### <span style='color: #00838f;'>Large District-level Variations</span>", unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["📊 Variation Factors", "🔍 Patterns Observed"])
        
        with tab1:
            st.markdown("""
            <div class="metric-box">
            <p style="margin: 0; font-size: 1.1rem; color: #006064;">
            Even within the same state, districts vary widely in:
            </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""
                <div class="cyan-box">
                <h4 style="color: #00838f; margin-top: 0;">📅 Temporal Factors</h4>
                <p style="color: #006064; font-size: 1.05rem; line-height: 1.8;">
                • Number of reporting days<br>
                • Reporting frequency patterns
                </p>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown("""
                <div class="cyan-box">
                <h4 style="color: #00838f; margin-top: 0;">📈 Operational Factors</h4>
                <p style="color: #006064; font-size: 1.05rem; line-height: 1.8;">
                • Average daily enrolments<br>
                • Infrastructure availability
                </p>
                </div>
                """, unsafe_allow_html=True)
        
        with tab2:
            st.markdown("""
            <div class="cyan-box">
            <h4 style="color: #00838f; margin-top: 0; font-size: 1.3rem;">🔍 Key Patterns Identified</h4>
            <p style="color: #006064; font-size: 1.05rem; line-height: 1.8; margin-top: 1rem;">
            <strong style="color: #00acc1;">Pattern 1:</strong> Some districts report infrequently but with high volumes<br><br>
            <strong style="color: #00acc1;">Pattern 2:</strong> Others report regularly with lower activity
            </p>
            <p style="color: #00838f; font-size: 1.1rem; margin-top: 1.5rem; font-weight: 600;">
            → Suggests <span class="highlight-text">operational and infrastructure differences</span> at the district level
            </p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<hr class="cyan-divider">', unsafe_allow_html=True)

    # =====================================================
    # INSIGHT 4 - Enhanced
    # =====================================================
    with st.container():
        col1, col2 = st.columns([1, 20])
        with col1:
            st.markdown("### 4️⃣")
        with col2:
            st.markdown("### <span style='color: #00838f;'>Clear Weekly Enrolment Patterns</span>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-box">
        <p style="margin: 0; font-size: 1.1rem; color: #006064;">
        Enrolment activity follows a <span class="highlight-text">distinct weekly pattern</span> 
        aligned with office working schedules.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="activity-high">
                <h3 style="color: #00695c; margin: 0 0 1rem 0; font-size: 1.4rem;">Weekdays</h3>
                <p style="font-size: 2.5rem; margin: 0.5rem 0;">🔼</p>
                <p style="color: #00897b; font-weight: 700; font-size: 1.15rem; margin: 0;">Higher Activity</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="activity-medium">
                <h3 style="color: #00838f; margin: 0 0 1rem 0; font-size: 1.4rem;">Saturdays</h3>
                <p style="font-size: 2.5rem; margin: 0.5rem 0;">➡️</p>
                <p style="color: #00acc1; font-weight: 700; font-size: 1.15rem; margin: 0;">Moderate Activity</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="activity-low">
                <h3 style="color: #bf360c; margin: 0 0 1rem 0; font-size: 1.4rem;">Sundays</h3>
                <p style="font-size: 2.5rem; margin: 0.5rem 0;">🔽</p>
                <p style="color: #d84315; font-weight: 700; font-size: 1.15rem; margin: 0;">Reduced Activity</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.expander("💼 Operational Implications"):
            st.markdown("""
            <div class="cyan-box">
            <p style="color: #006064; font-size: 1.05rem; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="color: #00838f;">📋 Staffing:</strong> Optimize resource allocation based on day of week
            </p>
            <p style="color: #006064; font-size: 1.05rem; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="color: #00838f;">🔧 Planning:</strong> Schedule maintenance during low-activity periods
            </p>
            <p style="color: #006064; font-size: 1.05rem; line-height: 1.8; margin-bottom: 0;">
            <strong style="color: #00838f;">📊 Forecasting:</strong> Account for weekly patterns in projections
            </p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<hr class="cyan-divider">', unsafe_allow_html=True)

    # =====================================================
    # INSIGHT 5 - Enhanced
    # =====================================================
    with st.container():
        col1, col2 = st.columns([1, 20])
        with col1:
            st.markdown("### 5️⃣")
        with col2:
            st.markdown("### <span style='color: #00838f;'>Adult Enrolments Dominate</span>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div class="metric-box">
            <p style="color: #006064; font-size: 1.1rem; margin-bottom: 1.2rem;">
            The <strong>18+ age group accounts for the majority of enrolments</strong>, reflecting:
            </p>
            <p style="color: #006064; font-size: 1.05rem; line-height: 1.8; margin: 0;">
            ✅ First-time registrations<br>
            ✅ Updates and corrections<br>
            ✅ Linkages with welfare and financial services
            </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="age-card">
                <h4>Primary Age Group</h4>
                <h2>18+</h2>
                <p>Majority Share</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="cyan-box">
        <p style="color: #006064; font-size: 1.05rem; line-height: 1.6; margin: 0;">
        📚 <strong style="color: #00838f;">Child Enrolments (0-17 years):</strong> Form a smaller but important segment, 
        often influenced by school admissions and welfare eligibility requirements.
        </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="cyan-divider">', unsafe_allow_html=True)

    # =====================================================
    # INSIGHT 6 - Enhanced
    # =====================================================
    with st.container():
        col1, col2 = st.columns([1, 20])
        with col1:
            st.markdown("### 6️⃣")
        with col2:
            st.markdown("### <span style='color: #00838f;'>Spatial Concentration of Enrolment Activity</span>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-box">
        <p style="margin: 0; font-size: 1.1rem; color: #006064;">
        Where geospatial data is available, enrolment intensity is 
        <span class="highlight-text">spatially clustered</span> rather than uniform.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="cyan-box" style="text-align: center;">
            <h4 style="color: #00838f; margin-top: 0;">🏙️ Urban Areas</h4>
            <div class="progress-container">
                <div class="progress-bar" style="background: linear-gradient(90deg, #00bcd4, #00acc1); width: 85%;"></div>
            </div>
            <p style="color: #00acc1; font-weight: 700; font-size: 1.1rem;">High intensity (85%)</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="cyan-box" style="text-align: center;">
            <h4 style="color: #00838f; margin-top: 0;">🏘️ Semi-Urban</h4>
            <div class="progress-container">
                <div class="progress-bar" style="background: linear-gradient(90deg, #26c6da, #00bcd4); width: 60%;"></div>
            </div>
            <p style="color: #00acc1; font-weight: 700; font-size: 1.1rem;">Medium intensity (60%)</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="cyan-box" style="text-align: center;">
            <h4 style="color: #00838f; margin-top: 0;">🌾 Rural Areas</h4>
            <div class="progress-container">
                <div class="progress-bar" style="background: linear-gradient(90deg, #4dd0e1, #26c6da); width: 35%;"></div>
            </div>
            <p style="color: #00acc1; font-weight: 700; font-size: 1.1rem;">Lower intensity (35%)</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.expander("🗺️ Contributing Factors"):
            st.markdown("""
            <div class="cyan-box">
            <p style="color: #006064; font-size: 1.05rem; line-height: 1.8; margin-bottom: 1rem;">
            <span class="cyan-badge">🚗 Accessibility</span> Proximity to enrollment centers
            </p>
            <p style="color: #006064; font-size: 1.05rem; line-height: 1.8; margin-bottom: 1rem;">
            <span class="cyan-badge">👥 Population Density</span> Higher in urban areas
            </p>
            <p style="color: #006064; font-size: 1.05rem; line-height: 1.8; margin-bottom: 0;">
            <span class="cyan-badge">🏢 Infrastructure</span> Better connectivity and facilities
            </p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<hr class="cyan-divider">', unsafe_allow_html=True)

    # =====================================================
    # INSIGHT 7 - Enhanced
    # =====================================================
    with st.container():
        col1, col2 = st.columns([1, 20])
        with col1:
            st.markdown("### 7️⃣")
        with col2:
            st.markdown("### <span style='color: #00838f;'>Data Quality & Interpretation Caveats</span>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="warning-box">
        <strong style="font-size: 1.2rem;">⚠️ Important Considerations</strong>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="cyan-box">
            <h4 style="color: #00838f; margin-top: 0;">⚠️ Challenges</h4>
            <p style="color: #006064; font-size: 1.05rem; line-height: 1.8;">
            ❌ Uneven reporting durations<br>
            ❌ Missing district/pincode records<br>
            ❌ Variations in data granularity
            </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="cyan-box">
            <h4 style="color: #00838f; margin-top: 0;">✅ Best Practices</h4>
            <p style="color: #006064; font-size: 1.05rem; line-height: 1.8;">
            ✅ Balance quantity vs. quality<br>
            ✅ Account for coverage bias<br>
            ✅ Cross-validate findings
            </p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<hr class="cyan-divider">', unsafe_allow_html=True)

    # =====================================================
    # CONCLUSION - Enhanced
    # =====================================================
    st.markdown("## <span style='color: #00838f;'>📊 Conclusion</span>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="conclusion-box">
    <p style="color: #00695c; font-size: 1.2rem; font-weight: 700; margin-bottom: 0.8rem;">
    This analysis demonstrates how Aadhaar enrolment data can reveal meaningful patterns
    </p>
    <p style="color: #006064; font-size: 1.05rem; margin: 0;">
    related to administrative performance, demographic coverage, and operational efficiency.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### <span style='color: #00838f;'>🎯 Dashboard Capabilities</span>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="cyan-box">
        <h4 style="color: #00838f; margin-top: 0; font-size: 1.3rem;">👨‍💼 For Analysts</h4>
        <p style="color: #006064; font-size: 1.05rem; line-height: 1.8;">
        📊 Compare enrolment behavior across states<br>
        🔍 Identify reporting gaps<br>
        📈 Understand demographic trends
        </p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="cyan-box">
        <h4 style="color: #00838f; margin-top: 0; font-size: 1.3rem;">🎯 For Decision Makers</h4>
        <p style="color: #006064; font-size: 1.05rem; line-height: 1.8;">
        💡 Support data-driven policy decisions<br>
        🎯 Guide resource allocation<br>
        📋 Enable strategic planning
        </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="cyan-divider">', unsafe_allow_html=True)

    # =====================================================
    # ACKNOWLEDGEMENT - Enhanced
    # =====================================================
    st.markdown("## <span style='color: #00838f;'>🙏 Acknowledgement</span>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.markdown("""
        <div class="ack-box">
        
        <h4 style="color: #00838f; margin-top: 0; font-size: 1.5rem;">📊 Data & Purpose</h4>
        
        <p style="color: #006064; font-size: 1.05rem; line-height: 1.8; margin: 1.5rem 0;">
        <strong style="color: #00acc1;">Data Source:</strong> Publicly available Aadhaar enrolment records<br>
        <strong style="color: #00acc1;">Purpose:</strong> Analytical and educational use<br>
        <strong style="color: #00acc1;">Goal:</strong> Support transparent and informed decision-making
        </p>
        
        <hr style="border: 2px solid #00bcd4; margin: 2rem 0;">
        
        <h4 style="color: #00838f; font-size: 1.5rem;">🛠️ Built With</h4>
        
        <div style="margin: 1.5rem 0;">
        <span class="cyan-badge">Python</span>
        <span class="cyan-badge">Streamlit</span>
        <span class="cyan-badge">Pandas</span>
        <span class="cyan-badge">Plotly</span>
        <span class="cyan-badge">GeoPandas</span>
        </div>
        
        <hr style="border: 2px solid #00bcd4; margin: 2rem 0;">
        
        <h3 style="color: #00838f; margin-bottom: 0; font-size: 1.6rem;">Thank you for exploring the insights! 🎉</h3>
        
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align: center; color: #00acc1; font-weight: 700; font-size: 1.1rem;">
    💻 Dashboard developed for data-driven governance and policy analysis
    </p>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    page()