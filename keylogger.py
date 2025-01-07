from pynput import keyboard

key_presses = []

def add_key(key):
    key_presses.append(key)

def key_pressed(key):
    keyPress = '{0}'.format(key)
    print(keyPress)
    add_key(keyPress)

def key_released(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def main():
    with keyboard.Listener(
        on_press=key_pressed,
        on_release=key_released
    ) as listener:
        listener.join()
        
    print(key_presses)

if __name__=="__main__":
    main()

