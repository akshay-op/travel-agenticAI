from crewai.tools import tool
from apidata import Flight,Hotel

@tool("search_flights")
def search_flights(start_location: str, destination: str, start_date: str) -> str:
    """ fetch flight  based on the query."""

    flight = Flight( from_airport=start_location, to_airport=destination, date=start_date, adults=1)
    return (flight.flightsearch())

@tool("search_hotels")
def search_hotels(destination: str, start_date: str, end_date: str) -> str:
    """ fetch hotel  based on the query."""

    hotel = Hotel(destination,start_date,end_date)
    return (hotel.hotelsearch())


