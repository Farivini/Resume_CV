from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
whatsapp_number = "5541999132478"  # Substitua pelo seu número real
whatsapp_image_url = "whatsapp.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Vinicius Farineli Freire"
PAGE_ICON = ":wave:"
NAME = "Vinicius Farineli Freire"
DESCRIPTION = """
Consultor, formado em Big data e Engenharia da computação, apoiando a tomada de decisões baseadas em dados e automações de tarefas.
"""
EMAIL = "viniciusfarineli@email.com"

SOCIAL_MEDIA = {
    "Site": "",
    "LinkedIn": "https://www.linkedin.com/in/vinicius-farineli/",
    "GitHub": "https://github.com/Farivini",
    
}
PROJECTS = {
    "Dashboard de Vendas de Carro": {
        "Link": "https://www.linkedin.com/services/page/7142403115320a0782/",
        "Descrição": "Desenvolvi um dashboard para acompanhar as vendas de carros, fornecendo métricas de retorno sobre o investimento (ROI) e monitoramento da evolução do faturamento ao longo do tempo. Este dashboard fornece insights valiosos para tomada de decisões estratégicas e identificação de oportunidades de crescimento.",
        "Imagem": "vendas.png",
        "Video": None
    },
    "Consolidação de KPIs em um App no Power BI": {
        "Link": "Desenvolvimento interno da empresa",
        "Descrição": "Responsável, junto com uma equipe dedicada, pela consolidação de todos os KPIs relevantes para monitoramento de rede em um aplicativo no Power BI. Este aplicativo integra mais de 50 relatórios individuais de power bi, usamos Mysql, Oracle, APIs e Power automate na construção dos paineis, todos elaborados por mim, abrangendo uma ampla gama de aspectos das operações de rede de telecomunicações. Essa centralização facilita a análise e tomada de decisões estratégicas, proporcionando uma visão abrangente do desempenho da rede.",
        "Imagem": None,
        "Video": None
    },
    "Monitoramento KPI de Disponibilidade e Impacto de Paradas na Rede": {
        "Link": "Desenvolvimento interno da empresa",
        "Descrição": "Participei ativamente do desenvolvimento de um sistema que usa PHP Mysql com consultas a APIs e que usa sistema op linux, um sitema online que verifica o status dos elementos de rede, identificando se estão fora de serviço. Este sistema é essencial para garantir a disponibilidade contínua dos serviços de rede e a rápida resolução de problemas.",
        "Imagem": None,
        "Video": None
    },

     "Automação de inserção de nota fiscal no sistema": {
        "Link": "https://www.linkedin.com/services/page/7142403115320a0782/",
        "Descrição": "Implementei um bot que faz a inserção de mais de 600 notas fiscais no sistema interno da empresa de carros salvados",
        "Imagem": None,
        "Video": None
    },

    
    "Bot de Consulta (Via Telegram)": {
        "Link": "https://www.linkedin.com/services/page/7142403115320a0782/",
        "Descrição": "Implementei um bot de consulta no aplicativo Telegram para fornecer suporte automatizado aos clientes. O bot é capaz de responder a consultas comuns dos clientes, fornecer informações sobre produtos e serviços, e encaminhar questões mais complexas para a equipe apropriada.",
        "Imagem": "bot.png",
        "Video": None
    },
    "Extração de Dados de PDF": {
        "Link": "https://www.linkedin.com/services/page/7142403115320a0782/",
        "Descrição": "Desenvolvi um sistema de extração de dados de arquivos PDF para automatizar o processo de coleta e análise de informações. Este sistema é capaz de extrair dados estruturados de documentos PDF, melhorando a eficiência e precisão na manipulação de grandes volumes de dados.",
        "Imagem": None,
        "Video": "https://www.youtube.com/watch?v=olP0nzFenkU"
    },
    "WebApp de Oficina Mecânica": {
        "Link": "https://www.linkedin.com/services/page/7142403115320a0782/",
        "Descrição": "Desenvolvi um WebApp para uma oficina mecânica, que permite o cadastro de clientes, busca desses clientes, e cadastro e busca de peças no estoque. Este WebApp otimiza os processos internos da oficina, proporcionando uma gestão eficiente de clientes e estoque de peças.",
        "Imagem": None,
        "Video":"https://www.youtube.com/watch?v=81edukb3RDc"
    },
    "WebApp Construído com Flutterflow": {
        "Link": "https://www.linkedin.com/services/page/7142403115320a0782/",
        "Descrição": "Utilizando a plataforma Flutterflow, desenvolvi um WebApp para oferecer uma experiência intuitiva aos usuários. Este WebApp oferece facilidade de compartilhar links importantes seu e do seu negocio.",
        "Imagem": "webapp.png",
        "Video": None
    }
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
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
    img = st.image(whatsapp_image_url,width=20) 
    wpp = st.markdown(f'[Me envie uma mensagem no WhatsApp](https://api.whatsapp.com/send?phone={whatsapp_number})', unsafe_allow_html=True)
    st.write("📫", EMAIL)
    # --- Botão de Download para o PDF ---
   
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
st.subheader("Experiencia & Qulificação")
st.write(
    """
- ✔️ 3 anos de experiência com extração e transformação de dados em bancos : SQL, Oracle.

- ✔️ 3 anos trabalhando com Power bi e Power automate.

- ✔️ 5 anos trabalhando com Python e Excel

- ✔️ Bom entendimento dos princípios estatísticos e suas respectivas aplicações

- ✔️ Excelente trabalho em equipe e demonstração de forte senso de iniciativa em tarefas
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA, DAX
- 📊 Visualização: PowerBi, MS Excel, Plotly
- 🗄️ Databases: Postgres, MongoDB, MySQL,Oracle
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Trabalho")
st.write("---")

# --- JOB 1
st.write("🚧", "**Consultor na TIM **")
st.write("01/2021 - Presente")
st.write(
    """
- ► Utilizei o PowerBI e SQL para redefinir e monitorar KPIs relacionados a rede de telecomunicações, fornecendo dados para maximizar o tratamento da rede de acesso.

- ► Redesenhei junto com time de especialistas o modo de visualização e tratamento de dados na area de operações.

- ► Ajudei na automação de ingestão de dados atraves de API , fornecimento de dados atraves de Paineis e Power automate
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Alguns Projetos e Desenvolvimentos")
st.write("---")
for project, details in PROJECTS.items():
    st.write(f"{project}:")
    st.write(f"  - Descrição: {details['Descrição']}")
    if details['Imagem']:
        st.image(details['Imagem'], width=600)
    if details['Video']:
        st.video(details['Video'])
    st.write(f"  - Link: {details['Link']}")
   
