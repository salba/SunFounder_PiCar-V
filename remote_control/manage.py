#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    dirname = os.path.dirname(os.path.abspath(__file__))
    basepath = dirname
    # sys.path.append(basepath)
    sys.path.append(basepath + "/")
    sys.path.append(basepath + "/remote_control/")
    sys.path.append(basepath + "/remote_control/templates/")
    for path in sys.path:
        print("path", path)
    print("syspath", sys.path)

    os.environ["DJANGO_SETTINGS_MODULE"] = "remote_control.settings"

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
