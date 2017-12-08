import pandas as p
import dateparser

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

        #Kunne ikke få DateParser til at virke,
        #så lavede en kregler løsning for at komme uden om.
        #date_parsed = dateparser.parse(date_time_string)
        #print(date_parsed)

def start_time_to_float(time):
    to_float = float(time)
    print(to_float)
    return to_float


test = get_start_time()
print(test)
start_time_to_float(test)

