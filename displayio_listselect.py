# SPDX-FileCopyrightText: Copyright (c) 2021 Tim C
#
# SPDX-License-Identifier: MIT
"""
`displayio_listselect`
================================================================================

ListSelect widget for CircuitPython DisplayIO.
  Display a list of strings with a selection indicator allow
  the user to move selection up and down.


* Author(s): Tim C

Implementation Notes
--------------------

**Hardware:**

Any CircuitPython device with displayio support.

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

"""

import terminalio
from adafruit_display_text.bitmap_label import Label
from displayio import Group


__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/foamyguy/CircuitPython_DisplayIO_ListSelect.git"


class ListSelect(Group):
    """
    ListSelect widget for CircuitPython DisplayIO.
    Display a list of strings with a selection indicator allow
    the user to move selection up and down.
    """

    # pylint:disable=too-many-arguments
    def __init__(
        self,
        items=None,
        font=terminalio.FONT,
        x=0,
        y=0,
        color=0xFFFFFF,
        background_color=0x000000,
        selected_index=0,
        visible_items_count=None,
        cursor_char=">",
        **kwargs
    ):
        super().__init__(x=x, y=y, scale=1)
        self._label = Label(
            font, text="", color=color, background_color=background_color, **kwargs
        )
        self._label.anchor_point = (0, 0)
        self._label.anchored_position = (0, 0)

        if visible_items_count == 0:
            raise ValueError(
                "Must have at least 1 visible item. Or None for unrestricted"
            )
        self.visible_items_count = visible_items_count
        self.visible_index = 0

        self.items = items
        self._selected_index = selected_index
        self.cursor_char = cursor_char

        self.append(self._label)
        self._refresh_label()

    def _refresh_label(self):
        """Called any time that we need to update the displayed label."""
        _full_str = ""
        if self.visible_items_count:
            loop_from = min(
                self.visible_index, len(self.items) - self.visible_items_count
            )
            loop_to = min(
                len(self.items), self.visible_index + self.visible_items_count
            )
        else:
            loop_from = 0
            loop_to = len(self.items)
        # print(f"showing indexes {self.visible_index} - {loop_to}")
        for i in range(loop_from, loop_to):
            item = self.items[i]

            if i == self.selected_index:
                _full_str += self.cursor_char
            else:
                _full_str += " "
            _full_str += item

            if i != len(self.items) - 1:
                _full_str += "\n"

        self._label.text = _full_str

    def move_selection_down(self):
        """
        Move the selection indicator down 1 space
        :return: None
        """
        if self.selected_index + 1 < len(self.items):
            self.selected_index += 1
            self._refresh_label()

    def move_selection_up(self):
        """
        Move the selection indicator up 1 space
        :return: None
        """
        if self.selected_index - 1 >= 0:
            self.selected_index -= 1
            self._refresh_label()

    @property
    def width(self):
        """The widget width, in pixels. (getter only)
        :return: int
        """
        return self._label.bounding_box[2]

    @property
    def height(self):
        """The widget height, in pixels. (getter only)
        :return: int
        """
        return self._label.bounding_box[3]

    @property
    def bounding_box(self):
        """
        The bounding box of the label that the
        list is shown within.
        :return: Tuple
        """
        return self._label.bounding_box

    def resize(self, new_width, new_height):
        """
        Not Implemented
        """
        raise NotImplementedError(
            "Label does not support arbitrary sizing, so neither does ListSelect."
        )

    @property
    def anchor_point(self):
        """
        The anchor point of the label that the list is shown within
        :return: Tuple
        """
        return self._label.anchor_point

    @anchor_point.setter
    def anchor_point(self, new_anchor_point):
        """
        The anchor point of the label that the list is shown within
        :param new_anchor_point:
        :return: None
        """
        self._label.anchor_point = new_anchor_point

    @property
    def anchored_position(self):
        """
        The anchored position of the label that the list is shown
        within
        :return: Tuple
        """
        return self._label.anchored_position

    @anchored_position.setter
    def anchored_position(self, new_anchored_position):
        """
        The anchored position of the label that the list is shown
        within
        :param new_anchored_position:
        :return: None
        """
        self._label.anchored_position = new_anchored_position

    @property
    def selected_index(self):
        """
        The currently selected index.
        :return: int
        """
        return self._selected_index

    @selected_index.setter
    def selected_index(self, new_index):
        """
        The currently selected index
        :param new_index:
        :return: None
        """
        self._selected_index = new_index
        if self.visible_items_count:
            self.visible_index = new_index
        self._refresh_label()

    @property
    def selected_item(self):
        """
        The string representing the currently selected item.
        :return: String
        """
        return self.items[self._selected_index]
