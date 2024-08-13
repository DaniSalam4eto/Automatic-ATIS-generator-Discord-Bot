# ATIS Bot for Discord

ATIS Bot is a Discord bot built for aviation enthusiasts and communities to broadcast Automated Terminal Information Service (ATIS) messages within a Discord server. This bot provides functionalities to set, update, and stop ATIS broadcasts in specific channels, with access restricted to users with a designated role.

## Features

- **Set ATIS Information**: Start broadcasting ATIS details including airport code, ATIS letter, winds, transition level, visibility, and active runway.
- **Update ATIS Information**: Modify any existing ATIS broadcast details.
- **Stop ATIS Broadcast**: Halt the ATIS broadcast in a specific channel.
- **Automated Broadcasting**: Broadcasts ATIS information every 5 minutes.
- **Role-Based Security**: Only users with the appropriate role can manage ATIS broadcasts.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/atis-bot.git
    cd atis-bot
    ```

2. Install the required dependencies:
    ```sh
    pip install discord.py
    ```

3. Set your bot token and allowed role ID in the code:
    ```python
    bot.run('YOUR_BOT_TOKEN')
    ALLOWED_ROLE_ID = 123456789  # Replace with your actual role ID
    ```

4. Run the bot:
    ```sh
    python bot.py
    ```

## Commands

- **/setatis**
  - Set ATIS information and start broadcasting.
  - Parameters:
    - `airport`: Airport code (e.g., KJFK)
    - `atis_letter`: Single letter ATIS identifier
    - `winds`: Current wind information
    - `trans_level`: Transition level
    - `visibility`: Visibility information
    - `active_rwy`: Active runway

- **/changeatis**
  - Update the existing ATIS information.
  - Parameters: Same as `/setatis`, all are optional.

- **/stopatis**
  - Stop the ATIS broadcast for the current channel.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- [discord.py](https://discordpy.readthedocs.io/) for the powerful API that makes this bot possible.
