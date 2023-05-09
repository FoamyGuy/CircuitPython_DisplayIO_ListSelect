# SPDX-FileCopyrightText: Copyright (c) 2021 Tim C, 2022 Jose D. Montoya
#
# SPDX-License-Identifier: MIT
"""
Example showing the Community library styles with ListSelect.
Please use circup to download it.
"""
import time
import displayio
import board
from styles import apply_style
from styles.styles import Topanga
from displayio_listselect import ListSelect


# Make the display context. Change size if you want
display = board.DISPLAY

# Make the display context
main_group = displayio.Group()
display.show(main_group)

items = ["First", "Second", "Third", "Fourth"]

list_select = ListSelect(scale=2, items=items)

# Applying some style to the list
apply_style(list_select, Topanga)

main_group.append(list_select)

list_select.anchor_point = (0.5, 0.5)
list_select.anchored_position = (display.width // 2, display.height // 2)

for i in range(3):
    list_select.move_selection_down()
    time.sleep(1)

for i in range(3):
    list_select.move_selection_up()
    time.sleep(1)

list_select.selected_index = 3
while True:
    pass
