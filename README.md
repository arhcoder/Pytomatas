# 🤖 Pytomata

**📌 Version 1.6.0**

<hr>

Pytomata allows to simulate Acceptor Automata in the console with Python, implementing its characteristics using different definitions (mathematics included), with the following types:

* **[DFA](https://github.com/arhcoder/Pytomata/docs/dfa.md  "DFA") (Deterministic Finite Automaton)**;
* **[NFA](https://github.com/arhcoder/Pytomata/docs/nfa.md "NFA") (Non-deterministic Finite Automaton)**;
* **[PDA](https://github.com/arhcoder/Pytomata/docs/pda.md "PDA") (Push-Down Automaton)**;
* **[TM](https://github.com/arhcoder/Pytomata/docs/tm.md "TM") (Turing Machine)**;

What can do?

- Create and manage various types of automaton: DFA, NFA, PDA, TM.
- Visualize automata information in console.
- Simulate automata acceptors based on strings.
- Observe the processes of steps and transitions when introducing a string to the automaton.

<br>

## 📍 Index

- **🛠 [Installation](#-installation)**;
- **💻 [Usage](#-usage)**;
  - **🧿 [First implementation](#-first-implementation)**;
  - **🧿 [Second implementation](#-second-implementation)**;
- **📓 [Documentation](#-documentation)**;
- **📚 [Examples](#-examples)**;
  - **🤖 [DFA](https://github.com/arhcoder/Pytomata/docs/dfa.md  "DFA")**;
  - **🤖 [NFA](https://github.com/arhcoder/Pytomata/docs/nfa.md "NFA")**;
  - **🤖 [PDA](https://github.com/arhcoder/Pytomata/docs/pda.md "PDA")**;
  - **🤖 [TM](https://github.com/arhcoder/Pytomata/docs/tm.md "TM")**;
  - **🔐 [Safebox](https://github.com/arhcoder/Pytomata/docs/xsafebox.md)**;
- **📁 [Repository](#-repository)**;
- **✍ [Contributing](#-contributing)**;
- **📜 [License](#-license)**;

<br>

## 🛠 Installation

You can install Pytomata using pip:

```bash
pip install pytomata
```

<br>

## 💻 Usage

There are two ways in which automata can be implemented:
1. Creating the empty automaton and then adding the properties.
2. Creating the automaton by passing its characteristics as in the mathematical definition.

Example of a DFA implementation...

#### 🧿 First implementation

**1. Creating empty automata and then give the data:**

```python
from pytomata import DFA

# Creates a DFA called "my_dfa":
my_dfa = DFA()

# Define to "my_dfa" a set of states names:
my_dfa.setStates( {"q0", "q1", "qfinal"} )

# Define to "my_dfa" a set of states characters of the alphabet:
my_dfa.setAlphabet( {"a", "b"} )

# Set the "Initial state" name of "my_dfa":
my_dfa.setInitial( "q0" )

# Define to "my_dfa" the set of "Final states" names:
my_dfa.setFinals( {"qfinal", "qf2"} )

# Add transitions to the DFA:
my_dfa.addTransition( ("q0", "a", "q1") )
my_dfa.addTransition( ("q0", "b", "qfinal") )
my_dfa.addTransition( ("q1", "a", "q1") )
my_dfa.addTransition( ("q1", "b", "q1") )
my_dfa.addTransition( ("qfinal", "a", "qfinal") )
my_dfa.addTransition( ("qfinal", "b", "qfinal") )

# Add more data to the existing one already in the automata:
my_dfa.addSymbol("c")
my_dfa.addState("qx")
my_dfa.addState("finalState2")
my_dfa.addFinal("finalState2")

# Prints the DFA information:
my_dfa.show()

# Check if a string is accepted on the defined automata "my_dfa":
# It returns True or False if the string is accepted or not:
word = "aaabb"
my_dfa.accepts(word)

# Checks if the string is accepted, but prints all the process and steps on transitions;
# Shows the flow of states while reading the string;
my_dfa.accepts(word, stepByStep=True)
```

#### 🧿 Second implementation

**2. Creating the automata passing the data:**

```python
from pytomata import DFA

# Declare the States:
Q = {"q0", "qa", "q1", "qb", "q2", "qf", "qx"}

# Declare the Alphabet:
A = {"a", "b"}

# Declare the Initial (start) state:
S = "q0"

# Declare the Finals states:
F = {"q2", "q3"}

# Declare the Transitions:
T = [
	("q0", "a", "qa"),
	("q0", "b", "q1"),
	("qa", "a", "qa"),
	("qa", "b", "qb"),
	("qf", "b", "qf"),
	("qx", "a", "qx"),
	("qx", "b", "qx")
]

# Declare the Automata:
my_dfa = DFA(Q, A, T, S, F)

# Show the automata information:
my_dfa.show()

# Check if a string is accepted on the defined automata "my_dfa":
# It returns True or False if the string is accepted or not:
word = "aaabb"
my_dfa.accepts(word)

# Checks if the string is accepted, but prints all the process and steps on transitions;
# Shows the flow of states while reading the string;
# It returns True or False if the string is accepted or not:
my_dfa.accepts(word, stepByStep=True)
```

#### 🛑 NOTE: These are only implementation examples, not actual implementations, so they are not complete real automata definitions 👆

* For more detailed information about the attributes and methods of the class, refer to **[Documentation](#-Documentation  "Documentation")**.

* For more detailed usage instructions and examples, please refer to **[Examples](#-Examples  "Examples")**.

<br>

## 📓 Documentation

Go to **[THIS LINK](http://github.com/arhcoder/Pytomata/docs/automatas.md "THIS LINK")** to see the documentation on all the features of the different types of automata, the functions they have, and examples of their implementation.

<br>

## 📚 Examples

1. **[DFA (Deterministic Finite Automaton)](https://github.com/arhcoder/Pytomata/docs/dfa.md  "DFA").**

2. **[NFA (Non-deterministic Finite Automaton)](https://github.com/arhcoder/Pytomata/docs/nfa.md "NFA").**

3. **[PDA (Push-Down Automaton)](https://github.com/arhcoder/Pytomata/docs/pda.md "PDA").**

4. **[TM (Turing Machine)](https://github.com/arhcoder/Pytomata/docs/tm.md "TM").**

5. **[Safebox Automata Implementation Project](https://github.com/arhcoder/Pytomata/docs/xsafebox.md).**

<br>

## 📁 Repository

Go to **[THIS LINK](https://github.com/arhcoder/Pytomata)** to check out the source code.

<br>

## ✍ Contributing

Contributions are welcome! If you encounter any issues, have suggestions, or would like to contribute to the project, please feel free to open an issue or submit a pull request on **[this repository](https://github.com/arhcoder/Pytomata)**.

<br>

## 📜 License

This project is licensed under the MIT License - see the **[LICENSE](https://github.com/arhcoder/Pytomata/blob/master/LICENSE)** file for details.

<br>

**Made with 💜 by @arhcoder**;

<br>