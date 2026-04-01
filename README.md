# ShockPad Macropad
This is my submission for HackPad.
It is a compact 4x3 macropad built using KMK firmware and the Seeed XIAO RP2040.

## Features
* Media Controls
  * Play/Pause, Next, Previous to navigate through music
* App Shortcuts
  * Launch apps using Windows taskbar shortcuts
* Rotary Encoder (Volume Control)
  * Turn right: Volume Up
  * Turn left: Volume Down
* OLED Display (0.91" SSD1306)
  * Startup message
  * Live clock (CST timezone)
  * Visual volume bar that updates as you turn the encoder

## Layout
[  Save   ][    Undo    ][ Close ][ Lock  ]

[ Spotify ][   Chrome   ][ PgUp  ][ PgDn  ]

[Previous ][ Play/Pause ][ Next  ][ Enter ]

## Firmware
* Built using KMK
  * Key matrix scanning (4x3)
  * Media keys
  * Encoder input
  * OLED display updates
Firmware file can be found in the /firmware folder (main.py).

## PCB

### Schematic
! (images/pcb_schematic_heba.png)
This is the schematic for the 4x3 macropad, including the XIAO RP2040, key matrix, rotary encoder, and OLED connections.

### PCB Layout
Empty PCB

## CAD

## Production Files
Located in /production:
* gerbers.zip
* Case part files (.stl)
* Firmware file (main.py)

## Bill of Materials (BOM)
* 1 Seeed XIAO RP2040
* 12x through-hole 1N4148 Diodes
* 12x MX-Style switches
* 1x EC11 Rotary encoder
* 1x 0.91 inch OLED display
* 12x white blank DSA keycaps
* 4x M3x16mm screws
* 4x M3x5mx4mm heatset inserts

### Other Notes
* The OLED clock is calculated in the firmware (CST offset).
* The Volume bar reflects the encoder input.
* The app shortcuts use Windows taskbar bindings (Win + number).