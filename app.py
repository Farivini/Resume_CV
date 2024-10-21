from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
whatsapp_number = "5541999132478"  # Replace with your real number
whatsapp_image_url = "whatsapp.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Vinicius Farineli Freire"
PAGE_ICON = ":wave:"
NAME = "Vinicius Farineli Freire"
DESCRIPTION = """
Consultant, graduated in Big Data and Computer Engineering, with a Postgraduate degree in Data Science, supporting data-driven decision making and task automation.
"""
EMAIL = "viniciusfarineli@email.com"

SOCIAL_MEDIA = {
    "Website": "",
    "LinkedIn": "https://www.linkedin.com/in/vinicius-farineli/",
    "GitHub": "https://github.com/Farivini",
    
}
PROJECTS = {
    "Car Sales Dashboard": {
        "Link": "https://app.powerbi.com/view?r=eyJrIjoiNTg4ZWNiMTUtOTViZS00NjFhLTk0YjEtYzEyODg5YjVkODdiIiwidCI6ImRlNjFmOTAxLTI1ZTYtNDIxZi1hMjViLTAwZWM1ZjAzYmY3NSJ9",
        "Descrição": "Developed a dashboard to monitor car sales, providing return on investment (ROI) metrics and revenue tracking over time. This dashboard offers valuable insights for strategic decision-making and identifying growth opportunities.",
        "Imagem": "vendas.png",
        "Video": None
    },
    "Consolidation of KPIs in a Power BI App": {
        "Link": "Internal development",
        "Descrição": "Led a team responsible for consolidating all relevant KPIs for network monitoring into a Power BI application. This app integrates more than 50 individual reports using MySQL, Oracle, APIs, and Power Automate, all dashboards built by me, covering a wide range of aspects of telecom network operations. This centralization facilitates analysis and strategic decision-making, providing a comprehensive view of network performance.",
        "Imagem": None,
        "Video": None
    },
    "KPI Monitoring of Network Availability and Downtime Impact": {
        "Link": "Internal development",
        "Descrição": "Actively participated in the development of a system using PHP MySQL with API queries, running on a Linux environment. It is an online system that checks the status of network elements, identifying if they are out of service. This system is essential for ensuring continuous service availability and quick problem resolution.",
        "Imagem": None,
        "Video": None
    },
    "Automated Invoice Insertion System": {
        "Link": "https://www.linkedin.com/services/page/7142403115320a0782/",
        "Descrição": "Implemented a bot that automates the insertion of over 600 invoices into the internal system of a car salvage company.",
        "Imagem": None,
        "Video": None
    },
    "Consultation Bot (Via Telegram)": {
        "Link": "https://www.linkedin.com/services/page/7142403115320a0782/",
        "Descrição": "Implemented a consultation bot on Telegram to provide automated customer support. The bot can respond to common customer queries, provide information about products and services, and forward more complex issues to the appropriate team.",
        "Imagem": "bot.png",
        "Video": None
    },
    "PDF Data Extraction System": {
        "Link": "https://www.linkedin.com/services/page/7142403115320a0782/",
        "Descrição": "Developed a data extraction system for PDF files to automate the process of data collection and analysis. This system can extract structured data from PDF documents, improving efficiency and accuracy in handling large volumes of data.",
        "Imagem": None,
        "Video": "https://www.youtube.com/watch?v=olP0nzFenkU"
    },
    "Mechanical Workshop WebApp": {
        "Link": "https://www.linkedin.com/services/page/7142403115320a0782/",
        "Descrição": "Developed a WebApp for a mechanical workshop, allowing customer registration, customer search, and part inventory management. This WebApp optimizes internal processes, providing efficient management of customers and stock.",
        "Imagem": None,
        "Video":"https://www.youtube.com/watch?v=81edukb3RDc"
    },
    "WebApp Built with Flutterflow": {
        "Link": "https://www.linkedin.com/services/page/7142403115320a0782/",
        "Descrição": "Using the Flutterflow platform, I developed a WebApp offering an intuitive user experience. This WebApp makes it easy to share important links related to your business.",
        "Imagem": "webapp.png",
        "Video": None
    }
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    img = st.image(whatsapp_image_url, width=20) 
    wpp = st.markdown(f'[Send me a WhatsApp message](https://api.whatsapp.com/send?phone={whatsapp_number})', unsafe_allow_html=True)
    st.write("📫", EMAIL)
   
    download_button = st.download_button(
        label="Download CV",
        data=PDFbyte,
        file_name="CV_Vinicius_Farineli_Freire.pdf",
        mime="application/pdf"
    )

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 4 years of experience in data extraction and transformation with SQL, Oracle RAC.

- ✔️ 4 years working with Python, Power BI, Azure, Kafka, and R.

- ✔️ 2 years of experience with Big Query and Data Storage.

- ✔️ Strong understanding of statistical principles and their applications.

- ✔️ Excellent team player with a strong sense of initiative.
    """
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), Pyspark, SQL, VBA, DAX, and Django
- 📊 Data Visualization & Tools: Power BI, MS Excel, Microstrategy, Plotly, Grafana, Apache Spark, Apache Kafka, Power Automate
- 🗄️ Databases: Postgres, MongoDB, MySQL, Oracle, Big Query.
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work Experience")
st.write("---")

# --- JOB 1
st.write("🚧", "**Consultant at TIM**")
st.write("01/2021 - Present")
st.write(
    """
- ► Utilized Power BI and SQL to redefine and monitor KPIs related to the telecommunications network, providing data for executive dashboards for strategic decision-making.

- ► Specialized in redefining and creating data pipelines with Kafka, including creating Dags.

- ► Automated data ingestion through APIs, sending data via Azure, and building executive dashboards with Power BI.

- ► Developed ML models using GCP - Big Query, Data Storage, and Vertex AI.

- ► Participated in a Yellow Belt project focused on improving the customer experience by optimizing and prioritizing maintenance of business-critical stations.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, details in PROJECTS.items():
    st.write(f"{project}:")
    st.write(f"  - Description: {details['Descrição']}")
    if details['Imagem']:
        st.image(details['Imagem'], width=600)
    if details['Video']:
        st.video(details['Video'])
    st.write(f"  - Link: {details['Link']}")
