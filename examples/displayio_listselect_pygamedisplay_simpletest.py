# SPDX-FileCopyrightText: Copyright (c) 2021 Tim C
#
# SPDX-License-Identifier: MIT
"""
Create a list with a few options and move the selection around programmatically.

Runs on a PC / RasPi in CPython using Blinka_DisplayIO and PyGameDisplay
"""
import time

import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
from displayio_listselect import ListSelect

# Make the display context. Change size if you want
display = PyGameDisplay(width=320, height=240)

# Make the display context
main_group = displayio.Group()
display.show(main_group)

items = ["First", "Second", "Third", "Fourth"]

list_select = ListSelect(scale=2, items=items)

main_group.append(list_select)

list_select.anchor_point = (0.5, 0.5)
list_select.anchored_position = (display.width // 2, display.height // 2)

print(list_select.anchor_point)
print(list_select.anchored_position)
print(list_select.x)
print(list_select.bounding_box)
# print(list_select._bounding_box)

for i in range(3):
    list_select.move_selection_down()
    time.sleep(1)

for i in range(3):
    list_select.move_selection_up()
    time.sleep(1)

list_select.selected_index = 3
while display.running:
    pass
