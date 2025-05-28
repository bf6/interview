FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install uv
RUN pip install uv

# Set work directory
WORKDIR /app

# Copy dependency definition
COPY pyproject.toml ./

# Install dependencies using uv
RUN uv pip install --system .

# Copy project
COPY . .

# Expose port
EXPOSE 8000