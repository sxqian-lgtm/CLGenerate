# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 17:24:31 2026

@author: nyinds
"""
API=''
from CLetter import generatecoverletter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# generate text
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
The Andover Companies
Insurance
Business Intelligence Summer Intern
Develop practical business analytics skills while gaining exposure to risk management and the insurance industry at a leading regional property & casualty mutual insurance carrier.

As a Business Intelligence Intern, you will take ownership of meaningful analytics projects from start to finish, working with real business data to support decision-making across the organization. You will be supported by experienced members of the Data Analytics team who will provide mentorship, technical guidance, and regular feedback throughout the summer.

Projects may include data acquisition and preparation, exploratory analysis, modeling, and the development of reports and dashboards that deliver actionable insights to business stakeholders. The work you produce will be used by the business, not created solely for training purposes.

In addition, you will receive a high-level overview and hands-on exposure to key business areas including Underwriting, Product Development, Claims, and Marketing. You will collaborate with interns from other departments to solve cross-functional business problems and present findings and recommendations to management.

We’re seeking candidates who:

Are pursuing a degree in business analytics, mathematics, statistics, data science, or a related analytics-focused field
Have strong analytical and problem-solving skills and a curiosity for exploring data
Are self-motivated, eager to learn, and comfortable taking ownership of work with guidance
Can clearly communicate insights in both written and verbal formats to technical and non-technical audiences
Are proficient in Excel
Exposure to analytics tools and techniques such as SQL, Python or R, statistical analysis including regression, and data visualization platforms (Tableau, Power BI, Qlik) is a plus, but not required.
"""

def PDFsave(text,output_path):
    # === Save to PDF ===
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    margin = 72
    y = height - margin
    
    for line in text.splitlines():
        # 自动换行（简单处理）
        if len(line) > 95:
            words = line.split()
            buf = ""
            for w in words:
                if len(buf) + len(w) + 1 > 95:
                    c.drawString(margin, y, buf)
                    y -= 14
                    buf = w
                    if y < margin:
                        c.showPage()
                        y = height - margin
                else:
                    buf = (buf + " " + w).strip()
            if buf:
                c.drawString(margin, y, buf)
                y -= 14
        else:
            c.drawString(margin, y, line)
            y -= 14
    
        if y < margin:
            c.showPage()
            y = height - margin
    
    c.save()
    
    print(f"\nPDF 已保存到: {os.path.abspath(output_path)}")
if __name__ == "__main__":
    text=generatecoverletter(API,resume_highlights,company_info)
    output_path = r"C:\Users\nyinds\Resume\cover_letter.pdf"   # 你可以改成任何路径
    PDFsave(text, output_path)
