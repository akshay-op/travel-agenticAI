from crewai import Agent
from llm_config import llm 

# 1. Trip Planner Agent (the master agent)
trip_planner = Agent(
    role="Trip Planner",
    goal="Plan a personalized trip using other agents.",
    backstory="You create travel itineraries by coordinating with agents for transport, stay, weather, and budget.",
    allow_delegation=True,
    verbose=False,
    llm=llm
)

# 2. Transport Agent
transport_agent = Agent(
    role="Transport Agent",
    goal="Suggest top transport options within the user’s budget and timeframe.",
    backstory="You specialize in finding flights, trains, and buses for travelers.",
    verbose=False,
    llm=llm
)

# 3. Stay Agent
stay_agent = Agent(
    role="Stay Agent",
    goal="Suggest hotels or stays within budget and close to key locations.",
    backstory="You find stays via hotel APIs and travel platforms.",
    verbose=False,
    llm=llm
)


# 4. Weather Agent
weather_agent = Agent(
    role="Weather Agent",
    goal="Give weather forecast and clothing advice.",
    backstory="You use forecast data to advise on weather and packing.",
    verbose=False,
    llm=llm
)

# 5. Budget Agent
budget_agent = Agent(
    role="Budget Agent",
    goal="Estimate total trip cost and suggest savings if needed.",
    backstory="You review transport and stay data to give cost breakdown.",
    verbose=False,
    llm=llm
)

