from flask import Flask, render_template, request, send_file
import urllib.request

app = Flask(__name__)

def classify_user(proficiency, past_experience, study_time):
    score = 0
    if proficiency.lower() == "beginner":
        score += 1
    elif proficiency.lower() == "intermediate":
        score += 2
    elif proficiency.lower() == "advanced":
        score += 3
    
    if past_experience.lower() == "yes":
        score += 1
    
    if study_time >= 2:
        score += 1
    if study_time >= 4:
        score += 1
    
    if score <= 3:
        return "Basic"
    elif score <= 5:
        return "Intermediate"
    else:
        return "Advanced"

def fetch_resources(language_level):
    # Sample resources for demonstration
    basic_resources = {
        "videos": ["Basic French for Beginners", "Introduction to French Pronunciation"],
        "exercises": ["Basic French Vocabulary Quiz", "Simple French Sentences Practice"],
        "roadmap": ["Week 1: Alphabet and Greetings", "Week 2: Numbers and Common Phrases"]
    }
    
    intermediate_resources = {
        "videos": ["Intermediate French Grammar Series", "Conversational French Practice"],
        "exercises": ["Intermediate French Listening Comprehension", "French Writing Exercises"],
        "roadmap": ["Week 1: Verb Tenses Review", "Week 2: Intermediate Vocabulary Building"]
    }
    
    advanced_resources = {
        "videos": ["Advanced French Literature Analysis", "French News Listening Practice"],
        "exercises": ["Advanced French Grammar Drills", "French Debate Topics"],
        "roadmap": ["Week 1: Advanced Vocabulary Expansion", "Week 2: Advanced Speaking and Writing Practice"]
    }
    
    if language_level == "Basic":
        return basic_resources
    elif language_level == "Intermediate":
        return intermediate_resources
    elif language_level == "Advanced":
        return advanced_resources

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        language = request.form["language"]
        proficiency = request.form["proficiency"]
        past_experience = request.form["past_experience"]
        study_time = float(request.form["study_time"])
        
        language_level = classify_user(proficiency, past_experience, study_time)
        resources = fetch_resources(language_level)
        
        if language_level == "Basic" and language.lower() == "french":
            # Generate and download a PDF file with basic French resources
            # You would replace this with actual PDF generation code
            return send_file("Beginner.pdf", as_attachment=True)
        elif language_level == "Intermediate" and language.lower() == "french":
            # Generate and download a PDF file with basic French resources
            # You would replace this with actual PDF generation code
            return send_file("Intermediate.pdf", as_attachment=True)
        elif language_level == "Advanced" and language.lower() == "french":
            # Generate and download a PDF file with basic French resources
            # You would replace this with actual PDF generation code
            return send_file("Advanced.pdf", as_attachment=True)
        
        return render_template("result.html", name=name, language_level=language_level, resources=resources)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
