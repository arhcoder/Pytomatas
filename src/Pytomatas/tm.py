'''
    TURING MACHINE
'''

class TM:

    #/ Attributes #
    States: list = []
    Alphabet: list = []
    Transitions: list = []
    Initial: str = ""
    Finals: list = []

    #* Constructor #
    def __init__(self, states: set={}, alphabet: set={}, transitions: list=[], initial: str="", finals: set={}):

        '''
            CONSTRUCTOR:
            NOTE: ALL THE PARAMETERS ARE OPTIONAL;
            NOTE: YOU CAN ADD ELEMENTS WITH RESPECTIVE FUNCTIONS:
            "TM" creates an instance of a Turing Machine.
            It receives:

            1. "states" (set of strings): In a set, add strings to represent
            each state of the Turing Machine. Example:
            {"q0", "q1", "q2", "qf", "qx", "dx"};

            2. "alphabet" (set of strings): In a set, add all the symbols that
            the Turing Machine reads. If you add two characters as a symbol,
            note that it will be considered as a single unique symbol.
            NOTE: Upper and lower case generate different symbols.
            Example:
            {"ea", "ra", "faszaa"} <- Three-symbol alphabet;
            {"A", "a", "B", "b"} <- Four-symbol alphabet;
            {"a", "b", "c", "d", "d", "d", "d"} <- Four-symbol alphabet;

            3. "transitions" (set of *transitionObject* (tuples)):
            *transitionObject* looks like this:
            ("q0", "a", "b", "R", "q1");
            Where:
                * "q0" is the current state of the transition;
                * "a" is the symbol that the Turing Machine reads on the current state;
                * "b" is the symbol that the Turing Machine writes on the current position;
                * "R" or "L" specifies the direction the Turing Machine head moves after the transition;
                * "q1" is the next state after the transition.
            Example of a transitions set:
            { ("q0", "a", "b", "R", "q1"), ("q0", "b", "c", "L", "q1"), ("q1", "a", "a", "R", "q1") };
            NOTE: FOR THE BLANK SYMBOL USE "*".

            4. "initial" (string): Represents the initial state of the Turing Machine.
            If it is not included in "states", it will be added to the set of states.
            Example: "q0";

            5. "finals" (set of strings): Set of final states of the Turing Machine.
            Example: {"q1", "q2", "qf"};

            RETURNS AN INSTANCE OF THE TURING MACHINE;
        '''

        # The values of the automata #
        self.States = states
        self.Alphabet = alphabet
        self.Transitions = transitions
        self.Initial = initial
        self.Finals = finals

    #* Getter:
    def __getattribute__(self, __name: str):
        return super(TM, self).__getattribute__(__name)
    
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
        '''Prints Turing Machine data'''
        print()
        print("═"*40)
        print("\nTURING MACHINE\n")
        print("═"*40)
        print(f"\nStates: {set(self.States)}")
        print(f"Alphabet: {set(self.Alphabet)}")
        print(f"Initial state: \"{self.Initial}\"")
        print(f"Final states: {set(self.Finals)}")
        for t in self.Transitions:
            t1 = t[1] if t[1] != "*" else "□"
            t2 = t[2] if t[2] != "*" else "□"
            print(f"* δ(\"{t[0]}\", \"{t1}\") = (\"{t[3]}\", \"{t2}\", \"{t[4]}\")")
        print()
        print("═"*40)
    
    def transite(self, symbol: str, printStep: bool = False):
        '''
            Receives the current reading symbol;
            Based on the current state and the transitions,
            it changes the current state and performs the necessary actions.
        '''

        # Check if the transition exists:
        validTransitions = []
        for transition in self.Transitions:
            if self.current == transition[0] and symbol == transition[1]:
                validTransitions.append(transition)
        
        # If the Turing Machine has no valid transitions or more than one valid transition
        if len(validTransitions) != 1:
            print(f" * Invalid transition in \"{self.current}\" reading \"{symbol}\"!")
            self.error = True
            return
        
        # Perform the transition:
        else:
            if printStep:
                print(f" * \"{self.current}\" reads \"{symbol}\", writes \"{validTransitions[0][2]}\", moves {str(validTransitions[0][3]).upper()}, goes to \"{validTransitions[0][4]}\";")
            
            self.current = validTransitions[0][4]
            self.tape[self.head] = validTransitions[0][2]

            # Move the head and extend the tape if necessary:
            if str(validTransitions[0][3]).upper() == "R":
                self.head += 1
                if self.head == len(self.tape):
                    self.tape.append("*")
            elif str(validTransitions[0][3]).upper() == "L":
                self.head -= 1
                if self.head < 0:
                    self.tape.insert(0, "*")
    
    def accepts(self, string: str, stepByStep: bool = False):
        '''
            Receives a string to process;
            Returns True if the string is accepted;
            Returns False if the string is not accepted;
        '''

        # Initialize the current state as the initial state and the tape with the string:
        self.current = self.Initial
        self.error = False
        self.tape = list(string)
        self.head = 0

        # It shows the step-by-step path for the string:
        if stepByStep:
            print(f"\nFor string \"{string}\":\n")

        # Process each symbol on the tape:
        while self.current not in self.Finals and not self.error:
            symbol = self.tape[self.head]
            self.transite(symbol, stepByStep)
        
        print()
        
        # Check if the string was accepted or not:
        if self.error:
            return False

        if self.current in self.Finals:
            return True
        else:
            return False