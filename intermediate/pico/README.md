# Hardware setup

Use the graphical guides printed on the Pimoroni RGB Keypad's PCB to align the Raspberry Pi Pico's pins to the board.

Make sure the Raspberry Pi Pico's GPIO pins are firmly pushed into the keypad.

Connect the keypad via USB to your computer.

# Install CircuitPython

Download the latest version of CircuitPython from for the Raspberry Pi Pico [here](https://circuitpython.org/board/raspberry_pi_pico/).

Mount the Pico and drag and drop the downloaded UF2 file into the Pico. The Pico will restart and remount with the label CIRCUITPY.

If this step doesn't work, hold down the BOOTSEL button on the Pico before plugging in the USB cable.

# VS Code Integration

## Installing the extension
In the extensions tab, search for and install the CircuitPython extension using the identifier: 

`joedevivo.vscode-circuitpython`

Once installed, this extension automatically detects when a workspace contains `code.txt`, `main.py`, `main.txt`, or `boot_out.txt`.

## Mount and test
Open the folder where the Pico is mounted, and open the command palette (Ctrl+Shift+p), and search for `CircuitPython: Open Serial Monitor`. Check out the terminal tab to see that a connection to the Pico has been established.

### Permissions
Note that when using a Linux operating system, the user needs to be in the `dialout` group for connections to work. Run the following command and restart to apply settings to the current user:

`sudo usermod -a -G dialout $USER`

Check that the current user is in the `dialout` group with:

`groups $USER`

## Read-eval-print loop (REPL)

In the terminal, you should see an output to press Ctrl-C or to press any key to enter the Pico's REPL environment. Once in, run `print("Hello World")` to confirm that it is working.

## Blinking LEDs

The Pylance extension will warn that the default filename with `code` is overriding the stdlib module "code". Our recommendation is to rename the file to `main.py` instead.

Type the following script into main.py. Change the LED timings to see how it affects the Pico.

```python

import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.1)

```

# Libraries to Create a MIDI Controller

## CircuitPython Libraries

Open the [following site](https://circuitpython.org/libraries) and choose the CircuitPython Bundle appropriate for your system. In this instance, if CircuitPython 8.x is installed, select the bundle for Version 8.x. We will be using the `/lib/adafruit_midi` folder, and `/lib/adafruit_dotstar.mpy` driver. Documentation for both libraries can be found [here](https://docs.circuitpython.org/projects/midi/en/latest/) and [here](https://docs.circuitpython.org/projects/dotstar/en/latest/) respectively.

Pimoroni Libraries

Next, download [the following git repository](https://github.com/pimoroni/pmk-circuitpython). We will be using the `/lib/pmk` folder. Documentation for this library is available in the README.md file.

## Installing Libraries

In the mounted Pico drive, select (or create if it's absent) a top level `lib` folder. Copy and paste the mentioned libraries into the `lib` folder.

# Example Code

This folder contains an example script for setting up the device as a MIDI controller, `main.py`. An example of the MIDI controller being used to play a simple tune can be found [here on YouTube](https://youtu.be/EL_KKd6TDmI).

Here is a reference file structure for the final project:

```
.
├── BOOTEX.LOG
├── boot_out.txt
├── lib
│   ├── adafruit_dotstar.mpy
│   ├── adafruit_midi
│   │   ├── channel_pressure.mpy
│   │   ├── control_change.mpy
│   │   ├── control_change_values.mpy
│   │   ├── __init__.mpy
│   │   ├── midi_continue.mpy
│   │   ├── midi_message.mpy
│   │   ├── mtc_quarter_frame.mpy
│   │   ├── note_off.mpy
│   │   ├── note_on.mpy
│   │   ├── pitch_bend.mpy
│   │   ├── polyphonic_key_pressure.mpy
│   │   ├── program_change.mpy
│   │   ├── start.mpy
│   │   ├── stop.mpy
│   │   ├── system_exclusive.mpy
│   │   └── timing_clock.mpy
│   └── pmk
│       ├── __init__.py
│       └── platform
│           ├── display
│           │   ├── dotstar.py
│           │   ├── __init__.py
│           │   └── keybow2040.py
│           ├── __init__.py
│           ├── keybow2040.py
│           ├── rgbkeypadbase.py
│           └── switches
│               ├── gpio.py
│               ├── __init__.py
│               └── tca9555.py
├── main.py
├── settings.toml
└── System Volume Information
    ├── IndexerVolumeGuid
    └── WPSettings.dat

8 directories, 33 files
```

# Recommended Digital Audio Workstation

[LMMS](https://lmms.io/) is a free and open source audio workstation app that is available for Linux, Windows, and macOS. Use it with your new MIDI controller to start making music!
