import sqlite3

conn = sqlite3.connect("careerbridge.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS colleges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    state TEXT NOT NULL,
    city TEXT,
    college_type TEXT,
    official_website TEXT
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    college_id INTEGER,
    course_name TEXT NOT NULL,
    FOREIGN KEY (college_id) REFERENCES colleges(id)
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS placements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    college_id INTEGER,
    academic_year TEXT,
    students_placed INTEGER,
    eligible_students INTEGER,
    average_package_lpa REAL,
    source_url TEXT,
    FOREIGN KEY (college_id) REFERENCES colleges(id)
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    company TEXT,
    location TEXT,
    job_type TEXT,
    application_url TEXT
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS internships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    company TEXT,
    location TEXT,
    application_url TEXT
)
""")

conn.commit()
conn.close()

print("CareerBridge database created successfully!")