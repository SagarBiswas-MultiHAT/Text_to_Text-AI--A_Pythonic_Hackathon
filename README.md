# Text_to_Text (AI) – GodMod

An experimental, terminal-based AI command assistant that can:

- Open popular web destinations with natural language (e.g. `open google`, `open youtube`).
- Play predefined music/video links from a tiny in-code library (e.g. `play animal`).
- Fall back to a large language model (Groq Llama 3 70B) for any other text-to-text interaction, while preserving multi‑turn conversational context.

> NOTE: The current system prompt in `main.py` is intentionally styled as a taunting, adversarial persona. You may want to replace or tone it down for production or public demos.

---

## ✨ Features

- Simple REPL loop (`python main.py`) – no extra framework.
- Dynamic conversation context retention across turns.
- Command router that distinguishes between:
  - URL launch commands
  - Music playback requests via a lightweight dictionary
  - Free-form AI chat
- Easily extensible mapping for new commands / services.

---

## 🗂 Project Structure

```
main.py            # Entry point & command loop; routes user input
musicLibraries.py  # Dictionary of song keywords → YouTube (or channel) links
```

---

## 🚀 Quick Start

### 1. Clone

```powershell
git clone https://github.com/SagarBiswas-MultiHAT/Text_to_Text-AI--A_Pythonic_Hackathon.git
cd "Text_to_Text-AI--A_Pythonic_Hackathon"
```

### 2. Create & Activate Virtual Environment (Recommended)

```powershell
python -m venv .venv
. .venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

At present the only external dependency is the `groq` Python SDK.

```powershell
pip install groq
```

(If you add linters, formatters, etc., document them here.)

### 4. Configure Your API Key Securely

```python
# Replace inside aiProsses
import os
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
```

### 5. Run

```powershell
python main.py
```

Sample session:

```
Hi, I'm Sagar. How can I help you?
==> open github
# (Browser opens GitHub)
==> play animal
# (Opens the configured YouTube link)
==> Explain decorators in python simply
AI Response: <model answer>
==> exit
```

---

## 🧠 How It Works (Flow)

1. Read user input.
2. Normalize to lowercase.
3. If it exactly matches a key in `url_map`, open that site.
4. If it starts with `play`, extract the second token as the song key and look up `musicLibraries.musicLinks`.
5. Otherwise, forward the raw command (plus accumulated context) to Groq's Chat Completions API with model `llama3-70b-8192`.
6. Append user + assistant messages to `context` for multi-turn continuity.

---

## 🔧 Extending

### Add a New Website Command

In `prossess_command` inside `main.py`:

```python
url_map = {
    # ...existing entries...
    "open reddit": "https://reddit.com"
}
```

### Add a New Song

In `musicLibraries.py`:

```python
musicLinks = {
    # ...existing songs...
    "lofi": "https://www.youtube.com/watch?v=5qap5aO4i9A"
}
```

Then in the terminal:

```
==> play lofi
```

### Change/Soften the Persona

Modify the first system message in `messages` within `aiProsses`.

---

## 🛡 Security & Privacy Notes

- DO NOT commit real API keys. Rotate the exposed key immediately if this repository has been published.
- Consider rate limiting or input sanitization if you later expose this via a web interface.
- The current persona text could be flagged as hostile; adjust for user safety & inclusivity.
- No logging/analytics layer—anything printed appears in the user’s console only.

---

## 🧪 Testing Ideas (Not Yet Implemented)

You can add a basic test scaffold (e.g., with `pytest`) to validate routing logic without calling the real API:

- Test: `open github` triggers `webbrowser.open` with correct URL (patch `webbrowser.open`).
- Test: `play animal` opens correct link.
- Test: `play missing_song` prints not found message.
- Test: Fallback path calls `Groq.chat.completions.create` once.

---

## 🗺 Roadmap / Ideas

- Replace blocking input loop with async + streaming responses.
- Pluggable command modules (e.g., `calc 2+2`, `weather Paris`).
- Local model fallback when API unavailable.
- Add logging + verbosity flags.
- Rich TUI (Textual / prompt_toolkit) for better UX.
- Persist context to disk (optional) between sessions.

---

## 🤝 Contributing

1. Fork the repo.
2. Create a feature branch: `git checkout -b feat/your-feature`.
3. Commit with clear messages: `git commit -m "Add command router refactor"`.
4. Open a Pull Request describing motivation & changes.

Please open an issue first for large changes.

---

## ❓ FAQ

Q: Why not just use ChatGPT directly?
A: This script demonstrates lightweight command multiplexing plus local extensibility.

Q: Does it store my chats?
A: Only in-memory during the session via the `context` list.

Q: How do I clear context mid-session?
A: Type something like `clear context` after adding a branch in code to reset (not yet implemented).

---

## 🧩 Troubleshooting

| Symptom                       | Possible Cause                | Fix                                    |
| ----------------------------- | ----------------------------- | -------------------------------------- |
| `ModuleNotFoundError: groq`   | Dependency missing            | Run `pip install groq`                 |
| API 401 / 403                 | Invalid or revoked key        | Recreate & export `GROQ_API_KEY`       |
| Nothing happens on `open ...` | Browser default misconfigured | Specify browser via `webbrowser.get()` |
| `play <song>` says not found  | Key mismatch                  | Check `musicLibraries.musicLinks` keys |

---

## 🙌 Acknowledgments

- Groq for fast LLM inference API.
- You, for exploring / hacking on this.

---

### Next Steps If You Publish Publicly

- Remove hard-coded key & rotate it.
- Add `requirements.txt` with pinned versions (e.g. `groq==<version>`).
- Add basic unit tests.
- Include a permissive license if you welcome contributions.

---

Feel free to request enhancements or ask me to implement any of the roadmap items next.
