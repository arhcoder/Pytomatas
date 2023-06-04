'''
    DETERMINISTIC FINITE AUTOMATONS
'''

class DFA:

    #/ Attributes #
    States: list = []
    Alphabet: list = []
    Transitions: list = []
    Initial: str = ""
    Finals: list = []

    #/ Variables #
    current: str = ""
    error: bool = False


    #* Constructor #
    def __init__(self, states: set={}, alphabet: set={}, transitions: list=[], initial: str="", finals: set={}):

        '''
            CONSTRUCTOR:
            NOTE: ALL THE PARAMETERS ARE OPTIONAL;
            NOTE: YOU CAN ADD ELEMENTS WITH RESPECTIVE FUNCTIONS:
            "DFA" create an instance of a Deterministic Finite Acceptor.
            It recieves:

            1. "states" (set of strings): In a set, add a strings to represent
            each state of the automata; Example:
            {"q0", "q1", "q2", "qf", "qx", "dx"};

            2. "alphabet" (set of strings): In a set, add all the symbols that
            the automata reads. If you add to chars as a symbol.
            NOTE: If you add a "symbol" as a string of more than one char, it will
            take it as a unique letter;
            NOTE: Upper and Lower case generates different symbols;
            Example:
            {"ea", "ra", "faszaa"} <- Three symbols alphabet;
            {"A", "a", "B", "b"} <- Four symbols alphabet;
            {"a", "b", "c", "d", "d", "d", "d"} <- Four symbols alphabet;

            3. "transitions" (set of *transitionObject* (tuples)):
            *transitionObject* looks like this:
            ("q0", "a", "q1");
            Where:
                * "q0" is the current state of the transition;
                * "a" is the symbol that will read on the current state;
                * "q1" is the next state after the symbol reading;
            Example of transitions set:
            { ("q0", "a", "q1"),  ("q0", "b", "q1"),  ("q1", "a", "q1")" };

            4. "initial" (string): Represents your initial state.
            If it is not included in "states", it will add on it;
            Example: "q0";

            5. "finals" (set of strings): Set of final states of the
            Automata; Example: {"q1, "q2", "qf"};

            RETURNS AN INSTANCE OF THE AUTOMATA;
        '''

        # The values of the automata #
        self.States = list(states)
        self.Alphabet = list(alphabet)
        self.Transitions = list(transitions)
        self.Initial = initial
        self.Finals = list(finals)
        self.current = initial

    #* Getter:
    def __getattribute__(self, __name: str):
        return super(DFA, self).__getattribute__(__name)
    
    #* Setters:
    #/ For Automata States:
    def addState(self, state: str):
        self.States.append(state)
    def setStates(self, states: set):
        self.States = list(states)
    
    #/ For Automata Alphabet:
    def addSymbol(self, symbol: str):
        self.Alphabet.append(symbol)
    def setAlphabet(self, alphabet: set):
        self.Alphabet = list(alphabet)
    
    #/ For Automata Transitions:
    def addTransition(self, transition: tuple):
        self.Transitions.append(transition)
    def setTransitions(self, transitions: list):
        self.Transitions = transitions
    
    #/ For Automata Initial State:
    def setInitial(self, initial: str):
        if not initial in self.States:
            self.States.append(initial)
        self.Initial = initial
        self.current = initial
    
    #/ For Automata Final States:
    def addFinal(self, final: str):
        self.Finals.append(final)
    def setFinals(self, finals: set):
        self.Finals = list(finals)
    

    #? Methods:
    def show(self):
        '''Prints Automata data'''
        print()
        print("═"*40)
        print("\nDETERMINISTIC FINITE AUTOMATON\n")
        print("═"*40)
        print(f"\nStates: {set(self.States)}")
        print(f"Alphabet: {set(self.Alphabet)}")
        print(f"Initial state: \"{self.Initial}\"")
        print(f"Final states: {set(self.Finals)}")
        for t in self.Transitions:
            t1 = t[1] if t[1] != "" else "λ"
            print(f"* δ(\"{t[0]}\", \"{t1}\") = (\"{t[2]}\")")
        print()
        print("═"*40)

    def transite(self, symbol: str, printStep: bool = False):
        '''
            Recieves an current reading symbol;
            Based on the current state and the transitions,
            It changes the current state to move;
        '''

        #/ The transition works like this:
        #* If self.current == [transition[0](current state on the transition tuple)]
        #* and symbol == [transition[1](letter on the transition tuple)], then:
        #* self.current = [transition[2](next state on the transition tuple)];
        validTransitions = []
        for transition in self.Transitions:
            if self.current == transition[0] and symbol == transition[1]:
                validTransitions.append(transition)
        
        # If Automata has 0 or more than 1 transitions;
        if len(validTransitions) != 1:
            print(f" * Transition δ(\"{self.current}\", \"{symbol}\") is invalid!")
            self.error = True
            return
        # Else; it generates a transition:
        else:
            if printStep:
                print(f" * \"{self.current}\" reads \"{symbol}\" => \"{validTransitions[0][2]}\";")
            self.current = validTransitions[0][2]
    
    def accepts(self, string: str, stepByStep: bool = False):
        '''
            Recieves a string to read;
            Returns true if the string is accepted;
            Returns false if the string is not accepted;
        '''

        # Initialize the current state as the initial:
        self.current = self.Initial
        self.error = False

        # It shows the step by step path for the string:
        if stepByStep:
            print(f"\nFor string \"{string}\":\n")

        # Reads letter per letter:
        for character in string:
            self.transite(character, stepByStep)
        
        print()
        
        # If the string was accepted or not:
        # Firstly checks if transitionsCount == word lenght,
        # If not, is because it has an invalid transition:
        if self.error:
            return False

        if self.current in self.Finals:
            return True
        else:
            return False