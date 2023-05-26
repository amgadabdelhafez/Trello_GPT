# Trello Integration System

This repository contains an integration system that connects Trello and the OpenAI ChatGPT API. The system processes tasks from Trello cards, generates subtasks using the ChatGPT API, and updates Trello cards with subtask checklists and task progress.

## Features

The Trello Integration System is designed to:

1. Fetch tasks from Trello cards.
2. Process tasks using the OpenAI ChatGPT API.
3. Generate subtasks based on the processed tasks.
4. Create subtask checklists within the corresponding Trello cards.
5. Report the progress and results of task execution back to Trello.

## Components

The system consists of three main components:

### TrelloComponent

This component interacts with the Trello API. It includes methods to fetch tasks from Trello cards, create a subtask checklist within a Trello card, add a new item to a checklist, and update the description of a Trello card.

### AIComponent

This component interacts with the OpenAI ChatGPT API. It includes methods to process a task and return the processed task, and generate subtasks based on the processed task and return a list of subtask names.

### IntegrationComponent

This component orchestrates the workflow of the application. It fetches tasks, processes them, generates subtasks, and updates Trello cards with the subtask checklists and task progress.

## File Structure

The application is organized into several files:

1. **trello_component.py**: Contains the `TrelloComponent` class.
2. **ai_component.py**: Contains the `AIComponent` class.
3. **app.py**: Contains the Flask application and the `IntegrationComponent` class.
4. **main.py**: The entry point of the application.

## Getting Started

To get started with the Trello integration system, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies specified in the `requirements.txt` file.
3. Obtain your Trello API key and token.
4. Obtain your OpenAI API key.
5. Set up the necessary configuration variables in the code.
6. Run the integration system by executing the `main.py` file.

## Usage

Here's an example of how to use the Trello integration system:

```python
from trello_component import TrelloComponent
from ai_component import AIComponent
from app import IntegrationComponent

# Instantiate the TrelloComponent
trello_component = TrelloComponent(api_key='your_api_key', token='your_token', board_id='your_board_id')

# Instantiate the AIComponent
ai_component = AIComponent(api_key='your_openai_key')

# Instantiate the IntegrationComponent
integration_component = IntegrationComponent(trello_component, ai_component)

# Process tasks and update Trello cards
integration_component.process_tasks()
