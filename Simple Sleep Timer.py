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
        h = abs(float(h))
        m = abs(float(m))
        s = (h*3600)+(m*60)
        s, sep, tail = str(s).partition('.')
        return s

#Converts number format to seconds
    def convert_number(t):
        t = abs(float(t))
        t = t*3600
        t, sep, tail = str(t).partition('.')
        return t

#Writes shutdown time to file
    def write_time(t):
        timestamp = int(time.time())
        timestamp = timestamp + int(t)
        print('Writing shutdown time to file...')
        f = open('data-shutdown.txt', 'w')
        f.write(str(timestamp))
        f.write('\n')
        f.close
        print("Done!\n")

#Shutdown function, converts time and sends shutdown signal, takes 2 variables t (time in seconds) and m (mode)
    def shutdown(t, m):
        try:
            if Timer.is_time(t) == True:
                s = Timer.convert_time(t)
            elif Timer.is_number(t) == True:
                s = Timer.convert_number(t)
        except ValueError:
            print("Incorrect input. Use hours:minutes")
        try:
            Timer.write_time(s)
            os.system("shutdown " + m + " -f -t " + str(s))
        except UnboundLocalError:
            print("Incorrect input. Use hours:minutes. Returning to main menu")

#Returns remaining time till shutdown
    def time_remaining():
        shutdown_data = open('data-shutdown.txt').readlines()
        placer = len(shutdown_data) - 1
        shutdown_time = shutdown_data[placer]
        current_time = int(time.time())
        time_remaining = int(shutdown_time) - current_time
        time_remaining = float(time_remaining)/60
        shutdown_time_human = datetime.datetime.fromtimestamp(
            int(shutdown_time)
        ).strftime('Shutting down at: %H:%M:%S on %d-%m-%y')
        return time_remaining, shutdown_time_human

#Cancels current shutdown scheduled
    def cancel_shutdown():
        print('Removing shutdown entry')
        shutdown_data = open('data-shutdown.txt').readlines()
        w = open('data-shutdown.txt', 'w')
        w.writelines([item for item in shutdown_data[:-1]])
        w.close
        os.system('shutdown -a')
        print('\nScheduled action aborted')

#---------------------------------Main------------------------------------------

print('\nSimple Sleep Timer (SST)\n\nAvailable commands:\nhours:minutes         - Shuts down the computer after the given time\nr, reboot or restart  - Enters reboot mode\nl, left or est        - Prints remaining time till shutdown\nc, cancel or abort    - Cancels previously scheduled action\ne, end or exit        - Exits the program')
while 1 == 1:
    sleep_time = input('\nTime till shutdown: ')

#Shutdown mode. If the input is a time format or decimal number, shutdown is assumed as the desired mode
    if Timer.is_time(sleep_time) == True or Timer.is_number(sleep_time) == True:
        Timer.shutdown(sleep_time, "-s")

#Reboot mode
    elif sleep_time.lower() == "r" or sleep_time.lower() == "reboot" or sleep_time.lower() == "restart":  #Checks for the words r, reboot, or restart
        os.system("cls")
        print('Simple Sleep Timer (SST)')
        print('Rebboot mode\n')
        reboot_time = input('Time til reboot: ')
        Timer.shutdown(reboot_time, "-r")

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
        Timer.cancel_shutdown()

#Exit program
    elif sleep_time.lower() == "e" or sleep_time.lower() == "exit" or sleep_time.lower() == 'end':
        break
    else:
        print('Incorrect input')
