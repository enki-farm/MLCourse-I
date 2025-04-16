import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

from agents.coinmarketcap_agent import CoinMarketCapAgent


# === Model Client Setup ===

API_KEY = os.getenv("OPENAI_API_KEY")

# Define a model client. You can use other model client that implements the `ChatCompletionClient` interface.
model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini",
    api_key=API_KEY,
)

# === Agent Setup ===

# 1. CoinMarketCap Agent
cmc_agent = CoinMarketCapAgent(name="MetaDataProvider", model_client=model_client).get_agent()

# 2. Bullish Analyst
bullish_agent = AssistantAgent(
    name="BullishAnalyst",
    model_client=model_client,
    model_client_stream=True,
    system_message="You are a bullish crypto analyst. Your goal is to make a compelling argument to buy the given token, using available data. Focus on strengths, growth potential, and momentum.",
)

# 3. Bearish Analyst
bearish_agent = AssistantAgent(
    name="BearishAnalyst",
    model_client=model_client,
    model_client_stream=True,
    system_message="You are a skeptical crypto analyst. Your role is to argue against buying the given token. Consider risks, volatility, weak fundamentals, or market conditions that may harm its future.",
)

# 4. Investment Judge
judge_agent = AssistantAgent(
    name="InvestmentJudge",
    model_client=model_client,
    model_client_stream=True,
    system_message=(
        "You are an impartial crypto investment advisor. Listen to both analysts, "
        "evaluate their arguments critically, and provide a final recommendation: BUY, HOLD, or AVOID. "
        "Justify your decision with reasoning and summarize key points."
        "Conclude with DECISION: <your decision>."
    ),
)


# === Group Chat Setup ===

text_termination = TextMentionTermination("DECISION")
team = RoundRobinGroupChat([cmc_agent, bullish_agent, bearish_agent, judge_agent], termination_condition=text_termination)

# === Trigger the discussion ===

async def main() -> None:
    await Console(team.run_stream(task="Get a investment recommendation for bitcoin (BTC)"))  # Stream the messages to the console.

asyncio.run(main())