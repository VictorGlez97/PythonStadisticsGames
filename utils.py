import csv
from datetime import datetime

def get_data():

    path = './project/MEX.csv'
    data = []

    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        header = next(reader)


        for row in reader:
            game_dict = { key: value for key, value in zip(header, row) if key == 'Home' or key == 'Away' or key == 'Country' or key == 'League' or key == 'Season' or key == 'Date' or key == 'Time' or key == 'HG' or key == 'AG' or key == 'Res' }
            data.append(game_dict)

    return data

def filters(item):
    League, Country = item
    print(League)
    print(Country)
    return League == 'Liga MX'


def filter_games_vs_last_teen(home, away):

    minimun_year = 2020
    data = get_data()
    # print(data)
    teams_filtered_item = list(filter(lambda item: ((item['Away'] == away and item['Home'] == home) or (item['Away'] == home and item['Home'] == away)) and (datetime.strptime(item['Date'], '%d/%m/%Y').year >= minimun_year), data))    

    print(teams_filtered_item)

    more_one = 0
    more_two = 0
    both_goal = 0

    for game in teams_filtered_item:

        if (int(game['HG']) + int(game['AG'])) > 1:
            more_one = more_one + 1

        if (int(game['HG']) + int(game['AG'])) > 2:
            more_two = more_two + 1

        if (int(game['HG']) >= 1) and (int(game['AG']) >= 1):
            both_goal = both_goal + 1

    # filtered_by_time = list(filter(filters, data))
    # print(teams_filtered_item)
    # teams_filtered = dict(teams_filtered_item)

    return more_one, more_two, both_goal


def increment(x):
    return x + 1

