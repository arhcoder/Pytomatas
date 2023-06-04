from pytomata.pda import PDA

# Second example of PDA Automata instance:
# Language of the Automata:
# L(Automata) = { w c (w)^R: w in {a, b}* };
# Any "a" and "b" combination string (also empty),
# with then a "c", and then his reverse;
# Implementation:

#* States:
Q = {"qw", "qc", "qf"}

#* Alphabet:
A = {"a", "b", "c"}

#* Starting state:
S = "qw"

#* Finals states:
F = {"qf"}

#* Stack alphabet:
X = {"Z", "1", "2"}

#* Initial stack:
I = ["Z"]

#* Transitions:
T = [
    ("qw", "a", "Z", "1Z", "qw"),
    ("qw", "b", "Z", "2Z", "qw"),
    ("qw", "a", "1", "11", "qw"),
    ("qw", "a", "2", "12", "qw"),
    ("qw", "b", "1", "21", "qw"),
    ("qw", "b", "2", "22", "qw"),

    ("qw", "c", "1", "1", "qc"),
    ("qw", "c", "2", "2", "qc"),
    ("qw", "c", "Z", "Z", "qc"),

    ("qc", "a", "1", "", "qc"),
    ("qc", "b", "2", "", "qc"),

    ("qc", "", "Z", "", "qf")
]

#? Automata:
Automata = PDA(Q, A, T, S, F, X, I)
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