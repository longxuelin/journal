一、前期准备
1.1 环境部署与依赖安装
遵循仓库部署指引完成环境搭建，确保开发环境配置正确：

bash
# 克隆项目仓库  
git clone https://github.com/lihuaju-dev/journal.git  
# 创建并激活虚拟环境（Windows系统）  
python -m venv venv  
venv\Scripts\activate  
# 安装Streamlit及项目依赖  
pip install streamlit  
# 启动应用  
streamlit run main.py  

![fad9a8e343690e3e9eea0d778fcb8bac](https://github.com/user-attachments/assets/58126c52-fd6f-49c4-9350-743630442345)

1.2 访问应用界面
应用启动后，通过以下方式访问：

本地环境：浏览器输入 http://localhost:8501
远程服务器：使用公网 IP 访问（如 http://<服务器IP>:8501）

![63bdcaf892dc8fc188be2cb221b8b491](https://github.com/user-attachments/assets/50316439-9203-4209-b7a6-7d61736cfe6a)
![ab644bc23fa716e95fd5539956991619](https://github.com/user-attachments/assets/1c4f9953-b5d1-4971-9964-d1169e9f3c90)

二、输入配置信息操作流程
1. 导航至创建页面
在 Streamlit 应用首页，通过左侧边栏菜单找到 “创建 RAG 聊天机器人” 选项，点击进入配置界面：

![ccfa3efa31a33056c597f1d0a01f9662](https://github.com/user-attachments/assets/7dc6d9b8-be08-403b-a8b2-82a81276877f)


注释 1：侧边栏导航由 main.py 中的 st.sidebar 组件实现，确保用户快速定位功能入口。
2. 填写核心配置参数
① Telegram Bot 令牌输入
输入位置：
在页面中部区域，设有明确标注为 Telegram Bot Token 的输入框，右上角以红色星号（*）醒目标注为必填项，确保用户快速识别关键信息。
令牌格式：
请通过 Telegram BotFather 官方工具创建机器人并获取标准格式令牌（形如 123456:ABCDEFGHIJKLMNOPQRSTUVWXYZ123456），该令牌由数字、字母及特殊符号组成，是验证机器人身份的唯一凭证。直接复制完整令牌至输入框，避免手动输入导致的格式错误。
交互安全设计：
输入框采用密码模式优化交互体验，用户输入时字符自动隐藏，显示为圆点（・）或星号（*），有效防止令牌泄露，提升敏感信息输入时的安全性。
② API 模型配置
Ⅰ. 预设模型（推荐新手使用）
选择方式：
通过下拉菜单快速选取官方认证的成熟模型，如 gpt-3.5-turbo（适合通用对话场景）、local-llama2（支持本地化部署的开源模型）等，列表内容随系统更新动态扩展。
智能填充：
选中预设模型后，系统自动填充模型所需的基础参数（如 temperature 控制回复随机性，max_tokens 限制单次生成的最大字符数），无需手动配置，大幅降低操作门槛。
Ⅱ. 自定义模型（适合进阶用户）
激活条件：
若需使用自建模型或第三方 API 服务，勾选输入框右侧的 “自定义 API” 选项，激活高级配置入口。
地址规范：
在激活的输入框中，需填写符合 OpenAI API 接口规范 的完整地址（示例：https://your-model-api.com/v1/chat/completions）。地址需包含协议前缀（http:// 或 https://）、服务器域名及具体端点路径，确保后台能够正确解析并调用模型服务。
3. 提交配置请求
确认信息无误后，点击页面底部 “立即创建” 按钮（高亮绿色按钮，悬停显示加载动画），触发后台验证与创建流程。
1.前端实时校验（非空 / 格式检查）；
2.后台深度验证（令牌有效性、模型连通性）；
3.配置持久化与机器人启动。
三、提交后的全链路处理逻辑
1. 前端实时校验（form.py 核心功能）
非空校验：
若 Telegram Bot 令牌 或 API 模型 字段为空，页面立即显示红色警示：
plaintext
❗ 请填写 Telegram Bot 令牌和 API 模型信息  

格式预校验：
Telegram 令牌：验证是否包含 : 分隔符，且长度符合 Telegram API 规范（非严格校验，后台将进行深度验证）。
API 模型：检查是否为预设值或合法 URL 格式（包含 http:// 或 https:// 前缀）。
2. 后台核心处理（set.py 技术实现）
① Telegram 令牌合法性验证
通过调用 Telegram Bot API 进行深度校验，确保令牌有效：

python
运行
# set.py 令牌验证逻辑  
import requests  
from requests.exceptions import RequestException  

def validate_telegram_token(token: str) -> bool:  
    api_url = f"https://api.telegram.org/bot{token}/getMe"  
    try:  
        response = requests.get(api_url, timeout=10)  
        if response.status_code == 200 and response.json().get("ok"):  
            return True  
        raise ValueError("令牌验证失败，可能为无效令牌或网络问题")  
    except RequestException as e:  
        raise ValueError(f"网络请求异常：{str(e)}")  
② 模型初始化与 RAG 组件组装
根据用户输入动态加载模型，并关联知识库构建 RAG 问答链：

python
运行
# 模型加载逻辑  
from langchain.llms import OpenAI  
from langchain.retrievers import ChromaRetriever  
from langchain.chains import RetrievalQA  

def initialize_llm(model_name: str, api_key: str):  
    if model_name.startswith("gpt-"):  
        return OpenAI(model_name=model_name, openai_api_key=api_key)  
    elif model_name.startswith("http"):  
        # 自定义API模型初始化（需实现LangChain兼容接口）  
        return CustomLLM(api_url=model_name)  
    else:  
        raise ValueError("不支持的模型类型")  

# 知识库关联与RAG链构建  
def build_rag_chain(llm, knowledge_file: str):  
    # 加载CSV知识库（需包含question/answer列）  
    df = pd.read_csv(knowledge_file)  
    # 创建向量索引（示例使用Chroma数据库）  
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
③ 配置持久化存储
将用户配置写入 config.ini 或数据库，支持后续管理与复用：

ini
; app/settings/config.ini 配置示例  
[telegram]  
token = 123456:ABCDEFGHIJKLMNOPQRSTUVWXYZ123456  ; 打码后存储为123456:*******123456  
[model]  
name = gpt-3.5-turbo  
api_key = sk-****************  ; OpenAI API密钥（需额外安全存储）  
[knowledge_base]  
file = PTO.csv  
3. 多场景反馈机制
反馈类型	界面表现	技术实现	功能验证
创建成功	顶部绿色横幅：
✔️ RAG聊天机器人创建成功！Telegram Bot已激活：@YourBotName
自动跳转至管理页面，显示令牌后四位（如 ****56）与模型名称	st.success() 组件 + st.experimental_set_query_params() 路由跳转	在 Telegram 中发送 /start，机器人应回复 PTO.csv 中的欢迎语（如 “您好！请咨询公司请假政策相关问题”）
四、注意事项
敏感信息保护：
截图中 Telegram 令牌需打码处理（如显示前 6 位和后 4 位，中间用****代替）。
模型兼容性：
若使用自定义 API 模型，需在set.py中提前定义接口规范（如请求头、参数格式）。
日志辅助调试：
在set.py中添加日志输出（如logging.info("模型初始化成功")），帮助定位失败原因。
