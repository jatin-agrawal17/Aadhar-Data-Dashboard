import streamlit as st
from utils.data_loader import load_data


def page():
    df = load_data()

    # =====================================================
    # ENHANCED HEADER WITH MODERN CYAN THEME STYLING
    # =====================================================
    st.markdown("""
    <style>
    /* Import modern font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    /* Global typography improvements */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Main header with gradient and animation */
    .main-header {
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #00bcd4, #0097a7, #00acc1);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        animation: gradientShift 4s ease infinite;
        letter-spacing: -0.5px;
    }
    
    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* Subheader styling */
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #00838f;
        margin-top: 2.5rem;
        margin-bottom: 1rem;
        padding-left: 0.5rem;
        border-left: 4px solid #00bcd4;
    }
    
    /* Enhanced metric box with hover effect */
    .metric-box {
        background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%);
        padding: 1.8rem;
        border-radius: 16px;
        border-left: 6px solid #00bcd4;
        margin: 1.5rem 0;
        box-shadow: 0 4px 6px rgba(0, 188, 212, 0.1);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .metric-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(255,255,255,0.3) 0%, transparent 100%);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .metric-box:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(0, 188, 212, 0.2);
    }
    
    .metric-box:hover::before {
        opacity: 1;
    }
    
    /* Enhanced cyan box with glass morphism effect */
    .cyan-box {
        background: linear-gradient(135deg, rgba(224, 247, 250, 0.95) 0%, rgba(178, 235, 242, 0.95) 100%);
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 16px;
        border: 2px solid #00bcd4;
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(0, 188, 212, 0.15);
        transition: all 0.3s ease;
    }
    
    .cyan-box:hover {
        box-shadow: 0 12px 40px rgba(0, 188, 212, 0.25);
        transform: translateY(-3px);
    }
    
    /* Enhanced warning box */
    .warning-box {
        background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%);
        padding: 1.8rem;
        border-radius: 16px;
        border-left: 6px solid #ffa726;
        margin: 1.5rem 0;
        box-shadow: 0 4px 6px rgba(255, 167, 38, 0.1);
        transition: all 0.3s ease;
    }
    
    .warning-box:hover {
        box-shadow: 0 8px 16px rgba(255, 167, 38, 0.2);
        transform: translateY(-2px);
    }
    
    /* Enhanced highlight text with pill design */
    .highlight-text {
        background: linear-gradient(135deg, #80deea, #4dd0e1);
        padding: 0.4rem 0.8rem;
        border-radius: 20px;
        font-weight: 700;
        color: #004d40;
        display: inline-block;
        box-shadow: 0 2px 4px rgba(0, 188, 212, 0.2);
        transition: all 0.2s ease;
    }
    
    .highlight-text:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0, 188, 212, 0.3);
    }
    
    /* Animated gradient divider */
    .cyan-divider {
        height: 4px;
        background: linear-gradient(90deg, transparent, #00bcd4, #0097a7, #00bcd4, transparent);
        background-size: 200% 100%;
        border: none;
        margin: 3rem 0;
        border-radius: 2px;
        animation: dividerFlow 3s ease infinite;
    }
    
    @keyframes dividerFlow {
        0%, 100% { background-position: 0% 0%; }
        50% { background-position: 100% 0%; }
    }
    
    /* Icon badge styling */
    .icon-badge {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        background: linear-gradient(135deg, #00bcd4, #0097a7);
        border-radius: 12px;
        font-size: 1.5rem;
        margin-right: 0.8rem;
        box-shadow: 0 4px 8px rgba(0, 188, 212, 0.3);
        transition: all 0.3s ease;
    }
    
    .icon-badge:hover {
        transform: rotate(5deg) scale(1.1);
    }
    
    /* Stats card */
    .stats-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 2px solid #e0f7fa;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    
    .stats-card:hover {
        border-color: #00bcd4;
        box-shadow: 0 8px 16px rgba(0, 188, 212, 0.15);
        transform: translateY(-4px);
    }
    
    .stats-number {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #00bcd4, #0097a7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0.5rem 0;
    }
    
    .stats-label {
        font-size: 0.9rem;
        color: #546e7a;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Conclusion box with special styling */
    .conclusion-box {
        background: linear-gradient(135deg, #006064 0%, #00838f 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 12px 40px rgba(0, 96, 100, 0.3);
        border: 3px solid #00bcd4;
    }
    
    .conclusion-box strong {
        color: #80deea;
    }
    
    /* Acknowledgement section */
    .ack-box {
        background: linear-gradient(135deg, #f5f5f5 0%, #e8f5e9 100%);
        padding: 2.5rem;
        border-radius: 20px;
        text-align: center;
        border: 2px solid #00bcd4;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
    }
    
    /* Streamlit expander customization */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #e0f7fa, #b2ebf2);
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        color: #00695c;
        border-left: 3px solid #00bcd4;
    }
    
    /* Pulse animation for key stats */
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    
    .pulse-stat {
        animation: pulse 2s ease infinite;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2.2rem;
        }
        .stats-number {
            font-size: 2rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # =====================================================
    # HEADER WITH ANIMATED BADGE
    # =====================================================
    st.markdown('''
    <div style="text-align: center; margin-bottom: 2rem;">
        <p class="main-header">📌 Key Insights & Observations</p>
        <p style="color: #546e7a; font-size: 1.1rem; font-weight: 500;">
            Data-Driven Analysis of Aadhaar Enrolment Patterns
        </p>
    </div>
    ''', unsafe_allow_html=True)

    # =====================================================
    # KEY STATISTICS OVERVIEW (NEW)
    # =====================================================
    st.markdown("### 📊 At a Glance")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stats-card">
            <div class="stats-label">States/UTs</div>
            <div class="stats-number pulse-stat">54→36</div>
            <div style="color: #00838f; font-weight: 600;">Normalized</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stats-card">
            <div class="stats-label">Districts</div>
            <div class="stats-number pulse-stat">984→772</div>
            <div style="color: #00838f; font-weight: 600;">Cleaned</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stats-card">
            <div class="stats-label">Age 0-5</div>
            <div class="stats-number pulse-stat">~65%</div>
            <div style="color: #00838f; font-weight: 600;">Of Enrolments</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stats-card">
            <div class="stats-label">Adult (18+)</div>
            <div class="stats-number pulse-stat">~3%</div>
            <div style="color: #00838f; font-weight: 600;">Only</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="cyan-divider">', unsafe_allow_html=True)

    # =====================================================
    # INSIGHT 1
    # =====================================================
    st.markdown('<p class="section-header">1️⃣ Geographic Identifier Inflation in Raw Data</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="metric-box">
    The raw Aadhaar enrolment dataset exhibited <strong>artificial inflation of geographic identifiers</strong>,
    containing <span class="highlight-text">54 state/UT labels, 984 district labels, and 19,462 pincodes</span>,
    far exceeding official administrative counts.
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🔍 Why this mattered", expanded=False):
        st.markdown("""
        - 🎯 **Root Cause**: Spelling variants, legacy names, formatting noise, and numeric word-order differences  
        - 📉 **Impact**: Aggregation and spatial analysis were severely distorted without correction  
        - ✅ **Solution**: Rule-based normalization reduced districts to **772 valid entities**
        - 🛠️ **Methodology**: Fuzzy matching, canonical name mapping, and administrative hierarchy validation
        """)

    st.markdown('<hr class="cyan-divider">', unsafe_allow_html=True)

    # =====================================================
    # INSIGHT 2
    # =====================================================
    st.markdown('<p class="section-header">2️⃣ Legacy Names & Administrative Renaming</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="cyan-box">
    Several states and districts appeared simultaneously under historical and current official names
    (e.g., <strong>Orissa → Odisha</strong>, <strong>Pondicherry → Puducherry</strong>,
    <strong>Dadra & Nagar Haveli + Daman & Diu</strong>).
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📊 Impact on analysis", expanded=False):
        st.markdown("""
        - ⚠️ **Problem**: Parallel labels artificially split enrolment counts  
        - 🔧 **Consolidation**: Enabled policy-aligned state and district comparisons  
        - ✨ **Precision**: Cleaning was selective and did not collapse valid districts
        - 📈 **Result**: More accurate trend analysis and geographic insights
        """)

    st.markdown('<hr class="cyan-divider">', unsafe_allow_html=True)

    # =====================================================
    # INSIGHT 3
    # =====================================================
    st.markdown('<p class="section-header">3️⃣ Uneven Reporting Coverage Across Time</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="warning-box">
    ⚡ National enrolment totals are highly sensitive to <strong>which districts report on a given day</strong>.
    Sharp fluctuations frequently coincide with changes in reporting coverage rather than true demand.
    </div>
    """, unsafe_allow_html=True)

    with st.expander("💡 Analytical implication", expanded=False):
        st.markdown("""
        - 🚫 **Issue**: Raw daily totals are misleading  
        - ✅ **Solution**: Coverage-aware metrics (average per reported day) are required  
        - 🔗 **Best Practice**: Enrolment trends must be interpreted jointly with reporting coverage
        - 📊 **Insight**: Normalized metrics reveal true operational intensity
        """)

    st.markdown('<hr class="cyan-divider">', unsafe_allow_html=True)

    # =====================================================
    # INSIGHT 4
    # =====================================================
    st.markdown('<p class="section-header">4️⃣ Month-Start Batch Upload Artifacts</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="metric-box">
    Aadhaar enrolments show extreme concentration on the <span class="highlight-text">1st day of the month</span>,
    with the largest spike on <strong>1st July</strong>.
    This reflects <strong>centralized batch uploads</strong>, not operational surges.
    </div>
    """, unsafe_allow_html=True)

    with st.expander("⏰ Why this matters", expanded=False):
        st.markdown("""
        - 📅 **Pattern**: Day-of-week and day-of-month peaks are administrative artifacts  
        - 🚫 **Caution**: Early-period spikes should not be interpreted as behavioural signals  
        - 📈 **Evolution**: Later months show transition to routine daily reporting
        - 🎯 **Takeaway**: Temporal analysis requires artifact-aware filtering
        """)

    st.markdown('<hr class="cyan-divider">', unsafe_allow_html=True)

    # =====================================================
    # INSIGHT 5 (ENHANCED AGE INSIGHT)
    # =====================================================
    st.markdown('<p class="section-header">5️⃣ Aadhaar Enrolment Is Child-Driven</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="cyan-box">
    👶 National Aadhaar enrolments are <strong>heavily concentrated in the 0–5 age group (≈65%)</strong>,
    followed by 5–17 years.
    Adult (18+) enrolments contribute <span class="highlight-text">only ~3%</span>,
    indicating a mature adult Aadhaar base.
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🎯 Policy interpretation", expanded=False):
        st.markdown("""
        - 👶 **Primary Function**: Aadhaar functions primarily as an early-life identity system  
        - 📊 **Demand Driver**: Current enrolment demand is driven by births and child inclusion  
        - 👨‍👩‍👧‍👦 **Adult Patterns**: Adult enrolments are residual or corrective in nature
        - 🏛️ **Policy Implication**: Resources should prioritize child enrolment infrastructure
        """)

    st.markdown('<hr class="cyan-divider">', unsafe_allow_html=True)

    # =====================================================
    # INSIGHT 6
    # =====================================================
    st.markdown('<p class="section-header">6️⃣ Coverage-Aware Inter-State Differences</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="metric-box">
    After adjusting for reporting coverage, <strong>Uttar Pradesh</strong> emerges as a clear outlier,
    followed by Bihar and Madhya Pradesh, reflecting sustained enrolment throughput
    rather than reporting frequency.
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🗺️ Key takeaway", expanded=False):
        st.markdown("""
        - 📍 **Persistence**: Differences persist after controlling for missing days  
        - 🌏 **Regional Pattern**: Northern and central states show structurally higher enrolment intensity  
        - 🎯 **Saturation**: Southern and northeastern states reflect enrolment saturation
        - 📈 **Policy Focus**: High-intensity states may need additional infrastructure support
        """)

    st.markdown('<hr class="cyan-divider">', unsafe_allow_html=True)

    # =====================================================
    # INSIGHT 7
    # =====================================================
    st.markdown('<p class="section-header">7️⃣ District-Level Metrics Require Coverage Thresholds</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="warning-box">
    ⚠️ Districts with low reporting days consistently show near-zero averages,
    indicating <strong>coverage artifacts rather than low enrolment demand</strong>.
    </div>
    """, unsafe_allow_html=True)

    with st.expander("✅ Best practice applied", expanded=False):
        st.markdown("""
        - 🎯 **Filtering**: District analysis restricted to minimum reporting thresholds  
        - 📊 **Quality**: High-coverage districts show stable and interpretable averages  
        - 🚫 **Prevention**: Prevents misleading low-activity classifications
        - 📈 **Standard**: Recommended minimum: 30+ reporting days for district-level analysis
        """)

    st.markdown('<hr class="cyan-divider">', unsafe_allow_html=True)

    # =====================================================
    # ENHANCED CONCLUSION
    # =====================================================
    st.markdown("## 🎯 Conclusion")

    st.markdown("""
    <div class="conclusion-box">
    <h3 style="color: #80deea; margin-top: 0;">Transforming Noise into Intelligence</h3>
    This analysis demonstrates how <strong>coverage-aware metrics</strong> and <strong>rigorous geographic standardization</strong>
    transform noisy administrative enrolment logs into <strong>policy-safe, auditable insights</strong>.
    <br><br>
    Observed patterns reflect <strong>genuine enrolment intensity</strong> rather than reporting artifacts,
    enabling reliable decision support for large-scale identity systems.
    <br><br>
    <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 8px; margin-top: 1.5rem;">
    ✨ <strong>Key Achievement</strong>: Converting 19,000+ raw pincodes and 984 districts into 
    772 validated entities with interpretable, coverage-adjusted metrics.
    </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="cyan-divider">', unsafe_allow_html=True)

    # =====================================================
    # ENHANCED ACKNOWLEDGEMENT
    # =====================================================
    st.markdown("## 🙏 Acknowledgement")

    st.markdown("""
    <div class="ack-box">
    <h3 style="color: #00838f; margin-top: 0;">📚 Data & Technology</h3>
    
    <div style="margin: 1.5rem 0;">
        <strong style="color: #00695c;">Data Source:</strong> UIDAI Aadhaar Enrolment Dataset (Anonymized)<br>
        <strong style="color: #00695c;">Purpose:</strong> Analytical & educational use<br>
        <strong style="color: #00695c;">Coverage:</strong> Multi-year national enrolment records
    </div>
    
    <div style="background: white; padding: 1.5rem; border-radius: 12px; margin: 1.5rem 0; box-shadow: 0 4px 8px rgba(0,0,0,0.05);">
        <strong style="color: #00838f;">Built with:</strong><br>
        <span style="color: #546e7a;">
        🐍 Python • 🎨 Streamlit • 📊 Pandas • 📈 Plotly • 🗺️ GeoPandas
        </span>
    </div>
    
    <p style="color: #546e7a; font-size: 0.95rem; margin-top: 1.5rem; font-style: italic;">
    Developed to support transparent, data-driven governance and policy analysis.
    </p>
    
    <div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 2px solid #e0e0e0;">
        <span style="color: #00838f; font-weight: 600;">
        💡 Committed to data quality, analytical rigor, and policy impact.
        </span>
    </div>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    page()