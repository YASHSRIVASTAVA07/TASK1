import autogen
from stock_tool import fetch_stock_data, visualize_stock_data

# Load API Configuration (Update this if needed)
config_list = autogen.config_list_from_json("OAI_CONFIG_LIST")

# ✅ Create the Data Fetching Agent
data_agent = autogen.AssistantAgent(
    name="DataAgent",
    llm_config={"config_list": config_list, "temperature": 0},
    system_message="You fetch financial stock data and generate visualizations."
)

# ✅ Create the Report Generating Agent
report_agent = autogen.AssistantAgent(
    name="ReportAgent",
    llm_config={"config_list": config_list, "temperature": 0},
    system_message="You analyze financial trends and generate summaries."
)

# ✅ Create the User Agent (This acts as the user)
user_agent = autogen.UserProxyAgent(
    name="UserAgent",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=3,
    is_termination_msg=lambda x: "exit" in x["content"].lower(),
    system_message="You request stock market analysis.",
)

# Function to run the agent system
def agent_workflow(ticker):
    # Step 1: Fetch Stock Data
    print(f"📊 Fetching stock data for {ticker}...")
    stock_data = fetch_stock_data(ticker)
    
    # Step 2: Visualize Stock Data
    visualize_stock_data(stock_data, ticker)

    # Step 3: Generate Report
    print(f"📈 Generating analysis report for {ticker}...")
    user_agent.initiate_chat(
        report_agent,
        message=f"Analyze the stock trends for {ticker} and provide insights.",
    )

# Example: Run for Apple Stock (AAPL)
if __name__ == "__main__":
    agent_workflow("AAPL")
