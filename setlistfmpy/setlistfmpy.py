# -*- coding: utf-8 -*-
import logging
import os
from datetime import date, timedelta
import requests
from datatypes import Artist, City, Setlist, Venue
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
API_KEY = os.getenv("SETLIST_FM_API_KEY")
if API_KEY is None:
    raise EnvironmentError(
        "The API Key for SETLIST.FM must be accessible from an environment variable called SETLIST_FM_API_KEY.")
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='debug.log',
                    filemode='w')
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(levelname)s - %(message)s')
ch.setFormatter(formatter)
# add the handlers to the logger
logging.getLogger('').addHandler(ch)

"""Main module."""
SETLIST_FM_HEADERS = {'x-api-key': API_KEY, 'Accept': 'application/json'}
__artist_search_url = 'https://api.setlist.fm/rest/1.0/search/artists'
SETLIST_SEARCH_URL = 'https://api.setlist.fm/rest/1.0/search/setlists'


def FindArtistByMbid(mbid):
    '''
    Look up an artist by Musicbrainz MBID
    :param mbid: a Musicbrainz MBID, e.g. 0bfba3d3-6a04-4779-bb0a-df07df5b0558
    :return: A single Artist
    '''
    # TODO: Complete FindByMbid
    return Artist()


def FindByTmid(tmid):
    '''
    Search for an Artist by Ticketmaster Identifier
    :param tmid: Ticketmaster identifier
    :return: A single Artist
    '''
    # TODO: Complete FindByTmid
    return Artist()


def FindArtistByName(artistName):
    r = requests.get(__artist_search_url, {'artistName': artistName, 'sort': 'relevance'},
                     headers=SETLIST_FM_HEADERS)
    print(r.url)
    results = r.json()
    return Artist(**results['artist'][0])


# Somehow convert this into a generator
def SearchArtist(artistName, sortName=True, maxResults=10):
    '''
    Search for artists
    :param artistName:
    :param sortName:
    :return: A list of artists matching the criteria specified
    '''
    # TODO: Complete SearchArtist
    return None


def FindCityByName(cityName):
    '''
        Search for a city by Name
        :param cityName: City name to find
        :return:
        '''
    # TODO: Complete FindCityByName
    return City()


def FindByState(stateName="", stateCode="", maxResults=20):
    '''
        Search for all cities in a particular State
        :param stateName: Full name of the state
        :param stateCode: State code (two digit code) for state
        :param maxResults: Maximum number of results to return in a call
        NOTE:stateName takes precedent if both are supplied)
        :return: list(City) objects
        '''
    # TODO: Complete FindByState
    return list(City())


def FindSetsInDateRange(artistName, startDate, range=0):
    logging.debug('FindSetsInDateRange %(artistName)s %(startDate)d')
    current_query_date = early_date = startDate - timedelta(days=range)
    last_date = startDate + timedelta(days=range)
    performances = {}
    while current_query_date != last_date + timedelta(days=1):
        # Make a setlist query
        r = requests.get(SETLIST_SEARCH_URL, {'artistName': artistName, 'date': _formatDateString(current_query_date)},
                         headers=SETLIST_FM_HEADERS)
        logging.debug(r.url)
        results = r.json()
        logging.debug(results)
        #  Do something with the results - like say yes we had a concert and here it is?
        s = InflateSetList(results)
        logging.debug(s)
        if not s is None:
            performances[s.setlistId]= {'eventDate':s.eventDate,
                                        'artist':s.artist.name,
                                        'venue_name':s.venue.name,
                                        'venue_city':s.venue.city.name,
                                        'venue_state':s.venue.city.stateCode}

        else:
            logging.info(str.format('Unable to find an event for {} on {}',artistName,current_query_date))
        current_query_date += timedelta(days=1)
    return performances


def _formatDateString(dt):
    return dt.strftime('%d-%m-%Y')


def InflateSetList(data):
    if 'type' in data and data['type'] == 'setlists':
        sl = data['setlist']
        s = Setlist.new()
        s.setlistId = sl[0]['id']
        s.eventDate = sl[0]['eventDate']
        s.artist = Artist(**sl[0]['artist'])
        s.venue = Venue(**sl[0]['venue'])
        s.venue.city = City(**sl[0]['venue']['city'])
    else:
        return None
    return s


def Run():
    ds =  pd.read_csv('c:/temp/PerformanceByArtist.csv',parse_dates=['PerformanceDate'])
    all_performances = {}
    for index, artist, perfdate in ds.itertuples():
        all_performances.update(FindSetsInDateRange(artist,perfdate, range=3))
    pd.DataFrame(all_performances).to_csv('c:/temp/after.csv')

if __name__ == '__main__':
    Run()
