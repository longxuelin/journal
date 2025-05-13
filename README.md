Methods to Obtain SUPABASE_URL and SUPABASE_KEY

1.Create a Supabase Project
First, you need to register an account on the Supabase official website. After logging in, click "New Project" in the upper right corner to create a new project. After filling in the project name and region, wait for a few seconds and you will enter the project console.
Find SUPABASE_URL and SUPABASE_KEY
After entering the console, click "Settings" → "API" in the left menu bar.

2.SUPABASE_URL: It is below "Project URL" and looks like https://xxx.supabase.co. This is the "house number" of the project, which is used in the code to locate the database.
SUPABASE_KEY: In the "API Keys" area, there are many types of keys (public key, private key, service key, etc.). Click "View Key" and you will see a long string.

Steps to Configure Parameters in the Code (Taking Python as an Example)

1.Install the Library
Open the terminal and enter "pip install supabase" to install the official library.

2.Import the Module and Define the Parameters
Create a new Python file (for example, named supabase_demo.py). First, import the client creation function:

from supabase import create_client

Then define two variables to store the keys and the address obtained just now.

# Real values obtained from the Supabase console
SUPABASE_URL = "https://your_project_ID.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxxxxxxxxxxxxx"  # Service key


3.Create the Client and Operate the Database
Use these two parameters to create the client:

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


Next,you can operate the database! For example, operations like supabase.table("set").insert(data).execute() and querying data (such as supabase.table("set").select("*").execute()).




CSV File Format Requirements

1.File Encoding: Use UTF-8 encoding to avoid garbled Chinese characters.
2.Field Separator: Use an English comma (,) to separate column data.
3.Line Terminator: Use a newline character (\n). In the Windows system, it is commonly CRLF (\r\n).
4.Header: The first row should contain column names, and the field names should be consistent with the program logic.
5.Data Format:
1.Numeric fields (such as dates and numbers) should conform to the format required by the program (for example, the date format is YYYY-MM-DD).
2.If text fields contain special characters (such as commas and quotation marks), they should be enclosed in English double quotation marks (").

File Placement

1.Default Path:
If there is no special specification in the program, it is recommended to place the file in the same directory as the program (that is, in the same folder as the execution file/script).
Example path: C:\Users\YourName\Program\test.csv.
2.Custom Path:
If you need to specify another location, you need to clearly state the file path in the program configuration or code (such as D:\Data\PTO.csv), and ensure that the program has the read permission.

