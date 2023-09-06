import streamlit as st
# import sys
# sys.path.insert(1, "C:\\Users\\asmaitha\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\streamlit_option_menu")  
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(layout="wide")

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("C:\\Users\\asmaitha\\Desktop\\Streamlit\\style\\style.css")
lottie_coder = load_lottie("https://lottie.host/0f41c61e-5c21-4b51-9e15-61014cec13f3/qslPiCmPpo.json")
lottie_contact = load_lottie("https://lottie.host/0eb0e22a-f761-4ad1-94f8-ef8706b5430f/CQ2nk4hnR2.json")
image = Image.open("C:\\Users\\asmaitha\\Desktop\\Streamlit\\Image\\insurance.jpg")
image1 = Image.open("C:\\Users\\asmaitha\\Desktop\\Streamlit\\Image\\Image_forge.png")
image2 = Image.open("C:\\Users\\asmaitha\\Desktop\\Streamlit\\Image\\port_folio.png")
# image = image.resize((100,50))
# desired_height = 400
# desired_width = None
# original_width, original_height = image.size
# aspect_ratio = original_width / original_height
# # desired_width = int(desired_height * aspect_ratio)
# if desired_width is None:
#     desired_width = int(desired_height * aspect_ratio)
# image = image.resize((desired_width, desired_height))
resized_image = image.resize((int(image.width * 0.3), int(image.height * 0.2)))
resized_image_1 = image1.resize((int(image.width * 0.3), int(image.height * 0.2)))
resized_image_2 = image2.resize((int(image.width * 0.3), int(image.height * 0.2)))
width = 300
height = 300



st.write("##")
st.subheader("Hello :wave:")
# st.title("My Portfolio Website")
st.markdown("<p style='font-size:50px;font-weight:bold;'> My <span style='color: #ff471a'> Portfolio </span> Website </p>",unsafe_allow_html=True)
# st.markdown("<p><span style='color:##ff0350'> Welcome to my portfolio, a showcase of my skills and experiences. Explore my work to see how I can make a valuable contribution to your team.</span></p>",unsafe_allow_html=True)
st.markdown("<p style='font-size:25px;font-family: Georgia, serif;'>Welcome to my portfolio, a showcase of my skills and experiences. Explore my work to see how I can make a valuable contribution to your team.</p>",unsafe_allow_html=True)
# st.write("""
# Welcome to my portfolio, a showcase of my skills and experiences. Explore my work to see how I can make a valuable contribution to your team.
#          """)
st.write("---")


with st.container():
    selected = option_menu (
        menu_title = None,
        options = ['About','Projects','Contact'],
        icons = ['person','code-slash','chat-right'],
        orientation = 'horizontal'
    )

custom_css = """
<style>
    .custom-text {
        font-family: Times New Roman, Times, serif;
        font-size: 20px; 
    }
</style>
"""
st.markdown(custom_css,unsafe_allow_html=True)

if selected == 'About':

    # with st.container():
    col1,col2 = st.columns([2,0.5])
    with col1:
        st.write("##")
        # st.title("My name is Asharani M G")
        st.markdown("<p style='font-size:40px;font-family: Times New Roman, Times, serif;'> My name is <span style='color: #ff471a;font-weight:bold;'> Asharani M G </span></p>",unsafe_allow_html=True)
        # st.subheader("BE Graduate")
        st.markdown("""<p style='font-size:22px;font-family: Georgia, serif;text-align: justify;'>I am a recent graduate with a Bachelor's degree in Information Science and Engineering from Sapthagiri college of Engineering.
                     Passionate about engineering and technology, I am excited to embark on a career that allows me to apply my knowledge and skills to real-world challenges.
                     As an engineer, I am driven by the desire to innovate and make a positive impact on society through my work.</p>""",unsafe_allow_html=True)
        # st.markdown("<p style='font-size:22px;font-family: Georgia, serif;'></p>",unsafe_allow_html=True)
    with col2:
        st.lottie(lottie_coder,width=width,height=height)
        # with st.echo():
        #     st_lottie("https://lottie.host/0f41c61e-5c21-4b51-9e15-61014cec13f3/qslPiCmPpo.json")

    st.write("------")

    col3,col4 = st.columns(2)
    with col3:
#         st.subheader("""
#         Education
#         - Sapthagiri college of Engineering
#             - Bachelor of Engineering -Information Science
#             - Cgpa -8.77
# """)
        st.markdown("<h1 style='font-size:30px;font-family: Times New Roman, Times, serif;'>Education</h1>",unsafe_allow_html=True)
        st.markdown("""
                    - <span class="custom-text">**Sapthagiri College of Engineering**</span>
                        - <span class="custom-text">Bachelor of Engineering - Information Science</span>
                        - <span class="custom-text">2019 - 2023</span>
                        - <span class="custom-text">Cgpa - 8.77</span>
                    - <span class="custom-text">**Jnana Bharathi PU College**</span>
                        - <span class="custom-text">PCMB</span>
                        - <span class="custom-text">2019</span>
                        - <span class="custom-text">95.16%</span>
                    - <span class="custom-text">**Jnana Bharathi English High School**</span>
                        - <span class="custom-text">SSLC</span>
                        - <span class="custom-text">2017</span>
                        - <span class="custom-text">97.12%</span>
                    """,unsafe_allow_html=True)
    with col4:
        st.markdown("<h1 style='font-size:30px;font-family: Times New Roman, Times, serif;'>Skills</h1>",unsafe_allow_html=True)
        st.markdown("""
                    - <span class="custom-text">Python</span>
                    - <span class="custom-text">Java</span>
                    - <span class="custom-text">HTML</span>
                    - <span class="custom-text">CSS</span>
                    - <span class="custom-text">SQL</span>
                    - <span class="custom-text">Git</span>
                    - <span class="custom-text">Github</span>
                    - <span class="custom-text">Gitlab</span>
                    - <span class="custom-text">MongoDB</span>
                    - <span class="custom-text">Jenkins</span>
                    - <span class="custom-text">Bitbucket</span>
                    - <span class="custom-text">Streamlit</span>
                    - <span class="custom-text">AWS</span>
                    """,unsafe_allow_html=True)
    
    st.markdown("<h1 style='font-size:30px;font-family: Times New Roman, Times, serif;'>Experience</h1>",unsafe_allow_html=True)
    st.markdown("""
                - <span class="custom-text">**Software Developer Intern**</span><br>
                    <span class="custom-text">*Asmaitha Wireless Technology Pvt. Ltd., Bengaluru, Karnataka.*</span><br>
                    <span class="custom-text">04/2023 - Present</span>
                    - <span class="custom-text">As a software developer intern, my role is to contribute to the creation, enhancement, and maintenance of software applications.</span>
                    - <span class="custom-text">My responsibilities include writing clean and efficient code, troubleshooting issues, and ensuring optimal performance and scalability.</span>
                    - <span class="custom-text">I am working with DevOps team and contributed to the development and maintenance of CI/CD pipelines using Jenkins, Bitbucket facilitating
                    automated building, testing, and deployment of applications.</span>
                    - <span class="custom-text"> Supported version control processes using Git, including branching, merging, and resolving conflicts, to facilitate smooth collaboration among developers.</span>
                    - <span class="custom-text">I actively stay updated with industry trends and technologies to bring innovative ideas to the table and continuously improve the software development process.</span>
                """,unsafe_allow_html=True)
    st.markdown("""
                - <span class="custom-text">**Machine Learning Internship**</span><br>
                    <span class="custom-text">*Karunadu Technologies, Bengaluru, Karnataka.*</span><br>
                    <span class="custom-text">08/2022 - 09/2022</span>
                    - <span class="custom-text">As a part of the internship program, I was asked to develop a “HEART FAILURE PREDICTION”.</span>
                    - <span class="custom-text">The dataset contains 11 features that are passed into a machine learning model to predict predict a possible heart disease.</span>
                    - <span class="custom-text"> The output displayed is whether that person is normal or have a heart disease based on the inputs given.</span>
                    - <span class="custom-text">Link to the project - https://github.com/ASHARANI-MG/HeartFailure-Prediction</span>
                """,unsafe_allow_html=True)
    st.markdown("""
                - <span class="custom-text">**Full Stck Web Development Internship**</span><br>
                    <span class="custom-text">*Compsoft Technologies, Bengaluru, Karnataka.*</span><br>
                    <span class="custom-text">05/2022 - 06/2022</span>
                    - <span class="custom-text">As a part of the internship program, I was asked to develop a “STUDENT RESULT MANAGEMENT SYSTEM”.</span>
                    - <span class="custom-text">In the website we designed, the admin can login and add the data for the respective student, namely their USN, marks, semester.</span>
                    - <span class="custom-text">Later, this information can be fetched by the student once he or she enters the USN and semester.</span>
                    - <span class="custom-text">The website is designed using CSS and HTML as the frontend languages, along with the supported framework Bootstrapv5.2</span>
                    - <span class="custom-text">The database used was MySQL server5.5. PHP5 was the backend.</span>
                    - <span class="custom-text">Link to the project - https://github.com/ASHARANI-MG/Student-result-management-system</span>
                """,unsafe_allow_html=True)
    
if selected == "Projects":
    st.markdown("<h1 style='font-size:30px;font-family: Times New Roman, Times, serif;'>My Projects</h1>",unsafe_allow_html=True)
    st.write("##")
    col5,col6 = st.columns([1,2])
    with col5:
        st.image(resized_image,caption="Insurance Cost Prediction")
        st.write("##")
        st.image(resized_image_1,caption="Image Forgery Detection")
        st.image(resized_image_2,caption="My Portfolio Website")
    with col6:
        st.subheader("Insurance Cost Prediction")
        st.markdown("""
                    - <span class="custom-text">A Machine Learning project where the details about the person is given as inputs and the output displayed is how much amount will that person get by insurance.</span>
                    - <span class="custom-text">Project link- https://github.com/ASHARANI-MG/InsuranceCost-Prediction</span>
                """,unsafe_allow_html=True)
        st.write("##")
        st.subheader("Image Forgery Detection using CNN")
        st.markdown("""
                    - <span class="custom-text">Developed a CNN-based system to detect and identify forged or manipulated regions within digital images.</span>
                    - <span class="custom-text">Implemented a deep learning architecture using Convolutional Neural Networks (CNNs) to analyse image features and classify regions as authentic or forged.</span>
                    - <span class="custom-text">Implemented the project using Python and utilized popular deep learning libraries.</span>
                """,unsafe_allow_html=True)
        # st.write("##")
        st.write("##")
        st.subheader("Portfolio Website")
        st.markdown("""
                    - <span class="custom-text">Created a frontend of Portfolio website using languages like HTML and CSS.</span>
                    - <span class="custom-text">Project Link - https://github.com/ASHARANI-MG/Portfolio</span>
            """,unsafe_allow_html=True)
        
if selected == "Contact":
    st.subheader("Get in touch!")
    st.write("##")
    st.write("##")

    contact_form = """
        <form action="https://formsubmit.co/ashaa12gowda@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message" required></textarea>
        <button type="submit">Send</button>
        </form>
    """

    left_col,right_col = st.columns((2,1))
    with left_col:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_col:
        st_lottie(lottie_contact,height=300)