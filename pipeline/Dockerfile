FROM python:3.13.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
WORKDIR /code
COPY .python-version pyproject.toml uv.lock ./
ENV PATH="/app/.venv/bin:$PATH"
RUN uv sync --locked

COPY pipeline.py .

ENTRYPOINT ["python", "pipeline.py"]