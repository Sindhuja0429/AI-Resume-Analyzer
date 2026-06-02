import os
from flask import Flask, render_template, request
from resume_parser import extract_text
# Import our calculator function
from skill_matcher import calculate_match

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files:
        return "No file part"
    
    file = request.files['resume']
    # Grab the text pasted into the Job Description box
    job_desc = request.form.get('job_description', '')
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # 1. Extract raw text from the resume
        resume_text = extract_text(file_path)
        
        # 2. Compute the dynamic score and matched skills
        score, matched_skills = calculate_match(resume_text, job_desc)
        
        # 3. Send everything over to result.html
        return render_template(
            'result.html', 
            filename=file.filename, 
            text=resume_text, 
            skills=matched_skills, 
            score=score
        )

if __name__ == '__main__':
    app.run(debug=True, port=5001)