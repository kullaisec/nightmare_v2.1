STATES = set()

def save(state):
    if state:
        STATES.add(state)

def valid(state):
    return state in STATES