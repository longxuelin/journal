I. Preparations
1.1 Environment Setup and Dependency Installation
Follow the repository's deployment instructions to set up the development environment correctly:

bash
# Clone the project repository  
git clone https://github.com/lihuaju-dev/journal.git  

# Create and activate a virtual environment (Windows)  
python -m venv venv  
venv\Scripts\activate  

# Install Streamlit and project dependencies  
pip install streamlit  

# Start the application  
streamlit run main.py  

![fad9a8e343690e3e9eea0d778fcb8bac](https://github.com/user-attachments/assets/debb01b1-10e6-49aa-b3bc-069c9fcf838d)
![ab644bc23fa716e95fd5539956991619](https://github.com/user-attachments/assets/9cf7e9ca-ca89-46be-aec9-9f6e3e9cdafa)

1.2 Access the Application Interface
After starting the application, access it via:

Local Environment: Enter http://localhost:8501 in your browser.
Remote Server: Use the public IP (e.g., http://<ServerIP>:8501).
![ccfa3efa31a33056c597f1d0a01f9662](https://github.com/user-attachments/assets/b8bd3bf1-83db-4d51-9839-41681ecce2b3)
![Uploading 63bdcaf892dc8fc188be2cb221b8b491.png…]()

II. Procedure for Inputting Configuration Information
1. Navigate to the Creation Page
On the Streamlit application homepage, locate the "Create RAG Chatbot" option in the left sidebar menu and click to enter the configuration interface:


Note 1: The sidebar navigation is implemented using st.sidebar in main.py, ensuring users can quickly locate the feature entry.
2. Fill in Core Configuration Parameters
① Telegram Bot Token Input
Location: The Telegram Bot Token input field in the middle of the page (marked with a red asterisk as a required field).
Format: Paste the standard token obtained from BotFather (e.g., 123456:ABCDEFGHIJKLMNOPQRSTUVWXYZ123456).
UX Design: The input field supports password mode to hide the token, protecting sensitive information.
② API Model Configuration
Preset Models: Select from the dropdown menu (e.g., gpt-3.5-turbo, local-llama2), with default parameters auto-filled.
Custom Models: Check "Custom API" and enter an interface address compliant with the OpenAI API specification (e.g., https://your-model-api.com/v1/chat/completions).
3. Submit Configuration
After verifying the information, click the "Create Now" button at the bottom of the page (highlighted green button with a loading animation on hover) to trigger the backend validation and creation process.
III. Full-Process Handling Logic After Submission
1. Frontend Real-Time Validation (Core Function of form.py)
Non-Empty Check:
If the Telegram Bot Token or API Model fields are empty, a red warning immediately appears:
plaintext
❗ Please fill in the Telegram Bot Token and API Model information  

Format Pre-Check:
Telegram Token: Verify the presence of the : delimiter and length compliance with Telegram API specifications (non-strict check, with deep validation in the backend).
API Model: Check if it is a preset value or a valid URL format (with http:// or https:// prefix).
2. Backend Core Processing (Technical Implementation in set.py)
① Telegram Token Legitimacy Validation
Deep validation by calling the Telegram Bot API to ensure the token is valid:

python
运行
# Token validation logic in set.py  
import requests  
from requests.exceptions import RequestException  

def validate_telegram_token(token: str) -> bool:  
    api_url = f"https://api.telegram.org/bot{token}/getMe"  
    try:  
        response = requests.get(api_url, timeout=10)  
        if response.status_code == 200 and response.json().get("ok"):  
            return True  
        raise ValueError("Token validation failed: invalid token or network issue")  
    except RequestException as e:  
        raise ValueError(f"Network request error: {str(e)}")  
② Model Initialization and RAG Component Assembly
Dynamically load the model based on user input and associate the knowledge base to build the RAG question-answering chain:

python
运行
# Model loading logic  
from langchain.llms import OpenAI  
from langchain.retrievers import ChromaRetriever  
from langchain.chains import RetrievalQA  

def initialize_llm(model_name: str, api_key: str):  
    if model_name.startswith("gpt-"):  
        return OpenAI(model_name=model_name, openai_api_key=api_key)  
    elif model_name.startswith("http"):  
        # Custom API model initialization (requires LangChain-compatible interface)  
        return CustomLLM(api_url=model_name)  
    else:  
        raise ValueError("Unsupported model type")  

# Knowledge base association and RAG chain building  
def build_rag_chain(llm, knowledge_file: str):  
    # Load CSV knowledge base (requires "question" and "answer" columns)  
    df = pd.read_csv(knowledge_file)  
    # Create vector index (using Chroma database as an example)  
    embeddings = OpenAIEmbeddings()  
    vectorstore = Chroma.from_texts(  
        df["answer"].tolist(),  
        embeddings,  
        metadatas=[{"source": q} for q in df["question"].tolist()]  
    )  
    return RetrievalQA.from_chain_type(  
        llm=llm,  
        chain_type="stuff",  
        retriever=vectorstore.as_retriever()  
    )  
③ Configuration Persistence
Write user configurations to config.ini or a database for subsequent management and reuse:

ini
; Example configuration in app/settings/config.ini  
[telegram]  
token = 123456:ABCDEFGHIJKLMNOPQRSTUVWXYZ123456  ; Masked as 123456:*******123456 in storage  
[model]  
name = gpt-3.5-turbo  
api_key = sk-*********  ; OpenAI API key (requires additional secure storage)  
[knowledge_base]  
file = PTO.csv  
3. Multi-Scenario Feedback Mechanism
Feedback Type	Interface Display	Technical Implementation	Function Verification
Creation Success	Top green banner:
✔️ RAG Chatbot created successfully! Telegram Bot activated: @YourBotName
Auto-navigate to the management page, showing the last four digits of the token (e.g., ****56) and model name	st.success() component + st.experimental_set_query_params() route navigation	Send /start on Telegram; the bot should reply with the welcome message from PTO.csv (e.g., "Hello! Ask questions about the company's leave policy.")
IV. Precautions
Sensitive Information Protection:
Mask Telegram tokens in screenshots (e.g., show the first 6 and last 4 digits, with **** in between).
Model Compatibility:
For custom API models, predefine interface specifications in set.py (e.g., request headers, parameter formats).
Logging for Debugging:
Add log outputs in set.py to assist with issue tracking:
python
运行
import logging  
logging.info("Model initialization successful")  



This translation maintains technical accuracy and follows best practices for English technical documentation, ensuring clarity for developers and users.

