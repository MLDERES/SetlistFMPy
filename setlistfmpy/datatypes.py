
class Artist:
    def __init__(self, mbid, name, sortName, tmid=None,  disambiguation="", url=""):
        '''
            https://api.setlist.fm/docs/1.0/json_Artist.html
            parameters:
                - mbid - (String) unique MusicBrainz identifer
                - tmid - (Int) unique Ticket Master identifier
                - name - (String) the artist's name
                - sortName - (String) the artist's sort name
                - disambiguation - (String) disambiguation to distinguish between artist's with the same name
                - url - (String) the attribution url
        '''
        self.mbid = mbid
        self.tmid = tmid
        self.name = name
        self.sortName = sortName
        self.disambiguation = disambiguation
        self.url = url

    def __str__(self):
        return str.format('ARTIST=>\n\tName:{}\n\tMBID:{}\n\tTMID:{}', self.name, self.mbid, self.tmid)

class City:
    def __init__(self, id, name, stateCode, state, coords, country):
        '''
            https://api.setlist.fm/docs/1.0/json_City.html
            params:
                - cityId - (String) unique identifier
                - name - (String) the city's name
                - stateCode - (String) the code of the city's state
                - state - (String) the name of city's state
                - coords - (Coords) the city's coordinates
                - country - (Country) the city's country
        '''
        self.cityId = id
        self.name = name
        self.stateCode = stateCode
        self.state = state
        self.latitude = coords['lat']
        self.longitude = coords['long']
        self.country = country

        def __str__(self):
            return str.format('CITY=>\n\tName:{}\n\tStateCode:{}\n\tState:{}', self.name, self.stateCode, self.state)

class Set:
	def __init__(self, name, encore, song):
		'''
			https://api.setlist.fm/docs/1.0/json_Set.html
			parameters:
				- name - (String) the description/name of the set
				- encore - (Int) if the set is an encore, this is the number of the encore
				- song - (array of Song) this set's songs
		'''
		self.name = name
		self.encore = encore
		self.song = song

class Setlist:
    def __init__(self, artist, venue, tour, sets, info, url, setlistId, versionId, eventDate, lastUpdated):
        """
        https://api.setlist.fm/docs/1.0/json_Setlist.html
        parameters:
            - artist - (Artist) the setlist's artist
            - venue - (Venue) the setlist's venue
            - tour - (Tour) the setlist's tour
            - sets - (array of Set) all sets of this setlist
            - info - (String) additional information on the concert
            - url - (String) the attribution url to which you have to link to wherever you use data from this setlist in your application
            - setlistId - (String) unique identifier
            - versionId - (String) unique identifier of the version
            - eventDate - (String) date of the concert in the form "dd-MM-yyyy"
            - lastUpdated - (String) date, time, and time zone of the last update to this setlist in the format "yyyy-MM-dd'T'HH:mm:ss.SSSZZZZZ"
        """
        self.artist = artist
        self.venue = venue
        self.tour = tour
        self.set = [x for x in sets]
        self.info = info
        self.url = url
        self.setlistId = setlistId
        self.versionId = versionId
        self.eventDate = eventDate
        self.lastUpdated = lastUpdated

    @classmethod
    def new(cls):
        return cls(artist=None, venue=None, tour="", sets=[], info="",
                   url="", setlistId="", versionId="", eventDate="", lastUpdated="")

    def __str__(self):
        return str.format('Setlist => \n\tArtist {}\n\tDate {}',self.artist,self.eventDate)
class Song:
    def __init__(self, name, withArtist, cover, info, tape):
        '''
            https://api.setlist.fm/docs/1.0/json_Song.html
            parameters:
                - name - (String) name of the song
                - withArtist - (Artist) different Artist than the performing one that joined the stage for this song
                - cover - (Artist) the original Artist of this song, if different than performing artist
                - info - (String) special incidents or additional information about the way the song was performed at this specific concert
                - tape - (Boolean) the song came from tape rather than being performed live
        '''
        self.withArtist = withArtist
        self.cover = cover
        self.info = info
        self.tape = tape

class User:
    def __init__(self, userId, fullName, lastFm, mySpace, twitter, flickr, website, about, url):
        '''
            https://api.setlist.fm/docs/1.0/json_User.html
            parameters:
                - userId - (String)
                - fullName - (String)
                - lastFm - (String)
                - mySpace - (String)
                - twitter - (String)
                - flickr - (String)
                - website - (String)
                - about - (String)
                - url - (String)
        '''
        self.userId = userId
        self.fullName = fullName
        self.lastFm = lastFm
        self.mySpace = mySpace
        self.twitter = twitter
        self.flickr = flickr
        self.website = website
        self.about = about
        self.url = url

class Venue:
    def __init__(self, city, url, id, name):
        '''
            https://api.setlist.fm/docs/1.0/json_Venue.html
            parameters:
                - city - (City) the city in which the venue is located
                - url - (String) the attribution url
                - venueId - (String) unique identifier
                - name - (String) the name of the venue, usually without city and country
        '''
        self.city = city
        self.url = url
        self.venueId = id
        self.name = name

    def __str__(self):
        return str.format('VENUE=>\n\tName:{}\n\tID:{}\n\t\tCity:{}', self.name, self.id, self.city)
