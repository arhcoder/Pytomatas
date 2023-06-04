## 🤖 TM

### Turing Machine

#### [📑 ATTRIBUTES](#-attributes "ATTRIBUTES")
#### [🎮 METHODS](#-methods "METHODS")
#### [💻 EXAMPLES](#-examples "EXAMPLES")

<hr>

<br>

#### 📑 ATTRIBUTES

**NOTE:** ALL THE PARAMETERS ARE OPTIONAL;

**NOTE:** YOU CAN ADD ELEMENTS WITH RESPECTIVE FUNCTIONS:
"TM" create an instance of a Turing Machine Acceptor.

<hr>

**1. states** `(set of strings)`: In a set, add a strings to represent each state of the automata; Example:

`{"q0", "q1", "q2", "qf", "qx", "dx"}`

<hr>

**2. alphabet** `(set of strings)`: In a set, add all the symbols that
the automata reads. If you add to chars as a symbol.

**NOTE:** If you add a "symbol" as a string of more than one char, it will
take it as a unique letter;

**NOTE:** Upper and Lower case generates different symbols;
Example:

`{"ea", "ra", "faszaa"}` <- Three symbols alphabet;

`{"A", "a", "B", "b"}` <- Four symbols alphabet;

`{"a", "b", "c", "d", "d", "d", "d"}` <- Four symbols alphabet;

<hr>

**3. transitions** `(set of *transitionObject* (tuples))`:

*transitionObject* looks like this:

`("q0", "a", "b", "R", "q1")`

Where:

* `"q0"` is the current state of the transition;

* `"a"` is the symbol that the Turing Machine reads on the current state;

* `"b"` is the symbol that the Turing Machine writes on the current position;

* `"R"` or `"L"` specifies the direction the Turing Machine head moves after the transition;

* `"q1"` is the next state after the transition.

Example of a transitions set:

`{ ("q0", "a", "b", "R", "q1"), ("q0", "b", "c", "L", "q1"), ("q1", "a", "a", "R", "q1") };`

**NOTE: FOR THE BLANK SYMBOL USE `"*"`.**

<hr>

**4. initial** `(string)`: Represents your initial state.

If it is not included in *"states"*, it will add on it;

Example: `"q0"`

<hr>

**5. finals** `(set of strings)`: Set of final states of the
Automata;

Example: `{"q1, "q2", "qf"}`

<hr>

<br>

#### 🎮 METHODS

- **Getter:**
  - **__getattribute__** `(__name: str)`: Returns the attribute of the class.

- **Setters:**
  - For Automata States:
    - **addState** `(state: str)`: Adds a state to the automaton.
    - **setStates** `(states: set)`: Sets the states of the automaton.

  - For Automata Alphabet:
    - **addSymbol** `(symbol: str)`: Adds a symbol to the alphabet.
    - **setAlphabet** `(alphabet: set)`: Sets the alphabet of the automaton.

  - For Automata Transitions:
    - **addTransition** `(transition: tuple)`: Adds a transition to the automaton.
    - **setTransitions** `(transitions: list)`: Sets the transitions of the automaton.

  - For Automata Initial State:
    - **setInitial** `(initial: str)`: Sets the initial state of the automaton.

  - For Automata Final States:
    - **addFinal** `(final: str)`: Adds a final state to the automaton.
    - **setFinals** `(finals: set)`: Sets the final states of the automaton.

- **Automata Functions:**

  - **show** `()`: Prints the automaton data.

  - **accepts** `(string: str, stepByStep: bool = False)`: Determines if the string is accepted by the automaton.
    - If `stepByStep` prints all the steps while reading the string.
    - If `stepByStep` is False, or is not defined, only does the reading process.
  
  - **transite** `(symbol: str, printStep: bool = False)`: Changes the current state based on the symbol and transitions.
    - If `printStep` is True, prints the transition.
    - If `printStep` is False, or is not defined, only does the transition.

- **Functions Details:**

	- **show** `()`
	  - ***Description:*** Prints the automaton data.
	  - ***Parameters:***
		- None.
	  - ***Returns:*** None.

	- **transite** `(symbol: str, printStep: bool = False)`
	  - ***Description:*** Changes the current state based on the symbol and transitions.
	  - ***Parameters:***
		- `symbol` (str): The current reading symbol.
		- `printStep` (bool): Whether to print each step or not (default: False).
	  - ***Returns:*** None.

	- **accepts** `(string: str, stepByStep: bool = False)`
	  - ***Description:*** Determines if the string is accepted by the automaton.
	  - ***Parameters:***
		- `string` (str): The string to read.
		- `stepByStep` (bool): Whether to show the step-by-step path (default: False).
	  - ***Returns:*** `True` if the string is accepted, `False` otherwise.

<hr>

<br>

#### 💻 EXAMPLES

📌 **First example:**

```python
from pytomata.tm import TM

# First example of TM Automata instance:
# Language of the Automata:
# Turing Machine to recognize the language;
# L = {0^n 1^n 2^n: n >= 1}
# All strings consisting of zero or more consecutive
# '0's followed by an equal number of consecutive '1's",
# and equal number of 2's then.

#* States:
Q = {"q0", "q1", "q2", "q4", "q5"}

#* Alphabet
#? (* is Blank Symbol):
A = {"0", "1", "2", "X", "Y", "Z", "*"}

#* Initial state:
S = "q0"

#* Accept states:
F = {"q5"}

#* Transitions:
#? (current_state, current_symbol, new_symbol, move_direction, next_state)
T = [
    ("q0", "0", "X", "R", "q1"),
    ("q0", "Y", "Y", "R", "q4"),

    ("q1", "Y", "Y", "R", "q1"),
    ("q1", "0", "0", "R", "q1"),
    ("q1", "1", "Y", "R", "q2"),

    ("q2", "Z", "Z", "R", "q2"),
    ("q2", "1", "1", "R", "q2"),
    ("q2", "2", "Z", "L", "q3"),

    ("q3", "X", "X", "R", "q0"),
    ("q3", "0", "0", "L", "q3"),
    ("q3", "1", "1", "L", "q3"),
    ("q3", "Y", "Y", "L", "q3"),
    ("q3", "Z", "Z", "L", "q3"),

    ("q4", "Y", "Y", "R", "q4"),
    ("q4", "Z", "Z", "R", "q4"),
    ("q4", "*", "*", "L", "q5")
]

#? Automata:
Automata = TM(Q, A, T, S, F)
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
```

**📌 Second example:**

```python
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
```

<br>

<hr>
💜