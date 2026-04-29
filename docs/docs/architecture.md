# Architecture

!!! note "Work in Progress"
    This page will be populated with architecture diagrams and design decisions as the project evolves.

## System Overview

The Threat Detection System consists of the following components:

- **Sensor Nodes** — Raspberry Pi 5 with AI camera modules performing edge inference
- **Cluster** — Raspberry Pi 3 worker nodes managed by a Pi 4/5 master node
- **Backend API** — FastAPI service managing sensor data, events, and storage
- **Frontend Dashboard** — React + TypeScript web application for monitoring
- **Monitoring** — Prometheus + Grafana stack for infrastructure observability
- **Notifications** — Telegram Bot for real-time alerts
