import datetime
from time import strftime


def main():
    print("Stock Data Unit Tests\n-------------------------\n")

    stock_symbol()
    chart_type()
    time_series()
    get_dates()


def stock_symbol():
    while True:
        stock = input("Enter the stock symbol you are looking for: ")

        # checks if stock is alphabetic and no more than 7 characters
        if stock.isalpha() and len(stock) <= 7:
            break
        else:
            print("Stock symbol must be alphabetic and 1-7 characters.")


def chart_type():
    print('Select 1 or 2 for Chart Type\n')
    print('1. Line')
    print('2. Bar')

    while True:
        try:
            graph_type = int(input('Your selection: '))
            if graph_type == 1 or graph_type == 2:
                break
            else:
                print("Please enter a valid input")
        except ValueError:
            print("Input must be a 1 or 2")


def time_series():
    print('Select the Time Series of the Chart You Wish to Generate\n')
    print('----------------------------------------------------------\n')
    print('1. Intraday')
    print('2. Daily')
    print('3. Weekly')
    print('4. Monthly')

    while True:
        try:
            time_type = int(input('Your selection: '))
            if time_type >= 1 and time_type <= 4:
                break
            else:
                print("Input must be an integer 1-4.")
                continue
        except ValueError:
            print("Input must be an integer 1-4.")


def get_dates():
    # While statement to loop until correct value is entered
    while (True):
        try:
            start = datetime.datetime.strptime(
                input("Please enter the start date (YYYY-MM-DD): "), '%Y-%m-%d')
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
            # continue
        else:
            break
    while (True):
        try:
            end = datetime.datetime.strptime(
                input("Please enter the end date (YYYY-MM-DD): "), '%Y-%m-%d')
            if (start >= end):
                print("End date must be AFTER the start date!")
                continue
        except ValueError:
            print("Invalid date, should be YYYY-MM-DD")
        else:
            break
    dates = [start, end]


main()
