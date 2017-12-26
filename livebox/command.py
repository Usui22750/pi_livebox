import requests


def _send_command(ip, command):
    command_ip = "{}:8080/remoteControl/cmd?operation=01&key={}&mode=0".format(ip, str(command))
    requests.get(command_ip)

def on_off(ip):
    _send_command(ip, 116)

def zero(ip):
    _send_command(ip, 512)

def one(ip):
    _send_command(ip, 513)

def two(ip):
    _send_command(ip, 514)

def three(ip):
    _send_command(ip, 515)

def four(ip):
    _send_command(ip, 516)

def five(ip):
    _send_command(ip, 517)

def six(ip):
    _send_command(ip, 518)

def seven(ip):
    _send_command(ip, 519)

def eight(ip):
    _send_command(ip, 520)

def nine(ip):
    _send_command(ip, 521)

def channel_plus(ip):
    _send_command(ip, 402)

def channel_minus(ip):
    _send_command(ip, 403)

def sound_plus(ip):
    _send_command(ip, 115)

def sound_minus(ip):
    _send_command(ip, 114)

def sound_mute(ip):
    _send_command(ip, 113)

def up(ip):
    _send_command(ip, 103)

def down(ip):
    _send_command(ip, 108)

def left(ip):
    _send_command(ip, 105)

def right(ip):
    _send_command(ip, 116)

def ok(ip):
    _send_command(ip, 352)

def back(ip):
    _send_command(ip, 158)

def menu(ip):
    _send_command(ip, 139)

def play_pause(ip):
    _send_command(ip, 164)

def backward(ip):
    _send_command(ip, 168)

def forward(ip):
    _send_command(ip, 159)

def record(ip):
    _send_command(ip, 167)

def video_on_demand(ip):
    _send_command(ip, 393)
