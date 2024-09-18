from db_setup import setup_database
from concert_operations import (
    play_in_venue,
    introduction,
    all_introductions,
    hometown_show,
    most_performances,
    concert_on,
    most_frequent_band,
)

# Setup the database and tables
setup_database()

# Example usage
play_in_venue('The Rockers', 'Stadium', '2024-09-20')
print(introduction(1))  # Replace 1 with a valid concert ID
print(all_introductions('The Rockers'))
print(hometown_show(1))
print(most_performances())
print(concert_on('Stadium', '2024-09-20'))
print(most_frequent_band('Stadium'))
