import tty, sys, termios

_save_setting = None

def save_setting():
    global _save_setting
    if not _save_setting:
        fd = sys.stdin.fileno()
        _save_setting = termios.tcgetattr(fd)

def restablish_setting():
    global _save_setting
    if _save_setting:
        fd = sys.stdin.fileno()
        termios.tcsetattr(fd, termios.TCSADRAIN, _save_setting)

def get_char():
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
    return ch
