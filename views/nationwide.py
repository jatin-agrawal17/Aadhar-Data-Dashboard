


import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import unicodedata
from utils.data_loader import load_data
from utils.national_prompt import build_national_report_prompt
from utils.pdf_report import create_pdf_report
from datetime import datetime
import os

from pathlib import Path
CHART_DIR = "reports/charts"
os.makedirs(CHART_DIR, exist_ok=True)


import matplotlib.pyplot as plt

def build_national_report_figures_matplotlib(df, age_data, top15_states, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # -------------------------
    # 1. Daily Trend
    # -------------------------
    daily = (
        df.groupby('date')
        .agg(total_enrolments=('total_daily_enrolement', 'sum'))
        .reset_index()
    )

    plt.figure(figsize=(10, 4))
    plt.plot(daily['date'], daily['total_enrolments'], linewidth=2)
    plt.title("Daily Aadhaar Enrolments")
    plt.xlabel("Date")
    plt.ylabel("Total Enrolments")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/daily_trend.png")
    plt.close()

    # -------------------------
    # 2. Weekday Pattern
    # -------------------------
    weekday = (
        df.groupby('day_name')['total_daily_enrolement']
        .sum()
        .reindex(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
    )

    plt.figure(figsize=(8, 4))
    weekday.plot(kind='bar')
    plt.title("Total Aadhaar Enrolments by Day of Week")
    plt.xlabel("Day")
    plt.ylabel("Total Enrolments")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/weekday_pattern.png")
    plt.close()

    # -------------------------
    # 3. Age Composition
    # -------------------------
    plt.figure(figsize=(6, 6))
    plt.pie(
        age_data["Share (%)"],
        labels=age_data["Age Group"],
        autopct='%1.1f%%',
        startangle=90
    )
    plt.title("Aadhaar Enrolment by Age Group")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/age_distribution.png")
    plt.close()

    # -------------------------
    # 4. Top States
    # -------------------------
    top_states = top15_states.sort_values('avg_enrolments_per_reported_day')

    plt.figure(figsize=(8, 6))
    plt.barh(
        top_states['state'],
        top_states['avg_enrolments_per_reported_day']
    )
    plt.title("Top States by Avg Enrolments per Reported Day")
    plt.xlabel("Avg Enrolments")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/top_states.png")
    plt.close()

    return [
        ("Daily Enrolment Trend", f"{output_dir}/daily_trend.png"),
        ("Weekly Pattern", f"{output_dir}/weekday_pattern.png"),
        ("Age Composition", f"{output_dir}/age_distribution.png"),
        ("Top Performing States", f"{output_dir}/top_states.png"),
    ]


# def build_national_report_figures(df, age_data, top15_states):
#     # Daily Trend
#     daily = (
#         df.groupby('date')
#         .agg(
#             total_enrolments=('total_daily_enrolement', 'sum'),
#             reporting_districts=('district', 'nunique')
#         )
#         .reset_index()
#     )

#     fig_trend = go.Figure()
#     fig_trend.add_trace(go.Scatter(
#         x=daily['date'],
#         y=daily['total_enrolments'],
#         mode='lines',
#         name='Total Enrolments'
#     ))

#     # Weekday Pattern
#     weekday = (
#         df.groupby('day_name')['total_daily_enrolement']
#         .sum()
#         .reset_index()
#     )

#     fig_weekday = px.bar(
#         weekday,
#         x='day_name',
#         y='total_daily_enrolement'
#     )

#     # Age Composition
#     fig_age = px.pie(
#         age_data,
#         values="Share (%)",
#         names="Age Group",
#         hole=0.4
#     )

#     # Top States
#     fig_top = px.bar(
#         top15_states.sort_values('avg_enrolments_per_reported_day'),
#         x='avg_enrolments_per_reported_day',
#         y='state',
#         orientation='h'
#     )

#     return fig_trend, fig_weekday, fig_age, fig_top



def page():
    # ----------------------------- 
    # Custom CSS for Enhanced UI - Modern Teal Theme
    # ----------------------------- 
    st.markdown("""
        <style>
        /* Main container styling */
        .main {
            padding: 1rem 2rem;
        }
        
        /* Header styling */
        .dashboard-header {
            background: linear-gradient(135deg, #0891b2 0%, #06b6d4 50%, #14b8a6 100%);
            padding: 2.5rem 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        
        .dashboard-title {
            color: white;
            font-size: 2.5rem;
            font-weight: 700;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }
        
        .dashboard-subtitle {
            color: rgba(255, 255, 255, 0.95);
            font-size: 1.2rem;
            margin-top: 0.8rem;
        }
        
        /* Metric card styling */
        .metric-card {
            background: white;
            padding: 1.8rem 1.5rem;
            border-radius: 12px;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.08);
            border-top: 4px solid #0891b2;
            transition: all 0.3s;
            text-align: center;
        }
        
        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
        }
        
        .metric-icon {
            font-size: 2.5rem;
            margin-bottom: 0.8rem;
        }
        
        .metric-label {
            font-size: 0.9rem;
            color: #64748b;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }
        
        .metric-value {
            font-size: 2rem;
            font-weight: 700;
            color: #0f172a;
        }
        
        /* Section header styling */
        .section-header {
            background: linear-gradient(135deg, #ecfeff 0%, #cffafe 100%);
            padding: 1rem 1.5rem;
            border-radius: 10px;
            border-left: 5px solid #06b6d4;
            margin: 2rem 0 1.5rem 0;
        }
        
        .section-title {
            color: #0891b2;
            font-size: 1.5rem;
            font-weight: 700;
            margin: 0;
        }
        
        /* Subsection styling */
        .subsection-title {
            color: #0891b2;
            font-size: 1.2rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }
        
        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background: linear-gradient(135deg, #f0fdfa 0%, #ccfbf1 100%);
            padding: 0.5rem;
            border-radius: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            background-color: white;
            border-radius: 8px;
            color: #0891b2;
            font-weight: 600;
            padding: 0 1.5rem;
            border: 2px solid transparent;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #0891b2 0%, #06b6d4 100%);
            color: white;
            border: 2px solid #0891b2;
        }
        
        /* Info box styling */
        .info-box {
            background: linear-gradient(135deg, #ecfeff 0%, #cffafe 100%);
            border-left: 5px solid #06b6d4;
            padding: 1rem 1.5rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        
        /* Success banner styling */
        .success-banner {
            background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
            border-left: 5px solid #10b981;
            color: #065f46;
            padding: 1rem 1.5rem;
            border-radius: 8px;
            text-align: center;
            font-weight: 600;
            margin-top: 2rem;
        }
        
        /* Dataframe styling */
        .dataframe {
            border-radius: 8px;
            overflow: hidden;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # ----------------------------- 
    # Helper Functions
    # ----------------------------- 
    STATE_ALIAS = {
        "nct of delhi": "delhi",
        "national capital territory of delhi": "delhi",
        "orissa": "odisha",
        "dadra and nagar haveli and daman and diu": "dadra and nagar haveli and daman and diu"
    }

    def normalize_and_map(name):
        if pd.isna(name):
            return name
        name = unicodedata.normalize('NFKD', name)
        name = ''.join(c for c in name if not unicodedata.combining(c))
        name = name.lower().strip()
        return STATE_ALIAS.get(name, name)

    def create_metric_card(label, value, icon):
        """Create a styled metric display"""
        return f"""
        <div class="metric-card">
            <div class="metric-icon">{icon}</div>
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """
    
    # ----------------------------- 
    # Header
    # ----------------------------- 
    st.markdown("""
        <div class="dashboard-header">
            <h1 class="dashboard-title">🌍 Nationwide Aadhaar Enrolment Analysis</h1>
            <p class="dashboard-subtitle">
                Comprehensive insights into Aadhaar enrolment activity across India
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # ----------------------------- 
    # Load Data
    # ----------------------------- 
    with st.spinner('📊 Loading data...'):
        df = load_data()
        df["date"] = pd.to_datetime(df["date"])
    
    # ----------------------------- 
    # High-level Metrics
    # ----------------------------- 
    observed_reporting_days = df['date'].nunique()
    states_reporting = df['state'].nunique()
    districts_standardized = df['district'].nunique()
    total_enrolments = df['total_daily_enrolement'].sum()
    avg_enrolments_per_reported_day = total_enrolments / observed_reporting_days
    
    # Display metrics in cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(create_metric_card(
            "Reporting Days", 
            f"{observed_reporting_days:,}", 
            "📅"
        ), unsafe_allow_html=True)
    
    with col2:
        st.markdown(create_metric_card(
            "States / UTs", 
            f"{states_reporting}", 
            "🗺️"
        ), unsafe_allow_html=True)
    
    with col3:
        st.markdown(create_metric_card(
            "Districts", 
            f"{districts_standardized:,}", 
            "🏙️"
        ), unsafe_allow_html=True)
    
    with col4:
        st.markdown(create_metric_card(
            "Avg Enrolments/Day", 
            f"{int(avg_enrolments_per_reported_day):,}", 
            "📊"
        ), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ============================= 
    # AGE GROUP ANALYSIS
    # ============================= 
    st.markdown("""
        <div class="section-header">
            <h2 class="section-title">👶 Age Group Composition</h2>
        </div>
    """, unsafe_allow_html=True)
    
    age_data = pd.DataFrame({
        "Age Group": ["0–5 years", "5–17 years", "18+ years"],
        "Enrolments": [
            df['age_0_5'].sum(),
            df['age_5_17'].sum(),
            df['age_18_greater'].sum()
        ]
    })
    age_data["Share (%)"] = (age_data["Enrolments"] / total_enrolments * 100).round(2)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig_age = px.pie(
            age_data,
            values="Share (%)",
            names="Age Group",
            hole=0.4,
            title="National Aadhaar Enrolment by Age Group",
            color_discrete_sequence=['#0891b2', '#06b6d4', '#14b8a6']
        )
        fig_age.update_traces(
            textinfo="percent+label",
            textfont_size=14,
            marker=dict(line=dict(color='white', width=2))
        )
        fig_age.update_layout(
            title_font_size=16,
            showlegend=True,
            height=400,
            template='plotly_white'
        )
        st.plotly_chart(fig_age, use_container_width=True)
        st.markdown(
    "**This pie chart presents the distribution of Aadhaar enrolments across age groups (0–5, 5–17, and 18+ years) using "
    "reported records only, highlighting the relative contribution of each demographic segment to total enrolment volume.**"
)


    
    with col2:
        st.markdown("### 📊 Breakdown")
        for _, row in age_data.iterrows():
            st.metric(
                label=row['Age Group'],
                value=f"{row['Share (%)']:.2f}%",
                delta=f"{row['Enrolments']:,} enrolments"
            )
    
    # ============================= 
    # TEMPORAL ANALYSIS TABS
    # ============================= 
    st.markdown("""
        <div class="section-header">
            <h2 class="section-title">📈 Temporal Analysis</h2>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📅 Daily Trend", 
        "📆 Day of Week", 
        "📊 Day of Month",
        "🗓️ Monthly View"
    ])
    
    with tab1:
        national_daily = (
            df.groupby('date')
            .agg(
                total_enrolments=('total_daily_enrolement', 'sum'),
                reporting_districts=('district', 'nunique')
            )
            .reset_index()
        )
        
        fig_trend = go.Figure()
        fig_trend.add_trace(go.Scatter(
            x=national_daily['date'],
            y=national_daily['total_enrolments'],
            mode='lines',
            name='Total Enrolments',
            line=dict(color='#0891b2', width=3),
            fill='tozeroy',
            fillcolor='rgba(8, 145, 178, 0.1)'
        ))

        fig_trend.add_trace(go.Scatter(
            x=national_daily['date'],
            y=national_daily['reporting_districts'],
            mode='lines',
            name='Reporting Districts',
            line=dict(color='#14b8a6', width=2, dash='dash'),
            yaxis='y2'
        ))
        fig_trend.update_layout(
            yaxis=dict(
                title=dict(text="Total Enrolments", font=dict(color='#0891b2'))
            ),
            yaxis2=dict(
                title=dict(text="Reporting Districts", font=dict(color='#14b8a6')),
                overlaying="y",
                side="right"
            ),
            title="National Aadhaar Enrolment and Reporting Coverage",
            hovermode='x unified',
            height=450,
            template='plotly_white'
        )
        st.plotly_chart(fig_trend, use_container_width=True)
        st.markdown(
    "**This time-series plot presents total Aadhaar enrolments at the national level alongside the number of reporting "
    "districts for each reported day, enabling joint interpretation of enrolment volumes and reporting coverage over time.**"
)
    
    with tab2:
        weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        daywise = (
            df.groupby('day_name')['total_daily_enrolement']
            .sum()
            .reindex(weekday_order)
            .reset_index()
        )
        
        fig_day = px.bar(
            daywise,
            x='day_name',
            y='total_daily_enrolement',
            text_auto='.2s',
            title="Total Aadhaar Enrolment by Day of Week",
            color='total_daily_enrolement',
            color_continuous_scale=['#cffafe', '#06b6d4', '#0891b2', '#0e7490'],
            labels={'day_name': 'Day of Week', 'total_daily_enrolement': 'Total Enrolments'}
        )
        fig_day.update_traces(textposition='outside')
        fig_day.update_layout(showlegend=False, height=450, template='plotly_white')
        st.plotly_chart(fig_day, use_container_width=True)
        st.markdown(
    "**This bar chart shows total Aadhaar enrolments aggregated by day of the week, based on reported records only, "
    "allowing comparison of cumulative enrolment volumes across weekdays and weekends.**"
)
    
    with tab3:
        dom = (
            df.groupby('day')['total_daily_enrolement']
            .sum()
            .reset_index()
            .sort_values('day')
        )
        
        fig_dom = px.bar(
            dom,
            x='day',
            y='total_daily_enrolement',
            title="Total Aadhaar Enrolment by Day of Month",
            color='total_daily_enrolement',
            color_continuous_scale=['#ccfbf1', '#14b8a6', '#0d9488', '#0f766e'],
            labels={'day': 'Day of Month', 'total_daily_enrolement': 'Total Enrolments'}
        )
        fig_dom.update_layout(showlegend=False, height=450, template='plotly_white')
        st.plotly_chart(fig_dom, use_container_width=True)
        st.markdown(
    "**The extreme concentration of enrolments on the 1st day of the month confirms systematic month-start batch reporting, "
    "indicating that day-of-month peaks reflect reporting behavior rather than real enrolment patterns.**"
)
    
    with tab4:
        df['month'] = df['date'].dt.month
        df['month_name'] = df['date'].dt.strftime('%B')
        monthly_stats = (
            df.groupby(['month', 'month_name'])
            .agg(
                total_enrolments=('total_daily_enrolement', 'sum'),
                reporting_days=('date', 'nunique')
            )
            .reset_index()
            .sort_values('month')
        )
        monthly_stats['avg_enrolments_per_reported_day'] = (
            monthly_stats['total_enrolments'] / monthly_stats['reporting_days']
        )
        
        fig_month = go.Figure()
        fig_month.add_trace(go.Bar(
            x=monthly_stats['month_name'],
            y=monthly_stats['total_enrolments'],
            name='Total Enrolments',
            marker_color='#0891b2',
            text=monthly_stats['total_enrolments'],
            texttemplate='%{text:.2s}',
            textposition='outside'
        ))
        fig_month.update_layout(
            title="Monthly Enrolment Performance",
            xaxis_title="Month",
            yaxis_title="Total Enrolments",
            height=450,
            template='plotly_white'
        )
        st.plotly_chart(fig_month, use_container_width=True)
        
        st.markdown('<h3 class="subsection-title">📋 Detailed Monthly Statistics</h3>', unsafe_allow_html=True)
        st.dataframe(
            monthly_stats[['month_name', 'total_enrolments', 'reporting_days', 'avg_enrolments_per_reported_day']].style.format({
                'total_enrolments': '{:,.0f}',
                'reporting_days': '{:.0f}',
                'avg_enrolments_per_reported_day': '{:,.2f}'
            }),
            use_container_width=True,
            hide_index=True
        )
    
    # ============================= 
    # STATE LEVEL ANALYSIS
    # ============================= 
    st.markdown("""
        <div class="section-header">
            <h2 class="section-title">🗺️ State-wise Analysis</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Calculate state statistics with age groups
    state_stats = (
        df.groupby('state')
        .agg(
            total_enrolments=('total_daily_enrolement', 'sum'),
            reporting_days=('date', 'nunique'),
            age_0_5=('age_0_5', 'sum'),
            age_5_17=('age_5_17', 'sum'),
            age_18_plus=('age_18_greater', 'sum')
        )
        .reset_index()
    )
    state_stats['avg_enrolments_per_reported_day'] = (
        state_stats['total_enrolments'] / state_stats['reporting_days']
    )
    
    # Calculate coverage percentage
    state_stats['coverage_pct'] = (
        state_stats['reporting_days'] / observed_reporting_days * 100
    )
    
    # Filter states with ≥70% coverage
    coverage_threshold = 0.70 * observed_reporting_days
    state_filtered = state_stats[
        state_stats['reporting_days'] >= coverage_threshold
    ].copy()
    
    # ============================= 
    # TOP 15 STATES ANALYSIS
    # ============================= 
    st.markdown('<h3 class="subsection-title">🏆 Top 15 States by Performance</h3>', unsafe_allow_html=True)
    
    top15_states = (
        state_filtered
        .sort_values('avg_enrolments_per_reported_day', ascending=False)
        .head(15)
    )
    
    # Horizontal bar chart for top 15 states
    fig_top15 = px.bar(
        top15_states.sort_values('avg_enrolments_per_reported_day'),
        x='avg_enrolments_per_reported_day',
        y='state',
        orientation='h',
        title='Top 15 States by Average Aadhaar Enrolments per Reported Day<br><sup>(States with ≥70% National Reporting Coverage)</sup>',
        labels={
            'avg_enrolments_per_reported_day': 'Avg Enrolments per Reported Day',
            'state': 'State'
        },
        hover_data={
            'reporting_days': True,
            'coverage_pct': ':.1f',
            'total_enrolments': ':,.0f'
        },
        color='avg_enrolments_per_reported_day',
        color_continuous_scale='Teal',
        text='avg_enrolments_per_reported_day'
    )
    
    fig_top15.update_traces(
        texttemplate='%{text:,.0f}',
        textposition='outside',
        textfont=dict(size=11)
    )
    
    fig_top15.update_layout(
        height=600,
        showlegend=False,
        yaxis={'categoryorder': 'total ascending'},
        template='plotly_white'
    )
    
    fig_top15.update_coloraxes(showscale=False)
    
    st.plotly_chart(fig_top15, use_container_width=True)
    st.markdown(
    "**This bar chart ranks states by average Aadhaar enrolments per reported day, restricted to states with ≥70% national "
    "reporting coverage, ensuring comparability by adjusting for missing or inconsistent reporting days rather than "
    "relying on raw totals.**"
)
    
    # Validation table
    # st.markdown('<h4 style="color: #0891b2; margin-top: 1.5rem;">📋 Top 15 States - Detailed Statistics</h4>', unsafe_allow_html=True)
    # validation_table = (
    #     top15_states[[
    #         'state',
    #         'reporting_days',
    #         'coverage_pct',
    #         'avg_enrolments_per_reported_day',
    #         'total_enrolments'
    #     ]]
    #     .sort_values('avg_enrolments_per_reported_day', ascending=False)
    # )
    
    # st.dataframe(
    #     validation_table.style.format({
    #         'reporting_days': '{:.0f}',
    #         'coverage_pct': '{:.1f}%',
    #         'avg_enrolments_per_reported_day': '{:,.0f}',
    #         'total_enrolments': '{:,.0f}'
    #     }),
    #     use_container_width=True,
    #     hide_index=True
    # )
    
    # ============================= 
    # AGE COMPOSITION BY STATE
    # ============================= 
    st.markdown('<h3 class="subsection-title">👶 Age Group Composition by State</h3>', unsafe_allow_html=True)
    
    # Calculate age percentages
    top15_states_age = top15_states.copy()
    top15_states_age['age_0_5_pct'] = (
        top15_states_age['age_0_5'] / top15_states_age['total_enrolments'] * 100
    )
    top15_states_age['age_5_17_pct'] = (
        top15_states_age['age_5_17'] / top15_states_age['total_enrolments'] * 100
    )
    top15_states_age['age_18_plus_pct'] = (
        top15_states_age['age_18_plus'] / top15_states_age['total_enrolments'] * 100
    )
    
    # Reshape for stacked bar chart
    age_long = top15_states_age.melt(
        id_vars=['state'],
        value_vars=['age_0_5_pct', 'age_5_17_pct', 'age_18_plus_pct'],
        var_name='Age Group',
        value_name='Share (%)'
    )
    
    age_long['Age Group'] = age_long['Age Group'].replace({
        'age_0_5_pct': '0–5 years',
        'age_5_17_pct': '5–17 years',
        'age_18_plus_pct': '18+ years'
    })
    
    # Create stacked bar chart
    fig_age_state = px.bar(
        age_long,
        x='state',
        y='Share (%)',
        color='Age Group',
        title="Age-Group Composition of Aadhaar Enrolment Activity<br><sup>Top 15 States by Average Enrolments per Reported Day</sup>",
        labels={
            'state': 'State',
            'Share (%)': 'Share of Enrolment Transactions (%)'
        },
        color_discrete_sequence=['#0891b2', '#06b6d4', '#14b8a6']
    )
    
    fig_age_state.update_layout(
        xaxis_tickangle=-45,
        yaxis=dict(range=[0, 100]),
        legend_title='Age Group',
        height=500,
        template='plotly_white'
    )
    
    st.plotly_chart(fig_age_state, use_container_width=True)
    st.markdown(
    "**This stacked bar chart shows the age-wise composition of enrolments (0–5, 5–17, 18+ years) for the top 15 states "
    "ranked by average enrolments per reported day, illustrating how enrolment activity is distributed across age groups "
    "within each state.**"
)
    
    # ============================= 
    # GEOGRAPHIC MAPS
    # ============================= 
    st.markdown('<h3 class="subsection-title">🗺️ Geographic Distribution</h3>', unsafe_allow_html=True)
    
    # Load GeoJSON
    india_states_gdf = gpd.read_file("data/geoBoundaries-IND-ADM1.geojson")
    if india_states_gdf.crs is None:
        india_states_gdf = india_states_gdf.set_crs(epsg=4326)
    else:
        india_states_gdf = india_states_gdf.to_crs(epsg=4326)
    
    state_stats['state_norm'] = state_stats['state'].apply(normalize_and_map)
    india_states_gdf['state_norm'] = india_states_gdf['shapeName'].apply(normalize_and_map)
    
    india_map_data = india_states_gdf.merge(
        state_stats,
        on='state_norm',
        how='left'
    )
    india_map_data['avg_enrolments_per_reported_day'] = pd.to_numeric(
        india_map_data['avg_enrolments_per_reported_day'],
        errors='coerce'
    )
    
    # Create tabs for different map views
    map_tab2, map_tab1 = st.tabs(["📊 Absolute Values", "🔥 Intensity Map (Quantiles)"])
    
    with map_tab1:
        valid_vals = india_map_data['avg_enrolments_per_reported_day'].dropna()
        india_map_data.loc[valid_vals.index, 'quantile'] = pd.qcut(
            valid_vals, q=5, duplicates='drop'
        )
        
        fig, ax = plt.subplots(1, 1, figsize=(14, 16))
        india_map_data.plot(
            column='quantile',
            cmap='YlGnBu',
            ax=ax,
            edgecolor='black',
            legend=True,
            missing_kwds={"color": "lightgrey"}
        )
        ax.set_title(
            "Coverage-aware Enrolment Intensity (Quantiles)",
            fontsize=18,
            fontweight='bold',
            pad=20
        )
        ax.axis("off")
        st.pyplot(fig)

    
    with map_tab2:
        fig2, ax2 = plt.subplots(1, 1, figsize=(14, 16))
        india_map_data.plot(
            column='avg_enrolments_per_reported_day',
            cmap='GnBu',
            linewidth=1.1,
            ax=ax2,
            edgecolor='black',
            legend=True,
            legend_kwds={
                'label': "Average Aadhaar Enrolments per Reported Day",
                'shrink': 0.65
            },
            missing_kwds={
                "color": "lightgrey",
                "edgecolor": "black",
                "label": "No reported data"
            }
        )
        ax2.set_title(
            "Average Aadhaar Enrolments per Reported Day (State-wise)",
            fontsize=18,
            fontweight='bold',
            pad=20
        )
        ax2.axis("off")
        
        # Label top 20 states
        top_states = (
            india_map_data[['shapeName', 'avg_enrolments_per_reported_day', 'geometry']]
            .dropna()
            .sort_values('avg_enrolments_per_reported_day', ascending=False)
            .head(20)
        )
        for _, row in top_states.iterrows():
            centroid = row.geometry.centroid
            ax2.text(
                centroid.x, centroid.y,
                f"{int(row.avg_enrolments_per_reported_day):,}",
                fontsize=9,
                ha='center',
                va='center',
                color='black',
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7)
            )
        
        st.pyplot(fig2)
        st.markdown(
    "**This choropleth map visualizes state-wise average Aadhaar enrolments per reported day using a coverage-aware metric, "
    "ensuring that differences reflect enrolment intensity on reporting days rather than variations in reporting frequency.**"
)
    
    # Top performing states table
    st.markdown('<h4 style="color: #0891b2; margin-top: 1.5rem;">🏆 Top 10 Performing States (Overall)</h4>', unsafe_allow_html=True)
    top_10_states = state_stats.nlargest(10, 'avg_enrolments_per_reported_day')
    st.dataframe(
        top_10_states[['state', 'total_enrolments', 'reporting_days', 'avg_enrolments_per_reported_day']].style.format({
            'total_enrolments': '{:,.0f}',
            'reporting_days': '{:.0f}',
            'avg_enrolments_per_reported_day': '{:,.2f}'
        }),
        use_container_width=True,
        hide_index=True
    )


    st.markdown("## 📄 Generate National Aadhaar Report")

    if st.button("📥 Download National Aadhaar Report"):

        # ✅ CORRECT: generate charts using Matplotlib
        chart_paths = build_national_report_figures_matplotlib(
            df=df,
            age_data=age_data,
            top15_states=top15_states,
            output_dir=CHART_DIR
        )

        report_date = datetime.today().strftime("%d %B %Y")

        report_text = build_national_report_prompt(
            report_date=report_date,
            total_enrolments=total_enrolments,
            observed_reporting_days=observed_reporting_days,
            states_reporting=states_reporting,
            districts_reporting=districts_standardized,
            age_df=age_data,
            top_states_df=top15_states[['state', 'avg_enrolments_per_reported_day']]
        )

        output_path = Path("reports/National_Aadhaar_Enrolment_Report.pdf")

        create_pdf_report(
            output_path=str(output_path),
            report_text=report_text,
            chart_paths=chart_paths
        )

        with open(output_path, "rb") as f:
            pdf_bytes = f.read()

        st.download_button(
            label="⬇️ Download National Aadhaar Report (PDF)",
            data=pdf_bytes,
            file_name="National_Aadhaar_Enrolment_Report.pdf",
            mime="application/pdf"
        )

        st.success("✅ National Aadhaar Report generated successfully")



# Run the page
if __name__ == "__main__":
    page()