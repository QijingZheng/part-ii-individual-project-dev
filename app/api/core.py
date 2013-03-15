"""
Core API.
"""

import time
import logging
from PySide import QtGui, QtCore
import functools

from app.ui import core

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def display(text,duration):

    logger.info("display(text=%s,duration=%s)",text,duration)

    app = _initialise_qt()
    # dialog = core.FullscreenDisplayDialog(text)
    core.FullscreenDisplayDialog.display(text, duration)

    # Close after duration
    # QtCore.QTimer.singleShot(duration*1000, d.close)

    # dialog.exec_()

    # app.exec_()
    # time.sleep(duration)

def ask_yes_no(text):
    """
    :rtype: Boolean
    """
    
    app = _initialise_qt()

    choice = core.FullscreenBooleanDialog.getBoolean(text)
    logger.info("ask_yes_no(text=%s) = %s",text,choice)
    return choice

def _initialise_qt():
    try:
        app = QtGui.QApplication([])
    except RuntimeError:
        app = QtCore.QCoreApplication.instance()
    return app
