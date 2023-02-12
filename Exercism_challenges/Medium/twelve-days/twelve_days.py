def reciteSong(start_verse, end_verse):

    start_ordinal = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']
    end_song = [
        "and a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, ",
        ]
    
    
    song_list = ''
    if start_verse == 1:
        end_song[0] = "a Partridge in a Pear Tree."
    for e in range(start_verse-1,-1,-1):
        song_list += end_song[e]
        song =f'On the {start_ordinal[start_verse-1]} day of Christmas my true love gave to me: {song_list}'
    return song

def recite(start_verse, end_verse):
    if start_verse == end_verse:
        song = reciteSong(start_verse, end_verse)
        return [song]
    else:
        song = []
        for i in range(start_verse, end_verse+1):
            spong = reciteSong(i, end_verse)
            song.append(spong)
        return song


