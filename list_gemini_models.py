import google.generativeai as genai

genai.configure(api_key="AIzaSyBlJ1QBYb1I5qKrVpGVEPaSKPwQKJfzQD4")  # Replace with your actual key

models = genai.list_models()

print("\n✅ Available Gemini Models:")
for model in models:
    print(f"- {model.name}")
