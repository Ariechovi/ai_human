# ai_human 最小系统

业务范围：企业技术支持助手。MVP 只做文字问答和本地文件上传，后续再扩展
ASR/TTS 与数字人。

## 目标技术栈

- FastAPI + SSE 流式回答
- LangChain 对话模型与 Embedding
- PostgreSQL + pgvector
- Redis 短期上下文
- 三段记忆：短期 / 摘要 / 长期事实
- 本地文件上传与 RAG 检索

## 当前进度

- 已完成：项目骨架、配置、`/health`、`/api/v1/chat` SSE 骨架、pgvector 数据模型。
- 未完成：文档入库、RAG 检索、三段记忆读写、评测与前端。

## 运行方式

1. 启动 SSH 隧道：
   `ssh -i C:\Users\LENOVO\.ssh\ariechovi.pem -L 16379:localhost:6379 -L 15432:localhost:5432 root@111.230.199.27`
2. 激活 Python 环境：`conda activate voiceagent`。
3. 复制 `.env.example` 为 `.env`，填写数据库密码、DeepSeek Key 和阿里云 Key。
4. 安装依赖：`uv sync` 或 `pip install -e .`。
5. 启动：`uvicorn app.main:app --reload --port 8000`。
6. 检查：`curl http://127.0.0.1:8000/health`。

## 待确认

- 数据库密码、DeepSeek Key、阿里云 Key 只写入本机 `.env`。
- `qwen3.7-text-embedding` 的准确 API 模型名与向量维度待核验。

