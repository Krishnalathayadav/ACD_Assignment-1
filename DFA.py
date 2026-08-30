class DFA:
    def __init__(self, transitions, start_state, accept_states):
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def run(self, string):
        current_state = self.start_state

        print("Input String:", string)
        print("Start State:", current_state)
        print("-" * 30)

        for symbol in string:
            next_state = self.transitions[(current_state, symbol)]

            print(f"{current_state} --{symbol}--> {next_state}")

            current_state = next_state

        print("-" * 30)
        print("Final State:", current_state)

        if current_state in self.accept_states:
            print("Result: ACCEPTED")
        else:
            print("Result: REJECTED")


# DFA for even number of 0s
transitions = {
    ('q0', '0'): 'q1',
    ('q0', '1'): 'q0',
    ('q1', '0'): 'q0',
    ('q1', '1'): 'q1'
}

dfa = DFA(
    transitions=transitions,
    start_state='q0',
    accept_states={'q0'}
)

# String is hardcoded here
test_string = "1001"

dfa.run(test_string)