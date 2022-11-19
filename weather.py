import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string)
  
    return(date.strftime("%A %d %B %Y"))


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    celsius = (float(temp_in_farenheit) - 32) * 5 / 9
    return round(celsius,1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    total = 0
    for x in weather_data:
        total += float(x)
    return total/len(weather_data)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    weather_data = []
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            if row == []:
                continue
            weather_data.append([row[0], float(row[1]), float(row[2])])
    return weather_data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if weather_data == []:
        return ()
    min_value = float(weather_data[0])
    min_index = 0
    
    for val in range(len(weather_data)):
        if float(weather_data[val]) <= min_value:
            min_value = float(weather_data[val])
            min_index = val
    results = (min_value , min_index)
    return results 

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if weather_data == []:
        return ()
    max_value = float(weather_data[0])
    max_index = 0
    
    for m_val in range(len(weather_data)):
        if float(weather_data[m_val]) >= max_value:
            max_value = float(weather_data[m_val])
            max_index = m_val
    results = (max_value , max_index)
    return results


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
    gen_summary = ""
    low = [] #contains all low temps
    high = [] #contins all high temps
    for row in weather_data:
        low.append(row[1]) #min temperatures
        high.append(row[2]) #max temperatures
    
    min_value, min_idx = find_min(low)
    max_value, max_idx = find_max(high)
    title  = f"{len(weather_data)} Day Overview\n"
    low_str =   f"  The lowest temperature will be {format_temperature(convert_f_to_c(min_value))}, and will occur on {convert_date(weather_data[min_idx][0])}.\n"
    high_str =  f"  The highest temperature will be {format_temperature(convert_f_to_c(max_value))}, and will occur on {convert_date(weather_data[max_idx][0])}.\n"
    ave_low =   f"  The average low this week is {format_temperature(convert_f_to_c(calculate_mean(low)))}.\n"
    ave_high =  f"  The average high this week is {format_temperature(convert_f_to_c(calculate_mean(high)))}.\n"
    gen_summary += title + low_str + high_str + ave_low + ave_high       
    return gen_summary


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    data = ""
    for row in weather_data:
        day =      f"---- {convert_date(row[0])} ----\n"
        min_temp = f"  Minimum Temperature: {format_temperature(convert_f_to_c(row[1]))}\n"
        max_temp = f"  Maximum Temperature: {format_temperature(convert_f_to_c(row[2]))}\n"
        data += day + min_temp + max_temp + "\n"
    return data
  
