from crewai import Task
from agents import trip_planner, transport_agent, stay_agent, weather_agent, budget_agent

trip_planner_task = Task(
    description="Plan a complete day-wise itinerary using info from other agents.",
    agent=trip_planner,
    expected_output="List format: Day-wise plan with place, activity, stay, transport, and key weather note.",
)

transport_task = Task(
    description="Find 3 good transport options from {start_location} to {destination} between {start_date} and {end_date}.",
    agent=transport_agent,
    expected_output="Short list: Mode, price (₹), time, and provider (max 3 entries).No explanation.",
)

stay_task = Task(
    description="Find 3 stays in {destination} for dates {start_date} to {end_date} within ₹{budget}.",
    agent=stay_agent,
    expected_output="Name, price/night (₹), area, and rating. Max 3 entries.No explanation.",
)

weather_task = Task(
    description="Get temperature, rain chance, and clothing advice for {destination} during the trip.",
    agent=weather_agent,
    expected_output="Temp range (°C), rain chance (%), and clothing tip.No explanation.",
)

budget_task = Task(
    description="Summarize total trip cost from transport and stay info. Suggest 1 cost-saving tip if needed.",
    agent=budget_agent,
    expected_output="Total cost (₹), per person (₹), and 1 cost-saving tip.No explanation.",
)
