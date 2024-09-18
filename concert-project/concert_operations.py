import sqlite3

def connect_db():
    return sqlite3.connect('concerts.db')

def play_in_venue(band_name, venue_title, date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO concerts (band_name, venue_title, date) 
        VALUES (?, ?, ?)
    ''', (band_name, venue_title, date))
    conn.commit()
    conn.close()

def introduction(concert_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT bands.name, bands.hometown, venues.city 
        FROM concerts 
        JOIN bands ON concerts.band_name = bands.name 
        JOIN venues ON concerts.venue_title = venues.title 
        WHERE concerts.id = ?
    ''', (concert_id,))
    band_name, band_hometown, venue_city = cursor.fetchone()
    conn.close()
    return f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"

def all_introductions(band_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT venues.city, bands.hometown 
        FROM concerts 
        JOIN bands ON concerts.band_name = bands.name 
        JOIN venues ON concerts.venue_title = venues.title 
        WHERE bands.name = ?
    ''', (band_name,))
    results = cursor.fetchall()
    conn.close()
    return [f"Hello {city}!!!!! We are {band_name} and we're from {hometown}" for city, hometown in results]

def hometown_show(concert_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT bands.hometown, venues.city 
        FROM concerts 
        JOIN bands ON concerts.band_name = bands.name 
        JOIN venues ON concerts.venue_title = venues.title 
        WHERE concerts.id = ?
    ''', (concert_id,))
    hometown, city = cursor.fetchone()
    conn.close()
    return hometown == city

def most_performances():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT band_name, COUNT(*) as concert_count 
        FROM concerts 
        GROUP BY band_name 
        ORDER BY concert_count DESC 
        LIMIT 1
    ''')
    result = cursor.fetchone()
    conn.close()
    return result

def concert_on(venue_title, date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM concerts 
        WHERE venue_title = ? AND date = ?
    ''', (venue_title, date))
    result = cursor.fetchone()
    conn.close()
    return result

def most_frequent_band(venue_title):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT band_name, COUNT(*) as band_count 
        FROM concerts 
        WHERE venue_title = ? 
        GROUP BY band_name 
        ORDER BY band_count DESC 
        LIMIT 1
    ''')
    result = cursor.fetchone()
    conn.close()
    return result
