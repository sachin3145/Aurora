from ctypes import windll


user32 = windll.user32
screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) - 40
screensize = screen_width, screen_height


def sh(percentage):
    return percentage*screen_height/100


def sw(percentage):
    return percentage*screen_width/100


def pix_w(pix):
    return  pix*(100/screen_width)


def pix_h(pix):
    return  pix*(100/screen_height-40)
