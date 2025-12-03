#!/usr/bin/env bash
# Deployment script for Google Cloud Run
# This script automates the process of deploying your containerized service to the cloud

# Deploy the service to Cloud Run
# This command builds your Docker container and deploys it
gcloud run deploy fasta-validator-service \
    --source . \
    --platform managed \
    --no-allow-unauthenticated \
    --region europe-west4 \
    --memory 512Mi \
    --cpu 1

# Explanation of deployment options:
# --source . : Build from current directory (uses Dockerfile)
# --platform managed : Use Google's fully managed Cloud Run (recommended)
# --no-allow-unauthenticated : Require authentication to access the service
# --region europe-west4 : Deploy to European data center (choose closest to users)
# --memory 512Mi : Allocate 512 megabytes of RAM (sufficient for this simple service)
# --cpu 1 : Allocate 1 CPU core (can handle moderate traffic)

# Prerequisites (run these commands first if needed):
# gcloud auth login                                    # Authenticate with Google Cloud
# gcloud config set project YOUR-PROJECT-ID           # Set your project ID
# gcloud services enable run.googleapis.com           # Enable Cloud Run API
# gcloud services enable cloudbuild.googleapis.com    # Enable Cloud Build API