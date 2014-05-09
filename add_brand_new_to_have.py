
# This will take in a raw CSV file and return a CSV file with all the duplicates removed.

import csv
import os


if __name__ == '__main__':
    new_songs = []
    have_songs = []
    combined = []

    with open('have_songs.csv', 'rU') as have_songs_csv:
        have_songs = csv.reader(have_songs_csv)
        for row in have_songs:
            combined.append(row)

    with open('brand_new_songs.csv', 'rU') as new_songs_csv:
        new_songs = csv.reader(new_songs_csv)
        for row in new_songs:
            if row not in combined:
                combined.append(row)

    combined.sort()

    os.remove('have_songs.csv')

    for row in combined:
        with open('have_songs.csv', 'ab') as output_file:
            output_data = csv.writer(output_file)
            output_data.writerow(row)

    print combined