# This file contains the AIComponent class, which is responsible for interacting with the OpenAI API.
import requests

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