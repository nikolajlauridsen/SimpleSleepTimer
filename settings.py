class Settings():
    """A class for storing the settings for SST."""

    def __init__(self):
        """Initialize the program's settings."""

        self.welcome_message = 'Simple Sleep Timer (SST)\n\nAvailable commands:' \
                               '\nhours:minutes         - Shuts down the computer after the given time' \
                               '\nr, reboot or restart  - Enters reboot mode' \
                               '\nl, left or est        - Prints remaining time till shutdown' \
                               '\nc, cancel or abort    - Cancels previously scheduled action' \
                               '\ne, end or exit        - Exits the program'

        self.reboot_menu = 'Reboot mode\n\nReboot commands:' \
                           '\nhours:minutes    - Restarts the computer af the given time' \
                           '\nAnything else    - Return to main menu'

        self.reboot_commands = [
            'r',
            'reboot',
            'restart'
        ]

        self.r_time_commands = [
            'l',
            'left',
            'est',
            'time left'
        ]

        self.cancel_commands = [
            'c',
            'cancel',
            'abort',
            'stop',
            'stop shutdown'
         ]

        self.exit_commands = [
            'e',
            'exit',
            'end'
        ]
