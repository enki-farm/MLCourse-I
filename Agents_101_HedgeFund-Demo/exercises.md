
# 🤖 AI Agent Workshop: Crypto Investment Debate

Welcome to this hands-on workshop exploring **multi-agent systems** for crypto investment analysis. You'll work with a set of AI agents in a structured debate format to generate investment recommendations.

Each exercise builds upon a base project that uses the `autogen-agentchat` framework and includes agents with specialized roles.

> ⏱️ **Total Time**: ~2 hours  
> 🛠️ **Prerequisites**: Python, async basics, LLM API usage

---

## 🧠 Exercise 1: Customize the Agents' Personalities

**Goal:** Understand role-specific behavior and prompt engineering.

### ✅ Task
- Modify `BullishAnalyst` to behave like a **hype-driven influencer**.
- Modify `BearishAnalyst` to act like a **conservative institutional advisor**.
- Run the debate and observe how tone and argumentation affect the final result.

### 💬 Discussion
- How does tone affect the investment decision and perceived credibility?

---

## 🔌 Exercise 2: Add a New Analyst Role

**Goal:** Learn how to extend the agent team.

### ✅ Task
- Create a new agent: `TechnicalAnalyst`, who evaluates tokens using technical indicators like RSI or MACD.
- Add this agent to the `RoundRobinGroupChat`.

### 💡 Bonus
- Provide mock data (e.g., `"RSI": 72`, `"MACD": "positive"`) to simulate indicator input.

### 💬 Discussion
- How does this additional perspective shift the judge’s final decision?

---

## 🔧 Exercise 3: Build and Integrate a Simple Tool

**Goal:** Explore agent tooling and external data usage.

### ✅ Task
- Create or extend a tool within `CoinMarketCapAgent` that returns:
  ```json
  {
    "symbol": "BTC",
    "market_cap": "...",
    "volume_24h": "...",
    "circulating_supply": "..."
  }
  ```
- Allow other agents to call this tool during their analysis.

### 💡 Bonus
- Make the analysts cite this data when arguing for or against the token.

### 💬 Discussion
- What are the trade-offs of giving agents access to external tools?

---

## 🤖 Exercise 4: Change the Coordination Logic

**Goal:** Understand group chat structure and its effect.

### ✅ Task
- Replace `RoundRobinGroupChat` with `HierarchicalGroupChat`.
- Set `MetaDataProvider` as the **leader agent** who assigns speaking turns.
- Re-run the analysis and compare dynamics.

### 💡 Bonus
- Try other coordination strategies or define your own.
- Experiment with different `termination_condition` values.

### 💬 Discussion
- How does order and hierarchy affect the final investment recommendation?

---

## 🎯 Exercise 5: Run an Evaluation Loop Over Multiple Tokens

**Goal:** Scale the system to multiple inputs and gather results.

### ✅ Task
- Define a list of tokens: `["BTC", "ETH", "DOGE"]`
- Run the entire group chat process for each token.
- Capture and display the final decision (`BUY`, `HOLD`, `AVOID`) in a table:

```
Token   | Decision
--------|----------
BTC     | BUY
ETH     | HOLD
DOGE    | AVOID
```

### 💬 Discussion
- How do decisions differ per token?
- Are the analysts consistent in their reasoning?

---

## 🎯 Exercise 6: Use a Local or Otherwise Hosted LLM

**Goal:** Explore alternatives to the default OpenAI models by integrating a local or hosted LLM.

### ✅ Task
- Set up a local LLM (e.g., `Llama`, `GPT4All`) or use a hosted model on Azure.
- Modify the agent framework to interact with this alternative LLM instead of the default OpenAI API.
- Run the group chat process and compare the results.

### 💡 Bonus
- Evaluate the performance, latency, and cost differences between the models.
- Experiment with fine-tuning or prompt optimization for the local/hosted model.

### 💬 Discussion
- How does the choice of LLM affect the quality of decisions?
- What are the trade-offs between local and hosted solutions?

---

## ✅ Optional Wrap-Up

- 💭 **Feedback**: What worked? What was confusing?
- 🧠 **Brainstorm**: Where else could this agent pattern be used?
- 🚀 **Next Steps**: How might we add real-time data, charts, or user feedback loops?

---

Happy hacking! 🧠💰🤖
