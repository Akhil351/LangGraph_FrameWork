# ✅ Import necessary tools
from typing import Dict, List, TypedDict  # For typed state definition
from langgraph.graph import START, END, StateGraph  # LangGraph core
import random  # For generating random numbers

# 🧠 Define the structure of the state that flows through the graph
class AgentState(TypedDict):
    name: str            # User's name (will be personalized)
    number: List[int]    # List of random numbers generated
    counter: int         # How many times the loop has run

# 👋 Node 1: Greet the user and reset the counter
def greeting_node(state: AgentState) -> AgentState:
    state["name"] = f"Hi there, {state['name']}!"  # Add greeting to name
    state["counter"] = 0                           # Reset counter at the start
    return state

# 🎲 Node 2: Generate a random number and increment the counter
def random_node(state: AgentState) -> AgentState:
    new_num = random.randint(1, 100)         # Generate random number
    state["number"].append(new_num)          # Add to number list
    state["counter"] += 1                    # Increase loop counter
    print(f"Generated: {new_num}, Counter: {state['counter']}")  # Debug log
    return state

# 🔁 Node Router: Decide whether to loop or exit
def should_continue(state: AgentState):
    if state["counter"] < 5:
        print("🔁 Looping again...", state["counter"])
        return "loop"  # Go back to random_node
    else:
        print("✅ Exiting loop.")
        return "exit"  # Finish the graph

# 🛠️ Build the graph using LangGraph
graph = StateGraph(AgentState)

# Add nodes to the graph
graph.add_node("greeting", greeting_node)
graph.add_node("random", random_node)

# 📌 Flow: Start → greeting → random
graph.add_edge(START, "greeting")
graph.add_edge("greeting", "random")

# 🚦 Decision logic: from "random", decide where to go
graph.add_conditional_edges(
    "random",               # from this node
    should_continue,        # use this function to decide
    {
        "loop": "random",   # if "loop" → go back to random
        "exit": END         # if "exit" → stop the graph
    }
)

# 🏁 Compile the graph to make it runnable
app = graph.compile()

# 🚀 Invoke the graph with initial input
result = app.invoke({
    "name": "Akhil",         # Initial name
    "number": [],            # Start with empty number list
    "counter": 0             # Start with 0 loops
})

# 🖨️ Print the final result after loop ends
print("\nFinal State:")
print(result)
