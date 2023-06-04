from pytomatas.pda import PDA

# First example of PDA Automata instance:
# Language of the Automata:
# L(Automata) = { (a^n)(b^2n): n >= 0 };
# "ab" structure with the double of b's respect to a's.
# It includes the empty string.
Automata = PDA()
Automata.setStates({"q0", "qa", "qb", "qf"})
Automata.setAlphabet({"a", "b"})
Automata.setInitial("q0")
Automata.setFinals({"qf"})
Automata.addTransition(("q0", "a", "Z", "aaZ", "qa"))
Automata.addTransition(("qa", "a", "a", "aaa", "qa"))
Automata.addTransition(("qa", "b", "a", "", "qb"))
Automata.addTransition(("qb", "b", "a", "", "qb"))
Automata.addTransition(("qb", "", "Z", "", "qf"))
Automata.setStackAlphabet({"a", "Z"})
Automata.setInitialStack(["Z"])

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
    print("═"*80)