import typing
class Node:
    def __init__(self):
        self.output_states = {}
        self.subnodes = {}

    def traverse_node(self, input_state, output_state):
        if self.subnodes[input_state] is not None:
            self.subnodes[input_state].update(output_state)
            return self.subnodes[input_state]
        else:
            self.subnodes[input_state] = Node()
            self.subnodes[input_state].update(output_state)
            return self.subnodes[input_state]

    def update(self, output_state):
        if self.output_states[output_state] is not None:
            self.output_states[output_state] += 1
        else:
            self.output_states[output_state] = 1

    def train_node(self, eval_method, goal_output_states, depth, max_depth):
        nextNode = traverse_node(eval_method(input_states)
