# ✅ Import TypedDict to define the structure (schema) of state data
from typing import TypedDict

# ✅ Import LangGraph tools to build and manage the graph
from langgraph.graph import StateGraph, START, END

# 🧠 Step 1: Define the structure of the data that will flow through the graph
class AgentState(TypedDict):
    num1: int         # First number for the operation
    num2: int         # Second number
    operation: str    # Operation symbol: '+' or '-'
    result: int       # Final result (to be calculated)

# ➕ Step 2: Define a function to perform addition
def add(state: AgentState) -> AgentState:
    state["result"] = state["num1"] + state["num2"]
    return state

# ➖ Step 3: Define a function to perform subtraction
def sub(state: AgentState) -> AgentState:
    state["result"] = state["num1"] - state["num2"]
    return state

# 🔁 Step 4: This function decides which node to go to based on the operation
def decide_next_node(state: AgentState):
    if state["operation"] == "+":
        return "addition_operator"   # key to map to 'add' node
    elif state["operation"] == "-":
        return "subtraction_operator"  # key to map to 'sub' node

# 🧩 Step 5: Create the graph and tell it what state type to use
graph = StateGraph(AgentState)

# Add nodes (steps) to the graph
graph.add_node("add", add)
graph.add_node("sub", sub)

# Router node — doesn't change state, just routes it
graph.add_node("router", lambda state: state)

# 🔄 Define graph flow:

# Start from 'router'
graph.add_edge(START, "router")

# From 'router', decide next node using a condition
graph.add_conditional_edges(
    "router",               # From this node
    decide_next_node,       # Use this function to decide
    {
        "addition_operator": "add",    # if function returns this → go to 'add'
        "subtraction_operator": "sub"  # if function returns this → go to 'sub'
    }
)

# End the graph after add/sub step
graph.add_edge("add", END)
graph.add_edge("sub", END)

# 🔧 Step 6: Compile the graph to make it runnable
app = graph.compile()

# 🚀 Step 7: Provide input and invoke the graph
state = AgentState(num1=1, num2=2, operation='-')  # type: ignore to allow dict-style init
result = app.invoke(state)

# 🖨️ Step 8: Print the final state
print(result)
