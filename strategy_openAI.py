import os
import openai
import ast
import re
import pandas as pd
import io
import streamlit as st


class OPEN_AI_STATELESS():
    """
    A class for fettching data from open AI
    """

    openai.api_key = os.getenv("OPENAI_API_KEY")
    media_plan= None
    media_plan_string = None

    def __init__(self, *args):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.VENUE_TYPES = """
                Transit|Airports- Screens located throughout terminals in arrival and departure areas, ticketing areas, baggage claim, gate-hold rooms, concourses, retail shops, and VIP lounges.
                Transit|Buses- Screens located on or in city or intercity buses.
                Transit|Taxi & Rideshare- TV	Screens inside taxis and rideshare vehicles visible to passengers in the back seat.
                Transit|Taxi & Rideshare Top- screens placed on top of taxi and rideshare vehicles visible to nearby pedestrian and drivers.
                Transit|Subway- screens placed inside subway trains or inside stations or on subway platforms.
                Transit|Train Stations- Screens placed inside train stations or on platforms.
                Retail|Gas Stations- Screens on gas station pumps and in gas stations
                Retail|Convenience Stores- Screen located on top of ATM machines, at the checkout, or in the isle of convenience stores
                Retail|Grocery- Screens placed in store isles and at the checkout of grocery and supermarket locations
                Retail|Liquor Stores- Screens placed in store isles and at the checkout of retail locations primarily selling alcoholic products
                Retail|Mall- Screens placed in concourses/walkways, outside retail stores, and in food courts in shopping malls
                Retail|Dispensaries- Screens places in retail stores that sell and dispenses cannabis and CBD products.
                Retail|Pharmacies- Screens on top health kiosks in pharmacies and next to pharmacy pick up counters
                Retail|Parking Garages- Screens on the ground floor or near entrances of parking garages
                Outdoor|Billboards- Large format screens on the side of roads easily viewable for people driving past them
                Outdoor|Urban Panels- Screens that are visible to pedestrians located on the sidewalk of cities and outside entrances of retail locations in shopping plazas
                Outdoor|Bus Shelters- Screens on the side of enclosures at bus stops, typically in urban environments. Screens may be on the interior or exterior of the enclosure.
                Health & Beauty|Gyms- Screens located at the entrance, above workout machine and weights, and locker rooms of gyms
                Health & Beauty|Salons- Screens placed on walls in hair and nail salons where customers can easily view the screens
                Health & Beauty|Spas- Screens placed on walls in spas where customers can easily view the screens
                Point of Care|Doctor’s Offices- Screens located in waiting rooms, hallways and exam rooms of Doctor's offices, non-hospital facility run by a physician
                Point of Care|Veterinary Offices- Screens located in waiting rooms of Veterinary Offices
                Education|Colleges and Universities- Screens located in book stores, rec centers, and study areas of higher education institutions
                Office Buildings|Office Buildings- Screens located in lobbies, common spaces, and elevators of office buildings
                Entertainment|Recreational Locations- Screens located in recreational locations, ex: art centers, indoor skating parks, arcade, indoor trampoline, ax thowirng, and more
                Entertainment|Movie Theaters- Screens placed in lobbies, concession, and ticket areas of movie theaters
                Entertainment|Sports Entertainment- Screens located in places where sports are played ex: TopGolf, golf courses, bowling alleys, c centers, arcades, and more
                Entertainment|Bars- Screens on TVs around the bar and on jukeboxes at establishments that predominantly serve alcoholic beverages.
                Entertainment|Casual Dining- Screens on TVs throughout restaurants and on jukeboxes in establishments that predominantly serve food in a casual atmosphere
                Entertainment|QSR- Screens on TVs at checkout, in line, and near tables in fast food restaurants
                Entertainment|Hotels- Screens in lobbies and near elevator entrances of hotels
                Residential|Apartment Buildings- Screens placed in lobbies, common areas, and elevators of apartment complexes
                """
        self.valid_venue_types = ['Transit|Airports', 'Transit|Buses', 'Transit|Taxi & Rideshare', 'Transit|Taxi & Rideshare Top', 'Transit|Subway', 'Transit|Train Stations', 'Retail|Gas Stations', 'Retail|Convenience Stores', 'Retail|Grocery', 'Retail|Liquor Stores', 'Retail|Mall', 'Retail|Dispensaries', 'Retail|Pharmacies', 'Retail|Parking Garages', 'Outdoor|Billboards', 'Outdoor|Urban Panels', 'Outdoor|Bus Shelters', 'Health & Beauty|Gyms',
                                  'Health & Beauty|Salons', 'Health & Beauty|Spas', 'Point of Care|Doctor’s Offices', 'Point of Care|Veterinary Offices', 'Education|Colleges and Universities', 'Office Buildings|Office Buildings', 'Entertainment|Recreational Locations', 'Entertainment|Movie Theaters', 'Entertainment|Sports Entertainment', 'Entertainment|Bars', 'Entertainment|Casual Dining', 'Entertainment|QSR', 'Entertainment|Hotels', 'Residential|Apartment Buildings']

        

    def get_media_strategy(self,goal,vertical):
        """
        makes a request to chat to replace the venue types with the most relevant valid one
        """
        # response_geo_list = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        response_geo_list = openai.ChatCompletion.create(model="gpt-4", messages=[
            {"role": "system", "content": "You are a helpful digital out of home media planner"},

            {"role": "user", "content": """Below are the possible digital out of home targeting tactics. Based on the below tactics recommend a list of relevant strategies for a given advertiser and goal that can use these tactics.  You do not need to use all of these tactics. Please only include the ones you think will be the most valuable for the brand.
                DOOH Targeting tactics: 
                - Audience Targeting
                    - 1st Party Data
                    - 3rd Party Data
                        - Demographics
                        - Household 
                        - Behaviors
                        - Interests
                        - Life Events
                        - etc   
                - Geo Targeting
                    - Administrative boundaries - DMA, City, Zip, Address,
                    - Radius around a point Radius, Lat/Long
                    - Custom Geofences - Along highways, neighborhoods, etc
                    - Spacial indexing - Find screens in-between two points with a certain overlaps
                - Venue Type Targeting
                    - Day/Week Parting to reach certain audiences on the venue types       
                - Event Targeting
                - Picking specific locations in retail
             
             Note: when recommending venue type targeting you can only use the following valid venue types:{}
             """.format(self.valid_venue_types)},
            {"role": "assistant", "content": "Ok, I will use those tactics and recommend relevant DOOH strategies"},
            # {"role": "assistant", "content": "Ok, I will respond with a CSV as requested with the headers:\nGeo / Targeting,DOOH Venue Types, Flights"},

            {"role": "user", "content": "Great, please generate a strategy for brand in the {} vertical looking to {}".format(vertical, goal)},
            # {"role": "assistant", "content": "Ok, I will respond with a CSV as requested with the headers:\nGeo / Targeting,DOOH Venue Types, Flights and I will only suggest valid venue types: Transit|Airports, Transit|Buses, Transit|Taxi & Rideshare, Transit|Taxi & Rideshare Top, Transit|Subway, Transit|Train Stations, Retail|Gas Stations, Retail|Convenience Stores, Retail|Grocery, Retail|Liquor Stores, Retail|Mall, Retail|Dispensaries, Retail|Pharmacies, Retail|Parking Garages, Outdoor|Billboards, Outdoor|Urban Panels, Outdoor|Bus Shelters, Health & Beauty|Gyms, Health & Beauty|Salons, Health & Beauty|Spas, Point of Care|Doctor’s Offices, Point of Care|Veterinary Offices, Education|Colleges and Universities, Office Buildings|Office Buildings, Entertainment|Recreational Locations, Entertainment|Movie Theaters, Entertainment|Sports Entertainment, Entertainment|Bars, Entertainment|Casual Dining, Entertainment|QSR, Entertainment|Hotels, Residential|Apartment Buildings"},


        ]
        )

        print(response_geo_list)
        # list_response_string = re.search(r"\[.*?\]",response_geo_list["choices"][0]['message']['content'] )
        # list_response_list= ast.literal_eval(list_response_string.group())

        # todo validate that it is in fact a list
        # return list_response_list
        # df = pd.read_csv(io.StringIO(
        #     response_geo_list["choices"][0]['message']['content']))

        # print(df)
        # df.to_csv("tmp/test.csv")
       
        # self.current_media_plan = response_geo_list["choices"][0]['message']['content']

        # OPEN_AI_STATELESS.media_plan=df
        # OPEN_AI_STATELESS.media_plan_description=response_geo_list["choices"][0]['message']['content'] 
        
        # print("state status\n",OPEN_AI_STATELESS.media_plan,"\n", OPEN_AI_STATELESS.media_plan_description)

        return(response_geo_list["choices"][0]['message']['content'])

     

if __name__ == '__main__':
    openai_class = OPEN_AI_STATELESS()
    # openai_class.extract_venue_types(
    #     "The client wants to reach people that go to the gym and salon")
    # openai_class.validate_actual_venue_types(['gym', 'mall', 'airport'])

    # openai_class.get_media_plan()
    openai_class.get_media_strategy("increase sales", "retail")

    # s = "Here's the list of closest matching valid venue types ['Health & Beauty|Gyms', 'Retail|Mall', 'Transit|Airports'] hi world"
    # list_response_string = re.search(r"\[.*?\]",s)
    # print(list_response_string.group())



"""
DOOH Targeting that an advertiser can use

- Audience Targeting
    - 1st Party Data
    - 3rd Party Data
        - Demographics
        - Household 
        - Behaviors
        - Interests
        - Life Events
        - etc   
- Geo Targeting
    - Administrative boundaries - DMA, City, Zip, Address,
    - Radius around a point Radius, Lat/Long
    - Custom Geofences - Along highways, neighborhoods, etc
    - Spacial indexing - Find screens in-between two points with a certain overlaps
- Venue Type Targeting
    - Day/Week Parting to reach certian audinces on the venue types       
- Event Targeting
- Picking specific locations in retail


Strategy:




setup : You are a helpful Digital out of home  (DOOH)planning expert 


Here are the possible DOOH targeting tactics. Based on the below tactics recommend a list of relevant strategies for a given advertiser and goal that can use these tactics. 

DOOH Targeting tactics: 
- Audience Targeting
    - 1st Party Data
    - 3rd Party Data
        - Demographics
        - Household 
        - Behaviors
        - Interests
        - Life Events
        - etc   
- Geo Targeting
    - Administrative boundaries - DMA, City, Zip, Address,
    - Radius around a point Radius, Lat/Long
    - Custom Geofences - Along highways, neighborhoods, etc
    - Spacial indexing - Find screens in-between two points with a certain overlaps
- Venue Type Targeting
    - Day/Week Parting to reach certian audinces on the venue types       
- Event Targeting
- Picking specific locations in retail


assiant: Ok, I will use those tactics and recommend creative dooh strategies
"""