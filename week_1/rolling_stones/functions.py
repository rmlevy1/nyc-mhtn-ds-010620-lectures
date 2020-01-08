def FindByName(x):
    for row in albums:
        if row['album'] == x:
            return {(row['album'])}


def FindByRank(x):
    for row in albums:
        if str(x) == row['number']:
            return [row['number'], row['album']]
        else:
            None
            

            
def FindByYear(x):
    yalbums = []
    for row in albums:
        if row['year'] == str(x):
            yalbums.append(row['album'])
    return yalbums

def FindByYears(x,y):
    yalbums = []
    for row in albums:
        if ((int(row['year']) >= x) and (int(row['year']) <= y)):
            yalbums.append(row['album'])
    return yalbums

def FindByRanks(x,y):
    yalbums = []
    for row in albums:
        if ((int(row['number']) > x) and (int(row['number']) < y)):
            yalbums.append(row['album'])
    return yalbums 

def AllTitles():
    yalbums = []
    for row in albums:
        yalbums.append(row['album'])
    return yalbums

def AllArtists():
    artists = []
    for row in albums:
        artists.append(row['artist'])
    return artists







