from crewai import Task
from agents import *

from crewai import Task

def create_itinerary_task(agent, destination, num_days):
    return Task(
        description=f"""Create a {num_days}-day itinerary for {destination}.
        Include:
        - Daily activities and attractions
        - Recommended areas to stay
        - Brief description of each day
        
        Keep it concise and practical.""",
        agent=agent,
        expected_output=f"Day-by-day itinerary for {num_days} days in {destination} with key locations and activities"
    )

def create_flight_task(agent, tools, origin, destination, departure_date, return_date):
    return Task(
        description=f"""Search for flights from {origin} to {destination}.
        Departure: {departure_date}
        Return: {return_date}
        Use IATA code of the airports near to {origin} and {destination} as input for the API for flight search.
        Find best options and provide summary.""",
        agent=agent,
        tools=tools,
        expected_output=f"Flight options from {origin} to {destination} with prices and times"
    )

def create_hotel_task(agent, tools, itinerary_context, checkin_date, checkout_date):
    return Task(
        description=f"""Based on the itinerary, search for hotels.
        Check-in: {checkin_date}
        Check-out: {checkout_date}
        
        Use itinerary locations to find suitable accommodation.
        Context: {itinerary_context}""",
        agent=agent,
        tools=tools,
        expected_output="Hotel recommendations with prices and locations matching the itinerary"
    )