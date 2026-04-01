# Welcome to my macropad called Heba's ShockPad (inspo from tranformers)
# This is the firmware for my 4x3 macropad with:
# - Media controls (Play/Pause, Next, Prev)
# - App shortcuts using windows taskbar (Ex. Chrome, Spotify)
# - Rotary encoder (volume control)
# - 0.91" OLED display with startup message, clock, and volume bar!

# Importing necessary modules
import board
import time
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextDisplay, SSD1306

keyboard = KMKKeyboard()
keyboard.modules.append(MediaKeys())

# MATRIX PINS (for 4x3 layout)
keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3) # 4 columns
keyboard.row_pins = (board.GP4, board.GP5, board.GP6,) # 3 rows
# Incase the diodes are reversed:
keyboard.diode_orientation = DiodeOrientation.COL2ROW 

# ROTARY ENCODER (for volume control)
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
# pins = (pin_a, pin_b, button_pin, reversed)
encoder_handler.pins = (
    (board.GP7, board.GP8, False), # 2 pins, no button
)
# Note: Volume is handled manually in oled_encoder_callback

# OLED Display (0.91" SSD1306)
i2c = busio.I2C(scl=board.GP9, sda=board.GP10)  # 2 pins
display = Display(
    display=SSD1306(i2c=i2c, device_address=0x3C, width=128, height=32),
    entries=[
        TextDisplay(text="Welcome, Heba", x=0, y=0, show=True),  # Startup Message
        TextDisplay(text="", x=0, y=12, show=True), # Displaying Volume Bar
        TextDisplay(text="", x=0, y=24, show=True), # Displaying Clock
    ],
)
keyboard.extensions.append(display)

# Helper functions for OLED
# Function to display the changing volume
def update_volume(vol_percent):
    # Horizontal bar for volume (Display of 10 blocks)
    blocks = int(vol_percent / 10)
    bar = "■" * blocks + "□" * (10 - blocks)
    display.entries[1].text = f"VOL: [{bar}] {vol_percent}%"
    display.entries[1].show = True

# Function to display time in CST timezone
def update_clock():
    t = time.localtime()
    # Convert to CST (UTC-6)
    hour_cst = (t.tm_hour - 6) % 24
    display.entries[2].text = f"{hour_cst:02d}:{t.tm_min:02d}"
    display.entries[2].show = True

# Keymap layout (4x3)
# [   Save   ][   Undo   ][ Close Tab ][  Lock  ]
# [ Spotify  ][  Chrome  ][   PageUp  ][PageDown]
# [ Previous ][Play/Pause][   Next    ][ Enter  ]
keyboard.keymap = [
    [
        KC.LCTL(KC.S),  KC.LCTL(KC.Z),  KC.LCTL(KC.W), KC.LGUI(KC.L),
        KC.LGUI(KC.N2), KC.LGUI(KC.N1), KC.PGUP,       KC.PGDOWN, 
        KC.MPRV,        KC.MPLY,        KC.MNXT,       KC.ENTER
    ]
]

# Encoder Callback for OLED
current_volume = 50 # Global variable to track volume (start at 50%)
update_volume(current_volume) # Show initial volume on OLED
def oled_encoder_callback(encoder, direction):
    global current_volume
    if direction == -1:
        current_volume = max(0, current_volume - 5) # Decrease by 5%
        keyboard.modules[0].volume_down() # Sends VOLD key
    elif direction == 1:
        current_volume = min(100, current_volume + 5) # Increase by 5%
        keyboard.modules[0].volume_up() # Sends VOLU key
    # Update the OLED bar
    update_volume(current_volume)

# Calling the function
encoder_handler.on_turn = oled_encoder_callback

# Main Loop: Continously updating and displaying the clock
def main_loop():
    update_clock()
    time.sleep(1)  # Update every 1 sec
keyboard.on_main_loop = main_loop

# Start the KMK keyboard:
if __name__ == '__main__':
    keyboard.go()