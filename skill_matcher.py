def calculate_match(resume_text, job_desc_text):
    # Standard list of technical keywords to track
    SKILL_KEYWORDS = [
        "python", "machine learning", "data analytics", "data science", 
        "artificial intelligence", "ai", "ml", "numpy", "pandas", 
        "matplotlib", "scikit-learn", "dbms", "sql", "git", "github","html", "css", "javascript", "react", "angular", "node.js",
    ]
    
    resume_lower = resume_text.lower()
    jd_lower = job_desc_text.lower()
    
    # 1. Identify which keywords exist in the pasted Job Description
    jd_skills = [skill for skill in SKILL_KEYWORDS if skill in jd_lower]
    
    # 2. See which of those specific JD skills are present in the resume
    matched_skills = [skill for skill in jd_skills if skill in resume_lower]
    
    # 3. Calculate percentage score safely
    if len(jd_skills) > 0:
        score = int((len(matched_skills) / len(jd_skills)) * 100)
    else:
        # Fallback if no specific keywords are found in the text box
        score = 0  
        
    # Format the skills neatly (e.g., "python" -> "Python")
    display_skills = [skill.title() for skill in matched_skills]
    
    return score, display_skills