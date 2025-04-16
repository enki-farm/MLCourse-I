import os

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.tools.http import HttpTool

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("COINMARKETCAP_API_KEY")
BASE_URL = "pro-api.coinmarketcap.com"

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": API_KEY,
}

cmc_meta_schema = {
    "type": "object",
    "properties": {
        "symbol": {"type": "string", "description": "The symbol of the cryptocurrency. Example: BTC, ETH."},
    },
}

cnc_meta_tool = HttpTool(
    name="coinmarketcap",
    description="Get metadata about a cryptocurrency.",
    scheme="https",
    host=BASE_URL,
    port=443,
    path="/v2/cryptocurrency/info",
    method="GET",
    headers=headers,
    json_schema=cmc_meta_schema
)

class CoinMarketCapAgent:
    def __init__(self, name: str, model_client):
        self.agent = AssistantAgent(
            name=name,
            model_client=model_client,
            tools=[cnc_meta_tool],
            system_message="You are a helpful assistant. You can use the coinmarketcap tool to get metadata about a cryptocurrency.",
            reflect_on_tool_use=True,
            model_client_stream=model_client,
        )

    def get_agent(self):
        return self.agent