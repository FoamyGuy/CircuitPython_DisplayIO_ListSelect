# SPDX-FileCopyrightText: 2020 Tim C
#
# SPDX-License-Identifier: MIT
"""
FunHouse example for ListSelect
Make a ListSelect and use up, down, and select buttons to interact with it.
"""
import time
import board
import displayio
from adafruit_funhouse.peripherals import Peripherals
from displayio_listselect import ListSelect


PREV_UP_STATE = False
PREV_DOWN_STATE = False
PREV_SELECT_STATE = False

display = board.DISPLAY
# Make the display context
main_group = displayio.Group()
display.show(main_group)

fun_house = Peripherals()
print(dir)

items = ["First", "Second", "Third", "Fourth"]

list_select = ListSelect(scale=2, items=items)

main_group.append(list_select)

list_select.anchor_point = (0.5, 0.5)
list_select.anchored_position = (display.width // 2, display.height // 2)


while True:

    if fun_house.button_up and not PREV_UP_STATE:
        list_select.move_selection_up()
    if fun_house.button_down and not PREV_DOWN_STATE:
        list_select.move_selection_down()
    if fun_house.button_sel and not PREV_SELECT_STATE:
        print(list_select.selected_item)

    PREV_UP_STATE = fun_house.button_up
    PREV_DOWN_STATE = fun_house.button_down
    PREV_SELECT_STATE = fun_house.button_sel

    time.sleep(0.05)
