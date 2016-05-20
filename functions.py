import datetime
import time
import os
from settings import Settings
settings = Settings()


# Checks if input is in time format (hr:m)
def is_time(u_input):
    try:
        u_input.index(':')
        return True
    except ValueError:
        return False


# Checks if input is number format (x.y hours)
def is_number(u_input):
    try:
        float(u_input)
        return True
    except ValueError:
        return False


# Converts input in time format to seconds
def convert_time(u_input):
    h, sep, m = str(u_input).partition(':')   # Seperates input as 2 variables and removes : (h, hours and m, minuts)
    s = abs(float(h))*3600+abs(float(m))*60
    s, sep, tail = str(s).partition('.')
    return s


# Converts number format to seconds
def convert_number(number):
    number = abs(float(number)) * 3600
    number, sep, tail = str(number).partition('.')
    return number


# Writes shutdown time to file
def write_time(duration):
    timestamp = int(time.time()) + int(duration)
    f = open('data-shutdown.txt', 'w')
    f.write(str(timestamp) + '\n')


# Removes shutdown time from file
def delete_time():
    shutdown_data = open('data-shutdown.txt').readlines()
    w = open('data-shutdown.txt', 'w')
    w.writelines([item for item in shutdown_data[:-1]])


# Returns remaining time till shutdown
def time_remaining():
    try:
        shutdown_data = open('data-shutdown.txt').readlines()
    except FileNotFoundError:
        return 0, 'NaN'
    placer = len(shutdown_data) - 1
    try:
        scheduled_action_time = shutdown_data[placer]
    except IndexError:
        scheduled_action_time = 0
    current_time = int(time.time())
    time_remaining = int(scheduled_action_time) - current_time
    time_remaining = float(time_remaining) / 60
    shutdown_time_human = datetime.datetime.fromtimestamp(
        int(scheduled_action_time)
    ).strftime('Shutting down at %H:%M:%S on %d-%m-%y')
    return time_remaining, shutdown_time_human


# Menu return
def menu_return(delay):
    print('\nReturning to menu')
    time.sleep(delay)
    os.system('cls')
    print(settings.welcome_message)
