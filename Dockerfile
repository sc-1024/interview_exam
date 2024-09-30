# 使用 Python 3.11 基礎映像
FROM python:3.11-slim
USER root

# 設定工作目錄
WORKDIR /app

# 複製 poetry.lock 和 pyproject.toml 以利安裝依賴
COPY pyproject.toml poetry.lock /app/

# 安裝 poetry
RUN pip install poetry

ENV PYTHONPATH="/app"

# 安裝專案的所有依賴 (不安裝開發依賴)
RUN poetry install --no-root

# 複製專案檔案
COPY . /app

# 執行 pytest，假設 entrypoint 是測試命令
CMD ["cd api_automation/star_wars"]
CMD ["poetry", "run", "pytest", "-v"]
