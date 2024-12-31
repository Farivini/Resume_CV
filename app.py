from pathlib import Path
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

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
    "Telegram bot + scrapping": {
        "Link": "https://www.linkedin.com/services/page/7142403115320a0782/",
        "Descrição": "Developed a Telegram bot capable of responding to user commands by performing web scraping to extract and return relevant information from web pages. The application can be utilized for various purposes, including price monitoring, news extraction, and specific data collection from websites.",
        "Imagem": None,
        "Video": None,
    },
    "Pipeline GCP + Power bi":{
        "Link": "https://github.com/Farivini/storage-dataflow-bigquery-powerbi",
        "Descrição": "Developed a complete pipeline integrated Cloud storage , Data flow , Big query and Power bi",
        "Imagem": None,
        "Video": None,

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
    wpp = st.markdown(
        f'[Send me a WhatsApp message](https://api.whatsapp.com/send?phone={whatsapp_number})',
        unsafe_allow_html=True,
    )
    st.write("📫", EMAIL)

    download_button = st.download_button(
        label="Download CV",
        data=PDFbyte,
        file_name="CV_Vinicius_Farineli_Freire.pdf",
        mime="application/pdf",
    )

# --- SOCIAL LINKS ---
st.write("\n")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 4 years of experience in data extraction and transformation with SQL, Oracle RAC.
- ✔️ 4 years working with Python, Power BI, Linux, and R.
- ✔️ 2 years of experience with Big Query, Dataflow and Data Storage.
- ✔️ Strong understanding of statistical principles and their applications.
- ✔️ Excellent team player with a strong sense of initiative.
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), Pyspark, SQL, VBA, DAX, and Streamlit
- 📊 Data Visualization & Tools: Power BI, Looker, Excel, Microstrategy, Plotly, Grafana, Airflow, Power Automate
- 🗄️ Databases: Postgres, MongoDB, MySQL, Oracle, Big Query, Neo4j.
"""
)

# --- WORK HISTORY ---
st.write("\n")
st.subheader("Work Experience")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Consultant at TIM**")
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
st.write("\n")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, details in PROJECTS.items():
    st.write(f"{project}:")
    st.write(f"  - Description: {details['Descrição']}")
    if details["Imagem"]:
        st.image(details["Imagem"], width=600)
    if details["Video"]:
        st.video(details["Video"])
    st.write(f"  - Link: {details['Link']}")

# --- IFAMES ---
st.write("\n")
st.subheader("Interactive Dashboards")
st.write("---")

st.write("### Dashboard Pipeline GCP")
components.iframe(
    src="https://app.powerbi.com/view?r=eyJrIjoiNWU1MTM3OWEtOTY3Yi00NjM4LWE3MGItN2E1Nzg3Y2M3OWVkIiwidCI6ImRlNjFmOTAxLTI1ZTYtNDIxZi1hMjViLTAwZWM1ZjAzYmY3NSJ9",
    width=600,
    height=373,
)

st.write("### Dashboard Resume Big numbers")
components.iframe(
    src="https://app.powerbi.com/view?r=eyJrIjoiMzdiYzg4MzAtMmVhYy00MTI2LTgzZTYtNWM5MmQ2MjVlM2VlIiwidCI6ImRlNjFmOTAxLTI1ZTYtNDIxZi1hMjViLTAwZWM1ZjAzYmY3NSJ9",
    width=600,
    height=373,
)
