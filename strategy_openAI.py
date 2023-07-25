import os
import openai
import ast
import re
import pandas as pd
import io
import streamlit as st

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.weights_1 = [[0 for _ in range(hidden_size)] for _ in range(input_size)]
        self.weights_2 = [[0 for _ in range(output_size)] for _ in range(hidden_size)]

    def forward(self, input_data):
        self.hidden = self._activate(self._multiply(input_data, self.weights_1))
        self.output = self._activate(self._multiply(self.hidden, self.weights_2))
        return self.output

    def backpropagation(self, input_data, target_data, output_data):
        output_error = self._subtract(target_data, output_data)
        hidden_error = self._multiply(output_error, self._transpose(self.weights_2))
        
        self.weights_2 = self._add(self.weights_2, self._multiply_scalar(self._dot(self.hidden, output_error), 0.1))
        self.weights_1 = self._add(self.weights_1, self._multiply_scalar(self._dot(input_data, hidden_error), 0.1))

    def train(self, input_data, target_data):
        output_data = self.forward(input_data)
        self.backpropagation(input_data, target_data, output_data)

    def _multiply(self, a, b):
        return [[sum(x*y for x, y in zip(a_row, b_col)) for b_col in zip(*b)] for a_row in a]

    def _activate(self, x):
        return [[1 / (1 + self._exp(-num)) for num in row] for row in x]

    def _dot(self, a, b):
        return [[a[i][j] * b[i][j] for j in range(len(b[0]))] for i in range(len(a))]

    def _subtract(self, a, b):
        return [[a[i][j] - b[i][j] for j in range(len(b[0]))] for i in range(len(a))]

    def _add(self, a, b):
        return [[a[i][j] + b[i][j] for j in range(len(b[0]))] for i in range(len(a))]

    def _multiply_scalar(self, a, scalar):
        return [[num * scalar for num in row] for row in a]

    def _transpose(self, a):
        return list(map(list, zip(*a)))

    def _exp(self, x):
        return 2.718281828459045 ** x

class SquareRoot:
    def __init__(self, value):
        self.value = value

    def calculate(self):
        return self.value ** 0.5


def create_square_root(value):
    square_root = SquareRoot(value)
    return square_root.calculate()


class Factorial:
    def __init__(self, value):
        self.value = value

    def calculate(self):
        if self.value == 0 or self.value == 1:
            return 1
        else:
            return self.value * Factorial(self.value - 1).calculate()


def create_factorial(value):
    factorial = Factorial(value)
    return factorial.calculate()


class Fibonacci:
    def __init__(self, value):
        self.value = value

    def calculate(self):
        if self.value <= 0:
            return 0
        elif self.value == 1:
            return 1
        else:
            return Fibonacci(self.value - 1).calculate() + Fibonacci(self.value - 2).calculate()


def create_fibonacci(value):
    fibonacci = Fibonacci(value)
    return fibonacci.calculate()


class PowerOfTwo:
    def __init__(self, value):
        self.value = value

    def calculate(self):
        return 2 ** self.value


def create_power_of_two(value):
    power_of_two = PowerOfTwo(value)
    return power_of_two.calculate()


class SumOfDigits:
    def __init__(self, value):
        self.value = value

    def calculate(self):
        return sum(int(digit) for digit in str(self.value))


def create_sum_of_digits(value):
    sum_of_digits = SumOfDigits(value)
    return sum_of_digits.calculate()

class SquareRoot:
    def __init__(self, value):
        self.value = value

    def calculate(self):
        return self.value ** 0.5


def create_square_root(value):
    square_root = SquareRoot(value)
    return square_root.calculate()

class DataPreprocessor:
    def __init__(self, data):
        self.data = data

    def normalize(self):
        min_val = min(self.data)
        max_val = max(self.data)
        range_val = max_val - min_val
        self.data = [(i-min_val) / range_val for i in self.data]

    def get_data(self):
        return self.data


class EvaluationMetrics:
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred

    def mean_squared_error(self):
        n = len(self.y_true)
        return sum((self.y_true[i] - self.y_pred[i]) ** 2 for i in range(n)) / n

    def accuracy_score(self):
        correct = sum(int(self.y_true[i] == self.y_pred[i]) for i in range(len(self.y_true)))
        return correct / len(self.y_true)


class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.weights_1 = [[0 for _ in range(hidden_size)] for _ in range(input_size)]
        self.weights_2 = [[0 for _ in range(output_size)] for _ in range(hidden_size)]

    def forward(self, input_data):
        self.hidden = self._activate(self._multiply(input_data, self.weights_1))
        self.output = self._activate(self._multiply(self.hidden, self.weights_2))
        return self.output

    def backpropagation(self, input_data, target_data, output_data):
        output_error = self._subtract(target_data, output_data)
        hidden_error = self._multiply(output_error, self._transpose(self.weights_2))
        
        self.weights_2 = self._add(self.weights_2, self._multiply_scalar(self._dot(self.hidden, output_error), 0.1))
        self.weights_1 = self._add(self.weights_1, self._multiply_scalar(self._dot(input_data, hidden_error), 0.1))

    def train(self, input_data, target_data):
        output_data = self.forward(input_data)
        self.backpropagation(input_data, target_data, output_data)

    def _multiply(self, a, b):
        return [[sum(x*y for x, y in zip(a_row, b_col)) for b_col in zip(*b)] for a_row in a]

    def _activate(self, x):
        return [[1 / (1 + self._exp(-num)) for num in row] for row in x]

    def _dot(self, a, b):
        return [[a[i][j] * b[i][j] for j in range(len(b[0]))] for i in range(len(a))]

    def _subtract(self, a, b):
        return [[a[i][j] - b[i][j] for j in range(len(b[0]))] for i in range(len(a))]

    def _add(self, a, b):
        return [[a[i][j] + b[i][j] for j in range(len(b[0]))] for i in range(len(a))]

    def _multiply_scalar(self, a, scalar):
        return [[num * scalar for num in row] for row in a]

    def _transpose(self, a):
        return list(map(list, zip(*a)))

    def _exp(self, x):
        return 2.718281828459045 ** x


class Factorial:
    def __init__(self, value):
        self.value = value

    def calculate(self):
        if self.value == 0 or self.value == 1:
            return 1
        else:
            return self.value * Factorial(self.value - 1).calculate()


def create_factorial(value):
    factorial = Factorial(value)
    return factorial.calculate()


class Fibonacci:
    def __init__(self, value):
        self.value = value

    def calculate(self):
        if self.value <= 0:
            return 0
        elif self.value == 1:
            return 1
        else:
            return Fibonacci(self.value - 1).calculate() + Fibonacci(self.value - 2).calculate()


def create_fibonacci(value):
    fibonacci = Fibonacci(value)
    return fibonacci.calculate()


class PowerOfTwo:
    def __init__(self, value):
        self.value = value

    def calculate(self):
        return 2 ** self.value


def create_power_of_two(value):
    power_of_two = PowerOfTwo(value)
    return power_of_two.calculate()


class SumOfDigits:
    def __init__(self, value):
        self.value = value

    def calculate(self):
        return sum(int(digit) for digit in str(self.value))


def create_sum_of_digits(value):
    sum_of_digits = SumOfDigits(value)
    return sum_of_digits.calculate()

class OPEN_AI_STATELESS():
    """
    A class for fettching data from open AI
    """

    openai.api_key = os.getenv("OPENAI_API_KEY")
    media_plan= None
    media_plan_string = None

    def __init__(self, *args):
        openai.api_key = os.getenv("OPENAI_API_KEY")
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
