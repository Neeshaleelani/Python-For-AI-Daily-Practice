from modules.ai_agent.tools import TOOLS
from core.services.llms import LLMS
from langchain_openai import ChatOpenAI
from langchain_core.messages import START, Message
def build_graph(model=None, tools=None):
    tools= TOOLS if tools is None else tools
    pass


SYSTEM_PROMPT ="""You are the friendly customer support assistant for Xander Restaurant.
Keep replies short. Prices are in Pakistani rupees. Use fetch_menu for menu/prices.
For complaints, collect customer name, phone, complaint and order ID. Validate the
order ID with validate_order_id, then call log_complaint only for a valid order.
Never invent facts. Ask for missing details."""

def create_chat_model(llms="grok"):
    return ChatOpenAI(**LLMS[llms], temprature=0)

def assistant(state:MessagesState, model_with_tools)



