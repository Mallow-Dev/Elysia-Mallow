# ============================
# Build stage for dependencies
# ============================
FROM python:3.13-alpine AS builder

# Prevent bytecode generation and ensure unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /build

# Install build dependencies
RUN apk add --no-cache build-base gcc python3-dev musl-dev linux-headers    # Copy requirements and install dependencies
COPY docker/requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# ============================
# Runtime stage
# ============================
FROM python:3.13-alpine AS runtime

# Add metadata labels
LABEL org.opencontainers.image.title="Elysia AI" \
    org.opencontainers.image.description="An open-source agentic platform for searching data" \
    org.opencontainers.image.version="0.2.dev1" \
    org.opencontainers.image.authors="Danny <danny@weaviate.io>" \
    org.opencontainers.image.source="https://github.com/weaviate/elysia"

# Prevent bytecode generation and ensure unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PATH="/home/appuser/.local/bin:$PATH"

# Create non-root user early
RUN addgroup -S appuser && adduser -S -G appuser -h /app appuser

WORKDIR /app

# Update system packages and install security updates
RUN apk update

# Copy Python dependencies from builder stage
COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local

# Update system packages and install security updates
RUN apk update \
    && apk upgrade --no-cache \
    && apk add --no-cache ca-certificates curl \
    && update-ca-certificates
# Copy application code
COPY --chown=appuser:appuser . .

# Change to non-root user
USER appuser

# Health check (check Python is responsive)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)" || exit 1

# Expose port if needed (based on common FastAPI patterns)
EXPOSE 8000

# Default to CLI, but can be overridden to run FastAPI server
CMD ["python", "-m", "elysia.cli"]
