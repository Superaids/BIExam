import pandas as p
import re
import dateparser


# 11:42 - Har lige set at jeg ikke selv skulle lave
# "get_start_time" og "start_time_to_float" funktioner...
# Men det har jeg altså gjort, og spildt tid på det...

def get_start_time():

    path = "./scraped_events.csv"

    csv = p.read_csv(path, skiprows=1)

    date_column_only = csv.iloc[:, 2]

    for x in date_column_only:
        date_time_string = ""
        for temp in x:
            date_time_string = date_time_string + temp
            print(temp)

        print(date_time_string)

        split_on_comma = date_time_string.split(",")

        time_only = split_on_comma[1]

        time_only_split = time_only.split()

        print(time_only_split[1].replace(".", ""))
        if time_only_split[1].replace(".", "") == "pm":
            print(time_only_split[1])
            time = int(time_only_split[0]) + 12
            print(time*100)
            return time
        else:
            return time_only_split[0]

def start_time_to_float(time):
    to_float = float(time)
    print(to_float)
    return to_float


test = get_start_time()
print(test)
start_time_to_float(test)

def get_price(price_str):
    price_regexp = r"(?P<price>\d+)"
    if 'Free admission' in price_str:
        price = 0
    elif 'ratis' in price_str:
      price = 0
    else:
      m = re.search(price_regexp, price_str)
    try:
      price = int(m.group('price'))
    except:
      price = None
    return price


