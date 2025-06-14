# FN XP Tool

**FN XP Tool** is a simple macro automation tool for Fortnite XP farming, especially suited for Lego Fortnite sandbox mode. It provides a graphical interface with customizable macros, key/mouse automation, and macro saving/loading functionality.

## Features

- **Lego AFK Macro**
  - Automatically presses the "P" key every 1 to 5 seconds.
  - Designed for AFK XP farming in Lego Fortnite.
  - Includes help popup with step-by-step instructions.

- **Custom Macro**
  - Supports any keyboard key or mouse scroll (`scrollup`, `scrolldown`).
  - Adjustable delay in seconds.
  - Ability to save and load macro settings for later use.

- **Stop All Macros**
  - Instantly stops any active macro.

- **Help Buttons**
  - Each button has a help popup explaining its functionality and usage.

## Requirements

- Python 3.8 or higher
- `pynput` Python package

## Installation

1. Clone this repository or download the `fn_xp_tool.py` file.

2. Install the required Python package using pip:
`pip install pynput`

3. Run the script:
`python fn_xp_tool.py`

## Usage

### Lego AFK Instructions

Before using the **Lego AFK** macro:

1. In Fortnite, set the mode to **Battle Royale**.
2. Change your **Fire** or **Fire Weapon** keybind to **P**.
3. Disable **Auto Claim Rewards** for all battle and brick passes.
4. Load into your **Lego sandbox world**.
5. Press the **Lego AFK** button in the tool to start the macro.

The macro will press the "P" key at random intervals between 1 and 5 seconds.

### Custom Macro

1. Enter a key (e.g. `a`, `space`, `scrollup`, `scrolldown`).
2. Set the delay in seconds (e.g. `1.5`).
3. Click **Custom Macro** to start.
4. Use **Save Macro** to save the current key and delay.
5. Use **Load Macro** to restore saved settings.

### Stop All

Click the **Stop All** button to instantly stop all running macros.

## Saving and Loading

Saved macro configurations are stored in a local file named `macro_config.json`.

- Click **Save Macro** to write the current macro settings to file.
- Click **Load Macro** to restore them automatically.

## Disclaimer

This tool is provided for educational and personal automation use only. Use responsibly and at your own risk.

