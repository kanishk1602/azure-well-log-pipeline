# Project: Azure Welllog Data Integration & Analytics Pipeline
# Goal: Build an end-to-end project that ingests well/field data CSVs,
# processes them via Azure Functions, stores them in Azure SQL,
# exposes REST APIs with FastAPI, and visualizes results in Angular.

# Requirements:
# 1. FastAPI backend with endpoints:
#    - GET /wells → list wells
#    - GET /wells/{id}/logs?from=&to=&property= → filtered logs
# 2. Azure Function (Python) to process CSV files and insert into Azure SQL.
# 3. Angular frontend with a dashboard:
#    - Page 1: Well list with basic info
#    - Page 2: Well log charts (depth vs property) with filters
# 4. Azure DevOps pipeline (YAML) for CI/CD:
#    - Run lint, pytest, Angular unit tests
#    - Build & deploy FastAPI API to Azure App Service
#    - Build & deploy Angular UI to Azure Static Web Apps
# 5. Infrastructure as code:
#    - ARM or Bicep templates for Blob storage, Data Factory, SQL DB, App Service
# 6. Observability:
#    - Application Insights for API
#    - Log query sample in README
# 7. Docs:
#    - README.md with overview, architecture diagram, setup steps, API usage, demo screenshots
#    - docs/ folder with architecture.png (use Mermaid or ASCII diagram)

# Tech stack:
# - Python 3.11, FastAPI, SQLAlchemy, Pytest
# - Angular 16, Chart.js or ngx-charts
# - Azure SQL, Azure Blob Storage, Azure Data Factory
# - Azure DevOps pipelines
# - ARM/Bicep for infra
# - Application Insights

# Repo structure:
# azure-welllog-pipeline/
# ├── api/ (FastAPI backend)
# ├── function/ (Azure Function for CSV ingestion)
# ├── ui/ (Angular frontend)
# ├── infra/ (ARM or Bicep templates)
# ├── ci/ (azure-pipelines.yml)
# ├── data/ (sample CSVs)
# ├── docs/ (architecture, screenshots)
# └── README.md

# Instructions to Copilot:
# - Scaffold the repo step by step, starting with api/main.py and requirements.txt.
# - Generate SQLAlchemy models for wells and logs.
# - Create sample unit tests with Pytest.
# - Add Angular components for WellList and WellLogsChart.
# - Provide azure-pipelines.yml for CI/CD with stages: build → test → deploy.
# - Write ARM/Bicep template for provisioning SQL DB + Blob storage.
# - Include a sample README.md with project overview, setup steps, API examples, and CI/CD badge placeholders.

# Let's start by generating the FastAPI backend (api/main.py + requirements.txt).
