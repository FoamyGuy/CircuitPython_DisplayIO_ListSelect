Introduction
============


.. image:: https://readthedocs.org/projects/circuitpython-displayio-listselect/badge/?version=latest
    :target: https://circuitpython-displayio-listselect.readthedocs.io/
    :alt: Documentation Status



.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/foamyguy/CircuitPython_DisplayIO_ListSelect/workflows/Build%20CI/badge.svg
    :target: https://github.com/foamyguy/CircuitPython_DisplayIO_ListSelect/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

ListSelect widget for circuitpython displayio. Display a list of strings with a selection indicator allow user to move selection up and down.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/circuitpython-displayio-listselect/>`_.
To install for current user:

.. code-block:: shell

    pip3 install circuitpython-displayio-listselect

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install circuitpython-displayio-listselect

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install circuitpython-displayio-listselect

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install displayio_listselect

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code-block:: python

    import time
    import displayio
    import board
    from displayio_listselect import ListSelect

    display = board.DISPLAY

    main_group = displayio.Group()
    display.show(main_group)

    items = ["First", "Second", "Third", "Fourth"]

    list_select = ListSelect(scale=2, items=items)

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

Documentation
=============
API documentation for this library can be found on `Read the Docs <https://circuitpython-displayio-listselect.readthedocs.io/>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/foamyguy/CircuitPython_DisplayIO_ListSelect/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
