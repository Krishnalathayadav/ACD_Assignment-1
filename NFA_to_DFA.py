from collections import deque

# NFA Transition Table
nfa = {
    ('q0', '0'): {'q0', 'q1'},
    ('q0', '1'): {'q0'},
    ('q1', '1'): {'q2'}
}

alphabet = ['0', '1']

start_state = frozenset(['q0'])

dfa_states = set()
dfa_transitions = {}

queue = deque([start_state])
dfa_states.add(start_state)

while queue:
    current = queue.popleft()

    for symbol in alphabet:
        next_states = set()

        for state in current:
            next_states.update(
                nfa.get((state, symbol), set())
            )

        next_states = frozenset(next_states)

        dfa_transitions[(current, symbol)] = next_states

        if next_states not in dfa_states:
            dfa_states.add(next_states)
            queue.append(next_states)

print("DFA States:")
for state in dfa_states:
    print(set(state))

print("\nDFA Transition Table:")
for (state, symbol), next_state in dfa_transitions.items():
    print(f"{set(state)} --{symbol}--> {set(next_state)}")