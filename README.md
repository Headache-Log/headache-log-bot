# Headache Log — Telegram Bot

Telegram bot for the Headache Log project.  
Provides a simple and private interface for logging headache and migraine episodes.

## Overview

The bot allows users to:
- create headache entries with a single action;
- view recent history;
- export their data as CSV;
- edit or delete existing entries.

Each user is identified by their Telegram `user_id`.  
No registration, passwords, or personal profiles are used.

## Core principles

- 🔒 Privacy-first (no tracking, no third-party analytics)
- 🧠 Simple journaling, no medical advice
- 👤 One Telegram user → one private log
- 🌍 Multilingual (based on Telegram language settings)

## Features (MVP)

- Create a new entry (timestamp is set automatically)
- View last 10 entries
- Export full history as CSV (date + comment)
- Edit comment
- Soft delete entries
- Inline keyboard-based UX

## Tech stack

- Python
- python-telegram-bot
- Async I/O
- REST API integration ([headache-log-api](https://github.com/Headache-Log/headache-log-api))

## Architecture

The bot is a thin client:
- contains no business logic;
- stores no persistent data;
- communicates with the backend API over HTTP.

  Telegram User
        ↓
  Telegram Bot
        ↓
Headache Log API
        ↓
    PostgreSQL

## Configuration

The bot is configured via environment variables:

- `BOT_TOKEN` — Telegram bot token
- `API_BASE_URL` — Headache Log API endpoint
- `BOT_DEFAULT_LANGUAGE` (optional)

Secrets must **not** be committed to the repository.

## Deployment

The bot is designed to run:
- in Docker
- inside Kubernetes
- on ARM64 (Raspberry Pi)

Production deployment is handled in the [headache-log-k8s](https://github.com/Headache-Log/headache-log-k8s) repository.

## Status

🚧 Early development (HomeLab project)

## Disclaimer

This project is **not** a medical application and does not provide medical advice.
