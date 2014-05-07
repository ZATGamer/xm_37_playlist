# This will take in a raw CSV file and return a CSV file with all the duplicates removed.

import csv


if __name__ == '__main__':
    trim_songs = []
    page_number = 0
    songs = []
    have_songs = []
    crap = []

    with open('have_songs.csv', 'rU') as crap_csv_file:
        crap_data = csv.reader(crap_csv_file)
        for row in crap_data:
            crap.append(row)

    with open('songs_have.csv', 'rU') as songs_csv_file:
        have_data = csv.reader(songs_csv_file)
        for row in have_data:
            have_songs.append(row)

    for song in have_songs:
        if song not in crap:
            trim_songs.append(song)

    print len(songs)
    print len(trim_songs)
    print trim_songs
    # with open('test.csv', 'rU') as csv_file:
#     song_data = csv.reader(csv_file)
#     for row in song_data:
#         if row not in trim_songs:
#             trim_songs.append(row)

    trim_songs.sort()

    for row in trim_songs:
        with open('brand_new_songs.csv', 'ab') as output_file:
            output_data = csv.writer(output_file)
            output_data.writerow(row)

    print trim_songs
