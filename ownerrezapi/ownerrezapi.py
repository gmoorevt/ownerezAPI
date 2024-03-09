import requests
from typing import List, Dict
import logging
import datetime
from constants import BASEURL as url
from model import *
from constants import *
from restAdapter import RestAdapter
from expeptions import OwerrezapiExeception


log = logging.getLogger(__name__)
headers = {'User-Agent':'My App','Content-Type':'application/json'}
log.setLevel(logging.DEBUG)

class Ownerrezapi(object):
    def __init__(self,username, token):
        self.username = username
        self.token = token
    
    
    def getproperties(self) -> list:

        restAdapt = RestAdapter(self.username,self.token)
        results = []
        property_list = restAdapt.get(endpoint='properties')
        for prop in property_list.data['items']:
            prop = Property(**prop)
            results.append(prop)
        return results

    def getbookings(self, property_id: int, since_utc: datetime) -> List[Booking]:
        """
        Get bookings for a property within a date range.
        """
        restAdapt = RestAdapter(self.username,self.token)
        results = []
        params = {'since_utc': since_utc, 'property_id': property_id}
        booking_list = restAdapt.get(endpoint='bookings', ep_params=params)
        

        for booking in booking_list.data['items']:
            booking = Booking(**booking)
            results.append(booking)
        return results
    
    def getbooking(self, booking_id: int) -> Booking:
        """
        Get a single booking by ID.
        """
        restAdapt = RestAdapter(self.username,self.token)
        booking = restAdapt.get(endpoint=f'bookings/{booking_id}')
        return Booking(**booking.data)