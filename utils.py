import os
import sys
import termios

def stringify_float_with_zeros(f, n):
    f = str(round(f, n)).split(".")
    f[1] = f[1].ljust(n, "0")
    return ".".join(f)

def clear_screen():
    os.system("clear")
    # subprocess.run("clear", shell=True)

def flush_terminal():
    # Called before most input calls to clear all stdio after sleeping.
    # Otherwise, accidentally pressing enter during sleep moments
    # would advance all succeeding input calls.
    # Uses termios, which is on python stdlibs on linux.
    # sys.stdin.flush() doesnt work for cause its printing only ig.
    # Please dont smite me for using termios sir
    termios.tcflush(sys.stdin, termios.TCIOFLUSH)