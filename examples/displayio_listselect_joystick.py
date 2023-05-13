# SPDX-FileCopyrightText: 2020 Tim C
#
# SPDX-License-Identifier: MIT
"""
Joystick example for ListSelect
Make a ListSelect and use up, down, and select buttons to interact with it.
"""
import time
import board
import displayio
import analogio
from displayio_listselect import ListSelect

# state variables for the joystick states we are interested in
STATE_JOYSTICK_DOWN = 0
STATE_JOYSTICK_UP = 1
STATE_JOYSTICK_NEUTRAL = 2

# current and previous iteration state variables
CUR_STATE = STATE_JOYSTICK_NEUTRAL
PREV_STATE = STATE_JOYSTICK_NEUTRAL

# setup analog in for the joystick Y (up/down) direction.
# This pin is for the PyGamer, change to the GPIO connected to your
# Joystick Y axis if not using PyGamer
joystick_y = analogio.AnalogIn(board.JOYSTICK_Y)

# use built-in display
display = board.DISPLAY

# Make the display context
main_group = displayio.Group()
# show our group
display.show(main_group)

# the items in the selectable list
items = ["First", "Second", "Third", "Fourth"]

# Create ListSelect object
list_select = ListSelect(scale=2, items=items)

# add it to the group so it will show on the display
main_group.append(list_select)

# center list select in the middle of the display
list_select.anchor_point = (0.5, 0.5)
list_select.anchored_position = (display.width // 2, display.height // 2)

# initial analog value of joystick
cur_value = joystick_y.value

while True:
    # update the analog value of joystick
    cur_value = joystick_y.value

    if cur_value < 15000:  # pygamer joystick up will have a value below 15,000
        CUR_STATE = STATE_JOYSTICK_UP
    elif cur_value > 50000:  # pygamer joystick down will have a value above 50,000
        CUR_STATE = STATE_JOYSTICK_DOWN
    else:  # pygamer joystick neutral will have a value around 32,000
        CUR_STATE = STATE_JOYSTICK_NEUTRAL

    # if we were in neutral, and now joystick is pushed up
    if PREV_STATE == STATE_JOYSTICK_NEUTRAL and CUR_STATE == STATE_JOYSTICK_UP:
        list_select.move_selection_up()

    # if we were in neutral, and now joystick is pushed down
    if PREV_STATE == STATE_JOYSTICK_NEUTRAL and CUR_STATE == STATE_JOYSTICK_DOWN:
        list_select.move_selection_down()

    # update previous state for next time
    PREV_STATE = CUR_STATE

    # small sleep
    time.sleep(0.05)
