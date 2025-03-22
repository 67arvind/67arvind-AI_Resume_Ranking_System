# Importing the Streamlit library and giving it an alias 'st' for building web apps
import streamlit as st 

# Importing the PdfReader class from the PyPDF2 library to read PDF files
from PyPDF2 import PdfReader  

# Importing the pandas library and giving it an alias 'pd' for data manipulation and analysis
import pandas as pd  
import datetime  # Import datetime module to get the current year

# Importing the TfidfVectorizer class from scikit-learn for transforming text data into TF-IDF feature vectors
from sklearn.feature_extraction.text import TfidfVectorizer  

# Importing the cosine_similarity function from scikit-learn for computing the cosine similarity between feature vectors
from sklearn.metrics.pairwise import cosine_similarity  

from pptx import Presentation   


# Function to extract text from PDF
def extract_text_from_pdf(file): # Define a function that takes the file path as input
    pdf = PdfReader(file)  # Create a PdfReader object
    text = "" # Initialize an empty string to store the extracted text
    for page in pdf.pages: # Iterate through each page of the PDF file
        text += page.extract_text() # Extract text from the current page and append it to the 'text' string
    return text # Return the extracted text



# Function to rank resumes based on job description
def rank_resumes(job_description, resumes): # Define a function that takes the job description and resumes as input
    # Combine job description with resumes with resumes
    
    documents = [job_description] + resumes # Combine the job description with resumes
    vectorizer = TfidfVectorizer().fit_transform(documents) # Create a TF-IDF Vectorizer object and transform the documents into feature vectors
    vectors = vectorizer.toarray()

    # Calculate cosine similarity
    job_description_vector = vectors[0] # Get the feature vector of the job description
    
    # Get the feature vectors of the resumes
    resume_vectors = vectors [1:]
    
    # Compute the cosine similarity between the job description and resumes
    cosine_similarities = cosine_similarity ([job_description_vector], resume_vectors).flatten() 
    
    
    return cosine_similarities # Return the cosine similarities
#================================Design Section================================
# Set the page configuration, including a favicon
st.set_page_config(
    page_title="AI Resume Screening",  # Title of the browser tab
    page_icon="📝",  # Favicon: use an emoji or a file path to an icon
    #layout="wide"    # Optional: sets the app layout to "wide"
)


# Footer Section

current_year = datetime.datetime.now().year  # Get the current year dynamically
st.markdown(
    f"""
    <style>
    footer {{
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: gray transparent;
        text-align: center;
        padding: 10px 0;
        font-size: 12px;
        color: gray;
        margin-top: 50px;

    }}
    </style>
    <footer>
        Copyright ©{current_year} All rights reserved | Don't forget to give feedback ❤️<br>
        Made by <b>Arvind_67</b> & <b>NRZ Tech Solutions</b>
    </footer>
    """,
    unsafe_allow_html=True  # Allow HTML to style the footer
)
#================================= End of Footer Section================================
#================================Design Section================================

# Streamlit app

# Logo and title
col1, col2 = st.columns([1, 9])  # Create two columns: one narrow for the logo, one wide for the title
with col1:
    st.image("image/logo.png", width=80)  # Replace "logo.png" with your logo file path and adjust the width if needed
with col2:
    st.markdown("<h1 style='display: inline-block;'>AI Resume Screening & Candidate Ranking System</h1>", unsafe_allow_html=True)

# Job description input
st.header("Job Description")
job_description= st.text_area ("Enter the job description") # Text area for entering the job description



# File uploader
st.header("Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF and PPTX files", type=["pdf", "pptx"], accept_multiple_files=True)



if uploaded_files and job_description: # If files are uploaded and job description is provided
    st.header("Ranking Resumes") # Display the 'Ranking Resumes' section header
    
    resumes = []
    for file in uploaded_files:
        text = extract_text_from_pdf(file) # Extract text from the uploaded PDF file
        resumes.append(text)

    # Rank resumes
    scores = rank_resumes(job_description, resumes)

    # Display scores
    results = pd.DataFrame({"Resume": [file.name for file in uploaded_files], "Score": scores }) 
    # Create a DataFrame with the resume names and scores
    
    results = results.sort_values(by="Score", ascending=False) 
    # Sort the results by score in descending order
    
        
    st.write(results)