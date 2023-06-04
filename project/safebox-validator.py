from Pytomatas.pda import PDA
# import os

def validatePassword(password: str):

    '''

        Receives a password and validate if
        it is correct for the context of the
        safebox, using a pushdown automaton
        that validates the following format:

        L = { (L^n)(R^m)(L^o)(R^p):
        (4  <=  n + m + o + p  <=  40) };

        That is to say; passwords with groups
        of L's, then R's, then L's, then R's,
        where each group has at least ONE
        character and max TEN, and together.

        This proposal is not implemented in the
        web application, so it is foreign to this
        one, and iy is as an interesting proposal
        to have passwords with the language:
        L' = { L = { (L^n)(R^m)(L^o)(R^p):
        (1 <= n, m, o, p <= 10 };

        That is to say; passwords of four alternating
        groups (same as the previous proposal, but in
        which each one only admits a maximum of 10
        symbols pero group).

        It is also proposed in the future to extend the
        language that accepts passwords beginning with
        groups of R's, not just L's.

        It returns True or False depending on whether
        or not it accepts the parameter password.
    '''

    #? The pushdown automaton is instantiated:
    States = {"q0", "q1", "q2", "q3", "q4", "q5"}
    Alphabet = {"L", "R"}
    Initial = "q0"
    Finals = {"q4"}
    Stackalph = {"1", "Z"}
    Stack = ["Z"]
    Transitions = [
        ("q0", "L", "Z", "1111111111111111111111111111111111111111Z", "q1"),
        ("q1", "L", "1", "", "q1"),
        ("q1", "R", "1", "", "q2"),
        ("q2", "R", "1", "", "q2"),
        ("q2", "L", "1", "", "q3"),
        ("q3", "L", "1", "", "q3"),
        ("q3", "L", "1", "", "q3"),
        ("q3", "R", "1", "", "q4"),
        ("q4", "R", "1", "", "q4"),
        ("q4", "", "Z", "Z", "q5")
    ]
    Automata = PDA(States, Alphabet, Transitions, Initial, Finals, Stackalph, Stack)
    Automata.show()
    print()
    return True if Automata.accepts(password, stepByStep=True) else False


#! Main execution point:
if __name__ == "__main__":

    while True:
        # os.system("cls")
        print()
        password = input("Password: ")
        if validatePassword(password):
            print(f"\nThe password \"{password}\" HAS a correct format!\n")
        else:
            print(f"\nThe password \"{password}\" HAS NOT a correct format!\n")
        print()
        print("═"*40)
        print("\n")
        # os.system("pause")