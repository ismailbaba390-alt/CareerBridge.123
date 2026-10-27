from flask import Flask, render_template

app = Flask(__name__)

# Sample college data
COLLEGES = [
    {
        "name": "JNTU Hyderabad",
        "state": "Telangana",
        "courses": ["CSE", "ECE", "EEE", "Mechanical"],
        "type": "University"
    },
    {
        "name": "Osmania University",
        "state": "Telangana",
        "courses": ["CSE", "ECE", "Civil", "Mechanical"],
        "type": "University"
    },
    {
        "name": "Andhra University",
        "state": "Andhra Pradesh",
        "courses": ["CSE", "ECE", "EEE", "Civil"],
        "type": "University"
    },
    {
        "name": "IIT Hyderabad",
        "state": "Telangana",
        "courses": ["CSE", "AI", "Data Science", "Electrical"],
        "type": "Institute of Technology"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/skills")
def skills():
    return render_template("skills.html")


@app.route("/resume")
def resume():
    return render_template("resume.html")


@app.route("/interview")
def interview():
    return render_template("interview.html")


@app.route("/opportunities")
def opportunities():
    return render_template("opportunities.html")


@app.route("/colleges")
def colleges():
    import sqlite3

    conn = sqlite3.connect("careerbridge.db")
    conn.row_factory = sqlite3.Row

    colleges = conn.execute("""
        SELECT *
        FROM ranked_colleges
        ORDER BY nirf_overall_rank ASC
    """).fetchall()

    conn.close()

    return render_template("colleges.html", colleges=colleges)


@app.route("/dashboard")
def dashboard():

    # Calculate statistics from the sample college list
    total_colleges = len(COLLEGES)

    all_courses = set()
    for college in COLLEGES:
        all_courses.update(college["courses"])

    total_courses = len(all_courses)

    # No real job, internship or placement database connected yet
    stats = {
        "total_colleges": total_colleges,
        "total_courses": total_courses,
        "total_jobs": None,
        "total_internships": None,
        "placement_percentage": None,
        "colleges": COLLEGES
    }

    return render_template("dashboard.html", stats=stats)


if __name__ == "__main__":
    app.run(debug=True)