import streamlit as st
import time
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
st.set_page_config(
    page_title="Amazon Review Analyzer",
    page_icon="🛒",
    layout="centered"
)
col1, col2, col3 = st.columns([2,1,2])

with col2:
    st.image("Assets/image.png", width=180)
st.bgcolor='red'
st.markdown(
    """
    <h1 style="text-align:center;">Amazon Review Analyzer</h1>
    <p style="text-align:center;color:gray;">
        Analyze thousands of reviews using AI
    </p>
    """,
    unsafe_allow_html=True,
)
url=st.text_input("Entre the Link of the product 🔗 ")
from dotenv import load_dotenv
load_dotenv()
from Webscrapping import ReviewExtractor
if st.button("Analyze"):
    if url:
        with st.spinner("Scrapping Data"):
            scraper = ReviewExtractor(url)
            time.sleep(2)
        image_url,data = scraper.scrap()
        st.write("image")
        st.markdown("""
            <style>

            .stApp{
                background:#000000;
            }

            .product-card{
                background:white;
                padding:20px;
                border-radius:15px;
                box-shadow:0px 4px 4px rgba(0,0,0,0.1);
                text-align:center;
            }

            </style>
            """, unsafe_allow_html=True)
        st.markdown(f"""
            <div class="product-card">
                <img src="{image_url}" width="250">
            </div>
            """, unsafe_allow_html=True)

        
        llm=HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct",
        )
        model=ChatHuggingFace(llm=llm)
        prompt=(f"{data}, this is the review and the data of the prduct send me the 5-6 summary of the product and  recomment me should i buy it or not")
        
        with st.spinner("Generating Summary"):
            res=model.invoke(prompt)
            time.sleep(2)
        st.write(res.content)


