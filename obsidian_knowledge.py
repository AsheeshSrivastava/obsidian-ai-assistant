"""
===============================================================================
OBSIDIAN KNOWLEDGE BASE
===============================================================================
Purpose: This file stores information about Obsidian, its plugins, and common
         use cases. Think of it as a reference library or encyclopedia.

What is Obsidian?
    - A note-taking app that uses markdown files
    - Powerful because of plugins and linking between notes
    - Popular with students, researchers, and knowledge workers

Why do we need this file?
    - Gives our AI context about Obsidian before answering questions
    - Contains examples and common solutions
    - Makes responses more accurate and helpful

How it works:
    - We store information in Python dictionaries (like filing cabinets)
    - Each dictionary has a topic and related information
    - Our main app reads this to help answer user questions
===============================================================================
"""


# ============================================
# SECTION 1: SYSTEM CONTEXT
# ============================================
"""
This section defines WHO the AI assistant is and what it knows.
Think of it like giving someone a job description and training manual.

We use a single string (text) that will be sent to the AI to help it
understand its role.
"""

# This is the AI's "personality" and knowledge base
# It tells the AI what it's supposed to be good at
SYSTEM_CONTEXT = """You are an expert Obsidian assistant with deep knowledge of:

1. Obsidian core features
2. Popular plugins like DataView, Templater, and Calendar
3. Query languages (DataView queries, search syntax)
4. Workflow optimization and note organization
5. Markdown formatting in Obsidian

Your goal is to provide clear, actionable answers with code examples when relevant.
Always structure your responses with examples that users can copy and use immediately.
"""


# ============================================
# SECTION 2: DATAVIEW PLUGIN KNOWLEDGE
# ============================================
"""
DataView is one of Obsidian's most powerful plugins.
It lets you query your notes like a database.

Why this matters:
    - Users often struggle with DataView syntax
    - Having examples helps explain concepts
    - We can show correct syntax immediately

Structure:
    - Dictionary with question as key
    - Answer with explanation and code example as value
"""

# Dictionary storing common DataView questions and answers
# A dictionary is like a real dictionary: you look up a word (key) to get its definition (value)
DATAVIEW_EXAMPLES = {
    "basic_table": {
        "question": "How do I create a basic DataView table?",
        "answer": """To create a DataView table, you use the TABLE command followed by the fields you want to display.

**Basic Syntax:**
```dataview
TABLE field1, field2, field3
FROM "folder-name"
```

**Real Example - Show all project notes with their status and due date:**
```dataview
TABLE status, due-date
FROM "Projects"
WHERE status != null
SORT due-date ASC
```

**What each line does:**
- TABLE: tells DataView we want a table format
- status, due-date: columns to show
- FROM "Projects": only look in the Projects folder
- WHERE status != null: only show notes that have a status
- SORT due-date ASC: arrange by due date, earliest first (ASC = ascending)
""",
    },
    "list_query": {
        "question": "How do I create a list in DataView?",
        "answer": """Lists are simpler than tables. Use the LIST command to show file names or specific fields.

**Basic Syntax:**
```dataview
LIST
FROM "folder-name"
```

**Example 1 - List all notes with a specific tag:**
```dataview
LIST
FROM #important
```

**Example 2 - List notes with a custom field shown:**
```dataview
LIST status
FROM "Projects"
WHERE status = "in-progress"
```

**What this does:**
- Shows note names in a bullet list
- You can add one field after LIST to show extra info
- Great for quick overviews without table complexity
""",
    },
    "task_query": {
        "question": "How do I query tasks with DataView?",
        "answer": """DataView can find all tasks (checkboxes) across your vault.

**Basic Syntax:**
```dataview
TASK
FROM "folder-name"
WHERE !completed
```

**Example - Show all incomplete tasks from Projects folder:**
```dataview
TASK
FROM "Projects"
WHERE !completed
GROUP BY file.link
```

**What each part means:**
- TASK: special command for finding checkboxes (- [ ] items)
- !completed: the ! means "not", so this finds incomplete tasks
- GROUP BY file.link: organizes tasks by which file they're in

**Another Example - Tasks due this week:**
```dataview
TASK
WHERE due <= date(today) + dur(7 days) AND !completed
SORT due ASC
```

This finds tasks due within the next 7 days that aren't finished yet.
""",
    },
}


# ============================================
# SECTION 3: TEMPLATER PLUGIN KNOWLEDGE
# ============================================
"""
Templater is a plugin that creates dynamic templates.
Think of it like mail merge or form letters - one template,
many customized outputs.

Why users need help:
    - Templater uses special syntax that's different from normal markdown
    - Functions can be confusing for non-programmers
    - Examples make it much clearer
"""

# Dictionary of common Templater use cases
TEMPLATER_EXAMPLES = {
    "daily_note": {
        "question": "How do I create a daily note template?",
        "answer": """A daily note template automatically fills in today's date and structure.

**Template Code:**
```markdown
---
date: <% tp.date.now("YYYY-MM-DD") %>
day: <% tp.date.now("dddd") %>
---

# <% tp.date.now("YYYY-MM-DD") %> - <% tp.date.now("dddd") %>

## Tasks for Today
- [ ]

## Notes


## Daily Reflection
What went well:
What to improve:
```

**What each part does:**
- `<% %>`: these brackets tell Templater "run this code"
- `tp.date.now()`: gets today's date
- `"YYYY-MM-DD"`: format for the date (2025-10-29)
- `"dddd"`: format for day name (Wednesday)

When you use this template, it automatically inserts today's date everywhere you see the code!
""",
    },
    "meeting_notes": {
        "question": "How do I create a meeting notes template?",
        "answer": """A meeting template helps you quickly capture meeting info consistently.

**Template Code:**
```markdown
---
meeting-date: <% tp.date.now("YYYY-MM-DD") %>
attendees:
tags: meeting
---

# Meeting: <% tp.system.prompt("Meeting Title") %>

**Date:** <% tp.date.now("YYYY-MM-DD") %>
**Attendees:** <% tp.system.prompt("Who attended?") %>

## Agenda


## Discussion Notes


## Action Items
- [ ]


## Next Meeting
Date:
```

**What the special parts do:**
- `tp.system.prompt()`: pops up a box asking you to type something
- The text inside quotes is what the popup asks
- This makes each meeting note customized with the right title and attendees

**How to use it:**
1. Run the template
2. Type the meeting title when prompted
3. Type attendees when prompted
4. Template fills everything in automatically
""",
    },
}


# ============================================
# SECTION 4: GENERAL OBSIDIAN TIPS
# ============================================
"""
This section covers basic Obsidian features that aren't plugin-specific.
These are the fundamentals every user needs to know.
"""

# Dictionary of general Obsidian advice
GENERAL_OBSIDIAN_TIPS = {
    "linking": {
        "question": "How do I link notes together?",
        "answer": """Linking is Obsidian's superpower! It creates connections between your ideas.

**Basic Link (to another note):**
```markdown
[[Note Name]]
```
This creates a link to a note called "Note Name". If it doesn't exist, clicking creates it.

**Link with Custom Text:**
```markdown
[[Note Name|different text to display]]
```
This links to "Note Name" but shows "different text to display" in your note.

**Link to a Specific Heading:**
```markdown
[[Note Name#Heading Name]]
```
This jumps directly to a heading inside the linked note.

**Link to a Block:**
```markdown
[[Note Name#^block-id]]
```

**Why linking matters:**
- Helps you find related information later
- Creates a "web" of connected knowledge
- Obsidian's graph view shows these connections visually

**Pro tip:** Use [[]] freely. Don't worry about organizing perfectly at first.
The links themselves create organization over time.
""",
    },
    "tags": {
        "question": "How do I use tags effectively?",
        "answer": """Tags help you categorize and find notes quickly.

**Basic Tag:**
```markdown
#tag-name
```
Use hyphens for multi-word tags: #project-alpha not #project alpha

**Nested Tags (categories within categories):**
```markdown
#project/work/client-a
#project/personal/learning
```
The slashes create a hierarchy. Great for organizing by type and subtype.

**Tags in YAML Frontmatter (at top of note):**
```markdown
---
tags:
  - project
  - urgent
  - work
---
```

**When to use tags vs folders:**
- Folders: physical organization (Projects, Archive, Daily Notes)
- Tags: flexible categories (a note can have multiple tags)
- Links: relationships between ideas

**Example strategy:**
- Tag by status: #active, #completed, #archived
- Tag by type: #meeting, #idea, #reference
- Tag by area: #work, #personal, #learning
""",
    },
    "search": {
        "question": "How do I search effectively in Obsidian?",
        "answer": """Obsidian has powerful search that goes beyond simple text matching.

**Basic Search:**
Just type in the search box. It finds text anywhere in your vault.

**Search Operators:**

1. **Exact phrase:**
```
"exact phrase here"
```

2. **Multiple words (AND):**
```
word1 word2
```
Finds notes with BOTH words

3. **Alternative words (OR):**
```
word1 OR word2
```
Finds notes with EITHER word

4. **Exclude words:**
```
word1 -word2
```
Finds word1 but NOT word2

5. **Search in specific location:**
```
path:"Projects" meeting
```
Finds "meeting" only in Projects folder

6. **Search by tag:**
```
tag:#important
```

7. **Search in file names only:**
```
file:project
```

**Combine operators:**
```
path:"Work" tag:#meeting -cancelled "action items"
```
This finds notes in Work folder, tagged #meeting, without the word "cancelled",
containing the phrase "action items"

**Pro tip:** Save common searches by starring them (star icon in search pane)
""",
    },
}


# ============================================
# SECTION 5: COMMON PROBLEMS AND SOLUTIONS
# ============================================
"""
This section addresses issues users frequently encounter.
Having solutions ready makes the AI more helpful.
"""

# Dictionary of problems and their solutions
COMMON_PROBLEMS = {
    "sync_issues": {
        "problem": "Notes not syncing between devices",
        "solution": """Sync issues usually come from conflicts or connection problems.

**Troubleshooting Steps:**

1. **Check your sync method:**
   - Obsidian Sync (paid): Check Settings > Sync > View logs
   - iCloud: Can be slow, wait 5-10 minutes
   - Third-party (Syncthing, Dropbox): Check their app status

2. **Look for conflict files:**
   - Search for files with "conflict" in the name
   - These appear when the same file was edited on different devices
   - Manually merge the changes and delete conflict copies

3. **Force a sync:**
   - Close Obsidian on all devices
   - Open on one device, let it fully sync
   - Then open on other devices one at a time

4. **Check file permissions:**
   - Make sure your vault folder isn't read-only
   - On mobile, check if Obsidian has storage permissions

5. **Last resort - re-sync:**
   - Backup your vault folder
   - Remove vault from other devices
   - Re-add vault and let it download fresh

**Prevention:**
- Close Obsidian properly (don't force quit)
- Wait for sync to complete before closing
- Use Obsidian's built-in sync if possible (most reliable)
""",
    },
    "plugin_not_working": {
        "problem": "Plugin installed but not working",
        "solution": """Plugin issues often come from conflicts or incorrect settings.

**Troubleshooting Steps:**

1. **Check if plugin is enabled:**
   - Settings > Community plugins
   - Find your plugin in the list
   - Make sure the toggle is ON (not gray)

2. **Look for error messages:**
   - Open Developer Console: Ctrl+Shift+I (Windows) or Cmd+Option+I (Mac)
   - Click "Console" tab
   - Look for red error messages mentioning the plugin
   - Google the error message for solutions

3. **Check for conflicts:**
   - Disable all other plugins
   - Enable only the problem plugin
   - If it works now, re-enable others one by one to find the conflict

4. **Update everything:**
   - Settings > About > Check for updates
   - Update Obsidian itself
   - Settings > Community plugins > Check for updates

5. **Reinstall the plugin:**
   - Settings > Community plugins
   - Find the plugin and click X to uninstall
   - Browse community plugins and reinstall it
   - Reconfigure settings

6. **Check plugin requirements:**
   - Some plugins need specific folder structures
   - Some need API keys or external services
   - Read the plugin's documentation (usually on GitHub)

**Common specific issues:**
- DataView: Needs "Enable JavaScript Queries" turned ON in settings
- Templater: Needs a templates folder specified in settings
- Calendar: Needs daily notes format set correctly
""",
    },
}


# ============================================
# SECTION 6: HELPER FUNCTIONS
# ============================================
"""
These functions help our main app access the knowledge base.
Each function has one specific job.
"""


def get_dataview_example(topic):
    """
    Retrieves a specific DataView example from our knowledge base.

    Think of this like looking up a recipe in a cookbook.
    You give it the recipe name (topic), it gives you the recipe (example).

    Parameters:
        topic (string): Which example to retrieve (like "basic_table")

    Returns:
        dictionary: Contains the question and answer, or None if not found

    Example usage:
        example = get_dataview_example("basic_table")
        print(example["answer"])  # Prints the explanation and code
    """

    # Check if the topic exists in our dictionary
    # .get() is safer than [] because it returns None instead of crashing
    # if the topic doesn't exist
    if topic in DATAVIEW_EXAMPLES:
        return DATAVIEW_EXAMPLES[topic]
    else:
        return None


def get_templater_example(topic):
    """
    Retrieves a specific Templater example from our knowledge base.

    Parameters:
        topic (string): Which example to retrieve (like "daily_note")

    Returns:
        dictionary: Contains the question and answer, or None if not found

    Example usage:
        example = get_templater_example("daily_note")
        if example:
            print(example["answer"])
    """

    # Same pattern as get_dataview_example
    if topic in TEMPLATER_EXAMPLES:
        return TEMPLATER_EXAMPLES[topic]
    else:
        return None


def get_general_tip(topic):
    """
    Retrieves a general Obsidian tip from our knowledge base.

    Parameters:
        topic (string): Which tip to retrieve (like "linking")

    Returns:
        dictionary: Contains the question and answer, or None if not found

    Example usage:
        tip = get_general_tip("linking")
        if tip:
            print(tip["answer"])
    """

    if topic in GENERAL_OBSIDIAN_TIPS:
        return GENERAL_OBSIDIAN_TIPS[topic]
    else:
        return None


def get_all_examples_as_context():
    """
    Combines ALL our knowledge into one big text string.
    This gets sent to the AI so it has all the context it needs.

    Think of it like creating a study guide with all important info
    in one place before an exam.

    Parameters: None

    Returns:
        string: All knowledge combined into readable text

    Example usage:
        context = get_all_examples_as_context()
        # Send this context to the AI along with user's question
    """

    # Start with an empty string
    # We'll add to it piece by piece
    context = ""

    # Add the system context first
    context += "=== YOUR ROLE ===\n"
    context += SYSTEM_CONTEXT + "\n\n"

    # Add all DataView examples
    context += "=== DATAVIEW EXAMPLES ===\n"
    # Loop through each example in the dictionary
    for topic_name, example_data in DATAVIEW_EXAMPLES.items():
        context += f"\n{example_data['question']}\n"
        context += f"{example_data['answer']}\n"

    # Add all Templater examples
    context += "\n=== TEMPLATER EXAMPLES ===\n"
    for topic_name, example_data in TEMPLATER_EXAMPLES.items():
        context += f"\n{example_data['question']}\n"
        context += f"{example_data['answer']}\n"

    # Add general tips
    context += "\n=== GENERAL OBSIDIAN TIPS ===\n"
    for topic_name, tip_data in GENERAL_OBSIDIAN_TIPS.items():
        context += f"\n{tip_data['question']}\n"
        context += f"{tip_data['answer']}\n"

    # Add common problems
    context += "\n=== COMMON PROBLEMS & SOLUTIONS ===\n"
    for problem_name, problem_data in COMMON_PROBLEMS.items():
        context += f"\nProblem: {problem_data['problem']}\n"
        context += f"Solution: {problem_data['solution']}\n"

    # Return the complete context
    return context


def search_knowledge_base(search_term):
    """
    Searches through our entire knowledge base for a specific word or phrase.

    This is useful when the user asks about something and we want to find
    relevant examples to show them.

    Parameters:
        search_term (string): What to search for (like "dataview table")

    Returns:
        list: All examples that contain the search term

    Example usage:
        results = search_knowledge_base("table")
        for result in results:
            print(result["answer"])
    """

    # Make search term lowercase for case-insensitive search
    # This means "TABLE", "table", and "Table" all match
    search_term_lower = search_term.lower()

    # Create an empty list to store matching results
    matching_examples = []

    # Search through DataView examples
    for topic_name, example_data in DATAVIEW_EXAMPLES.items():
        # Check if search term appears in question or answer
        # We convert to lowercase for case-insensitive matching
        question_lower = example_data["question"].lower()
        answer_lower = example_data["answer"].lower()

        if search_term_lower in question_lower or search_term_lower in answer_lower:
            # Found a match! Add it to our results
            matching_examples.append({
                "type": "DataView",
                "question": example_data["question"],
                "answer": example_data["answer"],
            })

    # Search through Templater examples (same pattern)
    for topic_name, example_data in TEMPLATER_EXAMPLES.items():
        question_lower = example_data["question"].lower()
        answer_lower = example_data["answer"].lower()

        if search_term_lower in question_lower or search_term_lower in answer_lower:
            matching_examples.append({
                "type": "Templater",
                "question": example_data["question"],
                "answer": example_data["answer"],
            })

    # Search through general tips (same pattern)
    for topic_name, tip_data in GENERAL_OBSIDIAN_TIPS.items():
        question_lower = tip_data["question"].lower()
        answer_lower = tip_data["answer"].lower()

        if search_term_lower in question_lower or search_term_lower in answer_lower:
            matching_examples.append({
                "type": "General Tip",
                "question": tip_data["question"],
                "answer": tip_data["answer"],
            })

    # Return all matches we found (or empty list if none)
    return matching_examples


# ============================================
# TESTING CODE
# ============================================
"""
This section only runs when you run this file directly.
It's for testing that everything works correctly.

When you import this file from app.py, this code doesn't run.
"""

if __name__ == "__main__":
    # This only runs if you execute: python obsidian_knowledge.py

    print("Testing knowledge base functions...\n")

    # Test 1: Get a specific example
    print("Test 1: Getting DataView basic_table example")
    example = get_dataview_example("basic_table")
    if example:
        print(f"✓ Found: {example['question']}")
    else:
        print("✗ Failed to retrieve example")

    print("\n" + "="*50 + "\n")

    # Test 2: Search functionality
    print("Test 2: Searching for 'table'")
    results = search_knowledge_base("table")
    print(f"✓ Found {len(results)} matching examples")
    for result in results:
        print(f"  - [{result['type']}] {result['question']}")

    print("\n" + "="*50 + "\n")

    # Test 3: Get all context
    print("Test 3: Getting complete context")
    context = get_all_examples_as_context()
    # Show just the first 200 characters to verify it's working
    print(f"✓ Generated context ({len(context)} characters)")
    print(f"Preview: {context[:200]}...")

    print("\n✓ All tests completed!")
