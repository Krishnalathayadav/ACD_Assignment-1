class NFA:
    def __init__(self, transitions, start_state, accept_states):
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def run(self, string):
        current_states = {self.start_state}

        print("Input String:", string)
        print("Start State:", current_states)
        print("-" * 40)

        for symbol in string:
            next_states = set()

            print(f"Current States = {current_states}")
            print(f"Input Symbol = {symbol}")

            for state in current_states:
                next_states.update(
                    self.transitions.get((state, symbol), set())
                )

            print(f"Next States = {next_states}")
            print("-" * 40)

            current_states = next_states

        print("Final States:", current_states)

        if current_states & self.accept_states:
            print("Result: ACCEPTED")
        else:
            print("Result: REJECTED")


transitions = {
    ('q0', '0'): {'q0', 'q1'},
    ('q0', '1'): {'q0'},
    ('q1', '1'): {'q2'}
}

nfa = NFA(
    transitions=transitions,
    start_state='q0',
    accept_states={'q2'}
)

# Hardcoded string
test_string = "1101"

nfa.run(test_string)