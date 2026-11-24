# Jarvis AI Chatbot

A web-based conversational AI assistant developed as an academic team project during the 2025–2026 academic year at Pallavi Engineering College, CSE (AI & ML).

The application combines a responsive HTML/CSS/JavaScript interface, a FastAPI backend, and Google's Gemini AI model. Conversation sessions are retained in the browser using LocalStorage.

## Features described in the project report

- AI-generated conversational responses using Google Gemini
- FastAPI endpoint for frontend/backend communication
- Multiple chat sessions, including new chat, switching and deletion
- Browser-based chat-history persistence with LocalStorage
- Markdown and code-response presentation
- Network/API error handling and retry behaviour
- Responsive dark-themed chat interface

## Technology stack

| Area | Technologies |
|---|---|
| Backend | Python, FastAPI, Uvicorn |
| AI integration | Google Gemini, Google GenAI SDK |
| Frontend | HTML5, CSS3, JavaScript |
| Conversation storage | Browser LocalStorage |

## Architecture

1. The user enters a message in the browser interface.
2. The frontend sends the message and conversation history to the FastAPI `/api/chat` endpoint.
3. The backend is intended to pass the prompt/context to the Gemini model through the Google GenAI SDK.
4. The response is returned to the frontend and displayed in the chat.
5. Chat sessions are saved in browser LocalStorage so they can be restored after a page refresh.

## Repository contents

- [Implementation snippets](./docs/implementation-snippets.md) — code excerpts transcribed from Section 6.8 of the academic report.
- [Project report](./docs/) — place the original report PDF here when it is added.

## Important implementation note

The academic report contains **source-code snippets, not a complete runnable source-code distribution**. In particular, the FastAPI endpoint in the report ends with `pass`, and the Gemini integration excerpt refers to values/imports that are not fully defined in the shown snippet. The documentation in this repository preserves that distinction. It does not claim that these excerpts alone form a working application.

To run the complete original application, the full frontend and backend source files and a valid Gemini API key are required. Never commit API keys or other secrets.

## Configuration and security

The report shows the Gemini API key being read from an environment variable named `GEMINI_API_KEY`. Keep the key outside source control and configure it in your local environment when implementing the complete backend.

## Academic project context

This was developed as a team project. The report contains inconsistent contributor lists across its certificate and declaration pages, so this repository does not attribute the entire project to one individual.

## Source

Prepared from the project report titled **“JARVIS AI CHATBOT”**, academic year 2025–2026, especially Chapter 6 (Implementation) and Section 6.8 (Source Code Snippets).
