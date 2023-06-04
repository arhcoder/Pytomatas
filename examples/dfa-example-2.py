from Pytomatas.dfa import DFA

# Second example of DFA Automata instance:
# Language of the Automata:
# L(Automata) = All strings with at least one "a",
# and exactly two b's:
#* States:
Q = {"q0", "qa", "q1", "qb", "q2", "qf", "qx"}

#* Alphabet:
A = {"a", "b"}

#* Starting state:
S = "q0"

#* Finals states:
F = {"qf"}

#* Transitions:
T = [
    ("q0", "a", "qa"),
    ("q0", "b", "q1"),

    ("qa", "a", "qa"),
    ("qa", "b", "qb"),

    ("q1", "a", "qb"),
    ("q1", "b", "q2"),

    ("qb", "a", "qb"),
    ("qb", "b", "qf"),

    ("q2", "a", "qf"),
    ("q2", "b", "qx"),
    
    ("qf", "a", "qf"),
    ("qf", "b", "qx"),

    ("qx", "a", "qx"),
    ("qx", "b", "qx")
]

#? Automata:
Automata = DFA(Q, A, T, S, F)
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