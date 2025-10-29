# 🧠 Obsidian AI Learning Assistant

**Part of [Aethalgard Academy™](https://academy.questandcrossfire.com) by [Quest & Crossfire™](https://questandcrossfire.com)**

An AI-powered chat assistant that helps you master [Obsidian](https://obsidian.md), the powerful note-taking app. Built as an educational Python project to teach Streamlit, API integration, and clean code practices.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)

---

## ✨ Features

### 🤖 **Flexible AI Provider System**
- **OpenAI (GPT models)**: Fast, high-quality responses (paid)
- **Hugging Face models**: Free alternative (community models)
- Switch providers & models instantly via UI dropdown - no restart needed!

### 🔬 **Deep Research Mode**
Inspired by Gemini and Claude's deep research features:
- Auto-selects strongest AI model (GPT-4 or Llama 2)
- Step-by-step reasoning methodology
- Multiple perspectives (beginner, advanced, practical)
- Comprehensive analysis with pros/cons
- 2-3x longer, more detailed responses

### 📁 **Project Management**
- Create unlimited conversation projects
- Switch between topics instantly
- Each project remembers its own chat history
- Organize learning by subject area

### 📚 **Built-in Obsidian Knowledge Base**
- DataView query examples
- Templater templates
- Plugin recommendations
- Best practices & workflows

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Git (optional, for cloning)
- An API key from [OpenAI](https://platform.openai.com/api-keys) or [Hugging Face](https://huggingface.co/settings/tokens)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/obsidian-ai-assistant.git
   cd obsidian-ai-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your API keys**
   ```bash
   # Copy the example secrets file
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml

   # Edit .streamlit/secrets.toml and add your API keys
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** to `http://localhost:8501`

---

## 🔑 API Setup

### Option A: OpenAI (Recommended)

**Pros:** Fast, high-quality, reliable
**Cons:** Requires payment (but very affordable - pennies per conversation)

1. Get your API key: https://platform.openai.com/api-keys
2. Add to `.streamlit/secrets.toml`:
   ```toml
   API_PROVIDER = "openai"
   OPENAI_API_KEY = "sk-proj-your_key_here"
   ```

### Option B: Hugging Face (Free)

**Pros:** Completely free
**Cons:** Can be slower, less sophisticated responses

1. Get your token: https://huggingface.co/settings/tokens
2. Add to `.streamlit/secrets.toml`:
   ```toml
   API_PROVIDER = "huggingface"
   HF_API_KEY = "hf_your_token_here"
   ```

**Pro Tip:** Add both keys! You can switch providers anytime using the sidebar dropdown.

---

## 📖 Usage

### Basic Usage
1. Type your Obsidian question in the chat input
2. Get instant AI-powered answers with code examples
3. Create projects to organize different learning topics

### Deep Research Mode
1. Toggle "🔬 Deep Research Mode" in the sidebar
2. AI automatically switches to strongest model
3. Get comprehensive, step-by-step analysis
4. Perfect for complex topics and in-depth learning

### Switching AI Providers
1. Use the "API Provider" dropdown in sidebar
2. Select different models for each provider
3. Changes take effect immediately - no restart!

---

## 🎓 Learning Resource

This project is designed as a **teaching tool** for Python beginners:

- ✅ Every line has detailed comments explaining WHAT, WHY, and HOW
- ✅ Multi-line section comments for context
- ✅ Clear variable names (no confusing abbreviations)
- ✅ Step-by-step logic (no complex one-liners)
- ✅ Docstrings with examples for every function

**Recommended reading order:**
1. `project_manager.py` - Learn classes and objects
2. `obsidian_knowledge.py` - Learn data structures
3. `app.py` - See it all come together

---

## 🌐 Deploy to Streamlit Cloud

Want to deploy this app for free? Follow these steps:

1. **Push to GitHub** (your repo must be public or use Streamlit's 1 free private app)

2. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**

3. **Create new app**:
   - Repository: `YOUR_USERNAME/obsidian-ai-assistant`
   - Branch: `main`
   - Main file: `app.py`

4. **Add your secrets** in Advanced Settings → Secrets:
   ```toml
   API_PROVIDER = "openai"
   OPENAI_API_KEY = "sk-proj-..."
   HF_API_KEY = "hf_..."
   ```

5. **Deploy!** Your app will be live at `your-app.streamlit.app`

6. **Custom domain?** Point a CNAME record to your Streamlit app URL

---

## 📁 Project Structure

```
obsidian-ai-assistant/
├── app.py                      # Main Streamlit application
├── obsidian_knowledge.py       # Obsidian knowledge base
├── project_manager.py          # Project/conversation management
├── requirements.txt            # Python dependencies
├── LICENSE                     # GPL-3.0 license
├── README.md                   # This file
└── .streamlit/
    └── secrets.toml.example    # API key template
```

---

## 🤝 Contributing

This is an open-source educational project! Contributions are welcome.

**Ways to contribute:**
- Fix typos or improve code comments
- Add more Obsidian examples to the knowledge base
- Suggest clearer explanations for beginners
- Report bugs or suggest features

**How to contribute:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **GPL-3.0 License** - see the [LICENSE](LICENSE) file for details.

**What this means:**
- ✅ You can use, modify, and distribute this code
- ✅ You can create commercial applications
- ⚠️ You must keep the same GPL-3.0 license
- ⚠️ You must credit Quest & Crossfire™
- ⚠️ You cannot use Quest & Crossfire™ or Aethalgard Academy™ branding

---

## 🏷️ Trademark Notice

**Quest & Crossfire™** and **Aethalgard Academy™** are trademarks.
Trademark registrations are pending.

While this code is open source (GPL-3.0), the brand names are protected trademarks. Please use your own branding when creating derivatives.

---

## 💡 Related Projects

Check out our other courses at **[Aethalgard Academy™](https://academy.questandcrossfire.com)**:
- 🐍 **Python AI Engineering** - Build AI-powered applications
- 🧠 **Obsidian Mastery** - Advanced note-taking workflows

---

## 📞 Support

- 🌐 **Website**: [questandcrossfire.com](https://questandcrossfire.com)
- 🎓 **Academy**: [academy.questandcrossfire.com](https://academy.questandcrossfire.com)
- 🐛 **Issues**: [GitHub Issues](https://github.com/YOUR_USERNAME/obsidian-ai-assistant/issues)

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- AI powered by [OpenAI](https://openai.com/) and [Hugging Face](https://huggingface.co/)
- Deep Research methodology inspired by [Gemini](https://gemini.google.com/) and [Claude](https://claude.ai/)
- Created by [Quest & Crossfire™](https://questandcrossfire.com)

---

**Made with ❤️ by Quest & Crossfire™**
*Small Fixes, Big Clarity*

---

© 2025 Quest & Crossfire™. Licensed under GPL-3.0.
