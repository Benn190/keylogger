from pynput import keyboard


def key_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        
    except AttributeError:
        print('special key {0} pressed'.format(key))
    
def key_release(key):
    a=1


with keyboard.Listener(on_press=key_press,
        on_release=key_release) as listener:
    listener.join()

'''
listener = keyboard.Listener(
    on_press=key_press,
    on_release=key_release)
listener.start()
'''