from flask import Flask, jsonify, render_template
from trello_component import TrelloComponent
from ai_component import AIComponent
from integration_component import IntegrationComponent
import os

app = Flask(__name__)

trello_component = TrelloComponent(api_key=os.getenv('TRELLO_API_KEY'), token=os.getenv('TRELLO_TOKEN'), board_id=os.getenv('TRELLO_BOARD_ID'))
ai_component = AIComponent(ai_api_key=os.getenv('OPENAI_API_KEY'))
integration_component = IntegrationComponent(trello_component, ai_component)

@app.route('/')
def home():
    tasks = integration_component.process_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/preview/<task_id>')
def preview(task_id):
    # TODO: Fetch AI-generated content from backend based on task_id
    task = {}  # Fetch the task using the task_id
    content = {}  # Fetch AI-generated content for the task
    return render_template('preview.html', task=task, content=content)

@app.route('/preview_tasks', methods=['POST'])
def preview_tasks():
    tasks = integration_component.process_tasks(preview=True)
    return jsonify(tasks)

@app.route('/confirm_task/<task_id>', methods=['POST'])
def confirm_task(task_id):
    # TODO: Update the Trello card and create checklist items for the confirmed task
    # Retrieve the task details based on task_id
    task = integration_component.get_task(task_id)

    # Update the Trello card with the AI-generated description
    updated_card = trello_component.update_card_description(task['id'], task['description'])

    if updated_card:
        # Create checklist items for the AI-generated subtasks
        trello_component.create_subtask_checklist_items(task['id'], task['subtasks'])

        # Return success message
        return jsonify({'message': 'Task confirmed and saved to Trello.'})
    else:
        # Return error message if card update failed
        return jsonify({'message': 'Failed to update Trello card.'}), 500

@app.route('/cancel_task/<task_id>', methods=['POST'])
def cancel_task(task_id):
    # TODO: Handle the cancellation of the task (if needed)
    # Retrieve the task details based on task_id
    task = integration_component.get_task(task_id)

    # Return success message
    return jsonify({'message': 'Task cancelled.'})

if __name__ == '__main__':
    app.run()
