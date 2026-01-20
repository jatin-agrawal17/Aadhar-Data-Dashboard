# 📊 Aadhaar Enrolment Analytics Dashboard (Streamlit)

An interactive **Streamlit-based analytics dashboard** developed for the **UIDAI Hackathon 2026**, designed to deliver **coverage-aware, policy-safe insights** from Aadhaar enrolment data across **national, state, district, and pincode levels**.

The application converts noisy administrative enrolment logs into **reliable decision-support intelligence** by explicitly handling **reporting gaps, batch uploads, and geographic inconsistencies**.

---

## 🔗 Live Dashboard

Link:  
https://aadhar-data-dashboard-gdhaemdgkzbziopqfyvfwg.streamlit.app/


## 🎯 Objective

Raw Aadhaar enrolment data suffers from:
- Batch uploads (especially on the 1st of each month)
- Non-reporting days
- Inconsistent state and district naming
- Legacy administrative labels

This dashboard ensures:
- Fair comparison across regions
- Separation of real enrolment demand from reporting artifacts
- Transparent and auditable analytics suitable for policy evaluation

---

## 🚀 Key Features

### 🌍 National-Level Analytics
- Total enrolments (reported days only)
- Reporting coverage indicators
- Day-of-week and day-of-month analysis
- Age-group composition (0–5, 5–17, 18+)
- Top states ranked by **average enrolments per reported day**
- Coverage-adjusted choropleth maps

### 🏛 State-Level Exploration
- Interactive selection of any state / UT
- Reporting days and district participation
- Coverage-aware average enrolments
- Temporal enrolment trends with coverage overlay
- Age-group composition
- District performance ranking using minimum reporting thresholds

### 💡 Insights
- Enrolment spikes are driven by **batch reporting**, not daily citizen activity.
- Raw totals are misleading without **reporting coverage adjustment**.
- Enrolment volume closely follows the **number of reporting districts**.
- Geographic inconsistencies inflate state, district, and pincode counts.
- Large north–central states show higher **average enrolments per reported day**.
- Aadhaar enrolment is largely **child-driven**, with minimal adult registrations.
- Low district enrolment often reflects **poor reporting continuity**, not low demand.
- Spatial patterns reveal **persistent high-intensity clusters**, not random noise.

---

## 📂 Project Structure (Streamlit App)

```text
UIDAI/
│
├── app.py                     # Streamlit entry point
├── views/                      # Streamlit pages
│   ├── overview.py             # National overview
│   ├── nationwide.py           # National-level analytics
│   ├── statewise.py            # State-level deep dive
│   ├── insights.py             # Key insights & summaries
│
├── utils/                      # Core utilities
│   ├── data_loader.py          # Data loading & preprocessing
│   ├── pdf_report.py           # PDF report generation
│   ├── gemini_report.py        # LLM-assisted insights
│   ├── national_prompt.py      # Prompt templates
│
├── data/                       # Processed datasets
├── reports/                    # Generated reports
│   ├── charts/
│   ├── National_Aadhaar_Enrolment_Report.pdf
│   ├── Uttar_Pradesh_Aadhaar_Report.pdf
│
├── requirements.txt
├── README.md
└── .env
```
---


## ▶️ Run Locally

Clone the project

```bash
git clone https://github.com/jatin-agrawal17/Aadhar-Data-Dashboard.git
```

Go to the project directory

```bash
cd project
```

Create a Virtual Environment

```bash
conda create -t venv python==3.10 -y
```

Install dependencies

```bash
pip install -r requiremrnts.txt
```

#### Write your own Gemini API key in .env file

Start the streamlit app
```bash
streamlit run app.py
```
---

### Acknowledgement

- We acknowledge UIDAI for anonymized Aadhaar data.  
- Thanks to NIC and MeitY for collaboration support.  
- This work was developed for UIDAI Hackathon 2026.
---
## 👤 Author

Jatin Agrawal  
📬 [LinkedIn](https://www.linkedin.com/in/jatin-agrawal-b80092367/)

## 📎 License

This project is open-source and available under the MIT License.


