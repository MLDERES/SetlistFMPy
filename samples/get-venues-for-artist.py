from setlistfmpy import Artist


def getVenueByArtistDate(artistName, startDate, endDate=""):
    #Find the artist
    # Use the artist Mbid to search venues
    # Make a request for every day between startDate and endDate
    #  If endDate ="" then just do it for one day
    endDate = startDate if (endDate== "") else endDate
    artist = Artist.Artist.SearchArtist(artistName,maxResults=1)
    if artist is None:
        raise ValueError("Artist '{}' not found", artistName)
    pass

getVenueByArtistDate('Kid Rock','21-09-2018')
