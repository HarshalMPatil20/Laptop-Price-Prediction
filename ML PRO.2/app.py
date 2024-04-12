import streamlit as st
import pickle
import numpy as np
import base64
import streamlit as st
import pickle
from st_social_media_links import SocialMediaIcons




with open("style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.markdown(
        """
        <style>
@font-face {
  font-family: 'nasalization-rg';
  font-style: normal;
  font-weight: 400;
  src: url(nasalization-rg.ttf) format('truetype');
 }

    html, body, [class*="css"]  {
    font-family: 'nasalization-rg';
    }
    </style>

    """,
        unsafe_allow_html=True,
    )

# Function to set background image for the entire app
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image
add_bg_from_local('wall.jpg')

# ... (rest of your code)

# Function to set background image for the sidebar
def add_bg_to_sidebar(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .sidebar .sidebar-content {{
            background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_to_sidebar('Login_bg.jpg')    



 

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))

file='df.pkl'
df = pickle.load(open(file,'rb'))

st.title('_Laptop price Predictor_')

def convert_boolean_to_custom_input(boolean_input):
  if boolean_input:
    return 'Yes'
  else:
    return 'No'

# brand
company = st.selectbox('#### Brand',df['Company'].unique(),index=None)
st.write('You selected:', company)

# type of laptop
type = st.selectbox('#### Type',df['TypeName'].unique(),index=None)
st.write('You selected:', type)

# Ram
ram = st.selectbox('#### RAM(in GB)',[2,4,6,8,12,16,24,32,64],index=None)
st.write('You selected:', ram)

# weight
weight = st.selectbox('#### Weight',df['Weight'].unique(),index=None)
st.write('You selected:', weight)

# Touchscreen

Touchscreen = st.checkbox('### Touchscreen')
touchscreen = convert_boolean_to_custom_input(Touchscreen)
st.write('You selected:', touchscreen)

# IPS
Ips = st.checkbox('### IPS')
ips = convert_boolean_to_custom_input(Ips)
st.write('You selected:', ips)

# screen size
screen_size = st.selectbox('#### Screen Size',[11.6,12,13.3,14,15.6,16,17],index=None)
st.write('You selected:', screen_size)

# resolution
resolution = st.selectbox('#### Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'],index=None)
st.write('You selected:', resolution)

#cpu
cpu = st.selectbox('#### CPU',df['Cpu brand'].unique() , index=None)
st.write('You selected:', cpu)

hdd = st.selectbox('#### HDD(in GB)',[0,128,256,512,1024,2048],index=None)
st.write('You selected:', hdd)

ssd = st.selectbox('#### SSD(in GB)',[0,8,128,256,512,1024],index=None)
st.write('You selected:', ssd)

gpu = st.selectbox('#### GPU',df['Gpu brand'].unique(),index=None)
st.write('You selected:', gpu)

os = st.selectbox('#### OS',df['os'].unique(),index=None)
st.write('You selected:', os)

if st.button('#### Predict Price'):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

    query = query.reshape(1,12)
    st.title("The predicted price of this configuration is " )
    st.title( "₹" + str(int(np.exp(pipe.predict(query)[0]))))

st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    img {
  display: block;
  width=500;
  margin: 0 auto;
  border-radius: 60%;
}
    </style>

    """,
    unsafe_allow_html=True
)

tab1, tab2, tab3 = st.tabs(["Info"])

with tab1:
   st.header("What Factors Affect Laptop Computer Prices?")
   st.write("Several different factors can affect laptop computer prices. These factors include the brand of computer and the number of options and add-ons included in the computer package. In addition, the amount of memory and the speed of the processor can also affect pricing. Though less common, some consumers spend additional money to purchase a computer based on the overall “look” and design of the system. In many cases, name brand computers are more expensive than generic versions. This price increase often has more to do with name recognition than any actual superiority of the product. One major difference between name brand and generic systems is that in most cases, name brand computers offer better warranties than generic versions. Having the option of returning a computer that is malfunctioning is often enough of an incentive to encourage many consumers to spend more money. Functionality is an important factor in determining laptop computer prices. A computer with more memory often performs better for a longer time than a computer with less memory. In addition, hard drive space is also crucial, and the size of the hard drive usually affects pricing. Many consumers may also look for digital video drivers and other types of recording devices that may affect the laptop computer prices. Most computers come with some software pre-installed. In most cases, the more software that is installed on a computer, the more expensive it is. This is especially true if the installed programs are from well-established and recognizable software publishers. Those considering purchasing a new laptop computer should be aware that many of the pre-installed programs may be trial versions only, and will expire within a certain time period. In order to keep the programs, a code will need to be purchased, and then a permanent version of the software can be downloaded. -Many consumers who are purchasing a new computer are buying an entire package. In addition to the computer itself, these systems typically include a monitor, keyboard, and mouse. Some packages may even include a printer or digital camera. The number of extras included in a computer package usually affects laptop computer prices. Some industry leaders in computer manufacturing make it a selling point to offer computers in sleek styling and in a variety of colors. They may also offer unusual or contemporary system design. Though this is less important to many consumers, for those who do value “looks,” this type of system may be well worth the extra cost.")


with st.sidebar:
    st.sidebar.image("Author1.png",  width="50%",use_column_width=True)
    st.markdown("<h1 style='text-align: center;'>Harshal Patil</h1>", unsafe_allow_html=True)
    social_media_links = [
    "discordapp.com/user/530693021193469973",
    "https://www.instagram.com/ll_harshal_patil_ll?igsh=OGhndmNwbjVuNHJq",
    "https://github.com/HarshalMPatil20",
    "https://www.linkedin.com/in/harshal-patil-87626022a"
    ]

    social_media_icons = SocialMediaIcons(social_media_links)

    social_media_icons.render()
    
    

    
    with open('Login_bg.jpg', "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .sidebar .sidebar-content {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        width: 375px;
        
    }}

     
    </style>
    """,
    unsafe_allow_html=True    
   
    )




