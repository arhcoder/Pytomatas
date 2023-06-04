from pytomata.nfa import NFA

# Second example of NFA Automata instance:
# Language of the Automata:
# L(Automata) = {aba(b^n): n>0} U
# {ab(a^n): n>=0};
#* States:
Q = {"q0", "qa", "qab", "qf", "qabf"}

#* Alphabet:
A = {"a", "b"}

#* Starting state:
S = "q0"

#* Finals states:
F = {"qf", "qabf"}

#* Transitions:
T = [
    ("q0", "a", "qa"),
    ("qa", "b", "qab"),
    ("qab", "a", "qf"),
    ("qf", "b", "qf"),
    ("qab", "", "qabf"),
    ("qabf", "a", "qabf")
]

#? Automata:
Automata = NFA(Q, A, T, S, F)
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