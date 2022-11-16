import requests
import streamlit as st
import streamlit_nested_layout
from streamlit_lottie import st_lottie
from PIL import Image
import os
import base64


@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


@st.cache(allow_output_mutation=True)
def get_img_with_href(local_img_path, target_url):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}" style="margin-left: 70px">
            <img style="height: 20px" src="data:image/{img_format};base64,{bin_str}" />
        </a>'''
    return html_code


st.set_page_config(page_title='My Bio', page_icon=':simple_smile:', layout='wide')


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_vDd5lrv57P.json')
fb_html = get_img_with_href('facebook.png', 'https://www.facebook.com/100006426110039')
git_html = get_img_with_href('github-logo.png', 'https://github.com/jindambhavaniprasad')
insta_html = get_img_with_href('instagram.png', 'https://www.instagram.com/bhavani_prasad_jindam/')
linkedIn_html = get_img_with_href('linkedin.png', 'https://www.linkedin.com/in/bhavani-prasad-05a1b320a/')
twitter_html = get_img_with_href('twitter.png', 'https://twitter.com/J_BhavaniPrasad')

padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)
with st.container():
    st.subheader('Hi I am Bhavani Prasad :wave:')
    st.title('Full Stack Developer and AI Engineer')
    st.write("A learner who is passionate to grow in ever growing Artificial Intelligence and have good knowledge on "
             "all phases of application development .Developed web applications using React JS and OS based "
             "applications usi ng react-native. Constantly learning and improving skills on Python and Machine "
             "Learning. Have hands on experience on building APIs from scratch and excellent skills on spring-boot "
             "microservices.")

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('What I do')
        st.write(" - Loves to code for fun (and money :wink:)")
        st.write(" - Enthusiastic who loves to explore new technologies and opportunities")
        st.write("- Learning and building my future towards becoming a data scientist.")
        st.write(" - Some of the skills and technologies I have hands on experience on:")
        ll_column, lr_column = st.columns(2)
        with ll_column:
            st.markdown(" :small_blue_diamond: React JS", 123)
            st.markdown(" :small_blue_diamond: Node JS")
            st.markdown(" :small_blue_diamond: Python*")
            st.markdown(" :small_blue_diamond: Machine Learning*")
        with lr_column:
            st.markdown(" :small_blue_diamond: SQL/MYSQL/Mongo DB")
            st.markdown(" :small_blue_diamond: React Native/Expo CLI")
            st.markdown(" :small_blue_diamond: Jenkins/PCF")
            st.markdown(" :small_blue_diamond: Java/Spring-Boot")
    with right_column:
        st.write('##')
        st.write('##')
        st_lottie(lottie_coding, height=300, key='lottie_coding')

with st.container():
    st.write('---')
    st.header(':computer: My Experience')
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader('TDCX - Nov 2022 - Present')
        st.write(" - Working as a full stack developer for developing web-based applications and Express API’s.")
        st.write(" - Worked on a hiring application based on React and Node JS.")
        st.write("- Developed and designed a Survey web application which includes sending out emails to users and "
                 "collect, analyze data")
        st.write(" - Worked on famous libraries Material UI, Bootstrap, React JS, Express JS, Sequelize and antd")
    with right_column:
        st.subheader('Capgemini - Jun 2019 - Nov 2021')
        st.write(" - Worked as a full stack developer for Synchrony client which is an American bank. Developed web "
                 "modules and react js applications from scratch. Actively participated in design discussions and "
                 "solving architectural problems.")
        st.write(" - Wrote stored procedures in SQL and MYSQL and know how to integrate them in Restful API’s.")
        st.write("- Fixed production bugs and have a good knowledge on Cloud Foundry and deployment of web "
                 "applications "
                 "and RestFul API’s.")
        st.write(" - Designed and Developed responsive web applications using bootstrap and thymeleaf.")
        st.write(" - Actively participated in release activities and have good knowledge on linux commands, putty tool "
                 "and maintenance.")

with st.container():
    st.write('---')
    st.header(':globe_with_meridians: Some of my Personal projects')

    st.subheader(' 1. Memories Lite')
    st.markdown(' - Github URL :- https://github.com/jindambhavaniprasad/memories-app')
    st.markdown(' - App URL :- https://memories-lite.netlify.app/')
    st.markdown(' - This is a MERN stack application in which a user can add a memory and like or delete them.')
    st.markdown(' - It uses JWT authentication and bcrypt algorithm to encrypt user data.')

    st.subheader(' 2. Test Taker - A demo coding app')
    st.markdown(' - Github URL :- https://github.com/jindambhavaniprasad/demo-test-taker')
    st.markdown(' - App URL :- https://demo-test-taker.netlify.app')
    st.markdown(' - This is a Coding test application built using React JS and Material UI')
    st.markdown(' - It uses Judge 0 Compiler API for running test cases')

    st.subheader(' 3. Hyderabad-Flavours')
    st.markdown(' - Github URL :- https://github.com/jindambhavaniprasad/Hyderabad-Flavours')
    st.markdown(' - App URL :- https://hyderabad-flavours.netlify.app/')
    st.markdown('- This is a React JS restaurant application in which a user can order a food item and view past '
                'orders.')
    st.markdown(' - It uses google firestore to store user data.')

    st.subheader(' 4. Quiz Lite')
    st.markdown(' - Github URL :- https://github.com/jindambhavaniprasad/quiz-app')
    st.markdown(' - App URL :- https://quiz-demo-cf574.web.app')
    st.markdown('- This is a React JS application which will allow the user to take a simple quiz on a category of '
                'his choice.')
    st.markdown(' - It uses google firestore to store user data.')

    st.subheader(' 5. Weatherio')
    st.markdown(' - Github URL :- https://github.com/jindambhavaniprasad/weatherio')
    st.markdown('- This is a React Native android application in which will be able to view Weather details and works '
                'on GPS.')
    st.markdown(' - A simple and elegant design in which user can choose his own metric system.')

    st.subheader(' 5. Todo List')
    st.markdown(' - Github URL :- https://github.com/jindambhavaniprasad/TodoList')
    st.markdown('- This is a React Native android application in which will be able to add a task and delete them '
                'upon completion.')
    st.markdown(' - It is built using Expo CLI which allows developer to build cross-platform applications.')

    st.subheader('Other Projects')
    st.markdown('- A demo payment application which has a simple design for hassle free payments for a user built '
                'using React Js and Node JS.')
    st.markdown('- A tool which will have all utility functions and frequently used links by our team built using '
                'React Js, Redux.')

with st.container():
    st.write('---')
    st.header(':mortar_board: Education')
    st.markdown('Bachelor of Technology, EEE in BVRIT (2015 - 2019)')

with st.container():
    st.write('---')
    st.header('Connect with me')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown(fb_html, unsafe_allow_html=True)
    with col2:
        st.markdown(git_html, unsafe_allow_html=True)
    with col3:
        st.markdown(insta_html, unsafe_allow_html=True)
    with col4:
        st.markdown(linkedIn_html, unsafe_allow_html=True)
    with col5:
        st.markdown(twitter_html, unsafe_allow_html=True)
