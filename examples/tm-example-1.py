from Pytomatas.tm import TM

# First example of TM Automata instance:
# Language of the Automata:
# Turing Machine to recognize the language;
# L = {0^n 1^n 2^n: n >= 1}
# All strings consisting of zero or more consecutive
# '0's followed by an equal number of consecutive '1's",
# and equal number of 2's then.

#* States:
Q = {"q0", "q1", "q2", "q4", "q5"}

#* Alphabet
#? (* is Blank Symbol):
A = {"0", "1", "2", "X", "Y", "Z", "*"}

#* Initial state:
S = "q0"

#* Accept states:
F = {"q5"}

#* Transitions:
#? (current_state, current_symbol, new_symbol, move_direction, next_state)
T = [
    ("q0", "0", "X", "R", "q1"),
    ("q0", "Y", "Y", "R", "q4"),

    ("q1", "Y", "Y", "R", "q1"),
    ("q1", "0", "0", "R", "q1"),
    ("q1", "1", "Y", "R", "q2"),

    ("q2", "Z", "Z", "R", "q2"),
    ("q2", "1", "1", "R", "q2"),
    ("q2", "2", "Z", "L", "q3"),

    ("q3", "X", "X", "R", "q0"),
    ("q3", "0", "0", "L", "q3"),
    ("q3", "1", "1", "L", "q3"),
    ("q3", "Y", "Y", "L", "q3"),
    ("q3", "Z", "Z", "L", "q3"),

    ("q4", "Y", "Y", "R", "q4"),
    ("q4", "Z", "Z", "R", "q4"),
    ("q4", "*", "*", "L", "q5")
]

#? Automata:
Automata = TM(Q, A, T, S, F)
Automata.show()

#/ Executes the Automata:
while True:
    print()
    word = input("String: ")
    if Automata.accepts(word, stepByStep=True):
        print(f"The string \"{word}\" IS accepted!")
    else:
        print(f"The string \"{word}\" IS NOT accepted!")
    print()
    print("═"*40)