#!/usr/bin/env python

import sys
import SettingsWindow
import ImageDescriber

if "-s" in sys.argv:
    settingsWindow = SettingsWindow.SettingsWindow()
    settingsWindow.show_all()
    settingsWindow.main()
    sys.exit(0)

if "-w" in sys.argv:
    ImageDescriber.describeWindow()
else:
    ImageDescriber.describe()