# ==============================================================================
# AutoSafe-Review: Enterprise Air-Gapped Workstation Container
# Tata Technologies TechPulse FY-26 | Case Study CS4
# Candidate: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE, Pune
#
# Standards: ISO 26262 ASIL-D Functional Safety / ISO/SAE 21434 Cybersecurity
# Deployment: 100% Air-Gapped On-Premises (Zero External Network Egress)
# ==============================================================================

FROM python:3.11-slim

# Set labels for automotive engineering audit
LABEL maintainer="Pranav Ravindra Harad <pranav.harad@pccoepune.org>"
LABEL project="AutoSafe-Review Automotive ECU Code Review Workstation"
LABEL institute="Pimpri Chinchwad College of Engineering, Pune (PCCOE)"
LABEL event="Tata Technologies TechPulse FY-26"
LABEL case_study="CS4 - Secure Code Debugging and Review Assistant"

# Set environment flags
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=5000 \
    WSGI_THREADS=6 \
    AUTO_OPEN_BROWSER=0

WORKDIR /app

# Install minimal OS dependencies for building C extensions and health checks
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code and benchmark packages
COPY . .

# Expose internal workstation port
EXPOSE 5000

# Docker healthcheck verifying the review cockpit is alive
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:5000/ || exit 1

# Production WSGI server entrypoint
CMD ["python", "run_production.py"]
