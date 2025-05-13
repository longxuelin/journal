I. Preparations
1. Environment Setup
1.1 Ensure environment setup is completed as per the repository's Deployment Instructions:
bash
git clone https://github.com/lihuaju-dev/journal.git  
python -m venv venv  
venv\Scripts\activate  
pip install streamlit  
streamlit run main.py  
![fad9a8e343690e3e9eea0d778fcb8bac](https://github.com/user-attachments/assets/d3cec3db-172f-4659-8d40-d82e9f92364e)


1.2 Access the application via http://localhost:8501 (local) or the server's public IP after startup.

![63bdcaf892dc8fc188be2cb221b8b491](https://github.com/user-attachments/assets/dba3f1e8-56fc-46b9-9824-32ca4e47d069)

![ab644bc23fa716e95fd5539956991619](https://github.com/user-attachments/assets/95adb57c-a925-4f7b-a28c-e7304043ad4e)

II. Operation Flow for Inputting Telegram Bot Token and API Model Information
1. Enter the Creation Page
On the Streamlit app's home page, locate the "Create RAG Chatbot" entry via the sidebar or top navigation bar and click to enter the configuration page.

image
2. Fill in Key Information
① Telegram Bot Token Input:

Location: The "Telegram Bot Token" input field in the middle of the page (marked with a red asterisk as a required field).
Format: Paste the token obtained from Telegram BotFather (e.g., 123456:ABCDEFGHIJKLMNOPQRSTUVWXYZ123456) directly into the input field.

② API Model Information Input:

Model Selection: Choose a preset model from the dropdown menu (e.g., gpt-3.5-turbo, local-llama2), or manually enter a custom API address (e.g., https://your-model-api.com/v1/chat) in the input field.
3. Submit Configuration
After verifying the information, click the "Create Now" button at the bottom of the page (typically blue or green, with a loading state when hovering).
III. Post-Submission Processing Logic (Core: set.py Function Analysis)
1. Frontend Data Validation (Assisted by form.py)
Non-empty Validation: If the Telegram token or model field is empty, a red warning immediately appears:
plaintext
❗ Please fill in the Telegram Bot token and API model information  

Format Pre-Validation:
Telegram Token: Check for the presence of : and valid length (non-strict validation, further verified in the backend).
API Model: Validate as a preset value or a valid URL format (e.g., contains http:// or https://).
2. Backend Core Processing (Core Functions in set.py)
① Token Legitimacy Validation:

python
运行
# Telegram token validation logic in set.py  
import requests  

def validate_telegram_token(token: str) -> bool:  
    url = f"https://api.telegram.org/bot{token}/getMe"  
    response = requests.get(url)  
    if response.status_code == 200 and response.json().get("ok"):  
        return True  
    raise ValueError("Telegram token is invalid or network connection failed")  

② Model Initialization and Configuration:

Model Loading: Load the corresponding LLM (Large Language Model) interface based on the input model name or API address. For example:
python
运行
if model == "gpt-3.5-turbo":  
    from langchain.llms import OpenAI  
    llm = OpenAI(model_name=model)  
elif model.startswith("http"):  
    # Custom API model calling logic  
    llm = CustomAPIModel(api_url=model)  

Knowledge Base Association: Automatically associate files like PTO.csv and test.csv in the repository as RAG knowledge base data sources.

③ Configuration Persistence:
Write the token and model information to config.ini or a database (example path: app/settings/config.ini):

ini
[telegram]  
token = 123456:ABCDEFGHIJKLMNOPQRSTUVWXYZ123456  
[model]  
name = gpt-3.5-turbo  
3. Result Feedback Mechanism
✅ Successful Creation:

Interface Feedback:
A green success banner pops up at the top of the page, displaying:
plaintext
✔️ RAG chatbot created successfully! Telegram Bot activated: @YourBotName  

Automatically redirects to the "Bot Management" page, showing the last four digits of the configured token (e.g., ****56) and the model name.
Function Validation:
Search for the Bot name in Telegram, send /start, and the bot should reply with a welcome message from the knowledge base (e.g., PTO policy in PTO.csv).

❌ Creation Failure:

Error Type	Typical Feedback	Snapshot Example
Invalid Token	❌ Telegram token validation failed. Please check if the token is valid from BotFather.	Snapshot 7
Model Unavailable	❌ API model connection failed: 404 Not Found (check model name or URL).	-
Network Timeout	❌ Connection timed out. Check server network or retry submission.	-
IV. Snapshot Instructions and Annotations
Required Snapshot List
Snapshot 1: App Home Page and Creation Entry
Show the Streamlit app's home page, marking the location of the "Create RAG Chatbot" button (e.g., in the sidebar menu).
Annotation 1: Navigate to the creation page via the Streamlit sidebar.
Snapshot 2: Form Input Details
Clearly display the Telegram Bot Token input field (with a star for required fields) and the API model selection/input area.
Annotation 2: Ensure input field labels match the parameter names in set.py (e.g., telegram_token, model_name).
Snapshot 3: Non-Empty Validation Failure Prompt
Intentionally leave a field empty, capture the red error prompt after submission (e.g., "Please fill in the Telegram Bot token").
Annotation 3: Frontend validation is implemented by form.py to block empty data from reaching the backend.
Snapshot 4: Successful Creation Feedback
Show the green banner + Bot name display, possibly with a "Start Chat" button at the bottom.
Annotation 4: Feedback includes the Telegram Bot's @username for quick user 定位 (location).
Snapshot 5: Invalid Token Error
Intentionally enter an incorrect token (e.g., missing :), capture the red warning "Telegram token validation failed".
Annotation 5: This error is thrown by the validate_telegram_token function in set.py.
V. Notes
1. Sensitive Information Protection
Redact Telegram tokens in snapshots (e.g., show first 6 and last 4 digits, with **** in between).
2. Model Compatibility
If using a custom API model, define the interface specification (e.g., request headers, parameter format) in set.py in advance.
3. Logging for Debugging
Add log outputs in set.py (e.g., logging.info("Model initialized successfully")) to help troubleshoot failures.
