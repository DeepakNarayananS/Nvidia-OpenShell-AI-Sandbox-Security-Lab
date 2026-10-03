FROM python:3.12-slim

# Create a non-root user
RUN useradd --create-home --uid 1000 --user-group app

# OpenShell-compatible workspace
WORKDIR /sandbox

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY --chown=app:app agent.py .
COPY --chown=app:app tools.py .
COPY --chown=app:app malicious.txt .

# Create a separate protected directory outside the workspace
# The application user must not be able to modify the protected file.
RUN mkdir -p /protected \
    && printf '%s\n' \
       'CONFIDENTIAL SECURITY LAB FILE' \
       'This file is used for the OpenShell isolation demonstration.' \
       'Status: PROTECTED' \
       > /protected/important.txt \
    && chown root:root /protected /protected/important.txt \
    && chmod 755 /protected \
    && chmod 444 /protected/important.txt

# Run as non-root
USER app

CMD ["python", "-u", "agent.py"]
