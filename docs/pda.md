## 🤖 PDA

### Pushdown Automaton
#### Deterministic / Non-Deterministic

#### [📑 ATTRIBUTES](#-attributes-1 "ATTRIBUTES")
#### [🎮 METHODS](#-methods-1 "METHODS")
#### [💻 EXAMPLES](#-examples-1 "EXAMPLES")

<hr>

<br>

#### 📑 ATTRIBUTES

**NOTE:** ALL THE PARAMETERS ARE OPTIONAL;

**NOTE:** YOU CAN ADD ELEMENTS WITH RESPECTIVE FUNCTIONS:
"PDA" create an instance of a Pushdown Automata Acceptor (Deterministic & Non-deterministic).

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

`("q0", "a", "Z", "11Z", "q1")`

Where:

* `"q0"` is the current state of the transition;

* `"a"` is the symbol that will read on the current state; **It can be `""`; for lambda/epsilon transitions;**

* `"Z"` is the top symbol on the stack on these transition;

* `"11Z"` is the symbols it will push on the stack:

In these order, the `"Z"` will be stay at the bottom of th stack;

It takes symbol per symbol, in a whole-string;

* `"q1"` is the next state after the transition;

Example of transitions set:

`{ ("q0", "a", "Z", "11Z", "q1"),  ("q1", "b", "1", "22", "q2")}`

**NOTE:** `("q0", "", "1", "", "q1")` is a lambda/epsilon transition from
`"q0"` to `"q1"`; only valid to `""` empty symbol definition;

**NOTE:** `("q0", "", "q1")` is a lambda/epsilon transition from `"q0"` to` "q1"`; only valid to `""` empty symbol definition;

<hr>

**4. initial** `(string)`: Represents your initial state.

If it is not included in *"states"*, it will add on it;

Example: `"q0"`

<hr>

**5. finals** `(set of strings)`: Set of final states of the
Automata;

Example: `{"q1, "q2", "qf"}`

<hr>

**6. stackAlphabet** `(set of strings)`: Set of the valide symbols on the
stack future data; it is only for show the automata information.

<hr>

**8. initialStack** `(list of strings)`: The strings should be characters
only. This is the initial state of the stack; `["Z"]` as default.

If you put: `["1", "2", "Z"]`: `"1"` is on the top, and `"Z"` in the bottom.

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

 - For Automata Stack:
    - **addStackSymbol** `(symbol: str)`: Adds a symbol for the automata stack alphabet.
    - **setStackAlphabet** `(alphabet: set)`: Sets the automata stack alphabet.

    - **setInitialStack** `(stack: list)`: Sets the initial stack of the automata.

- **Automata Functions:**

  - **show** `()`: Prints the automaton data.

  - **accepts** `(string: str, stepByStep: bool = False)`: Determines if the string is accepted by the automaton.
    - If `stepByStep` prints all the steps while reading the string.
    - If `stepByStep` is False, or is not defined, only does the reading process.
  
  - **transite** `(symbol: str, printStep: bool = False)`: Changes the actual state based on the symbol and transitions.
    - If `printStep` is True, prints the transition.
    - If `printStep` is False, or is not defined, only does the transition.

- **Functions Details:**

	- **show** `()`
	  - ***Description:*** Prints the automaton data.
	  - ***Parameters:***
		- None.
	  - ***Returns:*** None.

	- **transite** `(symbol: str, printStep: bool = False)`
	  - ***Description:*** Changes the actual state based on the symbol and transitions.
	  - ***Parameters:***
		- `symbol` (str): The actual reading symbol.
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
from Pytomatas.pda import PDA

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
```

**📌 Second example:**

```python
from Pytomatas.pda import PDA

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
```

<br>

<hr>
💜