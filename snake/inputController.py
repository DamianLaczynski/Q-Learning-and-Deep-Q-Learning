import keyboard

def get_input():
    action = None
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'w':
        action = 0
    elif event.event_type == keyboard.KEY_DOWN and event.name == 's':
        action = 1
    elif event.event_type == keyboard.KEY_DOWN and event.name == 'a':
        action = 2
    elif event.event_type == keyboard.KEY_DOWN and event.name == 'd':
        action = 3
    elif event.event_type == keyboard.KEY_DOWN and event.name == 'esc':
        return -1

    return action