# demoap
# CI/CD Pipeline for Containerized Application on Kubernetes

## Overview
This project demonstrates a complete CI/CD workflow for a containerized Python application.
The application is built using Docker, deployed on Kubernetes, and automated using GitHub Actions.

## Technologies Used
- Python
- Docker
- Kubernetes
- GitHub Actions
- Ansible

## CI/CD Workflow
1. Code is pushed to GitHub.
2. GitHub Actions CI job builds the Docker image.
3. CD job runs deployment steps and automation tasks.
4. Kubernetes manages application lifecycle and self-healing.

## Kubernetes Concepts Covered
- Pods and Deployments
- Self-healing and CrashLoopBackOff
- Services, selectors, and endpoints

## Automation
- Docker image build automation
- Kubernetes deployment automation
- Linux environment checks using Ansible

## Key Learnings
- End-to-end CI/CD pipeline design
- Container lifecycle management
- Kubernetes deployment strategies
- Linux automation using Ansible

