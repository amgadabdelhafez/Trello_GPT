# Trello Integration System

This repository contains an integration system that connects Trello and the OpenAI ChatGPT API. The system allows you to process tasks from Trello cards, generate subtasks using the ChatGPT API, and update Trello cards with subtask checklists and task progress.

## Requirements

1. Read tasks from Trello cards.
2. Process tasks using the OpenAI ChatGPT API.
3. Generate subtasks based on the processed tasks.
4. Create subtask checklists within the corresponding Trello cards.
5. Report the progress and results of task execution back to Trello.

## Components

The system consists of the following main components:

### TrelloComponent

- `fetch_tasks()`: Fetches tasks from Trello cards.
- `create_subtask_checklist(card_id, checklist_name)`: Creates a subtask checklist within a Trello card.
- `add_subtask_checklist_item(checklist_id, item_name)`: Adds a new item to a checklist.
- `update_card_description(card_id, description)`: Updates the description of a Trello card.

### AIComponent

- `process_task(task_description)`: Processes a task using the OpenAI ChatGPT API and returns the processed task.
- `generate_subtasks(processed_task)`: Generates subtasks based on the processed task and returns a list of subtask names.

### IntegrationComponent

- `process_tasks()`: Orchestrates the workflow by fetching tasks, processing them, generating subtasks, and updating Trello cards with the subtask checklists and task progress.

## Getting Started

To get started with the Trello integration system, follow these steps:

1. Install the required dependencies specified in the `requirements.txt` file.
2. Obtain your Trello API key and token.
3. Obtain your OpenAI API key.
4. Set up the necessary configuration variables in the code.
5. Run the integration system using the provided scripts or by executing the main entry point.

Please refer to the documentation and code comments for more detailed instructions on setting up and using the system.

## Usage

To use the Trello integration system, you can follow this example:

```python
from trello_component import TrelloComponent
from ai_component import AIComponent
from integration_component import IntegrationComponent

# Instantiate the TrelloComponent
trello_component = TrelloComponent(api_key='your_api_key', token='your_token')

# Instantiate the AIComponent
ai_component = AIComponent(api_key='your_openai_key')

# Instantiate the IntegrationComponent
integration_component = IntegrationComponent(
    trello_component=trello_component,
    ai_component=ai_component
)

# Process tasks and update Trello cards
integration_component.process_tasks()



