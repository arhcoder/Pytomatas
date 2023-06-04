from Pytomatas.nfa import NFA

# Second example of NFA Automata instance:
# Language of the Automata:
# L(Automata) = {(a^n): n>=0} U {(b^n)a: n>=1};
Automata = NFA()
Automata.setStates({"q0", "qb", "qa", "qba"})
Automata.setAlphabet({"a", "b"})
Automata.setInitial("q0")
Automata.setFinals({"qa", "qba"})
Automata.addTransition(("q0", "", "qa"))
Automata.addTransition(("q0", "b", "qb"))
Automata.addTransition(("qa", "a", "qa"))
Automata.addTransition(("qb", "a", "qba"))
Automata.addTransition(("qb", "b", "qb"))

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