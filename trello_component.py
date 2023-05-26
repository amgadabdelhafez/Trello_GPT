
# This file contains the TrelloComponent class, which is responsible for interacting with the Trello API.

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
