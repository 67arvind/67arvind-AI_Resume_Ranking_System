# **🚀 AI-Powered Resume Screening and Ranking System 🤖**

<img src="https://i.imgur.com/MojtCKB.jpeg" alt="App Logo" width="200">

An AI-based system to automate the resume screening process by ranking resumes based on their relevance to a job description. Built using **Python**, **Streamlit**, and **scikit-learn**.

---

## **Table of Contents**
1. [Introduction](#introduction)
2. [Screenshots](#screenshots)
3. [Features](#features)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Performance Metrics](#performance-metrics)
7. [Future Work](#future-work)
8. [Contributing](#contributing)
9. [License](#license)


---

## **Introduction**

The **AI-Powered Resume Screening and Ranking System** is designed to streamline the recruitment process by automating the initial screening of resumes. The system uses **Natural Language Processing (NLP)** techniques, such as **TF-IDF** and **cosine similarity**, to analyze and rank resumes based on their relevance to a given job description. This helps recruiters save time, reduce bias, and focus on the most suitable candidates.

---

## **Screenshots**

### **Dashboard Interface**

<p float="left">
  <img src="https://i.imgur.com/la7PqsV.png" alt="App Screenshot 1" width="900" />
  <img src="https://i.imgur.com/zR4D1xm.png" alt="App Screenshot 2" width="700" />
</p>


## **Flowchart of the Resume Ranking Process**

<p float="left">
  <img src="https://i.postimg.cc/GpGZ9S5p/flowchart.png" alt="App Screenshot" width="250" />
  <a href="https://postimg.cc/JH3jKSTC">
    <img src="https://i.postimg.cc/XqmxNbdq/Untitled-diagram-2025-03-21-115304.png" alt="Untitled diagram 1" width="250" />
  </a>
  <a href="https://postimg.cc/YGTw8svR">
    <img src="https://i.postimg.cc/90QFX3V6/Untitled-diagram-2025-03-21-115630.png" alt="Untitled diagram 2" width="250" />
  </a>
</p>
---

## **Features**

- **Resume Ranking**: Automatically ranks resumes based on their similarity to the job description.
- **Text Extraction**: Extracts text from PDF and PPTX files using **PyPDF2**.
- **TF-IDF Vectorization**: Converts text into numerical vectors for comparison.
- **Cosine Similarity**: Computes the similarity between the job description and resumes.
- **User-Friendly Interface**: Built using **Streamlit** for easy interaction.
- **Scalable**: Can handle large volumes of resumes efficiently.

---

## **Installation**

### **Prerequisites**
- Python 3.7 or higher
- Stable internet connection

### **Steps**
1. Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/AI-Resume-Screening.git
   cd AI-Resume-Screening

2. Install Dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the Streamlit App:
   ```bash
   streamlit run src/run resume_app.py

4. Open your browser and go to http://localhost:8501 to access the application.

---

### **Usage**
## Input Job Description:

- Enter the job description in the provided text area.

- Upload Resumes:

- Upload multiple resumes in PDF or PPTX format.

- View Ranked Results:

- The system will display the ranked list of resumes along with their similarity scores.

---

## **Performance Metrics**

The system is evaluated using the following metrics:

| **Metric**               | **Description**                                                                 | **Formula**                                                                 | **Expected Value** |
|--------------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------|--------------------|
| **Accuracy**             | Measures the percentage of correctly ranked resumes compared to manual ranking.  | \( \text{Accuracy} = \frac{\text{Number of Correct Rankings}}{\text{Total Rankings}} \times 100 \) | 85% - 95%         |
| **Precision**            | Measures the proportion of relevant resumes among the top-ranked resumes.        | \( \text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}} \) | 80% - 90%         |
| **Recall**               | Measures the proportion of relevant resumes that were correctly ranked.          | \( \text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}} \) | 75% - 85%         |
| **F1-Score**             | Combines precision and recall into a single metric using the harmonic mean.      | \( \text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} \) | 80% - 90%         |
| **Cosine Similarity**    | Measures the similarity between the job description and resumes.                 | \( \text{Cosine Similarity} = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|} \) | 0.7 - 1.0         |
| **Response Time**        | Measures the time taken to process and rank resumes.                            | \( O(n \times m) \) (where \( n \) = number of resumes, \( m \) = number of terms) | < 1 second/resume |
| **Scalability**          | Measures the system's ability to handle large volumes of resumes.                | -                                                                           | Supports up to 10,000 resumes |

---

### **Explanation of Metrics**

1. **Accuracy**:
   - This metric evaluates how often the system correctly ranks resumes compared to manual ranking by recruiters.
   - A high accuracy (85% - 95%) indicates that the system is reliable and effective.

2. **Precision**:
   - This metric measures the proportion of relevant resumes among the top-ranked resumes.
   - A high precision (80% - 90%) indicates that the system is good at identifying the most relevant candidates.

3. **Recall**:
   - This metric measures the proportion of relevant resumes that were correctly ranked.
   - A high recall (75% - 85%) indicates that the system is good at capturing all relevant candidates.

4. **F1-Score**:
   - This metric combines precision and recall into a single score using the harmonic mean.
   - A high F1-score (80% - 90%) indicates a good balance between precision and recall.

5. **Cosine Similarity**:
   - This metric measures the similarity between the job description and resumes.
   - A high cosine similarity score (0.7 - 1.0) indicates a strong match between the job description and the resume.

6. **Response Time**:
   - This metric measures the time taken to process and rank resumes.
   - The system should process each resume in less than 1 second for optimal performance.

7. **Scalability**:
   - This metric measures the system's ability to handle large volumes of resumes.
   - The system should support up to 10,000 resumes without significant performance degradation.

---

## **Future Work**
The **AI-Powered Resume Screening and Ranking System** has great potential for further enhancements. Below are some proposed improvements and their expected impact:

1. **Advanced NLP Models**
- **Enhancement:** Integrate advanced NLP models like **BERT** or **GPT** for better contextual understanding of resumes and job descriptions.

- **Impact:** Improved accuracy in matching resumes to job descriptions, especially for complex or nuanced roles.

2. **Support for More File Formats**
- **Enhancement:** Add support for additional file formats such as Word documents (DOCX) and scanned resumes (OCR).

- **Impact:** Broader compatibility with various resume formats, making the system more versatile.

3. **Skill and Experience Extraction**
- **Enhancement:** Implement techniques to extract and analyze skills, experience, and education from resumes.

- **Impact:** More accurate shortlisting of candidates based on specific qualifications and expertise.

4. **Real-Time Dashboard**
- **Enhancement:** Develop a real-time dashboard for recruiters to monitor the screening process and view analytics.

- **Impact:** Faster decision-making and improved user experience for recruiters.

5. **Bias Reduction**
- **Enhancement:** Implement techniques to reduce unconscious bias in the ranking process, such as anonymizing resumes or using fairness-aware algorithms.

- **Impact:** More fair and ethical hiring practices, promoting diversity and inclusion.

6. **Integration with HR Platforms**
- **Enhancement:** Provide API integration with popular HR platforms like Applicant Tracking Systems (ATS), LinkedIn, and Indeed.

- **Impact:** Seamless workflow for HR teams, eliminating the need for manual resume uploads.

7. **Cloud Deployment**
- **Enhancement:** Deploy the system on cloud platforms like AWS, Google Cloud, or Azure for better scalability and accessibility.

- **Impact:** Ability to handle large-scale recruitment processes with ease.

8. **Multi-Language** Support
- **Enhancement:** Add support for multiple languages to cater to global recruitment needs.

- **Impact:** Expanded usability for international organizations and non-English resumes.

9. **Feedback Mechanism**
- **Enhancement:** Implement a feedback mechanism for recruiters to provide input on the system's ranking results.

- **Impact:** Continuous improvement of the system based on real-world user feedback.

10. **Enhanced Security**
- **Enhancement:** Strengthen data security by implementing encryption and access control mechanisms for sensitive resume data.

- **Impact:** Increased trust and compliance with data protection regulations.
---

## **Contributing**

We welcome contributions! Feel free to fork this repo, create a new branch, and submit a Pull Request (PR).:

### **Steps to Contribute**

1. **Fork the Repository**:
   - Click the **Fork** button at the top right of the repository page to create your own copy of the project.

2. **Clone the Repository**:
   ```bash
   git checkout -b feature-new
   git commit -m "Added new feature"
   git push origin feature-new

---
**Guidelines for Contributions**
- **Code Style:** Follow the existing code style and add comments where necessary.

- **Testing:** Ensure your changes are tested and do not break existing functionality.

- **Documentation:** Update the README or other documentation if your changes introduce new features or modify existing ones.

**Need Help?**
 - If you're new to open-source contributions or need help, feel free to connect with us on [LinkedIn](https://www.linkedin.com/in/arvind-kumar-424554196/) open an issue, or reach out to us. We're happy to guide you!

---
Thank you for contributing! 🚀
---

## **License**

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/)License. See the LICENSE file for details.


   
