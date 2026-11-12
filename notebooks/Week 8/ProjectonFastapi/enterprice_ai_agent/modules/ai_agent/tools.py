from langchain_core.tools import tool
from core.database.sqlite import save_complaint

order_list = [
    "OR-1045",
    "OR-1046",
    "OR-1047"
]

@tool
def validate_order_id(order_id):
    if order_id in order_list:
        return True
    return False

@tool
def log_complaint(customer_name, order_id, phone, complaint):
    # temp_dict = {
    #     "customer_name": customer_name,
    #     "order_id": order_id,
    #     "phone": phone,
    #     "complaint": complaint,
    #     "status": "Pending"
    # }
    # complaint_list.append(temp_dict)
    return save_complaint(customer_name, order_id, phone,complaint)
     

@tool
def fetch_menu():
    return menu

@tool
def retrieve_knowledgebase():
    return None

TOOLS=[
    validate_order_id,
    fetch_menu,
    log_complaint
]