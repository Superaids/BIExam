import pandas as p

def get_start_time():

    path = "./scraped_events.csv"

    csv = p.read_csv(path, skiprows=1)

    date_column_only = csv.iloc[:, 2]

    for x in date_column_only:
        for temp in x:
            print(temp)
        split_on_comma = x.split()
        print("ass")
        for ass in split_on_comma:
            print(ass)
        split_on_spaces = split_on_comma.split()
        start_time = split_on_spaces[0]

        print(start_time)

        return start_time


test = get_start_time()
print(test)
