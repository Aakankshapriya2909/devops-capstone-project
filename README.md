# Project: Build an Automated CD DevOps Pipeline

## Project Overview
This repository contains the final project for the IBM DevOps and Software Engineering Capstone. It demonstrates a fully automated Continuous Deployment (CD) pipeline that containerizes a Flask-based accounts microservice, applies security headers, runs validation suites, and deploys the application onto a Kubernetes cluster using Tekton.

## Author Details
- **Learner Name:** Aakanksha Priya
- **Date:** June 2026
- **Course:** IBM DevOps and Software Engineering Capstone Project

## Pipeline Features & Architecture
- **Linting:** Automated code quality checks using `flake8`.
- **Unit Testing:** Automated testing execution via `nosetests` and `PyUnit` assertions to verify routing mechanics.
- **Security Engineering:** Integration of `Flask-Talisman` to enforce secure HTTP headers and control Cross-Origin Resource Sharing (`CORS`).
- **Containerization:** Creation and tagging of Docker images using production-ready Dockerfiles.
- **Deployment & Orchestration:** Manifest deployments handled automatically via a Tekton `pipeline.yaml` workflow targeted to a local Kubernetes environment.

## Key Configuration Files
- `pipeline.yaml`: Coordinates task orchestration execution flow.
- `tasks.yaml`: Stores custom task definitions for testing and compiling stages.
- `Dockerfile`: Defines the build environment and execution context for the microservice.
