# NexaShop-CI/CD Pipeline

## Project Overview
NexaShop, a mid-sized consumer electronics e-commerce site, manages its web app CI/CD pipeline in this repository.

## Tech Stack
- **Language:** Python
- **CI/CD:** GitHub Actions
- **Containerisation:** Docker

## Pipeline Stages
1. Code Commit & Version Control
2. Automated Build
3. Code Quality Analysis (SonarCloud)
4. Unit Testing
5. Integration Testing
6. Artefact Creation (Docker image build)
7. Artefact Push (to Docker registry)
8. Deployment to Staging
9. Manual Approval
10. Deployment to Production
11. Monitoring

## KPIs
- Automated Test Code Coverage (ATCC): 75%
- Deployment Frequency (DF): Multiple times per week
- Mean Time to Detection (MTTD): < 5 minutes
