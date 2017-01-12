import World

def main():
    while True:
        #pick the right action
        agent = World.player
        max_act, max_val = max_Q(agent)
        (agent, a, r, agent_updated) = do_action(max_act)
