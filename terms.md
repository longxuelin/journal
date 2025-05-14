
Usage Tutorial	使用教程
Technical Document	技术文档
Registration Log	登记日志
interface	界面
developer	开发者
approver	批准者
storage location	存储位置
registration date	注册日期
approval date	批准日期
application	申请
record	记录
table	表格
=======

英文术语-中文

Comma - Separated Values（CSV）     逗号分隔值

Character Encoding                  字符编码   

Garbled Characters                  乱码

Record                            记录

Data Field                         数据字段

Project Root Directory               项目根目录

Relative Path                      相对路径

Authentication                    身份验证，确认用户或程序的身份以授予相应权限

access control                     访问控制，管理对资源（如数据库）的访问权限

service key                        服务密钥，一种具有特定权限的密钥   
                  
client instance                    客户端实例，在代码中创建的用于与Supabase 数据库进行数据操作（如插入、查询）的对象



database operation                数据库操作，包括插入数据、查询数据等对数据库的操作行为

Insert                           插入，在数据库中添加新的数据记录

Select                           查询，从数据库中获取符合条件的数据


=======

Terms Glossary for Journal Project
1. General Project - related Terms
Journal Project
Definition: A collection of Streamlit - based applications. These applications are designed for multiple purposes, including registering technical documentation, setting up LLM and Telegram bots, and managing data associated with different workflows.
Relevance: It represents the overall scope of the software project.
Streamlit Application
Definition: Web applications created using the Streamlit Python library. Streamlit simplifies the process of building interactive web interfaces with Python code, eliminating the need for extensive front - end development knowledge.
Relevance: All the applications in the Journal Project are built using Streamlit.
Python Script
Definition: A text file containing Python code. In this project, multiple Python scripts (e.g., main.py, form.py, etc.) are used to implement different functionalities.
Relevance: The core components of the project are written as Python scripts.
CSV File
Definition: Comma - Separated Values file, a simple file format used to store tabular data. In the project, CSV files like test.csv and PTO.csv are used to store data related to different workflows.
Relevance: They serve as local data storage for the project's data - recording functions.
Supabase Database
Definition: An open - source Firebase alternative that provides a backend as a service. It includes features like a PostgreSQL database, authentication, and real - time subscriptions. In the project, it is used to store configuration data for LLM, Telegram bots, and RAG chat - bots.
Relevance: Enables centralized and secure storage of important configuration data.
2. main.py - specific Terms
Entry - point
Definition: In a software project, the entry - point is the first part of the program that is executed. In the Journal Project, main.py acts as an entry - point or a simple navigation tool.
Relevance: It provides users with an initial access point to the project and can guide them to other parts of the code or functionality.
st.markdown
Definition: A function provided by the Streamlit library. It is used to display Markdown - formatted text in a Streamlit application. Markdown is a lightweight markup language that allows for easy text formatting, such as creating headings, lists, and links.
Relevance: In main.py, it is used to display a clickable link.
3. Deployment - related Terms
Server Configuration
Definition: The process of setting up a server to meet the requirements of running an application. For the Journal Project, the recommended server configuration includes a Windows Server 2019 or later operating system, at least 2 CPU cores, 4GB of RAM, and 50GB of free disk space.
Relevance: Ensures that the server has sufficient resources to run the Streamlit applications.
Windows Firewall
Definition: A built - in security feature in Windows operating systems that controls incoming and outgoing network traffic. For the Streamlit application, port 8501 needs to be opened to allow external access.
Relevance: Allows the application to be accessed from external networks.
DNS Records
Definition: Domain Name System records that map domain names to IP addresses. If the project needs to be accessed via a domain name, correct DNS records must be set up.
Relevance: Enables users to access the application using a domain name instead of an IP address.
Virtual Environment
Definition: An isolated Python environment that allows different projects to have their own sets of dependencies. In the deployment process of the Journal Project, creating a virtual environment (e.g., using python -m venv myenv) is an optional but recommended step.
Relevance: Helps manage project - specific dependencies and avoid conflicts between different projects.
streamlit run
Definition: A command used to start a Streamlit application. In the deployment process, streamlit run main.py is used to launch the Streamlit application defined in the main.py file.
Relevance: This command is the key step to start the application.
4. Other Key Files - related Terms
LLM (Large Language Model)
Definition: A type of artificial intelligence model that can generate human - like text based on the input it receives. In the project, files like form.py are used to configure and launch an LLM.
Relevance: It is one of the main features of the project, and the configuration and management of LLM are important parts of the application's functionality.
Telegram Bot
Definition: A program that runs on the Telegram messaging platform. It can automate tasks, provide information, and interact with users. In the project, files like form.py and set.py are involved in setting up Telegram bots.
Relevance: Allows for integration with the Telegram platform and provides additional functionality for users.
RAG Chat - bot
Definition: A Retrieval - Augmented Generation chat - bot that combines retrieval from a knowledge base with text generation. The set.py file in the project is used to manage the settings for creating a RAG chat - bot.
Relevance: It is a specific type of chat - bot that the project supports.
=======

# Technical Terms Glossary | 技术术语表
| English Term | 中文术语 | Definition / 说明 |
| **Virtual Environment** | 虚拟环境 | An isolated Python environment for project dependencies |
| **Repository** | 代码仓库 | Storage location for version-controlled code |
| **Commit** | 提交 | Record changes to the repository |
| **Dependency** | 依赖项 | External libraries required by a project |
| **Package Manager** | 包管理器 | Tool for installing and managing packages |
| **CLI (Command Line Interface)** | 命令行界面 | Text-based user interface |

<!-- By Liu Yilin -->
=======

术语词汇表（Terms Glossary）
术语	         英文对照	        定义 / 说明
RAG            聊天机器人	RAG Chatbot	基于检索增强生成（Retrieval-Augmented Generation, RAG）技术的聊天机器人，结合知识库检索与大语言模型（LLM）生成能力，实现基于特定领域知识的智能对话。
Telegram Bot    令牌	Telegram Bot Token	由 Telegram BotFather 生成的唯一标识符，用于验证和授权对 Telegram 机器人 API 的访问，格式为 123456:ABCDEFGHIJKLMNOPQRSTUVWXYZ123456。
API           模型信息	API Model Information	指向大语言模型（LLM）服务的接口地址或预设模型名称（如 gpt-3.5-turbo），用于与模型进行交互以生成文本响应。
Streamlit	Streamlit	一个开源的 Python 框架，用于快速构建和部署数据驱动的 Web 应用，本项目中用于实现用户配置界面。
大语言模型（LLM）	Large Language Model (LLM)	一种基于深度学习的人工智能模型，能够理解和生成自然语言，支持复杂的语言处理任务，如对话生成、文本摘要等，例如 OpenAI 的 gpt-3.5-turbo。
前端数据校验	Frontend Data Validation	在用户提交表单前，通过客户端代码（如 Streamlit 表单组件）对输入数据进行格式和非空检查，防止无效数据进入后端处理，提升用户体验和数据安全性。
后端核心处理	Backend Core Processing	服务器端对用户提交的数据进行深度验证、逻辑处理和业务逻辑执行的过程，包括令牌合法性验证、模型初始化、知识库关联等核心功能。
令牌合法性验证	Token Legitimacy Validation	通过调用 Telegram API（如 getMe 接口）验证用户输入的 Bot 令牌是否有效，确保该令牌可正常访问 Telegram 机器人服务。
知识库关联	Knowledge Base Association	将项目中的数据文件（如 PTO.csv、test.csv）与 RAG 系统关联，作为智能对话的知识来源，使机器人能够基于这些文件内容回答用户问题。
配置持久化	Configuration Persistence	将用户输入的关键配置信息（如 Telegram 令牌、模型地址）存储到配置文件（如 config.ini）或数据库中，确保应用重启后配置信息不丢失。
非空校验	Non-empty Validation	检查表单输入字段是否为空，若为空则显示错误提示（如 “请填写 Telegram Bot 令牌”），确保必填信息完整。
格式预校验	Format Pre-Validation	对输入数据的格式进行初步检查，如 Telegram 令牌是否包含 :、API 模型地址是否以 http:// 或 https:// 开头，减少无效数据进入后端处理。
向量数据库	Vector Database	用于存储和检索向量数据的数据库，在 RAG 系统中用于存储知识库文档的向量化表示，支持高效的语义检索，如 Milvus、Pinecone 等。（注：文档中未明确提及，但 “API векторной базы” 对应此概念）
错误反馈机制	Error Feedback Mechanism	当操作失败时（如令牌无效、模型不可用），向用户显示明确的错误信息（如红色警告），帮助用户定位问题并修正输入，例如 “❌ Telegram 令牌验证失败”。
配置页面	Configuration Page	Streamlit 应用中用于输入和提交 Telegram 令牌、API 模型等关键信息的页面，标题为 “Создание чат-бота RAG”（创建 RAG 聊天机器人）。
提交按钮	Submit Button	页面底部用于提交表单数据的交互按钮（如 “立即创建”），点击后触发前端校验和后端处理逻辑，通常带有加载状态提示（如进度 spinner）。
成功反馈	Success Feedback	操作成功后显示的提示信息（如绿色横幅），包含 Bot 名称和状态（如 “RAG 聊天机器人创建成功！”），并自动跳转至管理页面。
敏感信息保护	Sensitive Information Protection	在截图或文档中对敏感数据（如 Telegram 令牌）进行打码处理（如显示前 6 位和后 4 位，中间用 **** 代替），避免泄露用户隐私或凭证。
模型兼容性	Model Compatibility	确保自定义 API 模型符合系统预设的接口规范（如请求头、参数格式），以便正确调用模型服务，避免因格式不匹配导致的连接失败。
日志辅助调试	Logging for Debugging	在代码中添加日志输出（如 logging.info），记录关键操作的状态（如模型初始化成功 / 失败），帮助开发人员定位和解决运行时错误。
=======
terms.md（术语词汇表）
术语	英文		定义
电子期刊管理应用	Electronic Journal Management Application	用于创建、编辑、审核和展示电子期刊相关信息的应用程序
Streamlit	Streamlit		一种用于快速开发数据应用程序的开源 Python 库
侧边栏	Sidebar	应用页面中位于一侧（通常是左侧）的导航和功能区域
主内容区	Main Content 应用页面中用于展示主要数据和功能的区域
期刊添加表单	Journal Addition Form		用于用户输入期刊相关信息（如部门、开发者、日期等）的表单
部门	Department	期刊所属的组织部门或科室
开发者	Developer		负责期刊内容的主要人员
接收日期 (通用)	Receipt Date (General)		期刊首次被系统接收的日期（通用场景下）
审核日期 (通用)	Review Date (General)		期刊内容首次审核通过的日期（通用场景下）
接收日期 (特定流程)	Receipt Date (Specific Process)		期刊在特定流程中的接收日期
审核日期 (特定流程)	Review Date (Specific Process)	期刊在特定流程中的审核日期
<!-- by 吴柳亿 -->


