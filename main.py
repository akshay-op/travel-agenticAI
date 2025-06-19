# # main.py
# import config  # This sets up the environment
# from crew import FlightCheckerCrew
# import sys
# from datetime import datetime, timedelta

# def validate_date(date_string):
#     """Validate date format YYYY-MM-DD"""
#     try:
#         datetime.strptime(date_string, '%Y-%m-%d')
#         return True
#     except ValueError:
#         return False

# def get_user_input():
#     """Get flight search parameters from user"""
#     print("🛫 AI Flight Checker")
#     print("=" * 40)
    
#     # Get cities
#     from_city = input("From city: ").strip()
#     to_city = input("To city: ").strip()
    
#     if not from_city or not to_city:
#         print("❌ Both cities are required!")
#         return None, None, None
    
#     # Get travel date (optional)
#     date_input = input("Travel date (YYYY-MM-DD) [optional]: ").strip()
#     travel_date = None
    
#     if date_input:
#         if validate_date(date_input):
#             travel_date = date_input
#         else:
#             print("⚠️ Invalid date format. Proceeding without specific date.")
    
#     return from_city, to_city, travel_date

# def main():
#     """Main application function"""
#     try:
#         print("🚀 Initializing Flight Checker AI...")
        
#         # Initialize the crew
#         flight_crew = FlightCheckerCrew()
        
#         # Option 1: Interactive mode
#         if len(sys.argv) == 1:
#             from_city, to_city, travel_date = get_user_input()
#             if not from_city or not to_city:
#                 return
        
#         # Option 2: Command line arguments
#         elif len(sys.argv) >= 3:
#             from_city = sys.argv[1]
#             to_city = sys.argv[2]
#             travel_date = sys.argv[3] if len(sys.argv) > 3 else None
            
#             if travel_date and not validate_date(travel_date):
#                 print("❌ Invalid date format. Use YYYY-MM-DD")
#                 return
        
#         else:
#             print("Usage: python main.py [from_city] [to_city] [travel_date]")
#             print("Or run without arguments for interactive mode")
#             return
        
#         # Search flights
#         print(f"\n🔍 Searching flights from {from_city} to {to_city}...")
#         if travel_date:
#             print(f"📅 For date: {travel_date}")
        
#         result = flight_crew.search_flights(from_city, to_city, travel_date)
        
#         print("\n" + "="*80)
#         print("✈️ FLIGHT SEARCH RESULTS")
#         print("="*80)
#         print(result)
#         print("="*80)
        
#     except KeyboardInterrupt:
#         print("\n\n👋 Flight search cancelled by user")
#     except Exception as e:
#         print(f"\n❌ An error occurred: {str(e)}")
#         print("Please check your configuration and try again")

# def demo():
#     """Run a demo search"""
#     print("🎯 Running Demo Flight Search...")
    
#     # Demo parameters
#     demo_searches = [
#         ("Mumbai", "Delhi", "2025-07-15"),
#         ("Bangalore", "Chennai", None),
#         ("New York", "Los Angeles", "2025-08-01")
#     ]
    
#     flight_crew = FlightCheckerCrew()
    
#     for from_city, to_city, travel_date in demo_searches:
#         print(f"\n{'='*60}")
#         print(f"🛫 Demo: {from_city} → {to_city}")
#         if travel_date:
#             print(f"📅 Date: {travel_date}")
#         print('='*60)
        
#         result = flight_crew.search_flights(from_city, to_city, travel_date)
#         print(result)
#         print("\n" + "🔄 Next search in 3 seconds...")
#         import time
#         time.sleep(3)

# if __name__ == "__main__":
#     # Uncomment the line below to run demo instead
#     # demo()
    
#     main()









import os
from datetime import datetime
from crew import TravelPlanningCrew

def main():
    # Set up environment variables
    # if not os.getenv("GROQ_API_KEY"):
    #     print("Please set GROQ_API_KEY environment variable")
    #     return
    
    # Get user input
    print("=== Travel Planning Assistant ===")
    
    origin = input("Enter your current location: ").strip()
    destination = input("Enter your destination: ").strip()
    departure_date = input("Enter departure date (YYYY-MM-DD): ").strip()
    return_date = input("Enter return date (YYYY-MM-DD): ").strip()
    num_days = input("Enter number of days: ").strip()
    
    # Validate inputs
    if not all([origin, destination, departure_date, return_date, num_days]):
        print("All fields are required!")
        return
    
    try:
        num_days = int(num_days)
        # Basic date validation
        datetime.strptime(departure_date, "%Y-%m-%d")
        datetime.strptime(return_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format or number of days!")
        return
    
    print(f"\nPlanning your {num_days}-day trip from {origin} to {destination}")
    print(f"Departure: {departure_date}, Return: {return_date}")
    print("\nProcessing... This may take a few minutes.\n")
    
    # Create crew and plan travel
    travel_crew = TravelPlanningCrew()
    
    try:
        result = travel_crew.plan_travel(
            origin=origin,
            destination=destination,
            departure_date=departure_date,
            return_date=return_date,
            num_days=num_days
        )
        
        print("=== Travel Plan Results ===")
        print(result)
        
    except Exception as e:
        print(f"Error planning travel: {str(e)}")

if __name__ == "__main__":
    main()
     
#     # Quick test
#     # from agents import create_hotel_agent
#     # from apitools import search_hotels
#     # from crewai import Task, Crew

#     from agents import create_flight_agent
#     from apitools import search_flights
#     from crewai import Task, Crew

    
# #     # itinerary_context ="""   
# #     #     **Day 1: Arrival and Exploring South Mumbai**                                                                                                     
# #     #     Arrive in Mumbai and check-in to a hotel in the Colaba or Fort area, which offers easy access to major attractions. Visit the Gateway of India, a 
# #     #     iconic landmark, and take a stroll along the Marine Drive. In the evening, explore the Colaba Causeway for shopping and dining.

# #     #     **Day 2: Mumbai's Cultural Heritage**
# #     #     Start the day with a visit to the Chhatrapati Shivaji Maharaj Vastu Sangrahalaya (CSMVS) museum, which showcases Indian art and culture. Next,    
# #     #     head to the Haji Ali Dargah, a historic mosque located on an islet off the coast of Worli. End the day with a visit to the Dhobi Ghat, a massive  
# #     #     open-air laundry facility.

# #     #     **Day 3: Bollywood and Shopping**
# #     #     Dedicate the day to exploring Mumbai's famous film industry, Bollywood. Take a guided tour of a film studio, such as the Film City or the RK      
# #     #     Studios. In the evening, visit the Linking Road or the High Street Phoenix for shopping and entertainment.

# #     #     **Day 4: Beaches and Street Food**
# #     #     Spend the day relaxing on the beaches of Mumbai, such as the Juhu Beach or the Versova Beach. Try some street food, like vada pav, pani puri, or  
# #     #     bhel puri, at the beach or at a street food stall. In the evening, visit the Carter Road or the Bandra Fort for a beautiful sunset view.

# #     #     **Day 5: Elephanta Caves and Harbor**
# #     #     Take a ferry to the Elephanta Caves, a UNESCO World Heritage Site, located on an island in the Arabian Sea. The caves feature ancient rock-cut    
# #     #     temples and sculptures. Return to Mumbai in the evening and explore the harbor area, including the Sassoon Docks and the Naval Dockyard.

# #     #     **Day 6: Sanjay Gandhi National Park**
# #     #     Visit the Sanjay Gandhi National Park, a large national park located in the northern part of Mumbai. Take a trek or a safari to explore the park's
# #     #     flora and fauna, which includes lions, tigers, and crocodiles. In the evening, visit the Gorai Beach or the Manori Beach for a peaceful evening.  

# #     #     **Day 7: Departure**
# #     #     Spend the morning shopping for souvenirs or visiting any last-minute attractions. Depart for the airport and head back home, bringing back        
# #     #     memories of the vibrant city of Mumbai.

# #     #     **Recommended Areas to Stay:**
# #     #     - Colaba: Known for its iconic Gateway of India and vibrant nightlife.
# #     #     - Fort: A historic area with many attractions, including the CSMVS museum.
# #     #     - Bandra: A trendy area with many restaurants, bars, and shopping centers.
# #     #     - Juhu: A beachside area with many hotels and restaurants.

# #     #     **Daily Activities and Attractions:**
# #     #     - Gateway of India
# #     #     - Marine Drive
# #     #     - Colaba Causeway
# #     #     - Chhatrapati Shivaji Maharaj Vastu Sangrahalaya (CSMVS) museum
# #     #     - Haji Ali Dargah
# #     #     - Dhobi Ghat
# #     #     - Film City or RK Studios
# #     #     - Linking Road or High Street Phoenix
# #     #     - Juhu Beach or Versova Beach
# #     #     - Elephanta Caves
# #     #     - Sassoon Docks and Naval Dockyard
# #     #     - Sanjay Gandhi National Park
# #     #     - Gorai Beach or Manori Beach

# #     #     This 7-day itinerary provides a mix of culture, history, entertainment, and relaxation, and is a great way to experience the vibrant city of      
# #     #     Mumbai."""
# #     itinerary_context = """
# #     Plan hotel stays in Mumbai from Day 1 to Day 7. Preferred areas to stay: Colaba, Fort, Bandra, or Juhu. Prioritize proximity to main attractions like Gateway of India, Marine Drive, Juhu Beach, and cultural sites. Budget and comfort should be balanced. Return top 3 stay options with price, rating, and area.


# # """

    
#     agent = create_flight_agent()
#     tool = search_flights
#     task = Task(

#         # description=f"""Search for flights from bangalore to bombay.
#         # Departure: "2025-06-25"        
#         # Find best options and provide summary.""",
#         # agent=agent,
#         # tools=[tool],
#         # expected_output=f"Flight options from bangalore to bombay with prices and times"

#         description=f"""Search for flights from Bangalore to Bombay.
#         Departure: "2025-06-25"
#         Return: "2025-07-1"
#         Use IATA code of the airports near to these cities as input for the API for flight search.
#         Find best options and provide summary.""",
#         agent=agent,
#         tools=[tool],
#         expected_output=f"Flight options from Bangalore to Bombay with prices and times"




#         # description=f"""Based on the itinerary, search for hotels.        
#         # Use itinerary locations to find suitable accommodation.
#         # Context: {itinerary_context}""",
#         # agent=agent,
#         # tools=[tool],
#         # expected_output="Hotel recommendations with prices and locations matching the itinerary"



#     )
#     # crew = Crew(agents=[agent], tasks=[task], verbose=True)
#     crew = Crew(agents=[agent], tasks=[task])
#     print(crew.kickoff())


