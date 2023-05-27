# This file contains the Flask application and the IntegrationComponent class.
# It imports and uses the TrelloComponent and AIComponent classes to process tasks when the /tasks endpoint is hit.

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
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def fetch_tasks():
    tasks = integration_component.process_tasks()
    # return jsonify(tasks)
    return render_template('tasks.html', tasks=tasks)

@app.route('/preview/<task_id>')
def preview(task_id):
    # TODO: fetch AI generated content from backend
    task = {}  # fetch the task using the task_id
    content = {}
    return render_template('preview.html', task=task, content=content)