import os

import functions as tf


class Timer():
    """checks input and send the shutdown signal"""

    def __init__(self):
        self.error_message = 'Incorrect input. Use hours:minutes. Returning to main menu'

    def start(self, duration, mode):
        time_remaining, shutdown_time = tf.time_remaining()
        if time_remaining <= 0:
            try:
                if tf.is_time(duration):
                    duration = tf.convert_time(duration)
                else:
                    duration = tf.convert_number(duration)
            except ValueError:
                print(self.error_message)
                return
            try:
                tf.write_time(duration)
                os.system('shutdown ' + mode + ' -t ' + str(duration))
                time_remaining, shutdown_time = tf.time_remaining()
                print(shutdown_time)
            except UnboundLocalError:
                print(self.error_message)
        else:
            print('Action already scheduled, please cancel it before trying to schedule another one.')
