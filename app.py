import streamlit as st 
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit.components.v1 import html
import webbrowser
from streamlit import config as st_config

st.set_page_config(page_title = "Sumeet Mehra's Personal Portfolio Website", page_icon = ":grinning_cat:", layout = "wide")


def load_url_lottie(url):
    r = requests.get(url)
    if(r.status_code!=200):
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("styles/style.css")


#Assets load
coding_anim = load_url_lottie("https://lottie.host/b8e27ffb-273c-42b0-86b0-46d719573437/SCiamXKBYT.json")
img_niti1 = Image.open("images/img1 copy.jpg")
img_niti2 = Image.open("images/img3 copy.png")
img_niti3 = Image.open("images/img4 copy.png")
img_niti4 = Image.open("images/img5 copy.png")

# Header:
st.subheader("Hi, I'm Sumeet. :wave:")
st.title("Frontend Developer | CS Junior @ IIIT Delhi")
st.write("I am an upcoming Junior at IIIT Delhi studying Computer Science and Social Sciences. I am deeply invested in working around Front-end dev related techstacks and making new and innovative websites. When i'm not coding, im deeply passionate about Wildlife Photography. I love participating in hackathons and projects with other people. Feel free to reach out if you want to collaborate on the same!")
# st.write("[My Resume :)](https://drive.google.com/file/d/1erdhQhne7pBWKkrvPvs6F-Mdpl_HB1i4/view?usp=sharing)")

# Previous Experiences:
with st.container():
    st.write("---------------------------------------------------------------------------------------------------")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Previous experiences: ")
        st.write("Intern at NITI Aayog, Govt. of India              May, 2023 - June, 2023")
        st.write("Worked under Dr. Amit Verma, Director, NITI Aayog in the Economics Vertical")
        st.write(
            """
            1. 📈 Delved into analysis of Economic Indicators like WPI, CPI, Exchange Rate, etc (worked on a total of 18 indicators) by importing datasets and tried to visualise these datasets in the form of Graphs, Choropleths and Heatmaps (using python libraries like plotly) to uncover valuable trends and patterns to get a deeper understanding of the Indian Economic Landscape.

            2. 🌐 Developed and deployed an interactive website in order to meticulously present and analyse the data. Techstack : Django, Python, HTML, CSS
            (https://lnkd.in/dy3Z9jKz)

            3. 💻 Also worked on a web scraper using Selenium which automates data updation and provides the latest visualisations and analysis of the economy.
            """
        )
        st.write("[Repository](https://github.com/sumeet21428/graphgen)")
        st.write("[Internship Completion Certificate](https://drive.google.com/file/d/1H2XH6buTgdxlBSsjGgTLPP6P-p-1weCG/view)")
        
    with right_column:
        st_lottie(coding_anim, height = 600, key = "coding")
        
st.write("")
st.write("")
        
# Projects: 
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        
        st.image(img_niti4)
        
        st.markdown(
        """
        <style>
        div[data-baseweb="button"] button {
            background-color: violet !important;
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
        
    with text_column:
        st.subheader("Interactive Portal for Economic Data (Web Developement)")
        st.write(
            """
            Created a website using Django where we compiled various Visualisations on Indian economic data using Python and provided a Detailed analysis.
            Also made a web scraper using selenium which updates the data at regular Intervals of time and hence makes the visualizations update in real time.
            Techstack: Django, Python, Selenium, HTML, CSS
            """
        )
        st.markdown("Repository [here](https://github.com/sumeet21428/graphgen)")
        
st.write("")
st.write("")
        
#Project 2
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        if st.button("Open GitHub Repository"):
                webbrowser.open_new_tab("https://github.com/sumeet21428/DBMS-Project")
    with text_column:
        st.subheader("Database App for Dairy store")
        st.write(
            """
            Developed and designed an e2e DB application for a dairy company which will be used for var- ious purposes including but not limited to inventory management,serializing and categorizing products and managing the company sales dynamically.
            Techstack - mySql, Python, Django
            """
        )
        
#Project 3
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        if st.button("Open GitHub Repo"):
                webbrowser.open_new_tab("https://github.com/sumeet21428/Tank-Stars-AP-Project-")
    with text_column:
        st.subheader("Clone for “Tank Stars” Game")
        st.write(
            """
            A clone of Android game-Tank Stars, made for Desktop using concepts of Object-Oriented Programming. 
            Techstack - Java, LibGDX, Figma.
            """
        )
        
        
#Project 4
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        if st.button("Open Github Repository"):
                webbrowser.open_new_tab("https://github.com/me-tusharchandra/CO-Project")
    with text_column:
        st.subheader("Assembly Language Simulator")
        st.write(
            """
            Developed an assembly language simulator that allows users to input assembly code and simulate its execution, including support for basic instruction sets and memory management
            """
        )
        
st.write("")
st.write("")
        
        
#Wildlife Photography
with st.container():
        st.subheader("""My Other Side\n
                    """)
        st.write("[Check out my work on Wildlife Photography!](https://www.instagram.com/sumitmehraphotography/)")
        num_rows = 4
        num_cols = 4
        
        for row in range(num_rows):
            image_row = st.columns(num_cols)
            
            for col in range(num_cols):
                image_number = row * num_cols + col + 1
                if image_number == 1:
                    image = "images/767A3370 copy.JPG"  
                elif image_number == 2:
                    image = "images/767A7505 copy.JPG"
                elif image_number == 3:
                    image = "images/767A8660 3 - Sumeet Mehra copy.JPEG"
                elif image_number == 4:
                    image = "images/308061462_1270734610340282_9177978074739654715_n copy.jpg"
                elif image_number == 5:
                    image = "images/Little Egret copy.JPG"
                elif image_number == 6:
                    image = "images/Brown Stonechat copy.JPG"
                elif image_number == 7:
                    image = "images/Common Kingfisher copy.JPG"
                elif image_number == 8:
                    image = "images/Eurasion Collared Dove_Lodhi Garden copy.JPG"
                elif image_number == 9:
                    image = "images/Wire-tailed Swallow_Bharatpur Bird Sanctuary copy.JPG"
                elif image_number == 10:
                    image = "images/Tiger_Corbett(1) copy.JPG"
                elif image_number == 11:
                    image = "images/Rainbow Bee-Eater_Sultanpur 2 copy.jpg"
                elif image_number == 12:
                    image = "images/Peacock copy.jpg"
                elif image_number == 13:
                    image = "images/Long-Tailed Shrike copy.jpg"
                elif image_number == 14:
                    
                    image = "images/IMG_9251 copy.jpg"
                elif image_number == 15:
                    image = "images/White Ibis copy.JPG"
                elif image_number == 16:
                    image = "images/Spotted Owlet copy.JPG"
                
                with image_row[col]:
                    st.image(image, use_column_width=True,)

st.write("")
st.write("")
st.write("")
st.write("")

#Contact me page
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/ba273f919a5ef4d244febef42c1d0ddb" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name: " required>
        <input type="email" name="email" placeholder="Your email: " required>
        <textarea name="message" placeholder="Your message here: " required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()