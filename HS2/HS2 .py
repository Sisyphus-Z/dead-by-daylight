import threading
import time

from pynput import mouse,keyboard
mouse1=mouse.Controller()

keyboard1=keyboard.Controller()


mouse_pos=(0,0)



def on_click(x, y, button, pressed):
    print(str(button))
    if str(button)=="Button.x1":
        mouse1.position=mouse_pos



def on_press(key):
    print(key)


    global mouse_pos
    if str(key)=="'d'":
        mouse_pos=mouse1.position
        print(mouse_pos)
    if str(key)=="'a'":
        mouse1.position=mouse_pos

def on_release(key):
    #print('弹起'+str(key))
    pass



def listen_mouse():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

def listen_keyboard():
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()



t_m=threading.Thread(target=listen_mouse)
t_m.start()

t_k=threading.Thread(target=listen_keyboard)
t_k.start()


t_m.join()
t_k.join()
