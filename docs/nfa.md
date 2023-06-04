## 🤖 NFA

### Non-deterministic Finite Automaton

#### [📑 ATTRIBUTES](#-attributes-1 "ATTRIBUTES")
#### [🎮 METHODS](#-methods-1 "METHODS")
#### [💻 EXAMPLES](#-examples-1 "EXAMPLES")

<hr>

<br>

#### 📑 ATTRIBUTES

**NOTE:** ALL THE PARAMETERS ARE OPTIONAL;

**NOTE:** YOU CAN ADD ELEMENTS WITH RESPECTIVE FUNCTIONS:
"NFA" create an instance of a Non-deterministic Finite Acceptor.

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

`("q0", "a", "q1")`

Where:

* `"q0"` is the current state of the transition;

* `"a"` is the symbol that will read on the current state; **It can be `""`; for lambda/epsilon transitions;**

* `"q1"` is the next state after the symbol reading;

Example of transitions set:

`{ ("q0", "a", "q1"),  ("q0", "", "q1"),  ("q1", "a", "q1")" };`

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
```

**📌 Second example:**

```python
from Pytomatas.nfa import NFA

# Second example of NFA Automata instance:
# Language of the Automata:
# L(Automata) = {aba(b^n): n>0} U
# {ab(a^n): n>=0};
#* States:
Q = {"q0", "qa", "qab", "qf", "qabf"}

#* Alphabet:
A = {"a", "b"}

#* Starting state:
S = "q0"

#* Finals states:
F = {"qf", "qabf"}

#* Transitions:
T = [
    ("q0", "a", "qa"),
    ("qa", "b", "qab"),
    ("qab", "a", "qf"),
    ("qf", "b", "qf"),
    ("qab", "", "qabf"),
    ("qabf", "a", "qabf")
]

#? Automata:
Automata = NFA(Q, A, T, S, F)
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