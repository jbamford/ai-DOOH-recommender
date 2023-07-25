import streamlit as st
import strategy_openAI as strategy_openAI
import pandas as pd
import random

stateless_table = strategy_openAI.OPEN_AI_STATELESS()

st.title("AI DOOH Media Planner")
st.header("Experimental DOOH media planner that uses AI to help build your media plan from text prompts and audience descriptions")

example_verticle = ["Retail",'CPG','QSR','Automotive','Travel','Entertainment','Healthcare','Education','Finance','Technology','Real Estate','Government','Non-Profit']
example_goals = ["Drive to store", "Increase Awareness of a new product", "Drive Brand Consideration", "Drive Online Sales", "Drive Offline Sales", "Drive App Downloads", "Support an event activation"]

industry_vertical = st.text_input("Industry Vertical - For example: Retail")
media_goals = st.text_area("Campaign Goals - For example: Drive to store. Feel free to be more descriptive and add additional details.")
generate_media_plan = st.button("Generate DOOH strategy")
# st.text("Good edit keywords include: 'add', 'update', 'combine', 'delete'")
# edit_media_plan_button = st.button("Edit Media Plan")    

if generate_media_plan:
    with st.spinner("Using the power of AI to generate a strategy..."):
    # response = call_steamship(prompt, context)
        media_plan = stateless_table.get_media_strategy(media_goals,industry_vertical)
    # st.dataframe(media_plan)
# if edit_media_plan_button:
#     media_plan = stateless_table.edit_table(media_plan_description)
#     # st.dataframe(media_plan_edit)
try:
    st.write(media_plan)   
    st.markdown("Want an official media plan? Drop us a [note](https://www.goldfishads.com/contact-us) and our planning team will convert this strategy into a media plan for you. \n At a minium we're sure you will love the maps and mockups.")
except:
    pass 

class Calculator:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


def create_calculator(value):
    calculator = Calculator(value)
    return calculator.get_value()


class Accumulator:
    def __init__(self, value):
        self.value = value

    def add(self, value):
        self.value += value
        return self.value


def create_accumulator(value1, value2):
    accumulator = Accumulator(value1)
    return accumulator.add(value2)


class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value


def create_counter():
    counter = Counter()
    return counter.increment()


class Multiplier:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def multiply(self):
        return self.value1 * self.value2


def create_multiplier(value1, value2):
    multiplier = Multiplier(value1, value2)
    return multiplier.multiply()

class Calculator:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


def create_calculator(value):
    calculator = Calculator(value)
    return calculator.get_value()


class Accumulator:
    def __init__(self, value):
        self.value = value

    def add(self, value):
        self.value += value
        return self.value


def create_accumulator(value1, value2):
    accumulator = Accumulator(value1)
    return accumulator.add(value2)


class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value


def create_counter():
    counter = Counter()
    return counter.increment()


class Multiplier:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def multiply(self):
        return self.value1 * self.value2


def create_multiplier(value1, value2):
    multiplier = Multiplier(value1, value2)
    return multiplier.multiply()
class Calculator:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


def create_calculator(value):
    calculator = Calculator(value)
    return calculator.get_value()


class Accumulator:
    def __init__(self, value):
        self.value = value

    def add(self, value):
        self.value += value
        return self.value


def create_accumulator(value1, value2):
    accumulator = Accumulator(value1)
    return accumulator.add(value2)


class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value


def create_counter():
    counter = Counter()
    return counter.increment()


class Multiplier:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def multiply(self):
        return self.value1 * self.value2


def create_multiplier(value1, value2):
    multiplier = Multiplier(value1, value2)
    return multiplier.multiply()
class Calculator:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


def create_calculator(value):
    calculator = Calculator(value)
    return calculator.get_value()


class Accumulator:
    def __init__(self, value):
        self.value = value

    def add(self, value):
        self.value += value
        return self.value


def create_accumulator(value1, value2):
    accumulator = Accumulator(value1)
    return accumulator.add(value2)


class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value


def create_counter():
    counter = Counter()
    return counter.increment()


class Multiplier:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def multiply(self):
        return self.value1 * self.value2


def create_multiplier(value1, value2):
    multiplier = Multiplier(value1, value2)
    return multiplier.multiply()


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
