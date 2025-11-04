# Contributing to Obsidian AI Assistant

Thank you for your interest in contributing to the Obsidian AI Learning Assistant!

## 🎯 Project Overview

This is a Streamlit-based AI assistant for learning Obsidian, developed as part of the OutSkill AI Engineering Bootcamp 2025. It demonstrates dual AI provider support, deep research mode, and project-based conversation management.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git
- API keys (OpenAI and/or Hugging Face)
- Basic understanding of Streamlit and AI APIs

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/AsheeshSrivastava/obsidian-ai-assistant.git
   cd obsidian-ai-assistant
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API keys**
   ```bash
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml
   # Edit .streamlit/secrets.toml with your API keys
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📐 Code Standards

### Python Style
- Follow PEP 8 guidelines
- Use type hints where appropriate
- Maximum line length: 100 characters
- Comprehensive docstrings with examples

Example:
```python
def switch_ai_provider(provider: str, model: str) -> dict:
    """Switch between OpenAI and Hugging Face providers.

    Args:
        provider: Either "openai" or "huggingface"
        model: Model name specific to the provider

    Returns:
        Dictionary with provider config and status

    Example:
        >>> switch_ai_provider("openai", "gpt-3.5-turbo")
        {'status': 'success', 'provider': 'openai', 'model': 'gpt-3.5-turbo'}
    """
    pass
```

### Streamlit Conventions
- Use `st.session_state` for all persistent data
- Implement proper error handling with try/except
- Use `st.error()`, `st.warning()`, `st.success()` for user feedback
- Test with both AI providers (OpenAI and Hugging Face)

### File Organization
```
obsidian-ai-assistant/
├── app.py                      # Main Streamlit UI
├── obsidian_knowledge.py       # Knowledge base management
├── project_manager.py          # Project/conversation management
├── requirements.txt            # Dependencies
├── LICENSE                     # AGPL-3.0 license
└── .streamlit/
    └── secrets.toml            # API keys (gitignored)
```

## 🔧 Pull Request Process

1. **Create feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make changes**
   - Write clean, documented code
   - Test with both AI providers
   - Verify Deep Research Mode works
   - Test project switching

3. **Test locally**
   ```bash
   streamlit run app.py

   # Test checklist:
   # - Create new project
   # - Switch AI providers (OpenAI ↔ Hugging Face)
   # - Toggle Deep Research Mode
   # - Send messages and verify responses
   # - Switch between projects
   # - Check error handling
   ```

4. **Commit changes**
   ```bash
   git add .
   git commit -m "feat: brief description of changes"
   ```

   **Commit message format:**
   - `feat:` - New feature
   - `fix:` - Bug fix
   - `docs:` - Documentation only
   - `style:` - Formatting changes
   - `refactor:` - Code refactoring
   - `test:` - Adding tests
   - `chore:` - Maintenance

5. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

   **In your Pull Request:**
   - Clear title describing change
   - Screenshots of new features (if UI changes)
   - Test results with both AI providers
   - Explanation of why the change is needed

## 🐛 Bug Reports

Include:
- Steps to reproduce the bug
- Expected vs actual behavior
- Screenshots or error messages
- Python version
- Streamlit version
- AI provider being used (OpenAI or Hugging Face)
- Operating system

**Example Bug Report:**
```markdown
**Bug:** Deep Research Mode fails with Hugging Face

**Steps to reproduce:**
1. Select Hugging Face as provider
2. Enable Deep Research Mode
3. Send message about Obsidian plugins
4. Error appears: "AttributeError: 'NoneType' object has no attribute 'content'"

**Expected:** Deep Research response from Hugging Face model
**Actual:** Error message displayed

**Environment:**
- Python: 3.9.7
- Streamlit: 1.28.0
- Provider: Hugging Face (meta-llama/Llama-2-7b-chat-hf)
- OS: Windows 11
```

## 💡 Feature Requests

For new features, please:
1. Check if it already exists in "Future Enhancements"
2. Explain the use case (who benefits and how)
3. Provide implementation ideas if possible
4. Consider impact on existing functionality

**Good Feature Request Example:**
```markdown
**Feature:** Export conversation to markdown

**Use case:**
Users want to save their learning conversations for their Obsidian vault.

**Proposal:**
- Add "Export" button in sidebar
- Generate markdown file with timestamp
- Include project name in filename
- Format as Q&A with proper headings

**Implementation idea:**
- Use `st.download_button()` for download
- Format: `project_name_YYYY-MM-DD.md`
- Structure: `# Conversation\n\n## Q: {question}\nA: {answer}\n\n`
```

## 🧪 Testing

### Manual Testing Checklist

Before submitting PR:
- [ ] App launches without errors
- [ ] Both AI providers work (OpenAI and Hugging Face)
- [ ] Can switch between providers mid-conversation
- [ ] Deep Research Mode toggles correctly
- [ ] Auto-selects strongest model in Deep Research
- [ ] Project creation works
- [ ] Project switching preserves history
- [ ] Messages appear in chat correctly
- [ ] Error handling displays user-friendly messages
- [ ] No API keys exposed in UI or logs

### Provider Testing

Test both providers separately:
- [ ] **OpenAI**: GPT-3.5 and GPT-4 models respond
- [ ] **Hugging Face**: Community models respond (may be slower)
- [ ] Deep Research Mode works with both
- [ ] Provider switch is instant (no restart required)

## 🎨 UI/UX Guidelines

### Streamlit Best Practices
- Use emojis consistently (🤖, 💬, 🔬, 📁)
- Provide clear user feedback for actions
- Show loading states for API calls
- Use sidebar for settings and controls
- Implement graceful error handling

### Design Principles
- Keep it simple and intuitive
- Minimize clicks for common actions
- Provide clear labels and instructions
- Use consistent spacing and formatting

## 🔐 Security

### API Key Management
- ⚠️ **NEVER commit API keys** to Git
- Use `.streamlit/secrets.toml` (gitignored)
- Verify `.gitignore` includes secrets file
- Test with invalid API keys to ensure proper error handling

### Data Privacy
- Conversation history stored locally in Streamlit session state
- No data sent to external servers except AI APIs
- No user tracking or analytics
- API keys encrypted by Streamlit Cloud deployment

## 📚 Documentation

When adding features:
- Update README.md if user-facing
- Add docstrings to new functions
- Include usage examples
- Update "Features" section if applicable
- Document any new API requirements

## 🏷️ Trademark Notice

**QUEST AND CROSSFIRE™** and **AETHELGARD ACADEMY™** are trademarks (Filed - awaiting certification).

When contributing:
- ✅ You may contribute code improvements
- ✅ You may fork and modify (with attribution)
- ❌ You may NOT claim ownership of these trademarks
- ❌ You may NOT use the trademarks for your own projects without permission

## 📄 License

By contributing, you agree that your contributions will be licensed under **AGPL-3.0**.

This means:
- Your code remains open source
- Derivative works must also be AGPL-3.0
- Network use triggers source disclosure requirement
- Commercial use is allowed (with license compliance)

## ❓ Questions & Support

- **Issues:** [GitHub Issues](https://github.com/AsheeshSrivastava/obsidian-ai-assistant/issues)
- **Website:** [questandcrossfire.com](https://questandcrossfire.com)
- **Academy:** [academy.questandcrossfire.com](https://academy.questandcrossfire.com)

## 🙏 Acknowledgments

Contributions welcome from:
- **Developers** - Code improvements, bug fixes
- **Designers** - UI/UX enhancements
- **Writers** - Documentation improvements
- **Testers** - Bug reports, feature suggestions
- **Obsidian experts** - Knowledge base additions

---

**Built with Streamlit, OpenAI, and Hugging Face**

**Part of OutSkill AI Engineering Bootcamp 2025**

**© 2025 QUEST AND CROSSFIRE™. Licensed under AGPL-3.0.**
