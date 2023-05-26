import os
from dotenv import load_dotenv
import requests
from flask import Flask, jsonify

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

class TrelloComponent:
    def __init__(self, api_key, token, board_id):
        self.base_url = 'https://api.trello.com/1'
        self.api_key = api_key
        self.token = token
        self.board_id = board_id
            
    # New method to fetch the checklists of a Trello card
    def fetch_card_checklists(self, card_id):
        print(f'Fetching checklists for card {card_id}...')
        url = f"{self.base_url}/cards/{card_id}/checklists?key={self.api_key}&token={self.token}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError if the response was unsuccessful
            checklists = response.json()
            print(f'Fetched {len(checklists)} checklists.')
            return checklists
        except Exception as e:
            print(f"Failed to fetch card checklists: {e}")
            return None  # Return None or some default value
        
    # New method to update the description of a Trello card
    def update_card_description(self, card_id, description):
        print(f'Updating description for card {card_id}...')
        url = f"{self.base_url}/cards/{card_id}?key={self.api_key}&token={self.token}"
        payload = {'desc': description}
        try:
            response = requests.put(url, json=payload)
            response.raise_for_status()  # Raises an HTTPError if the response was unsuccessful
            card = response.json()
            print(f'Updated card {card["id"]} with new description.')
            return card
        except Exception as e:
            print(f"Failed to update card description: {e}")
            return None  # Return None or some default value

    # Fetch tasks from the Trello board
    def fetch_tasks(self):
        print('Fetching tasks from Trello...')
        url = f"{self.base_url}/boards/{self.board_id}/cards?key={self.api_key}&token={self.token}"
        response = requests.get(url)
        tasks = response.json()
        print(f'Fetched {len(tasks)} tasks.')
        return tasks

    # Create checklist items for subtasks in a given card
    def create_subtask_checklist_items(self, card_id, subtasks):
        checklist = self.create_subtask_checklist(card_id, 'Subtasks by AI Assisstant')
        for subtask in subtasks:
            self.create_checklist_item(checklist['id'], subtask)

    # Create a new checklist in a card
    def create_subtask_checklist(self, card_id, name):
        print(f'Creating checklist {name} for card {card_id}...')
        url = f"{self.base_url}/cards/{card_id}/checklists?key={self.api_key}&token={self.token}"
        payload = {'name': name}
        response = requests.post(url, json=payload)
        checklist = response.json()
        print(f'Created checklist {checklist["id"]}.')
        return checklist

    # Create a new checklist item in a checklist
    def create_checklist_item(self, checklist_id, item_name):
        print(f'Creating checklist item {item_name}...')
        url = f"{self.base_url}/checklists/{checklist_id}/checkItems?key={self.api_key}&token={self.token}"
        payload = {'name': item_name, 'checked': False}
        response = requests.post(url, json=payload)
        checklist_item = response.json()
        print(f'Created checklist item {checklist_item["id"]}.')
        return checklist_item

class AIComponent:
    def __init__(self, ai_api_key):
        self.api_key = ai_api_key
        self.chatgpt_base_url = 'https://api.openai.com/v1/chat/completions'

    def generate_description(self, task_description):
        print('Generating task description...')
        prompt = f"Task: {task_description}\n\n Description:"
        try:
            response = self.generate_chat_response(prompt)
            description = response['choices'][0]['message']['content']
            print(f'Generated description: {description}')
            return description
        except Exception as e:
            print(f"Failed to generate task description: {e}")
            return None  # Return None or some default value
    
    # Process a task description to generate subtasks
    def process_task(self, task_description):
        print('Processing task...')
        prompt = f"Task: {task_description}\n\nSubtasks:"
        response = self.generate_chat_response(prompt)
        processed_task = response['choices'][0]['message']['content']
        print(f'Processed task: {processed_task}')
        return processed_task

    # Generate subtasks from a processed task
    def generate_subtasks(self, processed_task):
        print('Generating subtasks...')
        subtasks = [subtask.strip() for subtask in processed_task.split('\n')]
        print(f'Generated {len(subtasks)} subtasks.')
        return subtasks

    # Generate a chat response using OpenAI's ChatGPT
    def generate_chat_response(self, prompt):
        print('Generating chat response...')
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}
        data = {
            'model': 'gpt-3.5-turbo',  # Specify the ChatGPT model version
            'messages': [
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': prompt}
            ]
        }
        response = requests.post(self.chatgpt_base_url, headers=headers, json=data)
        response.raise_for_status()
        print('Chat response generated.')
        return response.json()

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
    
    # # Process all tasks from Trello
    # def process_tasks(self):
    #     print('Processing all tasks...')
    #     tasks = self.trello_component.fetch_tasks()
    #     processed_tasks = []
    #     for task in tasks:
    #         print(f'Processing task: {task["name"]}')
    #         processed_task = self.ai_component.process_task(f"{task['name']}: {task['desc']}")
    #         subtasks = self.ai_component.generate_subtasks(processed_task)
    #         self.trello_component.create_subtask_checklist_items(task['id'], subtasks)
    #         processed_tasks.append({'original_task': task, 'processed_task': processed_task, 'subtasks': subtasks})
    #     print('Finished processing all tasks.')
    #     return processed_tasks

@app.route('/tasks', methods=['GET'])
def fetch_tasks():
    trello_component = TrelloComponent(api_key=os.getenv('TRELLO_API_KEY'), token=os.getenv('TRELLO_TOKEN'), board_id=os.getenv('TRELLO_BOARD_ID'))
    ai_component = AIComponent(ai_api_key=os.getenv('OPENAI_API_KEY'))
    integration_component = IntegrationComponent(trello_component, ai_component)
    tasks = integration_component.process_tasks()
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)
