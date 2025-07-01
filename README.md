# 🚀 LangGraph Framework - Learning & Experimentation

A comprehensive learning project that demonstrates LangGraph patterns from basic concepts to advanced AI agent implementations.

## 📋 Table of Contents

- [Overview](#-overview)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Examples](#-examples)
- [Learning Path](#-learning-path)
- [Features](#-features)
- [Contributing](#-contributing)

## 🎯 Overview

This project serves as a **comprehensive tutorial** for learning LangGraph, starting from fundamental concepts and progressing to advanced AI agent patterns. It demonstrates:

- ✅ **Basic LangGraph concepts** (nodes, state, edges)
- ✅ **Control flow patterns** (sequential, conditional, looping)
- ✅ **AI integration** (OpenAI, conversation memory)
- ✅ **Advanced patterns** (ReAct, tool usage, function calling)

## 📁 Project Structure

```
LangGraph_FrameWork/
├── Agent/                     # Basic LangGraph concepts
│   ├── 1_hello_world_agent.py    # Single node example
│   ├── 2_multiple_inputs.py      # State management
│   ├── 3_sequential_agent.py     # Linear flow
│   ├── 4_conditional_agent.py    # Decision logic
│   └── 5_Looping.py             # Loop control
├── AI_Agent/                  # Advanced AI integration
│   ├── 1_agent_bot.py           # Chat agent with memory
│   └── 2_react_agent.py         # ReAct pattern with tools
├── .env                       # Environment variables
├── .gitignore                 # Git ignore rules
├── .python-version            # Python version (3.13)
├── pyproject.toml             # Project configuration
├── uv.lock                    # Dependency lock file
└── README.md                  # This file
```

## 🔧 Prerequisites

- **Python 3.13+**
- **OpenAI API Key** (for AI agent examples)
- **uv** package manager (recommended)

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd LangGraph_FrameWork
   ```

2. **Install dependencies using uv:**

   ```bash
   uv sync
   ```

   Or using pip:

   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

1. **Create a `.env` file** in the project root:

   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```

2. **Get your OpenAI API key:**
   - Visit [OpenAI Platform](https://platform.openai.com/api-keys)
   - Create a new API key
   - Add it to your `.env` file

## 🚀 Usage

### Running Basic Examples

Start with the fundamental LangGraph concepts:

```bash
# Hello World - Single node
python Agent/1_hello_world_agent.py

# Multiple inputs - State management
python Agent/2_multiple_inputs.py

# Sequential flow - Multiple nodes
python Agent/3_sequential_agent.py

# Conditional logic - Decision making
python Agent/4_conditional_agent.py

# Looping - Iterative processes
python Agent/5_Looping.py
```

### Running AI Agent Examples

```bash
# Chat agent with memory persistence
python AI_Agent/1_agent_bot.py

# ReAct agent with tool usage
python AI_Agent/2_react_agent.py
```

## 📚 Examples

### Agent/ Directory - Basic Concepts

#### 1. Hello World Agent

**File:** `Agent/1_hello_world_agent.py`

- **Concept:** Single node graph
- **Learning:** Basic StateGraph, TypedDict, state flow
- **Output:** Adds greeting to a message

#### 2. Multiple Inputs

**File:** `Agent/2_multiple_inputs.py`

- **Concept:** State management with multiple fields
- **Learning:** Handling lists, combining data
- **Output:** Processes numbers and generates personalized messages

#### 3. Sequential Agent

**File:** `Agent/3_sequential_agent.py`

- **Concept:** Linear flow with multiple nodes
- **Learning:** `add_edge()`, sequential execution
- **Output:** Builds messages step-by-step through different nodes

#### 4. Conditional Agent

**File:** `Agent/4_conditional_agent.py`

- **Concept:** Decision logic and routing
- **Learning:** `add_conditional_edges()`, router functions
- **Output:** Basic calculator (add/subtract based on operation)

#### 5. Looping

**File:** `Agent/5_Looping.py`

- **Concept:** Loop control with conditions
- **Learning:** Iterative processes, state persistence
- **Output:** Generates random numbers in a controlled loop

### AI_Agent/ Directory - Advanced Integration

#### 1. Agent Bot

**File:** `AI_Agent/1_agent_bot.py`

- **Concept:** Conversational AI with memory
- **Features:**
  - OpenAI GPT-4o integration
  - Conversation memory persistence
  - Message handling (HumanMessage/AIMessage)
  - Saves chat history to `logging.txt`
- **Usage:** Interactive chat interface

#### 2. ReAct Agent

**File:** `AI_Agent/2_react_agent.py`

- **Concept:** ReAct pattern (Reasoning + Acting)
- **Features:**
  - Function calling with custom tools
  - Mathematical operations (add, sub, mult, div)
  - Tool execution loop
  - Advanced state management
- **Usage:** AI can use tools to solve problems

## 🎓 Learning Path

This project follows a **progressive learning approach**:

1. **Fundamentals** → State, nodes, basic flows
2. **Control Flow** → Sequential, conditional, looping
3. **AI Integration** → Chat agents, memory management
4. **Advanced Patterns** → Tool usage, ReAct pattern

### Recommended Learning Order:

1. Start with `Agent/1_hello_world_agent.py`
2. Progress through `Agent/2_` to `Agent/5_`
3. Move to `AI_Agent/1_agent_bot.py`
4. Finally, explore `AI_Agent/2_react_agent.py`

## ✨ Features

### LangGraph Patterns Demonstrated

- ✅ **Single node graphs**
- ✅ **Sequential flows**
- ✅ **Conditional routing**
- ✅ **Looping mechanisms**
- ✅ **Message handling**
- ✅ **Tool integration**
- ✅ **State persistence**

### Technical Features

- **Modern Python 3.13** with type hints
- **Structured state management** with TypedDict
- **Environment variable handling**
- **Error handling and logging**
- **Memory persistence** for conversations
- **Function calling** capabilities

### AI Integration

- **OpenAI GPT-4o** integration
- **Conversation memory** with file persistence
- **System prompts** and message handling
- **Tool execution** with custom functions
- **ReAct pattern** implementation

## 🔒 Security Notes

- **API keys** are stored in `.env` file (not committed to git)
- **Never commit** API keys to version control
- **Rotate keys** if accidentally exposed
- **Use environment variables** for sensitive data

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your examples or improvements
4. Follow the existing code style
5. Submit a pull request

## 📝 License

This project is for educational purposes. Feel free to use and modify for learning LangGraph.

## 🆘 Troubleshooting

### Common Issues

1. **Import errors:**

   ```bash
   uv sync  # Ensure all dependencies are installed
   ```

2. **OpenAI API errors:**

   - Check your API key in `.env`
   - Ensure you have sufficient credits
   - Verify the API key is valid

3. **Python version issues:**
   - Ensure Python 3.13+ is installed
   - Use `uv` for dependency management

### Getting Help

- Check the [LangGraph documentation](https://langchain-ai.github.io/langgraph/)
- Review the [LangChain documentation](https://python.langchain.com/)
- Open an issue for project-specific problems

---

**Happy Learning! 🎉**

This project demonstrates the power and flexibility of LangGraph for building AI applications, from simple workflows to complex agent systems.
