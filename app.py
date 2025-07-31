import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint 
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-1.5-flash',temperature=0)



#set app to wide mode
st.set_page_config(layout="wide")

#Title of your app
st.title('BlogCraft: Your AI Writing Companion')

#create a subheader
st.subheader("Now you can craft perfect blogs with the help of AI- BlogCraft is your new AI Blog Companion")

#sidebar for user input
with st.sidebar:
    st.title("Input Your Blog Details")
    st.subheader("Enter Details of the Blog you want to generate")
   

    #Blog Title
    blog_title=st.text_input("Blog Title")

    #Keywords Input
    keywords=st.text_area("Keywords (comma-separated)")

    #No. of words
    num_words=st.slider("Number of Words",min_value=250, max_value=1000,step=250)

   
    #submit button
    submit_button=st.button("Generate Blog")

prompt=PromptTemplate(
    input_variables=['blog_title','keywords','num_words'],
    template="""
    Generate a comprehensive, engaging blog post relevant to the given title {blog_title} 
    and keyword {keywords}. Make sure to incorporate these keywords in the blog post. The blog should 
    be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, 
    informative and maintains a consistent tone throughout.
    """
)
    
chain = prompt|model
result=chain.invoke({'blog_title': blog_title,'keywords':keywords,'num_words': num_words })

if submit_button:
    st.write("Your Blog Post")
    st.write(result.content)