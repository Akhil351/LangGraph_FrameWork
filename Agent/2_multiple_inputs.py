# Import TypedDict to define structured state, and List to handle list of numbers
from typing import TypedDict, List

# Import StateGraph from LangGraph
from langgraph.graph import StateGraph

# 🧠 Define the shape of the state that flows through the graph
class AgentState(TypedDict):
    values: List[int]  # A list of numbers to add
    name: str          # The user's name
    result: str        # The output message (to be generated)

# ⚙️ Define the node logic (function) that processes the state
def process_value(state: AgentState) -> AgentState:
    # This adds a friendly message with the sum of the values
    state["result"] = f"Hi there {state['name']}! your sum = {sum(state['values'])}"
    return state  # Return the updated state

# 🧩 Create the graph and tell it to use AgentState for its data
graph = StateGraph(AgentState)

# Add a node named "processor" that runs the function process_value
graph.add_node("processor", process_value)

# Set "processor" as both the entry (start) and finish (end) node
graph.set_entry_point("processor")
graph.set_finish_point("processor")

# 🛠️ Compile the graph to get a runnable app
app = graph.compile()

# 🚀 Run the graph by giving it input data
response = app.invoke({
    "values": [1, 2, 3, 4],  # Numbers to sum
    "name": "akhil",         # User name
    "result": ""             # Empty result to be filled in
})

# 🖨️ Print the full final state returned by the graph
print(response["result"])
