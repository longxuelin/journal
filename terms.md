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
