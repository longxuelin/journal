一、前期准备
1.环境部署
 1.1 确保已按仓库Deployment Instructions完成环境搭建：
     bash
     git clone https://github.com/lihuaju-dev/journal.git  
     python -m venv venv  
     venv\Scripts\activate  
     pip install streamlit  
     streamlit run main.py  
![fad9a8e343690e3e9eea0d778fcb8bac](https://github.com/user-attachments/assets/c70f9f87-3a56-476c-8b3d-4c780986141a)

  1.2 启动后通过http://localhost:8501（本地）或服务器公网 IP 访问应用。
  ![63bdcaf892dc8fc188be2cb221b8b491](https://github.com/user-attachments/assets/965182b4-e9a2-4397-856a-1f21ac36365b)
![ab644bc23fa716e95fd5539956991619](https://github.com/user-attachments/assets/41a4771e-4cef-4bc5-9244-fd719d87e4a7)

二、输入 Telegram Bot 令牌与 API 模型信息操作流程
1. 进入创建页面
在 Streamlit 应用首页，通过侧边栏或顶部导航栏找到 “创建 RAG 聊天机器人” 入口，点击进入配置页面
![ccfa3efa31a33056c597f1d0a01f9662](https://github.com/user-attachments/assets/8a0b3ed4-89ae-4de0-969e-a0004d61d56b)

2. 填写关键信息
① Telegram Bot 令牌输入
位置：页面中部的Telegram Bot Token输入框（红色星号为必填标识）。
格式：从 Telegram BotFather 获取的令牌（形如123456:ABCDEFGHIJKLMNOPQRSTUVWXYZ123456），直接复制粘贴到输入框。
② API 模型信息输入
模型选择：下拉菜单选择预设模型（如gpt-3.5-turbo、local-llama2），或在输入框手动填写自定义 API 地址（如https://your-model-api.com/v1/chat）。
3. 提交配置
确认信息无误后，点击页面底部 “立即创建” 按钮（按钮颜色通常为蓝色或绿色，鼠标悬停显示加载状态）。
三、点击提交后的处理逻辑（核心：set.py 功能解析）
1. 前端数据校验（form.py 辅助）
非空校验：若 Telegram 令牌或模型字段为空，页面立即显示红色警告：
plaintext
❗ 请填写Telegram Bot令牌和API模型信息  

格式预校验：
Telegram 令牌：检查是否包含:且长度符合规范（非严格校验，后台会进一步验证）。
API 模型：验证是否为预设值或合法 URL 格式（如包含http://或https://）。
2. 后台核心处理（set.py 核心函数）
① 令牌合法性验证
python
运行
# set.py中Telegram令牌验证逻辑  
import requests  

def validate_telegram_token(token: str) -> bool:  
    url = f"https://api.telegram.org/bot{token}/getMe"  
    response = requests.get(url)  
    if response.status_code == 200 and response.json().get("ok"):  
        return True  
    raise ValueError("Telegram令牌无效或网络连接失败")  
② 模型初始化与配置
模型加载：根据输入的模型名称或 API 地址，加载对应的 LLM（大语言模型）接口，例如：
python
运行
if model == "gpt-3.5-turbo":  
    from langchain.llms import OpenAI  
    llm = OpenAI(model_name=model)  
elif model.startswith("http"):  
    # 自定义API模型调用逻辑  
    llm = CustomAPIModel(api_url=model)  

知识库关联：自动关联仓库中的PTO.csv、test.csv等文件作为 RAG 的知识库数据源。
③ 配置持久化
将令牌和模型信息写入config.ini或数据库（示例路径：app/settings/config.ini）：
ini
[telegram]  
token = 123456:ABCDEFGHIJKLMNOPQRSTUVWXYZ123456  
[model]  
name = gpt-3.5-turbo  

3. 结果反馈机制
✅ 创建成功
   界面反馈：
     页面顶部弹出绿色成功横幅，显示：
       plaintext：
         ✔️ RAG聊天机器人创建成功！Telegram Bot已激活：@YourBotName  

  自动跳转至 “机器人管理” 页面，显示当前配置的令牌后四位（如****56）和模型名称。
功能验证：
   通过 Telegram 搜索 Bot 名称，发送/start指令，机器人应回复知识库中的欢迎语（如PTO.csv中的请假政策说明）。
❌ 创建失败
 错误类型	典型反馈信息	截图示例
 令牌无效	❌ Telegram令牌验证失败，请检查是否从BotFather获取有效令牌	
 模型不可用	❌ API模型连接失败：404 Not Found（请检查模型名称或URL）	截
 网络超时	❌ 连接超时，请检查服务器网络或重试提交	截图 7
四、操作截图说明与注释
必需截图列表
截图 1：应用首页与创建入口
展示 Streamlit 应用首页，标注 “创建 RAG 聊天机器人” 按钮位置（如侧边栏菜单）。
注释1：通过Streamlit侧边栏导航进入创建页面
截图 2：输入表单详情
清晰显示 Telegram Bot Token 输入框（带星号必填标识）和 API 模型选择 / 输入区域。
注释2：确保输入框标签与代码中的`set.py`参数命名一致（如`telegram_token`、`model_name`）
截图 3：非空校验失败提示
故意留空某字段，提交后拍摄红色错误提示（如 “请填写 Telegram Bot 令牌”）。
注释3：前端校验由`form.py`实现，阻止空数据进入后台
截图 4：创建成功反馈
绿色横幅 + Bot 名称显示，底部可能附带 “开始对话” 引导按钮。
注释4：成功反馈需包含Telegram Bot的@用户名，便于用户快速定位
截图 5：令牌无效错误
故意输入错误令牌（如缺少:），拍摄红色警告 “Telegram 令牌验证失败”。
注释5：此错误由`set.py`中的`validate_telegram_token`函数抛出
五、注意事项
敏感信息保护：
截图中 Telegram 令牌需打码处理（如显示前 6 位和后 4 位，中间用****代替）。
模型兼容性：
若使用自定义 API 模型，需在set.py中提前定义接口规范（如请求头、参数格式）。
日志辅助调试：
在set.py中添加日志输出（如logging.info("模型初始化成功")），帮助定位失败原因。
