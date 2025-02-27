import google.generativeai as genai
from stock_tool import fetch_stock_data, visualize_stock_data

# ✅ Set up Gemini API
genai.configure(api_key="AIzaSyBlJ1QBYb1I5qKrVpGVEPaSKPwQKJfzQD4")

# ✅ Function to generate stock trend analysis using Gemini
def generate_stock_analysis(ticker):
    """
    Uses Google's Gemini AI to analyze stock trends and generate insights.
    """
    stock_data = fetch_stock_data(ticker)

    # Prepare the prompt
    prompt = f"""
    Analyze the following stock data for {ticker} and provide insights:
    {stock_data.tail(10).to_string()}
    """

    # Send request to Gemini AI
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)

    return response.text

# ✅ Main workflow
def agent_workflow(ticker):
    print(f"📊 Fetching stock data for {ticker}...")
    stock_data = fetch_stock_data(ticker)
    
    # Step 1: Visualize stock trends
    visualize_stock_data(stock_data, ticker)

    # Step 2: Get AI-generated analysis
    print(f"📈 Generating AI analysis report for {ticker}...")
    report = generate_stock_analysis(ticker)

    # Step 3: Display report
    print("\n📋 **Stock Analysis Report:**")
    print(report)

# ✅ Run the AI stock analysis for Apple (AAPL)
if __name__ == "__main__":
    agent_workflow("AAPL")
