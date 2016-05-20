import os

import functions as tf
from timer import Timer
from settings import Settings

timer = Timer()
timer_settings = Settings()

print(timer_settings.welcome_message)

while True:

    user_input = input('\nMenu: ')

    # Shutdown mode
    if tf.is_time(user_input) or tf.is_number(user_input):
        timer.start(user_input, '-s')

    # Reboot Mode
    elif user_input.lower() == 'r' or user_input.lower() == 'reboot' or user_input.lower() == 'restart':
        reboot_menu = timer_settings.reboot_menu
        os.system('cls')
        print(reboot_menu)
        user_input = input('\nReboot mode: ')
        if tf.is_time(user_input) or tf.is_time(user_input):
            timer.start(user_input, '-r')
            tf.menu_return(1)
        else:
            tf.menu_return(0.5)

    # Print remaining time
    elif user_input.lower() == 'l' or user_input.lower() == 'left' or user_input.lower() == 'est':
        remaining_time, shutdown_time = tf.time_remaining()
        if remaining_time > 0:
            print('Time remaining: ' + str(remaining_time) + ' minutes till shutdown')
            print(shutdown_time)
        else:
            print('No shutdown Scheduled')

    # Cancel shutdown.
    elif user_input.lower() == 'c' or user_input.lower() == 'cancel' or user_input.lower() == 'abort':
        remaining_time, shutdown_time = tf.time_remaining()
        if remaining_time > 0:
            tf.delete_time()
            os.system('shutdown -a')
            print('Scheduled action aborted')
        else:
            print('No shutdown scheduled')
    # Exit program
    elif user_input.lower() == 'e' or user_input.lower() == 'exit' or user_input.lower() == 'end':
        break

    else:
        print('Incorrect input. Use hours:minutes')
