# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 16:28:41 2026

@author: nyinds
writing cover letter
"""
# cover_letter_gemini_pdf.py
from google import genai
from google.genai import types
from datetime import datetime
API='AIzaSyAvw8qPZzJGT0cDpw4IxKg7G7Vet6n3ljE'
resume_highlights = """Resume Highlights:
- Partnered with clients on statistical consulting projects using regression and machine learning; built reproducible pipelines in Python/R.
- Built dashboards and visual reports (ggplot/matplotlib) to support client decision-making.
- Conducted causal inference and A/B testing to recommend data-driven actions.
- Cleaned and modeled 65,000 job records using R (tidyverse); built multilevel regression models with nested effects.
- Conducted DAG-based causal analysis to separate direct vs. mediated effects of education on salary.
- Modeled Parkinson’s progression using Random Forests and PCA-reduced protein data; reduced MSE by 50%.
- Implemented a Transformer with learnable kernels in PyTorch; reduced training time by 20% on IMDb dataset.
- Built MySQL database and Python automation for e-commerce analytics; supported weekly reporting for 1,000+ products.
"""
company_info = """
Acme Analytics is a fast-growing data science consultancy helping Fortune 500 clients make data-driven decisions. The internship involves statistical modeling, machine learning, and client-facing communication. Ideal candidates are proficient in Python/R, have experience with causal inference or ML, and can present insights clearly.
"""
def generatecoverletter(API,resume_highlights,company_info):
    
    today = datetime.now().strftime("%B %d, %Y")
    GEMINI_API_KEY = API
    client = genai.Client(api_key=GEMINI_API_KEY)
    # === Prompt ===
    prompt = f"""
    At the very top of the cover letter, Using the info of {today} write a correctly formatted English date in the style with NO blank line after it:
    "Month Day, Year", For example: "January 31, 2026". 
    
    Immediately below the date, include the following contact block exactly:
    Shuxin Qian
    sxqian@bu.edu
    +1 617 319 7248
    29 Cummings Rd, Brighton
    Boston, MA
    
    You are a professional cover letter writer. Write a 200–250 word cover letter for a graduate student in Statistical Practice at Boston University (Dec 2026), applying for a data science or machine learning internship. Use the resume highlights and company info below. Emphasize action, results, and quantification. Avoid repeating phrases.
    
    Resume Highlights:
    {resume_highlights}
    
    Company Info:
    {company_info}
    
    Constraints:
    - Tone: professional and enthusiastic
    - No invented facts
    - Use each resume point at most once
    - Output plain text only
    
    """
    # === Generate content ===
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_level="low")
        ),
    )
    # === Output ===
    print("\n=== GENERATED COVER LETTER ===\n")
    print(response.text)
    return response.text

