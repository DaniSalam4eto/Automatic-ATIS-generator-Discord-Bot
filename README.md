# Automatic ATIS Generator Discord Bot

The Automatic ATIS Generator is a Discord bot built to broadcast Automated Terminal Information Service (ATIS) messages within Discord channels, designed specifically for aviation communities and virtual flight simulation groups.

## Features

- **Set ATIS Information**: Start broadcasting ATIS details, such as airport code, ATIS letter, winds, transition level, visibility, and active runway.
- **Update ATIS Information**: Modify the existing ATIS broadcast without stopping the current session.
- **Stop ATIS Broadcast**: Easily stop the ATIS broadcast for a specific channel.
- **Automated Broadcasting**: Broadcast ATIS information every 5 minutes automatically.
- **Role-Based Access**: Ensure that only users with the designated role can manage the ATIS broadcasts.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Automatic-ATIS-generator-Discord-Bot.git
    cd Automatic-ATIS-generator-Discord-Bot
    ```

2. Install the required dependencies:
    ```sh
    pip install discord.py
    ```

3. Set your bot token and allowed role ID in `main.py`:
    ```python
    bot.run('YOUR_BOT_TOKEN')
    ALLOWED_ROLE_ID = 123456789  # Replace with your actual role ID
    ```

4. Run the bot:
    ```sh
    python main.py
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





