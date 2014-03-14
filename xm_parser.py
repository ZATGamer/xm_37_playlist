# This will take in a raw CSV file and return a CSV file with all the duplicates removed.

import csv
from lxml.html import parse


if __name__ == '__main__':
    trim_songs = []
    base_url = \
        'http://www.dogstarradio.com/search_playlist.php?channel=37'
    page_number = 0
    songs = []
    have_songs = []
    while True:

        page = parse('{}&page={}'.format(base_url, page_number))

        rows = page.xpath('body/center/table')[0].findall('tr')[3:-1]

        if len(rows) == 0:
            break

        for row in rows:
            columns = row.findall('td')

            songs.append([
                columns[1].text_content(),
                columns[2].text_content(),
            ])

        page_number += 1

        print len(songs)
        print songs

    print len(songs)
    print songs

    crap = []
    with open('crap.csv', 'rU') as crap_csv_file:
        crap_data = csv.reader(crap_csv_file)
        for row in crap_data:
            crap.append(row)

    try:
        with open('songs_have.csv', 'rU') as songs_csv_file:
            have_data = csv.reader(songs_csv_file)
            for row in have_data:
                have_songs.append(row)
    except IOError:

    # have_songs = []
    # with open('songs_have.csv', 'rU') as songs_csv_file:
    #     have_data = csv.reader(songs_csv_file)
    #     for row in have_data:
    #         have_songs.append(row)

        for song in songs:
            if song not in trim_songs and song not in crap and song not in have_songs:
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
            with open('songs_have.csv', 'ab') as output_file:
                output_data = csv.writer(output_file)
                output_data.writerow(row)

        print trim_songs

