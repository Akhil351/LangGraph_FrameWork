# Import TypedDict to define structured state (data format)
from typing import TypedDict

# Import StateGraph from LangGraph to build the flow
from langgraph.graph import StateGraph

# 🧠 Step 1: Define the structure of the agent's state (data that flows between nodes)
class AgentState(TypedDict):
    name: str       # User's name
    age: int        # User's age
    final: str      # Final message (we will build this step-by-step)

# ⚙️ Step 2: First node — adds a greeting to the final message
def first_node(state: AgentState) -> AgentState:
    state["final"] = f"Hi {state['name']}! "
    return state  # Returns the updated state

# ⚙️ Step 3: Second node — adds age info to the final message
def second_node(state: AgentState) -> AgentState:
    state["final"] = state["final"] + f"You are {state['age']} years old!"
    return state  # Returns the updated state

# 🔧 Step 4: Build the LangGraph
graph = StateGraph(AgentState)

# Add both nodes to the graph
graph.add_node("first_node", first_node)
graph.add_node("second_node", second_node)

# Set the entry point (start node)
graph.set_entry_point("first_node")

# Connect first_node → second_node (sequential flow)
graph.add_edge("first_node", "second_node")

# Set the finish point (end node)
graph.set_finish_point("second_node")

# 🛠️ Step 5: Compile the graph into a runnable app
app = graph.compile()

# 🚀 Step 6: Run the graph with input data
result = app.invoke({
    "name": "akhil",     # User name
    "age": 21,           # User age
    "final": ""          # Start with an empty message
})

# 🖨️ Step 7: Print the final message
print(result["final"])
