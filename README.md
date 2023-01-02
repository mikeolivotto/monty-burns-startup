# Monty Burns computer startup

## Custom startup sequence for the Pimoroni Pico Display pack

Inspired by Mr Smithers' own custom computer startup sequence from [The Simpsons season 5, episode 14](https://www.youtube.com/watch?v=8YzSHIYxdRs), _Lisa Vs. Malibu Stacy_.

![Monty Burns startup sequence gif](monty-burns-startup.gif)

### Requirements

- Raspberry Pi Pico
- Pimoroni Pico Display Pack
- Micro USB data cable (ensure it's not a power-only cable)

### Before you begin

The following assumes you already know how to set up a pico with MicroPython. If you're completely new, check out Pimoroni's [Getting started with Raspberry Pi Pico](https://learn.pimoroni.com/article/getting-started-with-pico) tutorial, and install their Micropython custom firmware.

### Usage

Clone this repo to your local, [uploading the files to your Pi Pico](https://www.freva.com/transfer-files-between-computer-and-raspberry-pi-pico/). **You must remove the `monty-burns-startup.gif`** as the pico only has 2MB of available memory. The rest of the repo is approx 23kb total.


### Adding it to your own project

`main.py` is a barebones setup for initialising the display, running the sequence and then clearing the screen. Presuming you're using this as a fun addition to your own project, simply add your own project code after the call to `clear()` at the end of the file.