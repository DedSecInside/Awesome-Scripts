#!/usr/bin/env python3

# Created by Siddharth Dushantha
# 2 October 2018

"""
This script lets you turn on/off dark mode from the commandline on MacOS
"""
import subprocess as sp
import sys
import platform
from os import system

prefix = """osascript -e 'tell application \"System Events\" to tell appearance preferences to"""
get_status = "defaults read -g AppleInterfaceStyle"


def show_help():
    """
    Show the help message

    Args:
    """
    help_message = """
Usage: python3 dark-mode.py [command]

Commands
  <none>  Toggle dark mode
  on      Enable dark mode
  off     Disable dark mode
  status  Dark mode status
  """
    
    print(help_message)


def status():
    """
    Get current status, "Dark Mode" or "Light Mode".
    """

    try:
        status = sp.check_output(get_status.split(), stderr=sp.STDOUT).decode()
        status = status.replace("\n", "")

    except sp.CalledProcessError:
        return "Light Mode"

    if status == "Dark":
        return "Dark Mode"


def set_mode(mode):
    """
    Set the mode
    
    :param mode: The mode to be set
    :type mode: str
    """

    if mode == "Null":
        mode = "not dark mode"
    
    cmd = prefix+" set dark mode to {}'".format(mode)
    
    # I know I should use subprocess but it messes up.
    # I will try to fix it.
    system(cmd)


def main():
    """
    Main function.

    Args:
    """
    if platform.system() != "Darwin":
        print("Can only be run on macOS!")
        sys.exit()

    if len(sys.argv) == 1:
        set_mode("Null")

    elif sys.argv[1] == "on":
        set_mode("True")

    elif sys.argv[1] == "off":
        set_mode("False")

    elif sys.argv[1] == "status":
        print(status())

    else:
        show_help()


if __name__=="__main__":
	main()
