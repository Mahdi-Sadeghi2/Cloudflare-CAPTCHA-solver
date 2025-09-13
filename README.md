# Cloudflare CAPTCHA Bypass Automation

A Python automation tool that bypasses Cloudflare CAPTCHA challenges using human-like mouse movements and browser automation techniques.

# Features

Human-like Mouse Movements: Simulates natural mouse behavior with curved paths and random deviations

# Dual Approach:

Attempts both Selenium-based clicking and coordinate-based clicking

# Undetected ChromeDriver:

Uses stealth browser automation to avoid detection

# Cloudflare Iframe Handling:

Automatically detects and switches to Cloudflare challenge iframes

# Visual Feedback:

Provides detailed console logging of the automation process

# Requirements

PyAutoGUI

Selenium

Undetected-Chromedriver

# Installation

Install the required dependencies:

bash
pip install pyautogui selenium undetected-chromedriver
Usage
Run the script:

bash
python cloudflare_bypass.py
The script will:

Launch a Chrome browser window

Navigate to the Cloudflare login page

Attempt to detect and solve the CAPTCHA challenge

Use human-like mouse movements to click the verification checkbox

Provide status updates throughout the process

# Configuration

Before running the script, you may need to adjust the coordinates for the CAPTCHA checkbox:

# Change these coordinates according to your screen resolution

center_x, center_y = 460, 685
To find the correct coordinates:

Run the script once

Use a tool to identify the exact position of the CAPTCHA checkbox on your screen

Update the coordinates in the script

# How It Works

Browser Setup: Launches an undetected Chrome browser instance

Iframe Detection: Attempts to find and switch to the Cloudflare challenge iframe

Checkbox Identification: Looks for the CAPTCHA checkbox element

Human-like Interaction:

Simulates natural mouse movement with random deviations

Adds realistic delays before clicking

Uses either Selenium clicking or coordinate-based clicking

Verification: Checks if the challenge was successfully solved

# File Structure

text
cloudflare-bypass/
├── cloudflare_bypass.py # Main automation script
└── README.md # This file

# Important Notes

This tool is designed for educational purposes only

Use only on websites you own or have permission to test

Cloudflare regularly updates their protection mechanisms

The effectiveness may vary depending on the specific implementation of Cloudflare challenges

Always comply with websites' terms of service

# Troubleshooting

Coordinate Issues: If the script clicks in the wrong place, adjust the center_x and center_y values

Browser Detection: If Cloudflare still detects automation, try adding more human-like behaviors

Timing Issues: If the script runs too fast, increase the sleep durations

# Disclaimer

This tool is intended for educational purposes and legitimate testing only. Always ensure you have proper authorization before attempting to bypass any security measures on websites you don't own. The developers are not responsible for any misuse of this tool.
