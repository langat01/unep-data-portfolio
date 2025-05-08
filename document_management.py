# document_management.py
import sqlite3
from datetime import datetime

# Setup database
conn = sqlite3.connect("unep_documents.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        doc_type TEXT CHECK(doc_type IN ("Proposal", "Report", "Evaluation")),
        project_id TEXT,
        upload_date TEXT,
        file_path TEXT
    )
''')

# Add sample documents
sample_docs = [
    ("GEF_Biodiversity_Proposal", "Proposal", "BD-001", "2025-01-15", "/docs/BD-001.pdf"),
    ("Land_Degradation_Report", "Report", "LD-003", "2025-02-20", "/docs/LD-003.pdf")
]

cursor.executemany('''
    INSERT INTO documents (title, doc_type, project_id, upload_date, file_path)
    VALUES (?, ?, ?, ?, ?)
''', sample_docs)

conn.commit()

# Query example
print("📂 Sample Document Query Results:")
for row in cursor.execute("SELECT * FROM documents"):
    print(f"ID: {row[0]}, Title: {row[1]}, Type: {row[2]}, Project: {row[3]}")

conn.close()
print(" Database created! Run queries with `search_documents(project_id='BD-001')`.")
