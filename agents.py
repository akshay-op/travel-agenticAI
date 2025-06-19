from crewai import Agent
from llm_config import llmL33_70BV,llm3_70B8,llm31_8BI,llm4s17b16ei

def create_itinerary_agent():
    return Agent(
        role="Travel Itinerary Planner",
        goal="Create day-by-day travel itinerary based on destination and duration",
        backstory="Expert travel planner who creates efficient itineraries with key attractions and activities",
        llm=llm4s17b16ei,
        verbose=True,
        max_iter=4,
        memory=False
    )

def create_flight_agent():
    return Agent(
        role="Flight Booking Specialist",
        goal="Find and recommend best flight options for travel dates",
        backstory="Airline booking expert who finds optimal flights based on dates and budget",
        llm=llmL33_70BV,
        verbose=True,
        max_iter=4,
        memory=False
    )

def create_hotel_agent():
    return Agent(
        role="Hotel Booking Specialist", 
        goal="Find suitable accommodation based on itinerary locations",
        backstory="Hotel booking expert who matches accommodation to travel plans and budget",
        llm=llmL33_70BV,
        verbose=True,
        max_iter=4,
        memory=False
    )