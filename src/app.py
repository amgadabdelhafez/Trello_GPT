# This file contains the Flask application and the IntegrationComponent class.
# It imports and uses the TrelloComponent and AIComponent classes to process tasks when the /tasks endpoint is hit.

from flask import Flask, jsonify, render_template
from trello_component import TrelloComponent
from ai_component import AIComponent
import os

class IntegrationComponent:
    def __init__(self, trello_component, ai_component):
        self.trello_component = trello_component
        self.ai_component = ai_component

    def process_tasks(self):
        print('Processing all tasks...')
        tasks = self.trello_component.fetch_tasks()
        processed_tasks = []
        for task in tasks:
            print(f'Processing task: {task["name"]}')

            # Check if the card already has a description
            if task['desc']:
                print(f"Card {task['id']} already has a description. Skipping...")
                continue
            
            # Check if the card already has a checklist by AI assistant
            checklists = self.trello_component.fetch_card_checklists(task['id'])
            if checklists is None:
                print(f"Failed to fetch checklists for card {task['id']}")
                continue  # Skip this task and move on to the next one
            if any(checklist['name'] == 'Subtasks by AI Assisstant' for checklist in checklists):
                print(f"Card {task['id']} already has a checklist by AI assistant. Skipping...")
                continue

            # Generate a description for the task using AI, and update the card's description
            description = self.ai_component.generate_description(f"{task['name']}: {task['desc']}")
            if description is None:
                print(f"Failed to generate a description for task {task['name']}")
                continue  # Skip this task and move on to the next one
            updated_card = self.trello_component.update_card_description(task['id'], description)
            if updated_card is None:
                print(f"Failed to update the description for card {task['id']}")
                continue  # Skip this task and move on to the next one

            # Continue processing the task as before
            processed_task = self.ai_component.process_task(f"{task['name']}: {task['desc']}")
            subtasks = self.ai_component.generate_subtasks(processed_task)
            self.trello_component.create_subtask_checklist_items(task['id'], subtasks)
            
            processed_tasks.append({
                'original_task': task,
                'processed_task': processed_task,
                'subtasks': subtasks,
                'description': description
            })
        
        print('Finished processing all tasks.')
        return processed_tasks
    
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def fetch_tasks():
    trello_component = TrelloComponent(api_key=os.getenv('TRELLO_API_KEY'), token=os.getenv('TRELLO_TOKEN'), board_id=os.getenv('TRELLO_BOARD_ID'))
    ai_component = AIComponent(ai_api_key=os.getenv('OPENAI_API_KEY'))
    integration_component = IntegrationComponent(trello_component, ai_component)
    tasks = integration_component.process_tasks()
    # return jsonify(tasks)
    return render_template('tasks.html', tasks=tasks)

@app.route('/preview/<task_id>')
def preview(task_id):
    # TODO: fetch AI generated content from backend
    task = {}  # fetch the task using the task_id
    content = {}
    return render_template('preview.html', task=task, content=content)