import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
keyboard.modules.append(MediaKeys())

# MATRIX PINS (for 4x4 layout)
keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3)  # 4 columns
keyboard.row_pins = (board.GP4, board.GP5, board.GP6, board.GP7)  # 4 rows

# Incase the diodes are reversed
keyboard.diode_orientation = DiodeOrientation.COL2ROW 

# ROTARY ENCODER
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# pins = (pin_a, pin_b, button_pin, reversed)
encoder_handler.pins = (
    (board.GP8, board.GP9, board.GP10, False),
)
# Map encoder actions: (rotating left for decreasing volume, right for increasing, and pressing to mute/unmute)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),)
]

# Keymap layout (4x4)
# [   Save   ][  Undo   ][   Redo    ][ Lock  ]
# [ Previous ][  Play   ][   Next    ][ PgUp  ]
# [ Spotify  ][ UpArrow ][  Chrome   ][ PgDn  ]
# [LeftArrow ][DownArrow][Right Arrow][ Enter ]

keyboard.keymap = [
    [
        KC.LCTL(KC.S),   KC.LCTL(KC.Z),   KC.LCTL(KC.Y),   KC.LGUI(KC.L),
        KC.MPRV,         KC.MPLY,         KC.MNXT,         KC.PGUP,
        KC.LGUI(KC.N2),  KC.UP,           KC.LGUI(KC.N1),  KC.PGDN,
        KC.LEFT,         KC.DOWN,         KC.RIGHT,        KC.ENTER
    ]
]

# Start KMK keyboard
if __name__ == '__main__':
    keyboard.go()