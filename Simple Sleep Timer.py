import os
import time
import datetime

class Timer:
    '''Timer object, converts time, checks input and sends the shutdown signal'''

#Checks if input is in time format (hr:m)
    def is_time(t):
        try:
            t.index(':')
            return True
        except ValueError:
            return False

#Checks if input is number format (x.y hours)
    def is_number(t):
        try:
            float(t)
            return True
        except ValueError:
            return False

#Converts input in time format to seconds
    def convert_time(t):
        h, sep, m = str(t).partition(':')   #Seperates input as 2 variables and removes : (h, hours and m, minuts)
        s = abs(float(h))*3600+abs(float(m))*60
        s, sep, tail = str(s).partition('.')
        return s

#Converts number format to seconds
    def convert_number(t):
        t = abs(float(t))*3600
        t, sep, tail = str(t).partition('.')
        return t

#Writes shutdown time to file
    def write_time(t):
        timestamp = int(time.time()) + int(t)
        f = open('data-shutdown.txt', 'w')
        f.write(str(timestamp) + '\n')
        f.close

#Removes shutdown time from file
    def delete_time():
        shutdown_data = open('data-shutdown.txt').readlines()
        w = open('data-shutdown.txt', 'w')
        w.writelines([item for item in shutdown_data[:-1]])
        w.close

#Shutdown function, converts time and sends shutdown signal, takes 2 variables t (time in seconds) and m (mode)
    def shutdown(t, m):
        try:
            if Timer.is_time(t) == True:
                s = Timer.convert_time(t)
            elif Timer.is_number(t) == True:
                s = Timer.convert_number(t)
        except ValueError:
            print("Incorrect input. Use hours:minutes. Returning to main menu")
            return
        try:
            Timer.write_time(s)
            os.system("shutdown " + m + " -t " + str(s))
            time_remaining, shutdown_time = Timer.time_remaining()
            print(shutdown_time)
        except UnboundLocalError:
            print("Incorrect input. Use hours:minutes. Returning to main menu")

#Returns remaining time till shutdown
    def time_remaining():
        try:
            shutdown_data = open('data-shutdown.txt').readlines()
        except FileNotFoundError:
            return 0, "NaN"
        placer = len(shutdown_data) - 1
        try:
            shutdown_time = shutdown_data[placer]
        except IndexError:
            shutdown_time = 0
        current_time = int(time.time())
        time_remaining = int(shutdown_time) - current_time
        time_remaining = float(time_remaining)/60
        shutdown_time_human = datetime.datetime.fromtimestamp(
            int(shutdown_time)
        ).strftime('Shutting down at %H:%M:%S on %d-%m-%y')
        return time_remaining, shutdown_time_human

#---------------------------------Main------------------------------------------
welcome_message = 'Simple Sleep Timer (SST)\n\nAvailable commands:\nhours:minutes         - Shuts down the computer after the given time\nr, reboot or restart  - Enters reboot mode\nl, left or est        - Prints remaining time till shutdown\nc, cancel or abort    - Cancels previously scheduled action\ne, end or exit        - Exits the program'
print(welcome_message)
while 1 == 1:
    sleep_time = input('\nMenu: ')

#Shutdown mode. If the input is a time format or decimal number, shutdown is assumed as the desired mode
    if Timer.is_time(sleep_time) == True or Timer.is_number(sleep_time) == True:
        Timer.shutdown(sleep_time, "-s")

#Reboot mode
    elif sleep_time.lower() == "r" or sleep_time.lower() == "reboot" or sleep_time.lower() == "restart":  #Checks for the words r, reboot, or restart
        os.system('cls')
        print('Reboot mode')
        print('\nReboot commands:')
        print('hours:minutes    - Restarts the computer af the given time')
        print('Anything else    - Return to main menu')
        reboot_time = input('\nReboot mode: ')
        if Timer.is_time(reboot_time) == True or Timer.is_number(reboot_time) == True:
            Timer.shutdown(reboot_time, "-r")
            print('\nReturning to menu')
            time.sleep(1)
            os.system('cls')
            print(welcome_message)
        else:
            print('\nReturning to menu')
            time.sleep(.5)
            os.system('cls')
            print(welcome_message)

#Time remaining mode
    elif sleep_time.lower() == "l" or sleep_time.lower() == "left" or sleep_time.lower() == "est":
        remaining, shutdown_time = Timer.time_remaining()
        if remaining > 0:
            print("Time remaining: " + str(remaining) + " minutes till shutdown")
            print(shutdown_time)
        else:
            print("No shutdown scheduled")

#Cancel shutdown
    elif sleep_time.lower() == "c" or sleep_time.lower() == "cancel" or sleep_time.lower() == "abort":  #Checks for the words c, cancel, or abort
        remaining_time, shutdown_time = Timer.time_remaining()
        if remaining_time > 0:
            Timer.delete_time()
            os.system('shutdown -a')
            print('Scheduled action aborted')
        else:
            print("No shutdown Scheduled")

#Exit program
    elif sleep_time.lower() == "e" or sleep_time.lower() == "exit" or sleep_time.lower() == 'end':
        break
    else:
        print('Incorrect input. Use hours:minutes.')
