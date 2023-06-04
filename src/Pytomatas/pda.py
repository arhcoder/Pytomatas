'''
    PUSHDOWN FINITE AUTOMATON
'''

class PDA:

    #/ Attributes #
    States: list = []
    Alphabet: list = []
    Transitions: list = []
    Initial: str = ""
    Finals: list = []
    StackAlphabet: list = []
    InitialStack: list = ["Z"]

    #/ Variables #
    currents: list = []
    correct: bool = False
    error: bool = False
    stack: list = []

    #* Constructor #
    def __init__(self, states: set={}, alphabet: set={}, transitions: list=[], initial: str="", finals: set={}, stackAlphabet: set={}, initialStack: list = ["Z"]):

        '''
            CONSTRUCTOR:
            NOTE: ALL THE PARAMETERS ARE OPTIONAL;
            NOTE: YOU CAN ADD ELEMENTS WITH RESPECTIVE FUNCTIONS:
            "PDA" create an instance of a No-Deterministic Pushdown Acceptor.
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
            ("q0", "a", "Z", "11Z", "q1");
            Where:
                * "q0" is the current state of the transition;
                * "a" is the symbol that will read on the currents state;
                It can be ""; for lambda/epsilon transitions;
                * "Z" is the top symbol on the stack on these transition;
                * "11Z" is the symbols it will push on the stack:
                In these order, the "Z" will be stay at the bottom of th stack;
                It takes symbol per symbol, in a whole-string;
                * "q1" is the next state after the transition;
            Example of transitions set:
            { ("q0", "a", "Z", "11Z", "q1"),  ("q1", "b", "1", "22", "q2")};
            NOTE: ("q0", "", "1", "", "q1") is a lambda/epsilon transition from
            "q0" to "q1"; only valid to "" empty symbol definition;

            4. "initial" (string): Represents your initial state.
            If it is not included in "states", it will add on it;
            Example: "q0";

            5. "finals" (set of strings): Set of final states of the
            Automata; Example: {"q1, "q2", "qf"};

            6. "stackAlphabet" (set of strings): Set of the valide symbols on the
            stack future data; it is only for show the automata information.

            8. "initialStack" (list of strings): The strings should be characters
            only. This is the initial state of the stack; ["Z"] as default.
            If you put: ["1", "2", "Z"]: "1" is on the top, and "Z" in the bottom.

            RETURNS AN INSTANCE OF THE AUTOMATA;
        '''

        # The values of the automata #
        self.States = list(states)
        self.Alphabet = list(alphabet)
        self.Transitions = list(transitions)
        self.Initial = initial
        self.Finals = list(finals)
        self.StackAlphabet = list(stackAlphabet)
        self.InitialStack = list(initialStack)
        self.currents = list([initial])
        self.stack = list(initialStack)

    #* Getter:
    def __getattribute__(self, __name: str):
        return super(PDA, self).__getattribute__(__name)
    
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
        self.currents = [initial]
    
    #/ For Automata Final States:
    def addFinal(self, final: str):
        self.Finals.append(final)
    def setFinals(self, finals: set):
        self.Finals = list(finals)
    
    #/ For Automata Stack Alphabet:
    def addStackSymbol(self, symbol: str):
        self.StackAlphabet.append(symbol)
    def setStackAlphabet(self, alphabet: set):
        self.StackAlphabet = list(alphabet)

    #/ For Automata Initial stack:
    def setInitialStack(self, stack: list):
        self.InitialStack = list(stack)
    

    #? Methods:
    def show(self):
        '''Prints Automata data'''
        print()
        print("═"*40)
        print("\nPUSHDOWN FINITE AUTOMATON\n")
        print("═"*40)
        print(f"\nStates: {set(self.States)}")
        print(f"Alphabet: {set(self.Alphabet)}")
        print(f"Initial state: \"{self.Initial}\"")
        print(f"Final states: {set(self.Finals)}")
        print(f"Stack alphabet: {set(self.StackAlphabet)}")
        userShowStack = self.InitialStack[:]
        userShowStack.reverse()
        print(f"Initial stack: {userShowStack}")
        for t in self.Transitions:
            t1 = t[1] if t[1] != "" else "λ"
            t2 = t[2] if t[2] != "" else "λ"
            t3 = t[3] if t[3] != "" else "λ"
            print(f"* δ(\"{t[0]}\", \"{t1}\", \"{t2}\") = (\"{t3}\", \"{t[4]}\")")
        print()
        print("═"*40)

    def transite(self, symbol: str, printStep: bool = False):
        '''
            Recieves a reading symbol;
            Based on the currents states and the transitions,
            It changes the currents states to move;
        '''

        #* Example of moving transition:
        #* ("q0", "a", "1", "11Z" "q1");

        #/ The transition works like this:
        #* If self.currents in [transition[0](currents state on the transition tuple)]
        #* and symbol == [transition[1](letter on the transition tuple)]:
        #* and top stack symbol == transition[2], then:
        #* push on the stack each character of transition[3], and:
        #* self.currents.append([transition[4](next state on the transition tuple)]);

        validTransitions = []
        for current in self.currents:
            for transition in self.Transitions:
                # print(self.stack[len(self.stack)-1])
                # print(f"if ({current} == {transition[0]}) and ({symbol} == {transition[1]} or {transition[1]} == \"\") and ({self.stack[len(self.stack)-1]} == {transition[2]}):")
                #* If it has an empty stack and pendient transitions:
                if len(self.stack) == 0:
                    topSymbol = ""
                else:
                    topSymbol = self.stack[len(self.stack)-1]
                if (current == transition[0]) and (symbol == transition[1] or transition[1] == "") and (topSymbol == transition[2]) and (not self.error):
                    print(" * Transition to take:", transition)
                    validTransitions.append(transition)
        
        # If Automata has 0 transitions, it will go to the "limbo"; means error;
        # But only if it is more string to read:
        takesALambdaTransition = False
        if len(validTransitions) == 0 and len(self.stack) > 0:
            # If there is no more string:
            if symbol == "":
                # Checks if it arrives to a final state:
                for current in self.currents:
                    if current in self.Finals:
                        self.correct = True
                    # The state is lost; the string is not accepted:
                    else:
                        self.correct = True
                        self.currents.clear
                        self.error = True
                return
            else:
                self.currents.clear
                self.error = True
                return
        # It still can moves:
        else:
            newStates = []
            for transition in validTransitions:
                # Prints the path:
                if printStep:
                    print(" * Current states:", self.currents)
                    print(" * Reading symbol:", symbol)
                    userShowStack = self.stack[:]
                    userShowStack.reverse()
                    print(" * Stack:", userShowStack)
                    if len(self.stack) == 0:
                        topSymbol = ""
                    else:
                        topSymbol = self.stack[len(self.stack)-1]
                    print(" * Top symbol on stack:", topSymbol)
                    print(" * Symbol to stack", transition[3])
                    destinies = []
                    for destiny in validTransitions:
                        destinies.append(destiny[4])
                    print(" * Destinations: ", destinies)

                    print()

                # It moves to the next states:
                newStates.append(transition[4])

                # It pop the stack top symbol:
                if len(self.stack) > 0:
                    self.stack.pop()
                else:
                    # self.error = True
                    return

                # It push down symbols on the stack:
                stacking = transition[3]
                if len(stacking) > 0:
                    stacking = reversed(stacking)
                    for stackSymbol in stacking:
                        self.stack.append(stackSymbol)

                # If it came from a lambda transition,
                # It has to preserve the readed symbol:
                if transition[1] == "":
                    takesALambdaTransition = True

            self.currents = newStates
            if takesALambdaTransition and len(self.currents) == 1:
                self.transite(symbol)

    def accepts(self, string: str, stepByStep: bool = False):
        '''
            Recieves a string to read;
            Returns true if the string is accepted;
            Returns false if the string is not accepted;
        '''

        # Initialize the currents state as the initial:
        self.stack = list(self.InitialStack)
        self.currents = [self.Initial]
        self.error = False
        self.correct = False
        
        # It shows the step by step path for the string:
        if stepByStep:
            print(f"\nTo string \"{string}\":\n")

        # If the string is empty:
        if len(string) == 0:
            # Moves while it can:
            while len(self.currents) > 0 and not self.correct:
                self.transite("", stepByStep)

        # Reads letter per letter:
        for character in string:
            self.transite(character, stepByStep)
        
        # Moves while it can:
        while len(self.currents) > 0 and not self.correct:
            self.transite("", stepByStep)
        
        # If the string was accepted or not:
        # Firstly checks if transitionsCount == word lenght,
        # If not, is because it has an invalid transition:
        if self.error:
            return False

        for current in self.currents:
            if current in self.Finals:
                return True
        if self.correct == True:
                return True
        return False