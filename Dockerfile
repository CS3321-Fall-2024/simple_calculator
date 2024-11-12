# Step 1: Use Python/Alpine as the base image
# Make sure the Python version matches your project
FROM python:3.13-alpine

# Step 2: Install Poetry
RUN apk add --no-cache curl \
    && curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.8.2 python3 -

# Add poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Step 3: Set the working directory and copy project files
WORKDIR /app
COPY . .

# Step 4: Install project dependencies
RUN poetry install

# Step 5: Run tests
RUN poetry run pytest

# Step 6: Run the project interactively
CMD ["poetry", "run", "python", "calculator/calculator.py"]
