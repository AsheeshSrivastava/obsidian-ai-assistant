"""
===============================================================================
PROJECT MANAGER
===============================================================================
Purpose: This file manages multiple conversation "projects". A project is like
         a separate chat session where you can discuss a specific topic.

Why do we need projects?
    - You might be learning about DataView in one chat
    - And learning about Templater in another chat
    - Projects keep these conversations separate and organized

Real-world analogy:
    Think of projects like having multiple notebooks:
    - One notebook for math class
    - One notebook for history class
    - Each has its own notes, but they don't mix together

How it works:
    - Each project has a name and stores its messages
    - We can switch between projects
    - Each project remembers its conversation history
===============================================================================
"""


# ============================================
# SECTION 1: IMPORT WHAT WE NEED
# ============================================
"""
We need a couple of Python tools:
- datetime: To track when projects are created
- copy: To safely duplicate data without accidents
"""

from datetime import datetime  # For timestamps like "2025-10-29 14:30"
import copy  # For making safe copies of data


# ============================================
# SECTION 2: THE PROJECT CLASS
# ============================================
"""
A class is like a blueprint for creating objects.
Think of it like a cookie cutter: the class is the cutter,
and each project you create is a cookie.

We use a class because each project needs:
- Its own name
- Its own messages
- Its own creation date
- Its own methods to manage itself
"""


class ConversationProject:
    """
    This class represents a single project (conversation session).

    Each project is independent and stores:
    - Project name (like "Learning DataView")
    - List of all messages in this conversation
    - When it was created
    - Research mode setting (normal vs deep research)

    Example usage:
        my_project = ConversationProject("DataView Help")
        my_project.add_message("user", "How do I create a table?")
        my_project.add_message("assistant", "Here's how...")
    """

    def __init__(self, project_name):
        """
        This special function runs when you create a new project.
        It's called a "constructor" or "initializer".

        Think of it like setting up a new notebook:
        - Write the subject on the cover (project_name)
        - Start with blank pages (empty message list)
        - Write today's date on the first page

        Parameters:
            project_name (string): What to call this project

        Example:
            project = ConversationProject("My First Project")
        """

        # Store the project name
        # self.name means "this project's name"
        # The "self" refers to this specific project instance
        self.name = project_name

        # Create an empty list to store messages
        # Each message will be a dictionary with "role" and "content"
        self.messages = []

        # Record when this project was created
        # datetime.now() gets the current date and time
        # We format it nicely like "2025-10-29 14:30:45"
        self.created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Research mode setting
        # False = normal chat mode
        # True = deep research mode (more detailed responses)
        self.deep_research_mode = False

        # Track how many messages have been sent
        # Useful for showing project activity level
        self.message_count = 0

    def add_message(self, role, content):
        """
        Adds a new message to this project's conversation history.

        Think of it like writing a new entry in a dialogue:
        - Role is who's speaking: "user" or "assistant"
        - Content is what they said

        Parameters:
            role (string): Either "user" or "assistant"
            content (string): The actual message text

        Returns:
            None (just adds to the list)

        Example:
            project.add_message("user", "How do I link notes?")
            project.add_message("assistant", "Use [[note name]]")
        """

        # Create a dictionary for this message
        # A dictionary stores related information together
        # Like a labeled box: {"role": "user", "content": "Hello"}
        new_message = {
            "role": role,        # Who said it: "user" or "assistant"
            "content": content,  # What they said
        }

        # Add this message to our list of messages
        # .append() puts it at the end of the list
        self.messages.append(new_message)

        # Increase our message counter
        # This helps us track how active this project is
        self.message_count = self.message_count + 1

    def get_messages(self):
        """
        Returns all messages in this project.

        This is useful when you want to display the conversation
        or send it to the AI for context.

        Parameters: None

        Returns:
            list: All messages as dictionaries with "role" and "content"

        Example:
            all_messages = project.get_messages()
            for message in all_messages:
                print(f"{message['role']}: {message['content']}")
        """

        # Return a copy of messages, not the original
        # Why? If someone modifies the returned list, we don't want
        # it to accidentally change our stored messages
        # copy.deepcopy() creates a completely separate copy
        return copy.deepcopy(self.messages)

    def clear_messages(self):
        """
        Deletes all messages in this project (starts fresh).

        Think of it like erasing a whiteboard or starting a new page.
        The project still exists, but its conversation is cleared.

        Parameters: None
        Returns: None

        Example:
            project.clear_messages()  # Now project.messages is empty
        """

        # Reset messages to an empty list
        # This removes all previous messages
        self.messages = []

        # Reset message counter back to zero
        self.message_count = 0

    def get_summary(self):
        """
        Returns a brief summary of this project.

        Useful for displaying a list of projects with key info
        without showing all the messages.

        Parameters: None

        Returns:
            dictionary: Contains name, date, message count, mode

        Example:
            summary = project.get_summary()
            print(f"Project: {summary['name']}")
            print(f"Messages: {summary['message_count']}")
        """

        # Create a dictionary with summary information
        summary = {
            "name": self.name,
            "created_date": self.created_date,
            "message_count": self.message_count,
            "deep_research_mode": self.deep_research_mode,
        }

        return summary

    def toggle_research_mode(self):
        """
        Switches research mode on or off.

        Deep research mode tells the AI to give more detailed,
        thorough responses. Normal mode is quicker and more concise.

        Parameters: None
        Returns: None (just flips the setting)

        Example:
            project.toggle_research_mode()  # If False, becomes True
            project.toggle_research_mode()  # If True, becomes False
        """

        # The "not" operator flips True to False or False to True
        # If deep_research_mode is False, "not False" makes it True
        # If deep_research_mode is True, "not True" makes it False
        self.deep_research_mode = not self.deep_research_mode

    def get_last_message(self):
        """
        Returns the most recent message in this project.

        Useful for showing a preview of the conversation
        or checking what was last discussed.

        Parameters: None

        Returns:
            dictionary: The last message, or None if no messages exist

        Example:
            last = project.get_last_message()
            if last:
                print(f"Last message: {last['content']}")
        """

        # Check if there are any messages
        # len() tells us how many items are in the list
        if len(self.messages) > 0:
            # Return the last message
            # In Python, [-1] means "the last item in the list"
            return self.messages[-1]
        else:
            # No messages exist yet
            return None


# ============================================
# SECTION 3: THE PROJECT MANAGER CLASS
# ============================================
"""
The ProjectManager is like a librarian for all your projects.
It keeps track of multiple projects and helps you:
- Create new projects
- Switch between projects
- Delete projects you don't need
- Find a specific project
"""


class ProjectManager:
    """
    This class manages all conversation projects.

    Think of it as a filing cabinet where each drawer is a project.
    The ProjectManager helps you:
    - Create new drawers (projects)
    - Open a specific drawer (switch projects)
    - Remove old drawers (delete projects)
    - List all drawers (get all projects)

    Example usage:
        manager = ProjectManager()
        manager.create_project("DataView Learning")
        manager.create_project("Templater Help")
        manager.switch_to_project("DataView Learning")
    """

    def __init__(self):
        """
        Sets up the project manager when you first create it.

        This runs once when you start your app.
        It prepares an empty space to store projects.

        Parameters: None

        Example:
            manager = ProjectManager()  # Ready to manage projects!
        """

        # Create an empty dictionary to store all projects
        # Key = project name, Value = Project object
        # Example: {"DataView Help": <ConversationProject object>}
        self.projects = {}

        # Keep track of which project is currently active
        # At the start, no project is selected yet
        self.current_project_name = None

    def create_project(self, project_name):
        """
        Creates a new project with the given name.

        Like creating a new notebook and adding it to your shelf.

        Parameters:
            project_name (string): What to name the new project

        Returns:
            boolean: True if created successfully, False if name already exists

        Example:
            success = manager.create_project("Learning DataView")
            if success:
                print("Project created!")
        """

        # Check if a project with this name already exists
        # We don't want two projects with the same name (confusing!)
        if project_name in self.projects:
            # Name is taken, can't create
            return False

        # Create a new ConversationProject object
        new_project = ConversationProject(project_name)

        # Add it to our dictionary of projects
        # Now self.projects["Learning DataView"] = the new project
        self.projects[project_name] = new_project

        # If this is the first project, make it the current one
        # This is helpful for users - they don't have to switch manually
        if self.current_project_name is None:
            self.current_project_name = project_name

        # Success! Project was created
        return True

    def delete_project(self, project_name):
        """
        Removes a project permanently.

        Like throwing away a notebook. Be careful - you can't undo this!

        Parameters:
            project_name (string): Which project to delete

        Returns:
            boolean: True if deleted, False if project doesn't exist

        Example:
            manager.delete_project("Old Project")
        """

        # Check if the project exists
        if project_name not in self.projects:
            # Can't delete something that doesn't exist
            return False

        # Remove the project from our dictionary
        # del removes a key-value pair from the dictionary
        del self.projects[project_name]

        # If we just deleted the current project, we need to switch
        # to a different one (or None if no projects left)
        if self.current_project_name == project_name:
            # Get list of remaining project names
            remaining_projects = list(self.projects.keys())

            # If there are other projects, switch to the first one
            # If not, set current_project_name to None
            if len(remaining_projects) > 0:
                self.current_project_name = remaining_projects[0]
            else:
                self.current_project_name = None

        # Successfully deleted
        return True

    def switch_to_project(self, project_name):
        """
        Changes which project is currently active.

        Like closing one notebook and opening another.

        Parameters:
            project_name (string): Which project to switch to

        Returns:
            boolean: True if switched, False if project doesn't exist

        Example:
            manager.switch_to_project("DataView Learning")
        """

        # Check if the project exists
        if project_name not in self.projects:
            # Can't switch to something that doesn't exist
            return False

        # Update which project is current
        self.current_project_name = project_name

        # Successfully switched
        return True

    def get_current_project(self):
        """
        Returns the project that's currently active.

        Like asking "which notebook am I currently working in?"

        Parameters: None

        Returns:
            ConversationProject: The active project, or None if no project selected

        Example:
            current = manager.get_current_project()
            if current:
                print(f"Working in: {current.name}")
        """

        # Check if a project is selected
        if self.current_project_name is None:
            return None

        # Check if the current project name actually exists
        # (safety check in case something went wrong)
        if self.current_project_name not in self.projects:
            return None

        # Return the actual project object
        return self.projects[self.current_project_name]

    def get_all_project_names(self):
        """
        Returns a list of all project names.

        Useful for showing users what projects exist so they can choose one.

        Parameters: None

        Returns:
            list: Names of all projects

        Example:
            names = manager.get_all_project_names()
            for name in names:
                print(f"- {name}")
        """

        # Get all the keys from our projects dictionary
        # Keys are the project names
        # list() converts it to a regular list
        return list(self.projects.keys())

    def get_all_projects_summary(self):
        """
        Returns summary info for all projects.

        Like getting a table of contents showing all your notebooks
        with key info about each one.

        Parameters: None

        Returns:
            list: List of summary dictionaries for each project

        Example:
            summaries = manager.get_all_projects_summary()
            for summary in summaries:
                print(f"{summary['name']}: {summary['message_count']} messages")
        """

        # Create an empty list to store summaries
        summaries = []

        # Loop through each project in our dictionary
        # .values() gives us the actual project objects (not just names)
        for project in self.projects.values():
            # Get this project's summary
            summary = project.get_summary()

            # Add it to our list
            summaries.append(summary)

        # Return all summaries
        return summaries

    def project_exists(self, project_name):
        """
        Checks if a project with the given name exists.

        Simple helper function to avoid errors.

        Parameters:
            project_name (string): Name to check

        Returns:
            boolean: True if exists, False if not

        Example:
            if manager.project_exists("My Project"):
                print("Found it!")
        """

        # Check if the name is in our dictionary
        # "in" checks if a key exists
        return project_name in self.projects

    def get_project_count(self):
        """
        Returns how many projects exist.

        Parameters: None

        Returns:
            integer: Number of projects

        Example:
            count = manager.get_project_count()
            print(f"You have {count} projects")
        """

        # len() tells us how many items are in the dictionary
        return len(self.projects)


# ============================================
# SECTION 4: TESTING CODE
# ============================================
"""
This code only runs if you execute this file directly.
It's for testing that our classes work correctly.
"""

if __name__ == "__main__":
    # This only runs if you execute: python project_manager.py

    print("Testing ProjectManager...\n")

    # Test 1: Create manager and project
    print("Test 1: Creating manager and project")
    manager = ProjectManager()
    success = manager.create_project("Test Project")
    if success:
        print("✓ Project created successfully")
    else:
        print("✗ Failed to create project")

    print("\n" + "="*50 + "\n")

    # Test 2: Add messages to project
    print("Test 2: Adding messages")
    current = manager.get_current_project()
    if current:
        current.add_message("user", "Test question")
        current.add_message("assistant", "Test answer")
        print(f"✓ Added messages. Total: {current.message_count}")
    else:
        print("✗ Could not get current project")

    print("\n" + "="*50 + "\n")

    # Test 3: Create multiple projects
    print("Test 3: Creating multiple projects")
    manager.create_project("DataView Help")
    manager.create_project("Templater Learning")
    all_names = manager.get_all_project_names()
    print(f"✓ Total projects: {len(all_names)}")
    for name in all_names:
        print(f"  - {name}")

    print("\n" + "="*50 + "\n")

    # Test 4: Switch projects
    print("Test 4: Switching projects")
    switched = manager.switch_to_project("DataView Help")
    if switched:
        current = manager.get_current_project()
        print(f"✓ Switched to: {current.name}")
    else:
        print("✗ Failed to switch")

    print("\n" + "="*50 + "\n")

    # Test 5: Get summaries
    print("Test 5: Getting project summaries")
    summaries = manager.get_all_projects_summary()
    print(f"✓ Got {len(summaries)} summaries:")
    for summary in summaries:
        print(f"  - {summary['name']} ({summary['message_count']} messages)")

    print("\n✓ All tests completed!")
