from pytomata.tm import TM

# Second example of TM Automata instance:
# Language of the Automata:
# Turing Machine to recognize the language;
# L = {0^n 1^n 2^n: n >= 1}
# All strings consisting of zero or more consecutive
# '0's followed by an equal number of consecutive '1's",
# and equal number of 2's then.

Automata = TM()
Automata.setStates({"q0", "q1", "q2", "q4", "q5"})
Automata.setAlphabet({"0", "1", "2", "X", "Y", "Z", "*"})
Automata.setInitial("q0")
Automata.setFinals({"q5"})
Automata.addTransition(("q0", "0", "X", "R", "q1"))
Automata.addTransition(("q0", "Y", "Y", "R", "q4"))
Automata.addTransition(("q1", "Y", "Y", "R", "q1"))
Automata.addTransition(("q1", "0", "0", "R", "q1"))
Automata.addTransition(("q1", "1", "Y", "R", "q2"))
Automata.addTransition(("q2", "Z", "Z", "R", "q2"))
Automata.addTransition(("q2", "1", "1", "R", "q2"))
Automata.addTransition(("q2", "2", "Z", "L", "q3"))
Automata.addTransition(("q3", "X", "X", "R", "q0"))
Automata.addTransition(("q3", "0", "0", "L", "q3"))
Automata.addTransition(("q3", "1", "1", "L", "q3"))
Automata.addTransition(("q3", "Y", "Y", "L", "q3"))
Automata.addTransition(("q3", "Z", "Z", "L", "q3"))
Automata.addTransition(("q4", "Y", "Y", "R", "q4"))
Automata.addTransition(("q4", "Z", "Z", "R", "q4"))
Automata.addTransition(("q4", "*", "*", "L", "q5"))
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