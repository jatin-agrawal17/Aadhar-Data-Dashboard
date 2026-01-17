def build_national_report_prompt(
    report_date,
    total_enrolments,
    observed_reporting_days,
    states_reporting,
    districts_reporting,
    age_df,
    top_states_df
):
    return f"""
Aadhaar Enrolment Analysis – India

State-wise Aadhaar Enrolment Performance Report

Report Date:
{report_date}

Prepared For:
Government of India
Unique Identification Authority of India (UIDAI)

Prepared By:
Data Analytics Unit

--- PAGE BREAK ---

1. Executive Summary
This report presents a nationwide analysis of Aadhaar enrolment activity across India.
A total of {int(total_enrolments):,} enrolments were recorded over {observed_reporting_days}
reporting days, covering {states_reporting} States and Union Territories and
{districts_reporting} districts.

2. National Reporting Coverage
Reporting activity was observed across {states_reporting} States and Union Territories.
Coverage-aware indicators were used to ensure comparability.

3. Demographic Composition of Enrolments
{age_df.to_string(index=False)}

4. Temporal Enrolment Trends
Daily, weekly, and monthly patterns reveal systematic batch-based reporting behaviour.

5. State-wise Performance Analysis
Top-performing states based on average enrolments per reported day:
{top_states_df.to_string(index=False)}

6. Data Limitations and Caveats
This analysis is based on reported records only and may not capture delayed submissions.

7. Operational Implications and Recommendations
a) Sustain child enrolment momentum  
b) Address adult enrolment gaps  
c) Improve reporting consistency  
d) Strengthen data quality assurance
"""
