6. Configuration Page Layout Description
bash
LLM Configuration Area:
        1. API Key: Enter the API key of the LLM service provider.
        2. Model Name: Select the LLM model to be used.
Telegram Bot Configuration Area:
        1. Bot Token: Enter the Telegram Bot token obtained from BotFather.
        2. Chat ID: Enter the chat ID for receiving notifications.
Verification Options:
        You can choose to verify the validity of the LLM and Telegram configurations.
Submission Operation Feedback
Successful Saving:
        Display a green success message: "Configuration has been successfully saved!"
        If the verification option is checked, the configuration validity will be verified first.
        After successful verification, the corresponding success prompt will be displayed.
Possible Error Messages:
        Display a red error message when an input field is empty.
        Display the specific error reason when verification fails (such as API connection failure, invalid Bot token, etc.).