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

1. 复制 `.env.example` 为 `.env`，填写真实配置。
2. 安装依赖：`uv sync` 或 `pip install -e .`。
3. 启动：`uvicorn app.main:app --reload --port 8000`。
4. 检查：`curl http://127.0.0.1:8000/health`。

## 待确认

- SSH 隧道的本地端口与数据库密码，只写入本机 `.env`。
- 对话模型与 Embedding 供应商。

