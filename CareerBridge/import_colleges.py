import sqlite3

COLLEGES = [
    ("Indian Institute of Technology Madras", "Chennai", "Tamil Nadu", "University", 1),
    ("Indian Institute of Science", "Bengaluru", "Karnataka", "University", 2),
    ("Indian Institute of Technology Bombay", "Mumbai", "Maharashtra", "University", 3),
    ("Indian Institute of Technology Delhi", "New Delhi", "Delhi", "University", 4),
    ("Indian Institute of Technology Kanpur", "Kanpur", "Uttar Pradesh", "University", 5),
    ("Indian Institute of Technology Kharagpur", "Kharagpur", "West Bengal", "University", 6),
    ("Indian Institute of Technology Roorkee", "Roorkee", "Uttarakhand", "University", 7),
    ("All India Institute of Medical Sciences Delhi", "New Delhi", "Delhi", "Medical", 8),
    ("Jawaharlal Nehru University", "New Delhi", "Delhi", "University", 9),
    ("Banaras Hindu University", "Varanasi", "Uttar Pradesh", "University", 10),
    ("Indian Institute of Technology Guwahati", "Guwahati", "Assam", "University", 11),
    ("Indian Institute of Technology Hyderabad", "Hyderabad", "Telangana", "University", 12),
    ("Jamia Millia Islamia", "New Delhi", "Delhi", "University", 13),
    ("Manipal Academy of Higher Education", "Manipal", "Karnataka", "University", 14),
    ("University of Delhi", "Delhi", "Delhi", "University", 15),
    ("Birla Institute of Technology and Science Pilani", "Pilani", "Rajasthan", "University", 16),
    ("Amrita Vishwa Vidyapeetham", "Coimbatore", "Tamil Nadu", "University", 17),
    ("Jadavpur University", "Kolkata", "West Bengal", "University", 18),
    ("Aligarh Muslim University", "Aligarh", "Uttar Pradesh", "University", 19),
    ("Homi Bhabha National Institute", "Mumbai", "Maharashtra", "University", 20),
    ("Vellore Institute of Technology", "Vellore", "Tamil Nadu", "University", 21),
    ("SRM Institute of Science and Technology", "Chennai", "Tamil Nadu", "University", 22),
    ("Saveetha Institute of Medical and Technical Sciences", "Chennai", "Tamil Nadu", "University", 23),
    ("Indian Agricultural Research Institute", "New Delhi", "Delhi", "Agriculture", 24),
    ("Siksha O Anusandhan", "Bhubaneswar", "Odisha", "University", 25),
    ("University of Hyderabad", "Hyderabad", "Telangana", "University", 26),
    ("Osmania University", "Hyderabad", "Telangana", "University", 53),
    ("International Institute of Information Technology Hyderabad", "Hyderabad", "Telangana", "University", 89),
]

conn = sqlite3.connect("careerbridge.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS ranked_colleges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    city TEXT,
    state TEXT,
    college_type TEXT,
    nirf_overall_rank INTEGER,
    ranking_year INTEGER,
    source_url TEXT
)
""")

source = "https://www.nirfindia.org/Rankings/2025/OverallRanking.html"

conn.executemany("""
INSERT OR IGNORE INTO ranked_colleges
(name, city, state, college_type, nirf_overall_rank, ranking_year, source_url)
VALUES (?, ?, ?, ?, ?, 2025, ?)
""", [college + (source,) for college in COLLEGES])

conn.commit()

count = conn.execute(
    "SELECT COUNT(*) FROM ranked_colleges"
).fetchone()[0]

conn.close()

print("College import completed!")
print("Unique ranked colleges in database:", count)
print("Note: This is a starter dataset, not yet 50 colleges.")