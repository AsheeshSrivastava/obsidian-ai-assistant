"""
===============================================================================
OBSIDIAN AI LEARNING ASSISTANT - MAIN APPLICATION
===============================================================================
Part of Aethalgard Academy™ by Quest & Crossfire™

Purpose: This is the main application file that creates the web interface
         and connects everything together.

What this app does:
    1. Creates a chat interface where users ask Obsidian questions
    2. Sends questions to an AI along with Obsidian knowledge
    3. Manages multiple conversation projects
    4. Displays responses in a user-friendly way

How it works:
    - Streamlit creates the web interface (no HTML/CSS needed!)
    - We use session state to remember things between page refreshes
    - OpenAI or Hugging Face API provides the AI responses
    - Our knowledge base gives context to the AI

Copyright (c) 2025 Quest & Crossfire™
Licensed under GPL-3.0 - see LICENSE file for details
Quest & Crossfire™ and Aethalgard Academy™ are trademarks. Applications pending.

Author: Quest & Crossfire™ - Educational Python Project
Date: 2025-10-30
===============================================================================
"""


# ============================================
# SECTION 1: IMPORTING LIBRARIES
# ============================================
# Think of imports like gathering tools before starting a project.
# Each library (tool) has a specific purpose.

# Streamlit: Creates our web interface
# Instead of writing HTML/CSS, we use simple Python commands
import streamlit as st

# Requests: Helps us talk to web APIs (like calling the AI)
# Think of it like making a phone call to another service
import requests

# JSON: Helps us work with structured data
# JSON is like a filing system for organizing information
import json

# Time: Lets us add delays and timestamps
# Useful for preventing API rate limits
import time

# OpenAI: Official client for OpenAI API (ChatGPT)
# We use this to communicate with OpenAI's models
from openai import OpenAI

# Import our custom files
# These are the files we created earlier
from obsidian_knowledge import get_all_examples_as_context, search_knowledge_base
from project_manager import ProjectManager


# ============================================
# IMPORTANT: STREAMLIT PAGE CONFIG
# ============================================
# st.set_page_config() MUST be the VERY FIRST Streamlit command.
# It must come immediately after imports, before ANY other code.
#
# This is a strict Streamlit requirement. If ANY other Streamlit command
# runs before this (even accessing st.session_state), you'll get an error.

# Configure the Streamlit page
# This MUST be here, right after imports!
st.set_page_config(
    page_title="Obsidian AI Assistant | Aethalgard Academy™",  # Shows in browser tab
    page_icon="🧠",                       # Emoji shown in browser tab
    layout="wide",                         # Use full screen width (not centered)
)


# ============================================
# SECTION 2: CONFIGURATION & CONSTANTS
# ============================================
# Configuration means "settings we use throughout the app".
# We put them all at the top so they're easy to find and change.
#
# Think of it like a control panel where all the important
# switches and dials are in one place.

# Page title - appears in browser tab
PAGE_TITLE = "Obsidian AI Assistant"

# Page icon - small emoji in browser tab
PAGE_ICON = "🧠"

# API Provider Configuration
# Which AI service to use: "openai" or "huggingface"
# OpenAI: Fast, reliable, requires paid API key (but cheap - pennies per query)
# Hugging Face: Free, but slower and less reliable
DEFAULT_API_PROVIDER = "openai"

# OpenAI API settings
# OpenAI provides ChatGPT models - very fast and high quality
OPENAI_MODEL_NORMAL = "gpt-3.5-turbo"      # Fast and cheap ($0.0005/1K tokens)
OPENAI_MODEL_ADVANCED = "gpt-4o-mini"      # Better quality, still affordable

# Hugging Face API settings
# Hugging Face hosts AI models we can use for free
HF_API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"

# Alternative model for deep research (better but slower)
# GPT-2 is larger and gives more detailed responses
HF_DEEP_RESEARCH_URL = "https://api-inference.huggingface.co/models/gpt2"

# Maximum number of messages to send as context
# Why limit this? The AI can only handle so much text at once
# Newer messages are more relevant anyway
MAX_CONTEXT_MESSAGES = 10

# Timeout for API calls (in seconds)
# If the AI takes longer than this, we'll show an error
# This prevents users from waiting forever
API_TIMEOUT = 30

# ============================================
# DEEP RESEARCH METHODOLOGY
# ============================================
# This section defines how "Deep Research Mode" works.
# Like Gemini or Claude's deep research feature, we use
# a special methodology for more thorough analysis.

# Deep Research System Prompt
# This tells the AI how to behave in deep research mode
DEEP_RESEARCH_INSTRUCTIONS = """
You are operating in DEEP RESEARCH MODE. This means you should:

1. **THINK STEP-BY-STEP**: Break down complex questions into smaller parts
   - Identify what the user is really asking
   - Consider multiple aspects of the question
   - Build your answer methodically

2. **PROVIDE COMPREHENSIVE ANALYSIS**: Don't just give quick answers
   - Explain the "why" behind your recommendations
   - Discuss pros and cons of different approaches
   - Consider edge cases and potential issues

3. **USE MULTIPLE PERSPECTIVES**: Look at questions from different angles
   - Beginner perspective: Easy to understand explanations
   - Advanced perspective: Technical details and best practices
   - Practical perspective: Real-world examples and use cases

4. **BE THOROUGH**: Provide more detail than usual
   - Include code examples with detailed comments
   - Explain how things work under the hood
   - Suggest related topics to explore further

5. **VERIFY ACCURACY**: Be more careful with information
   - Double-check technical details
   - Provide context for when advice applies
   - Mention any limitations or caveats

This mode is for users who want deep understanding, not just quick answers.
"""

# Normal Mode System Prompt
# This is for regular, quick responses
NORMAL_MODE_INSTRUCTIONS = """
You are an expert Obsidian assistant. Provide clear, concise, and practical answers.
Focus on being helpful and accurate while keeping responses reasonably brief.
Include code examples when helpful, but keep explanations focused.
"""


# ============================================
# SECTION 3: STREAMLIT PAGE SETUP
# ============================================
# This function sets up the basic appearance of our page.
# Run this once at the start of the app.


def setup_page():
    """
    Adds the page header and description.

    This function creates the title and welcome message.
    Note: st.set_page_config() is now at the TOP of the file
    (module level) because it must be the first Streamlit command.

    Parameters: None
    Returns: None (just sets up the page header)

    Example usage:
        setup_page()  # Call once at app start
    """

    # Add a large title at the top
    # st.title() creates big, bold text
    st.title("🧠 Obsidian AI Learning Assistant")

    # Add a description below the title
    # st.markdown() lets us use formatting (bold, italic, etc.)
    st.markdown("""
    **Welcome to Aethalgard Academy™!** I'm here to help you master Obsidian, the powerful note-taking app.

    Ask me about:
    - 📊 **DataView** - Query your notes like a database
    - 📝 **Templater** - Create dynamic note templates
    - 🔗 **Linking & Organization** - Build your knowledge graph
    - 🔌 **Plugins** - Extend Obsidian's capabilities
    - 🔍 **Search & Queries** - Find exactly what you need

    **Tip:** Create different projects for different learning topics!

    ---
    *Part of [Aethalgard Academy™](https://academy.questandcrossfire.com) by [Quest & Crossfire™](https://questandcrossfire.com)*
    """)

    # Add a horizontal line to separate header from content
    # st.divider() draws a line across the page
    st.divider()


# ============================================
# SECTION 4: SESSION STATE INITIALIZATION
# ============================================
# Session state is Streamlit's way of remembering things.
#
# Why do we need this?
#     - Streamlit reruns your entire script every time you click something
#     - Without session state, we'd lose all our data each time
#     - Session state acts like the app's memory
#
# Think of it like sticky notes on your desk:
#     - Even if you leave and come back, the notes are still there
#     - Session state keeps data between page refreshes


def initialize_session_state():
    """
    Sets up session state variables if they don't exist yet.

    Session state is like the app's memory. We store:
    - The project manager (manages all conversations)
    - Whether we've run setup yet (to avoid repeating it)

    This function checks: "Do these variables exist?"
    If not, it creates them with default values.

    Parameters: None
    Returns: None (just sets up session state)

    Example usage:
        initialize_session_state()  # Call at app start
    """

    # Check if "project_manager" exists in session state
    # st.session_state is like a dictionary that persists
    # If "project_manager" is not already in it, create it
    if "project_manager" not in st.session_state:
        # Create a new ProjectManager object
        # This manages all our conversation projects
        st.session_state.project_manager = ProjectManager()

        # Create a default project so users can start immediately
        # No project name? No problem! We create one automatically
        st.session_state.project_manager.create_project("General Questions")

    # Check if we've run initial setup
    # This flag prevents us from running setup code multiple times
    if "setup_complete" not in st.session_state:
        st.session_state.setup_complete = True

    # ========================================
    # NEW: API Provider Selection
    # ========================================
    # Store which API provider the user wants to use (OpenAI or Hugging Face)
    #
    # WHY STORE THIS IN SESSION STATE?
    # - User can change it in the UI without editing config files
    # - Selection persists while the app is running
    # - Makes switching between providers easy
    #
    # Default: Try to read from secrets.toml, otherwise use OpenAI
    if "selected_api_provider" not in st.session_state:
        # Try to get default from secrets.toml
        try:
            st.session_state.selected_api_provider = st.secrets.get("API_PROVIDER", "openai").lower()
        except:
            # If secrets.toml doesn't exist or has issues, default to OpenAI
            st.session_state.selected_api_provider = "openai"

    # ========================================
    # NEW: OpenAI Model Selection
    # ========================================
    # Store which OpenAI model the user wants to use
    #
    # AVAILABLE MODELS:
    # - gpt-3.5-turbo: Fast, cheap, good for simple questions
    # - gpt-4o-mini: More advanced, better quality, slightly more expensive
    # - gpt-4: Most powerful, expensive, best for complex tasks
    #
    # Default: gpt-3.5-turbo (fast and affordable)
    if "selected_openai_model" not in st.session_state:
        st.session_state.selected_openai_model = "gpt-3.5-turbo"

    # ========================================
    # NEW: Hugging Face Model Selection
    # ========================================
    # Store which Hugging Face model the user wants to use
    #
    # AVAILABLE MODELS:
    # - microsoft/DialoGPT-medium: Good conversational AI, free
    # - gpt2: Classic language model, free
    # - meta-llama/Llama-2-7b-chat-hf: Advanced open-source model
    #
    # Default: microsoft/DialoGPT-medium (good balance)
    if "selected_hf_model" not in st.session_state:
        st.session_state.selected_hf_model = "microsoft/DialoGPT-medium"


# ============================================
# SECTION 5: API COMMUNICATION FUNCTIONS
# ============================================
# These functions handle talking to AI APIs (OpenAI or Hugging Face).
# Think of them like translators between our app and the AI.


def get_api_provider():
    """
    Determines which API provider to use (OpenAI or Hugging Face).

    ⚠️ NOTE: This function is now DEPRECATED (not used anymore).
    We now use session state instead: st.session_state.selected_api_provider
    This allows users to switch providers via the UI dropdown.

    LEGACY PURPOSE (kept for reference):
    This function used to read API_PROVIDER from secrets.toml.
    We keep it here in case we need to fall back to config file.

    Parameters: None

    Returns:
        string: "openai" or "huggingface"

    Example usage (OLD - don't use this anymore):
        provider = get_api_provider()
        if provider == "openai":
            # Use OpenAI
    """

    try:
        # Check if user specified a provider in secrets.toml
        provider = st.secrets.get("API_PROVIDER", DEFAULT_API_PROVIDER)
        return provider.lower()  # Convert to lowercase for consistency
    except:
        # If secrets.toml doesn't exist or has no API_PROVIDER, use default
        return DEFAULT_API_PROVIDER


def get_api_key(provider=None):
    """
    Retrieves the appropriate API key based on the provider.

    Secrets are sensitive information (like passwords) stored securely.
    We don't put API keys directly in code because:
    1. It's a security risk if code is shared
    2. Secrets are stored in a separate, secure file

    Parameters:
        provider (string): "openai" or "huggingface". If None, auto-detects.

    Returns:
        string: The API key, or None if not found

    Example usage:
        key = get_api_key("openai")
        if key:
            # Use the key
        else:
            # Show error to user
    """

    # If no provider specified, detect it
    if provider is None:
        provider = get_api_provider()

    # Try to get the API key from secrets
    # st.secrets is a special dictionary for sensitive info
    # We use try/except because if the key doesn't exist, it causes an error
    try:
        if provider == "openai":
            # Look for OPENAI_API_KEY in secrets.toml
            api_key = st.secrets["OPENAI_API_KEY"]
        else:
            # Look for HF_API_KEY in secrets.toml
            api_key = st.secrets["HF_API_KEY"]

        return api_key
    except:
        # If key not found, return None
        # The calling function will handle this error
        return None


def send_message_to_openai(user_message, conversation_history, use_deep_research=False):
    """
    Sends a message to OpenAI's ChatGPT API and gets a response.

    OpenAI's API is different from Hugging Face - it uses a chat format
    where you send a list of messages with roles (system, user, assistant).

    NEW: Deep Research Mode Support
    When use_deep_research=True, this function:
    1. Uses special methodology prompts (step-by-step analysis, multiple perspectives)
    2. Allows longer responses (2500 tokens vs 1000)
    3. Uses more focused temperature (0.5 vs 0.7)
    4. Model selection is handled by session state (auto-switched by toggle)

    Parameters:
        user_message (string): What the user just asked
        conversation_history (list): Previous messages in this chat
        use_deep_research (boolean): If True, use Deep Research methodology (like Gemini/Claude)

    Returns:
        dictionary: Contains "success" (True/False) and "response" (AI's answer or error message)

    Example usage:
        result = send_message_to_openai("How do I use DataView?", [], use_deep_research=True)
        if result["success"]:
            print(result["response"])  # Will be thorough, step-by-step analysis
    """

    # Get API key
    api_key = get_api_key("openai")

    # If no API key found, return error
    if api_key is None:
        return {
            "success": False,
            "response": "❌ OpenAI API key not found. Please set OPENAI_API_KEY in .streamlit/secrets.toml"
        }

    # ========================================
    # Choose which model to use
    # ========================================
    # NEW: Model selection now comes from session state (user's UI choice)
    # The model dropdown in the sidebar controls which model we use
    #
    # WHY USE SESSION STATE?
    # - User can switch models without changing code
    # - Selection persists during the session
    # - More flexible than hardcoded values
    #
    # OLD BEHAVIOR (kept for compatibility):
    # If use_deep_research is True, we used to switch to advanced model
    # Now we ignore this and use whatever the user selected in UI

    # Get the model from session state (user's selection in sidebar)
    model = st.session_state.selected_openai_model

    # Note: The model can also be auto-selected when Deep Research toggle is used
    # The Deep Research toggle (in sidebar) automatically switches to GPT-4 when enabled

    try:
        # Create OpenAI client
        client = OpenAI(api_key=api_key)

        # ========================================
        # Build System Prompt with Deep Research Methodology
        # ========================================
        # The system prompt tells the AI how to behave
        # We change this based on whether Deep Research is enabled

        # Get Obsidian knowledge context
        obsidian_context = get_all_examples_as_context()

        # Choose methodology based on Deep Research mode
        if use_deep_research:
            # DEEP RESEARCH MODE: Use comprehensive analysis methodology
            methodology_instructions = DEEP_RESEARCH_INSTRUCTIONS
        else:
            # NORMAL MODE: Use quick, concise responses
            methodology_instructions = NORMAL_MODE_INSTRUCTIONS

        # Build the complete system prompt
        # Format: Methodology Instructions + Obsidian Knowledge
        system_prompt = f"""{methodology_instructions}

=== OBSIDIAN KNOWLEDGE BASE ===
{obsidian_context}

Remember: Help users master Obsidian with clear explanations and practical examples."""

        # Build messages list for OpenAI
        # OpenAI expects messages in this format:
        # [{"role": "system", "content": "You are..."}, {"role": "user", "content": "Hello"}]
        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        # Add recent conversation history
        recent_messages = conversation_history[-MAX_CONTEXT_MESSAGES:]
        for message in recent_messages:
            messages.append({
                "role": message["role"],
                "content": message["content"]
            })

        # Add the new user message
        messages.append({
            "role": "user",
            "content": user_message
        })

        # ========================================
        # Configure API Parameters for Deep Research
        # ========================================
        # Different parameters based on mode for optimal results

        if use_deep_research:
            # DEEP RESEARCH MODE: Allow longer, more detailed responses
            temperature = 0.5      # More focused and careful (less creative)
            max_tokens = 2500      # Much longer responses for thorough analysis
        else:
            # NORMAL MODE: Quick, concise responses
            temperature = 0.7      # Balanced creativity and focus
            max_tokens = 1000      # Standard response length

        # Send request to OpenAI
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,   # How creative/focused the AI should be
            max_tokens=max_tokens,     # Maximum length of response
            timeout=API_TIMEOUT        # How long to wait before giving up
        )

        # Extract the AI's response
        ai_response = response.choices[0].message.content

        # Clean up and return
        ai_response = ai_response.strip()

        return {
            "success": True,
            "response": ai_response
        }

    # Catch timeout errors
    except Exception as error:
        error_message = str(error)

        # Check if it's an authentication error
        if "authentication" in error_message.lower() or "api key" in error_message.lower():
            return {
                "success": False,
                "response": "❌ Invalid OpenAI API key. Please check your OPENAI_API_KEY in secrets.toml"
            }

        # Check if it's a quota/billing error
        if "quota" in error_message.lower() or "billing" in error_message.lower():
            return {
                "success": False,
                "response": "❌ OpenAI API quota exceeded. Please check your billing at https://platform.openai.com/account/billing"
            }

        # General error
        return {
            "success": False,
            "response": f"❌ OpenAI API Error: {error_message}"
        }


def send_message_to_ai(user_message, conversation_history, use_deep_research=False):
    """
    Sends a message to the AI and gets a response.

    This function automatically detects which API to use (OpenAI or Hugging Face)
    based on your secrets.toml configuration.

    This is the heart of our app! It:
    1. Detects which API provider to use
    2. Routes the request to the appropriate function
    3. Returns the AI's response

    Think of it like a telephone operator:
    - You make a call (send a message)
    - They route it to the right person (OpenAI or Hugging Face)
    - You get your answer back

    Parameters:
        user_message (string): What the user just asked
        conversation_history (list): Previous messages in this chat
        use_deep_research (boolean): If True, use better model

    Returns:
        dictionary: Contains "success" (True/False) and "response" (AI's answer or error message)

    Example usage:
        result = send_message_to_ai("How do I use DataView?", [])
        if result["success"]:
            print(result["response"])
        else:
            print(f"Error: {result['response']}")
    """

    # ========================================
    # Detect which API provider to use
    # ========================================
    # NEW: Provider selection now comes from session state (user's UI choice)
    # The user selects provider in the sidebar dropdown
    #
    # OLD BEHAVIOR: We used to read from secrets.toml via get_api_provider()
    # NEW BEHAVIOR: User can switch providers in real-time via UI
    #
    # WHY THIS IS BETTER:
    # - No need to edit config files
    # - No need to restart the app
    # - User has direct control

    # Get provider from session state (user's selection in sidebar)
    provider = st.session_state.selected_api_provider

    # ========================================
    # Route to the appropriate API function
    # ========================================
    # Based on which provider is selected, call the correct function
    # Think of this like a phone operator directing your call

    if provider == "openai":
        # Use OpenAI ChatGPT
        return send_message_to_openai(user_message, conversation_history, use_deep_research)
    else:
        # Use Hugging Face (fallback for free alternative)
        return send_message_to_huggingface(user_message, conversation_history, use_deep_research)


def send_message_to_huggingface(user_message, conversation_history, use_deep_research=False):
    """
    Sends a message to Hugging Face API and gets a response.

    This is the original implementation for Hugging Face.
    Kept for backwards compatibility and as a free alternative.

    NEW: Deep Research Mode Support
    When use_deep_research=True, this function:
    1. Uses special methodology prompts (step-by-step analysis, multiple perspectives)
    2. Allows longer responses (1500 tokens vs 500)
    3. Uses more focused temperature (0.5 vs 0.7)
    4. Model selection is handled by session state (auto-switched by toggle)

    Parameters:
        user_message (string): What the user just asked
        conversation_history (list): Previous messages in this chat
        use_deep_research (boolean): If True, use Deep Research methodology (like Gemini/Claude)

    Returns:
        dictionary: Contains "success" (True/False) and "response" (AI's answer or error message)

    Example usage:
        result = send_message_to_huggingface("How do I use DataView?", [], use_deep_research=True)
        if result["success"]:
            print(result["response"])  # Will be thorough, step-by-step analysis
    """

    # Get API key
    api_key = get_api_key("huggingface")

    # If no API key found, return error
    if api_key is None:
        return {
            "success": False,
            "response": "❌ Hugging Face API key not found. Please set HF_API_KEY in .streamlit/secrets.toml"
        }

    # ========================================
    # Choose which AI model to use
    # ========================================
    # NEW: Model selection now comes from session state (user's UI choice)
    # The model dropdown in the sidebar controls which model we use
    #
    # WHY USE SESSION STATE?
    # - User can switch between different Hugging Face models
    # - No need to restart app or edit code
    # - More flexible than hardcoded URLs
    #
    # HOW HUGGING FACE URLS WORK:
    # Format: https://api-inference.huggingface.co/models/{model_name}
    # Example: https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium
    #
    # We build the URL dynamically based on selected model

    # Get the model ID from session state (user's selection in sidebar)
    selected_model = st.session_state.selected_hf_model

    # Build the API URL for this specific model
    api_url = f"https://api-inference.huggingface.co/models/{selected_model}"

    # Note: The model can also be auto-selected when Deep Research toggle is used
    # The Deep Research toggle (in sidebar) automatically switches to Llama 2 when enabled

    # Prepare the headers for our API request
    # Headers are like an envelope's return address - they identify us
    headers = {
        "Authorization": f"Bearer {api_key}",  # "Bearer" means we're carrying this key
        "Content-Type": "application/json",    # We're sending JSON formatted data
    }

    # ========================================
    # Build Prompt with Deep Research Methodology
    # ========================================
    # Hugging Face models don't have separate "system" messages
    # So we build everything into one prompt

    # Get our Obsidian knowledge base
    obsidian_context = get_all_examples_as_context()

    # Choose methodology based on Deep Research mode
    if use_deep_research:
        # DEEP RESEARCH MODE: Use comprehensive analysis methodology
        methodology_instructions = DEEP_RESEARCH_INSTRUCTIONS
    else:
        # NORMAL MODE: Use quick, concise responses
        methodology_instructions = NORMAL_MODE_INSTRUCTIONS

    # Build the full prompt for the AI
    # Format: Methodology + Knowledge Base + Conversation + New Question
    full_prompt = f"""{methodology_instructions}

=== OBSIDIAN KNOWLEDGE BASE ===
{obsidian_context}

=== CONVERSATION ===

"""

    # Add recent conversation history for context
    # We only include the last few messages (MAX_CONTEXT_MESSAGES)
    # Why? Too much context confuses the AI and costs more
    recent_messages = conversation_history[-MAX_CONTEXT_MESSAGES:]

    # Loop through recent messages and add them to prompt
    for message in recent_messages:
        role = message["role"]      # "user" or "assistant"
        content = message["content"]  # What was said

        # Format nicely for the AI
        if role == "user":
            full_prompt += f"User: {content}\n"
        else:
            full_prompt += f"Assistant: {content}\n"

    # Add the new user message
    full_prompt += f"User: {user_message}\n"
    full_prompt += "Assistant: "

    # ========================================
    # Configure API Parameters for Deep Research
    # ========================================
    # Different parameters based on mode for optimal results

    if use_deep_research:
        # DEEP RESEARCH MODE: Allow longer, more detailed responses
        max_length = 1500       # Much longer responses for thorough analysis
        temperature = 0.5       # More focused and careful (less creative)
    else:
        # NORMAL MODE: Quick, concise responses
        max_length = 500        # Standard response length
        temperature = 0.7       # Balanced creativity and focus

    # Prepare the data to send to the API
    # This is formatted as JSON (structured data)
    payload = {
        "inputs": full_prompt,  # The full prompt we built above
        "parameters": {
            "max_length": max_length,      # Maximum length of AI response
            "temperature": temperature,     # How creative/focused the AI should be
            "return_full_text": False,     # Only return new text, not full prompt
        }
    }

    # Try to send the request to the AI
    # We use try/except because network calls can fail
    try:
        # Send POST request to Hugging Face API
        # POST means "I'm sending you data"
        # timeout means "give up after this many seconds"
        response = requests.post(
            api_url,
            headers=headers,
            json=payload,
            timeout=API_TIMEOUT
        )

        # Check if request was successful
        # Status code 200 means "OK, everything worked"
        if response.status_code == 200:
            # Parse the JSON response
            # The AI sends back JSON formatted data
            response_data = response.json()

            # Extract the AI's actual text response
            # The structure is: [{"generated_text": "the response"}]
            # So we get the first item [0] and then the "generated_text" field
            ai_response = response_data[0]["generated_text"]

            # Clean up the response
            # Sometimes the AI adds extra text we don't want
            ai_response = ai_response.strip()

            # Return success!
            return {
                "success": True,
                "response": ai_response
            }

        # If status code is not 200, something went wrong
        else:
            # Return error with status code
            return {
                "success": False,
                "response": f"❌ API Error: Status code {response.status_code}. The AI service might be busy. Try again in a moment."
            }

    # Catch timeout errors
    # This happens if the AI takes too long to respond
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "response": f"❌ Request timed out after {API_TIMEOUT} seconds. The AI service might be overloaded. Please try again."
        }

    # Catch any other errors
    # This is a safety net for unexpected problems
    except Exception as error:
        # Convert error to string for display
        error_message = str(error)
        return {
            "success": False,
            "response": f"❌ Unexpected error: {error_message}"
        }


# ============================================
# SECTION 6: UI COMPONENT FUNCTIONS
# ============================================
# These functions create parts of the user interface.
# Each function builds a specific section of the page.


def render_sidebar():
    """
    Creates the sidebar with project management controls.

    The sidebar is the panel on the left side of the screen.
    It contains:
    - List of all projects
    - Button to create new project
    - Button to delete current project
    - Research mode toggle

    Parameters: None
    Returns: None (just draws the sidebar)

    Example usage:
        render_sidebar()  # Creates sidebar on the left
    """

    # Get the project manager from session state
    # This is where all our projects are stored
    manager = st.session_state.project_manager

    # Start the sidebar
    # Everything inside this "with" block appears in the sidebar
    with st.sidebar:
        # ========================================
        # NEW SECTION: AI Configuration
        # ========================================
        # This section lets users choose which AI service and model to use
        # It's at the top because it affects how the whole app works

        st.header("🤖 AI Configuration")

        # Add explanatory text about what this section does
        st.markdown("Choose which AI service and model to use for responses.")

        # ----------------------------------------
        # API Provider Selector
        # ----------------------------------------
        # This dropdown lets users choose between OpenAI and Hugging Face
        #
        # WHY TWO OPTIONS?
        # - OpenAI: Paid service, high quality, fast, requires API key
        # - Hugging Face: Free service, decent quality, sometimes slower
        #
        # st.selectbox creates a dropdown menu
        # The user clicks it and selects one option

        # Define the available provider options
        # This list determines what appears in the dropdown
        provider_options = ["OpenAI", "Hugging Face"]

        # Find which option matches the current session state
        # We need to convert "openai" -> "OpenAI" for display
        if st.session_state.selected_api_provider == "openai":
            current_provider_index = 0  # OpenAI is first in list
        else:
            current_provider_index = 1  # Hugging Face is second in list

        # Create the dropdown selector
        selected_provider = st.selectbox(
            "API Provider:",  # Label shown above dropdown
            options=provider_options,  # List of choices
            index=current_provider_index,  # Which one is selected by default
            help="OpenAI requires a paid API key. Hugging Face is free but may be slower."  # Tooltip on hover
        )

        # Update session state when user changes selection
        # Convert display name back to lowercase for internal use
        if selected_provider == "OpenAI":
            st.session_state.selected_api_provider = "openai"
        else:
            st.session_state.selected_api_provider = "huggingface"

        # ----------------------------------------
        # Model Selector (Changes Based on Provider)
        # ----------------------------------------
        # Show different models depending on which provider is selected
        #
        # WHY DIFFERENT MODELS?
        # Each AI service has multiple models with different capabilities:
        # - Faster models: Quick responses, good for simple questions
        # - Advanced models: Slower but better quality, good for complex questions

        # Check which provider is currently selected
        if st.session_state.selected_api_provider == "openai":
            # -------- OpenAI Model Selector --------

            # Define available OpenAI models
            # Format: Display Name -> Internal Model ID
            openai_models = {
                "GPT-3.5 Turbo (Fast & Affordable)": "gpt-3.5-turbo",
                "GPT-4o Mini (Better Quality)": "gpt-4o-mini",
                "GPT-4 (Most Powerful)": "gpt-4"
            }

            # Get list of display names
            openai_model_names = list(openai_models.keys())

            # Find which model is currently selected
            # We need to find the display name for the current model ID
            current_model_id = st.session_state.selected_openai_model
            current_model_index = 0  # Default to first option

            # Loop through to find matching index
            for i, display_name in enumerate(openai_model_names):
                if openai_models[display_name] == current_model_id:
                    current_model_index = i
                    break

            # Create the model selector dropdown
            selected_model_name = st.selectbox(
                "OpenAI Model:",  # Label
                options=openai_model_names,  # List of model display names
                index=current_model_index,  # Currently selected model
                help="GPT-3.5 is fast and cheap. GPT-4 is slower but gives better answers."  # Tooltip
            )

            # Update session state with selected model ID
            st.session_state.selected_openai_model = openai_models[selected_model_name]

        else:
            # -------- Hugging Face Model Selector --------

            # Define available Hugging Face models
            # Format: Display Name -> Model URL/ID
            hf_models = {
                "DialoGPT Medium (Conversational)": "microsoft/DialoGPT-medium",
                "GPT-2 (Classic)": "gpt2",
                "Llama 2 Chat (Advanced)": "meta-llama/Llama-2-7b-chat-hf"
            }

            # Get list of display names
            hf_model_names = list(hf_models.keys())

            # Find which model is currently selected
            current_model_id = st.session_state.selected_hf_model
            current_model_index = 0  # Default to first option

            # Loop through to find matching index
            for i, display_name in enumerate(hf_model_names):
                if hf_models[display_name] == current_model_id:
                    current_model_index = i
                    break

            # Create the model selector dropdown
            selected_model_name = st.selectbox(
                "Hugging Face Model:",  # Label
                options=hf_model_names,  # List of model display names
                index=current_model_index,  # Currently selected model
                help="DialoGPT is good for conversation. Llama 2 is more advanced but slower."  # Tooltip
            )

            # Update session state with selected model ID
            st.session_state.selected_hf_model = hf_models[selected_model_name]

        # Add a divider to separate AI config from project management
        st.divider()

        # ========================================
        # END OF NEW SECTION
        # ========================================

        # Add a header
        st.header("📁 Projects")

        # Add some explanatory text
        st.markdown("Create separate projects for different topics or learning goals.")

        # Add a divider line
        st.divider()

        # Section for creating new project
        st.subheader("Create New Project")

        # Text input for project name
        # The user types a name here
        new_project_name = st.text_input(
            "Project Name:",
            placeholder="e.g., Learning DataView",  # Example text shown in box
            help="Give your project a descriptive name"  # Hover tooltip
        )

        # Button to create the project
        # st.button returns True when clicked
        if st.button("➕ Create Project", use_container_width=True):
            # Check if user entered a name
            if new_project_name and new_project_name.strip() != "":
                # Try to create the project
                success = manager.create_project(new_project_name.strip())

                if success:
                    # Show success message
                    # st.success shows a green success box
                    st.success(f"✓ Created project: {new_project_name}")
                    # Rerun the app to refresh the project list
                    # st.rerun() restarts the script from the top
                    time.sleep(0.5)  # Brief pause so user sees success message
                    st.rerun()
                else:
                    # Project name already exists
                    # st.error shows a red error box
                    st.error("❌ A project with this name already exists")
            else:
                # User didn't enter a name
                st.warning("⚠️ Please enter a project name")

        st.divider()

        # Section for switching between projects
        st.subheader("Your Projects")

        # Get list of all project names
        all_project_names = manager.get_all_project_names()

        # Get current project name
        current_project_name = manager.current_project_name

        # Check if any projects exist
        if len(all_project_names) > 0:
            # Loop through each project and create a button
            for project_name in all_project_names:
                # Check if this is the current project
                is_current = (project_name == current_project_name)

                # Create a button for this project
                # If it's current, show with a ► symbol
                if is_current:
                    button_label = f"► {project_name}"
                else:
                    button_label = f"   {project_name}"

                # Create the button
                # type="primary" makes current project blue
                button_type = "primary" if is_current else "secondary"

                if st.button(
                    button_label,
                    key=f"project_btn_{project_name}",  # Unique key for each button
                    use_container_width=True,
                    type=button_type
                ):
                    # User clicked this project button
                    # Switch to this project
                    manager.switch_to_project(project_name)
                    # Rerun to refresh the display
                    st.rerun()

        else:
            # No projects exist (shouldn't happen due to default project)
            st.info("No projects yet. Create one above!")

        st.divider()

        # Section for project actions
        st.subheader("Project Actions")

        # Get current project
        current_project = manager.get_current_project()

        if current_project:
            # Show project info
            st.markdown(f"**Current:** {current_project.name}")
            st.markdown(f"**Messages:** {current_project.message_count}")

            # ========================================
            # Deep Research Mode Toggle
            # ========================================
            # This is like Gemini or Claude's "Deep Research" feature
            #
            # WHAT IT DOES:
            # 1. Automatically uses the STRONGEST model available
            # 2. Applies special methodology:
            #    - Step-by-step reasoning
            #    - Multiple perspectives
            #    - More thorough analysis
            #    - Longer, more detailed responses
            #
            # WHY TWO APPROACHES?
            # - Normal mode: Quick answers, good for simple questions
            # - Deep Research: Comprehensive analysis, good for complex topics

            # Create the toggle switch
            research_mode = st.toggle(
                "🔬 Deep Research Mode",
                value=current_project.deep_research_mode,  # Current state
                help="Uses the strongest AI model and deep analysis methodology for comprehensive, step-by-step responses"
            )

            # If toggle state changed, update the project
            if research_mode != current_project.deep_research_mode:
                current_project.toggle_research_mode()

                # ========================================
                # AUTO-SELECT STRONGEST MODEL
                # ========================================
                # When Deep Research is enabled, automatically switch to the best model

                if research_mode:
                    # Deep Research is now ON - use strongest model
                    if st.session_state.selected_api_provider == "openai":
                        # For OpenAI: GPT-4 is the strongest
                        st.session_state.selected_openai_model = "gpt-4"
                    else:
                        # For Hugging Face: Llama 2 Chat is the most advanced
                        st.session_state.selected_hf_model = "meta-llama/Llama-2-7b-chat-hf"
                else:
                    # Deep Research is now OFF - switch to fast/affordable model
                    if st.session_state.selected_api_provider == "openai":
                        # For OpenAI: GPT-3.5 Turbo is fast and cheap
                        st.session_state.selected_openai_model = "gpt-3.5-turbo"
                    else:
                        # For Hugging Face: DialoGPT is good and fast
                        st.session_state.selected_hf_model = "microsoft/DialoGPT-medium"

                st.rerun()

            # Button to clear conversation
            if st.button("🗑️ Clear Conversation", use_container_width=True):
                current_project.clear_messages()
                st.success("✓ Conversation cleared")
                time.sleep(0.5)
                st.rerun()

            # Button to delete project
            # Only show if more than one project exists
            if len(all_project_names) > 1:
                if st.button("❌ Delete Project", use_container_width=True, type="secondary"):
                    # Delete current project
                    manager.delete_project(current_project.name)
                    st.success(f"✓ Deleted project: {current_project.name}")
                    time.sleep(0.5)
                    st.rerun()
            else:
                # Can't delete the only project
                st.info("Create another project before deleting this one")


def render_chat_interface():
    """
    Creates the main chat interface where conversation happens.

    This is the central part of the app where:
    - Previous messages are displayed
    - User types new messages
    - AI responses appear

    Parameters: None
    Returns: None (just draws the interface)

    Example usage:
        render_chat_interface()  # Creates chat area
    """

    # Get project manager and current project
    manager = st.session_state.project_manager
    current_project = manager.get_current_project()

    # If no project selected, show error
    # (This shouldn't happen due to default project)
    if current_project is None:
        st.error("❌ No project selected. Create a project in the sidebar.")
        return

    # Display project name as header
    st.header(f"💬 {current_project.name}")

    # ========================================
    # Deep Research Mode Indicator
    # ========================================
    # Show a prominent indicator when Deep Research is active
    # This helps users understand they'll get more thorough responses

    if current_project.deep_research_mode:
        # Get current provider and model to show in indicator
        current_provider = st.session_state.selected_api_provider
        current_model = ""

        if current_provider == "openai":
            current_model = st.session_state.selected_openai_model
        else:
            # For Hugging Face, show short model name
            hf_model = st.session_state.selected_hf_model
            # Extract just the model name from the full path
            if "/" in hf_model:
                current_model = hf_model.split("/")[-1]
            else:
                current_model = hf_model

        # Display the indicator with details
        st.info(f"""
        🔬 **Deep Research Mode is ACTIVE**

        **What this means:**
        - Using the strongest model: `{current_model}`
        - Step-by-step analysis methodology
        - Multiple perspectives considered
        - More thorough and detailed responses
        - Longer response length allowed

        *Like Gemini or Claude's deep research feature*
        """)

    st.divider()

    # Create a container for displaying messages
    # st.container() groups elements together
    chat_container = st.container()

    # Display all messages in the conversation
    with chat_container:
        # Get all messages from current project
        messages = current_project.get_messages()

        # If no messages yet, show welcome message
        if len(messages) == 0:
            st.markdown("""
            👋 **Get started by asking a question!**

            Try asking:
            - "How do I create a DataView table?"
            - "Show me a daily note template"
            - "How do I link notes together?"
            - "What's the best way to organize my vault?"
            """)
        else:
            # Loop through messages and display each one
            for message in messages:
                role = message["role"]
                content = message["content"]

                # Display based on role
                if role == "user":
                    # User messages: show with chat_message
                    # "user" avatar shows a person icon
                    with st.chat_message("user"):
                        st.markdown(content)
                else:
                    # Assistant messages: show with chat_message
                    # "assistant" avatar shows a robot icon
                    with st.chat_message("assistant"):
                        st.markdown(content)

    # Add divider before input
    st.divider()

    # Create input area for new messages
    # st.chat_input creates a text box at the bottom
    user_input = st.chat_input(
        "Ask me anything about Obsidian...",
        key="chat_input"
    )

    # If user submitted a message (pressed Enter or clicked send)
    if user_input:
        # User typed something!

        # Add user message to project
        current_project.add_message("user", user_input)

        # Display user message immediately
        with st.chat_message("user"):
            st.markdown(user_input)

        # Show "thinking" indicator while waiting for AI
        with st.chat_message("assistant"):
            # Create empty placeholder for AI response
            message_placeholder = st.empty()

            # Show loading message
            message_placeholder.markdown("🤔 Thinking...")

            # Get conversation history
            conversation_history = current_project.get_messages()

            # Send message to AI
            result = send_message_to_ai(
                user_input,
                conversation_history,
                use_deep_research=current_project.deep_research_mode
            )

            # Check if successful
            if result["success"]:
                # Got a response! Display it
                ai_response = result["response"]

                # Update placeholder with actual response
                message_placeholder.markdown(ai_response)

                # Add to project history
                current_project.add_message("assistant", ai_response)

            else:
                # Error occurred
                error_message = result["response"]

                # Display error
                message_placeholder.markdown(error_message)

                # Still add to history so user can see what went wrong
                current_project.add_message("assistant", error_message)


def render_help_section():
    """
    Creates an expandable help section with usage tips.

    This is a collapsible section at the bottom that users
    can open if they need help using the app.

    Parameters: None
    Returns: None (just draws the help section)

    Example usage:
        render_help_section()  # Adds help at bottom
    """

    # Create an expander (collapsible section)
    # st.expander creates a section that starts collapsed
    with st.expander("❓ Help & Tips"):
        st.markdown("""
        ### How to Use This App

        **Projects:**
        - Create separate projects for different learning topics
        - Each project maintains its own conversation history
        - Switch between projects using the sidebar

        **Deep Research Mode:**
        - Toggle this for more detailed, thorough responses
        - Uses a more powerful AI model
        - Responses may take slightly longer

        **Tips for Best Results:**
        - Be specific in your questions
        - Ask for code examples when you need them
        - If an answer isn't clear, ask for clarification
        - Use projects to organize different areas of learning

        **Example Questions:**
        - "How do I create a DataView table showing all notes with a specific tag?"
        - "Give me a Templater template for meeting notes"
        - "What's the difference between tags and links?"
        - "How can I search for notes modified in the last week?"

        ### Troubleshooting

        **If you get an error:**
        1. Check that your API key is set in `.streamlit/secrets.toml`
        2. Try again - sometimes the AI service is busy
        3. Make sure you have internet connection
        4. Check the error message for specific guidance

        **If responses are slow:**
        - The free Hugging Face API can be slow during busy times
        - Deep Research Mode is slower but more thorough
        - Consider shorter questions for faster responses
        """)


# ============================================
# SECTION 7: MAIN APPLICATION
# ============================================
# This is where we put everything together.
# The main() function orchestrates the entire app.


def main():
    """
    Main function that runs the entire application.

    This is the conductor of the orchestra - it calls
    all the other functions in the right order to
    create the complete app.

    Think of it as a recipe that says:
    1. First, set up the page
    2. Then, initialize data storage
    3. Then, draw the sidebar
    4. Then, draw the chat interface
    5. Finally, add the help section

    Parameters: None
    Returns: None

    Example usage:
        main()  # Runs the entire app
    """

    # Step 1: Set up the page appearance
    setup_page()

    # Step 2: Initialize session state (app memory)
    initialize_session_state()

    # Step 3: Draw the sidebar with project controls
    render_sidebar()

    # Step 4: Draw the main chat interface
    render_chat_interface()

    # Step 5: Add help section at the bottom
    render_help_section()


# ============================================
# SECTION 8: RUN THE APP
# ============================================
# This code runs when you execute: streamlit run app.py
#
# The if __name__ == "__main__" check ensures this only
# runs when we execute this file directly, not when it's
# imported by another file.

if __name__ == "__main__":
    # Run the main application
    main()
