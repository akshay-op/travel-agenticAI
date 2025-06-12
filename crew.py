from crewai import Crew
from agents import trip_planner, transport_agent, stay_agent, weather_agent, budget_agent
from tasks import trip_planner_task, transport_task, stay_task, weather_task, budget_task


# Define your Crew
trip_planner_crew = Crew(
    agents=[
        trip_planner,
        transport_agent,
        # stay_agent,
        # weather_agent,
        budget_agent
    ],
    tasks=[
        trip_planner_task,
        transport_task,
        # stay_task,
        # weather_task,
        budget_task
    ],
    verbose=True
)

