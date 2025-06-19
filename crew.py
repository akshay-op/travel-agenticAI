from crewai import Crew, Process
from agents import create_itinerary_agent, create_flight_agent, create_hotel_agent
from tasks import create_itinerary_task, create_flight_task, create_hotel_task
from apitools import search_flights, search_hotels

class TravelPlanningCrew:
    def __init__(self):
        self.flight_tool = search_flights
        self.hotel_tool = search_hotels
        
    def plan_travel(self, origin, destination, departure_date, return_date, num_days):
        # Create agents
        itinerary_agent = create_itinerary_agent()
        flight_agent = create_flight_agent()
        hotel_agent = create_hotel_agent()
        
        # Create tasks
        itinerary_task = create_itinerary_task(itinerary_agent, destination, num_days)
        
        flight_task = create_flight_task(
            flight_agent, 
            [self.flight_tool], 
            origin, 
            destination, 
            departure_date, 
            return_date
        )
        
        hotel_task = create_hotel_task(
            hotel_agent,
            [self.hotel_tool],
            "Will be provided by itinerary task",
            departure_date,
            return_date
        )
        
        # Create crew
        crew = Crew(
            agents=[itinerary_agent, flight_agent, hotel_agent],
            tasks=[itinerary_task, flight_task, hotel_task],
            process=Process.sequential,
            verbose=True
        )
        
        # Execute
        result = crew.kickoff()
        return result