"""
Database Creation Script for Mental Wellness Assistant
This script creates and populates the quotes.db database.
Run this script ONCE to create the database with all motivational quotes.
"""

import sqlite3
import os

# Step 1: Connect to database (creates file if doesn't exist)
# Location: Same folder as this script
# File path: quotes.db (in project root)
conn = sqlite3.connect('quotes.db')
cursor = conn.cursor()

# Step 2: Create the quotes table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS quotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mood TEXT NOT NULL,
        quote TEXT NOT NULL,
        author TEXT,
        category TEXT,
        keywords TEXT
    )
""")

print("✓ Table 'quotes' created successfully")

# Step 3: Check if database already has data
cursor.execute("SELECT COUNT(*) FROM quotes")
existing_count = cursor.fetchone()[0]

if existing_count > 0:
    print(f"✓ Database already contains {existing_count} quotes")
    print("✓ Database is ready to use!")
else:
    # Step 4: Insert sample motivational quotes
    # Note: In reality, you'd insert all 190 quotes here
    print("⚠ Database is empty. Inserting sample quotes...")
    
    quotes_data = [
        ('sad', 'It\'s okay to not be okay. You don\'t have to be strong all the time.', None, None, None),
        ('sad', 'This feeling will pass. You\'ve survived 100% of your worst days so far.', None, None, None),
        ('sad', 'You are stronger than you think. This sadness is temporary, but your strength is permanent.', None, None, None),
        ('happy', 'The only way to do great work is to love what you do.', None, None, None),
        ('happy', 'Happiness is not something ready made. It comes from your own actions.', None, None, None),
        ('angry', 'Anger is an acid that can do more harm to the vessel in which it is stored than to anything on which it is poured.', None, None, None),
        ('anxious', 'Anxiety is the dizziness of freedom.', None, None, None),
        ('exhausted', 'You can\'t pour from an empty cup. Take care of yourself first.', None, None, None),
        # Add more quotes here to match your database
    ]
    
    # Insert quotes into database
    cursor.executemany("""
        INSERT INTO quotes (mood, quote, author, category, keywords)
        VALUES (?, ?, ?, ?, ?)
    """, quotes_data)
    
    print(f"✓ Inserted {len(quotes_data)} sample quotes into database")

# Step 5: Commit changes (save to disk)
conn.commit()

# Step 6: Verify final count
cursor.execute("SELECT COUNT(*) FROM quotes")
final_count = cursor.fetchone()[0]
print(f"✓ Total quotes in database: {final_count}")

# Step 7: Close connection
conn.close()

print(f"✓ Database 'quotes.db' ready at: {os.path.abspath('quotes.db')}")
print("\n✅ Database setup complete!")


