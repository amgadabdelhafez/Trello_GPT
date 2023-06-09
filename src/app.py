import os
from flask import Flask, jsonify, render_template
from integration_component import IntegrationComponent
from trello_component import TrelloComponent
from ai_component import AIComponent

app = Flask(__name__)

api_key = os.getenv('TRELLO_API_KEY')
token = os.getenv('TRELLO_TOKEN')
board_id = os.getenv('TRELLO_BOARD_ID')
ai_api_key = os.getenv('OPENAI_API_KEY')

trello_component = TrelloComponent(api_key=api_key, token=token, board_id=board_id)
ai_component = AIComponent(ai_api_key=ai_api_key)
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
    task = integration_component.get_task(task_id)
    return jsonify({'message': 'Task confirmed.'})

@app.route('/cancel_task/<task_id>', methods=['POST'])
def cancel_task(task_id):
    # TODO: Handle the cancellation of the task (if needed)
    task = integration_component.get_task(task_id)
    return jsonify({'message': 'Task cancelled.'})

if __name__ == '__main__':
    app.run()
