# https://github.com/theOehrly/Fast-F1
# https://docs.fastf1.dev/core.html#fastf1.core.Laps

# Necessary Packages
import pandas as pd
import fastf1

# Load the 2021 Abu Dhabi Race
session = fastf1.get_session(2021, 'abudabi', 'Race')
session.load(weather=False, messages=False)

# Get the last lap data for position
ver_last_lap = session.laps.pick_lap(58).pick_driver('VER').get_pos_data()
ham_last_lap = session.laps.pick_lap(58).pick_driver('HAM').get_pos_data()

# Convert DataFrames into json to use
ver_last_lap.to_json('./static/ver_tele')
ham_last_lap.to_json('./static/ham_tele')