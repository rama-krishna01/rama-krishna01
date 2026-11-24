# Implementation snippets from the project report

These excerpts are transcribed from **Chapter 6, Section 6.8 — Source Code Snippets** of the *JARVIS AI CHATBOT* academic report (PDF pages 30–33). They are presented as documentation excerpts, not as a complete application.

## 1. FastAPI backend excerpt (Section 6.8.1)

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="AI Chatbot Backend")

class ChatMessage(BaseModel):
    message: str
    history: List[Dict[str, str]] = []

@app.post("/api/chat")
async def chat_endpoint(req: ChatMessage):
    pass
```

**Report limitation:** The endpoint body is shown as `pass`; the report does not provide the complete request-processing implementation in this excerpt.

## 2. Gemini AI integration excerpt (Section 6.8.2)

```python
from google import genai

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=contents
)

return {"response": response.text}
```

**Report limitation:** The excerpt references `os` and `contents` without showing their definitions/imports in this section. It is a partial integration example, not a complete standalone function.

## 3. LocalStorage management excerpt (Section 6.8.3)

The report shows the following operations for saving and restoring sessions:

```javascript
function saveSessions() {
    localStorage.setItem(
        'jarvis_chats',
        JSON.stringify(sessions)
    );
}

function loadSessionsFromStorage() {
    const store =
        localStorage.getItem('jarvis_chats');

    if (store) {
        sessions = JSON.parse(store);
    }
}
```

## 4. New chat session excerpt (Section 6.8.4)

```javascript
newChatBtn.addEventListener('click', () => {
    currentSessionId = Date.now().toString();
    chatHistory = [];
    chatContainer.innerHTML = '';
    chatContainer.appendChild(welcomeMessage);
});
```

## 5. Sending user messages excerpt (Section 6.8.5)

The report shows the request configuration below; the code continues across the page break:

```javascript
const response = await fetch('/api/chat', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        message: text,
        history: chatHistory
    })
});
```

## 6. Frontend chat interface excerpt (Section 6.8.6)

```html
<div class="input-wrapper">
    <textarea
        id="chat-input"
        placeholder="Message Jarvis..."
        rows="1">
    </textarea>

    <button id="send-btn" disabled>
        <i class="fa-solid fa-paper-plane"></i>
    </button>
</div>
```

## Notes

- These excerpts preserve the code and names visible in the report.
- The report does not show all frontend/backend files, complete endpoint logic, complete error/retry implementation, or the full page styling in this section.
- Do not treat these snippets as a ready-to-run codebase without completing and testing the missing implementation.
- The report identifies Python, FastAPI, Uvicorn, Google Gemini AI, HTML5, CSS3, JavaScript, Visual Studio Code and GitHub in its software/tools list.
