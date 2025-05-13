1. Page Layout and Functionality:
1.1 Layout
The application employs a layout with a sidebar on the left and a main content area on the right.
Sidebar: It serves as the input interface for journal data. It contains multiple input fields for data entry, such as department, developer, and various date - related fields. It also supports form validation, with mandatory fields marked (e.g., the "Разработчик" field).
Main Content Area: This area displays a table of added journal data. The table shows key information about the journals, including department, developer, and different dates. It also supports functions like data filtering and sorting.
1.2 Functionality
The sidebar is designed for users to input journal - related data. After successful submission, the data is presented in the table in the main content area.
2. Sidebar Journal Data Entry Fields:
2.1 Department (Подразделение)
Meaning: Indicates the department or section to which the journal belongs.
Input Method: Users are provided with a dropdown list that contains preset options. These options typically include names of various departments such as "АХО" (which could stand for a specific administrative or operational department) and "ИТ" (presumably the Information Technology department). The user simply selects the appropriate department from this list.
Example: АХО
2.2 Developer (Разработчик)
Meaning: Refers to the main person responsible for the journal content.
Input Method: It is a text - input field where users must manually type in the name. As a mandatory field, it is essential for accurately attributing the journal to its creator and for tracking purposes.
Example: Иванов И.И.
2.3 Receipt Date (ГУД)
Meaning: The date when the journal is first received by the system (general date).
Input Method: The application provides a date picker widget, which conforms to the YYYY-MM-DD format. This standard format ensures consistency and ease of comparison across different journal records. Users can click on the date picker to select the appropriate date from a calendar interface.
Example: 2025-05-13
2.4 Review Date (ГУД)
Meaning: The date when the journal content is first reviewed and approved (general date).
Input Method: Similar to the receipt date field, it uses a date picker with the YYYY-MM-DD format. Users can select the date from the calendar widget, which helps in maintaining a standardized record - keeping system.
Example: 2025-05-13
2.5 Receipt Date (ПППД)
Meaning: The date when the journal is received in a specific process (e.g., "ПППД").
Input Method: It also employs a date picker with the YYYY-MM-DD format. Users can easily select the relevant date from the provided calendar interface, ensuring accurate recording of this specific event.
Example: 2025-05-13
2.6 Review Date (ПППД)
Meaning: The date when the journal is reviewed in a specific process (e.g., "ПППД").
Input Method: Just like the other date fields, it uses a date picker with the YYYY-MM-DD format. Users can choose the appropriate date from the calendar, maintaining the integrity of the data records.
Example: 2025-05-13
2.7 Form Validation Rules
Mandatory Field: Разработчик (Developer) must be filled.
Date Format: Automatically verified to conform to the YYYY-MM-DD standard.
Department Selection: Only allow selection from the preset values in the dropdown list.
3. Prompt Information after Successful Data Submission:
When the user successfully submits the journal data, the system will:
Automatically add a new record to the table in the main content area.
Provide an implicit indication of successful submission (no pop - up, confirmed by table update).
Keep the form field values for continuous entry of multiple data entries.
4. Data Presentation in the Table:
The journal data is presented in a table in the main content area with the following columns:
Serial Number	Department (Подразделение)	Developer (Разработчик)	Receipt Date (ГУД)	Review Date (ГУД)	Receipt Date (ПППД)	Review Date (ПППД)
1	АХО	dsdsdsd	2024-03-07	2024-03-07	2024-03-07	2024-03-07
5. Screenshots of the Operation Process:
5.1 Journal Addition Page
5.2 Table Update after Successful Submission
6. Technical Implementation Details:
6.1 Development Framework
The application is developed using Streamlit.
6.2 Data Storage
Currently, data is stored in memory. It is recommended to connect to a database in the future.
6.3 Deployment
The application is run locally (localhost:8501).
6.4 Date Format
The date format used is YYYY-MM-DD, which conforms to the ISO 8601 standard.
Annotations
The code implementation is based on Streamlit v1.25.0.
The date fields use the st.date_input component.
The department field uses the st.selectbox component.
The table is displayed using the st.dataframe component.
All fields support keyboard shortcut input.
The system uses local time by default to generate date values.
It is recommended to add persistent data storage in a production environment.
