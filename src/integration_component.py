
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
                description = task['desc']
                # Check if the card already has a checklist by AI assistant
                checklists = self.trello_component.fetch_card_checklists(task['id'])
                if checklists is None:
                    print(f"Failed to fetch checklists for card {task['id']}")
                    # continue  # Skip this task and move on to the next one
                if any(checklist['name'] == 'Subtasks by AI Assisstant' for checklist in checklists):
                    print(f"Card {task['id']} already has a checklist by AI assistant. Skipping...")
                    subtasks = ''
                    for item in checklists[0]['checkItems']:
                        subtasks += f"{item['name']}"
                    # continue

                    processed_tasks.append({
                        'name': task['name'],
                        'status': 'Closed' if task['closed'] else 'Open',
                        'original_task': task,
                        'subtasks': subtasks,
                        'description': task['desc']
                    })
                            
                print(f"Card {task['id']} already has a description. Skipping...")
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
                'name': task['name'],
                'original_task': task,
                'processed_task': processed_task,
                'subtasks': subtasks,
                'description': description
            })
        
        print('Finished processing all tasks.')
        return processed_tasks
