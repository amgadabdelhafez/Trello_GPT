
class IntegrationComponent:
    def __init__(self, trello_component, ai_component):
        self.trello_component = trello_component
        self.ai_component = ai_component

    def process_tasks(self, preview=True):
        # go through all tasks
        # if new task, has no description or checklist items, then we get description and checklist from AI, then preview to user, but not save to trello yet
        # user preview, either save or discard
        # if save, then update the description and checklist items in trello
        # if discard, then do nothing and move on to the next task
        
        print(f'Processing all tasks, Preview: {preview}')

        tasks = self.trello_component.fetch_tasks()
        processed_tasks = []
        for task in tasks:
            print(f'Processing task: {task["name"]}')

            # Check if the card already has a description
            if task['desc']:
                description = task['desc']
                print(f'task has description: {description}')
                has_description = True
                # Check if the card already has a checklist by AI assistant
                checklists = self.trello_component.fetch_card_checklists(task['id'])
                if checklists is not None and any(checklist['name'] == 'Subtasks by AI Assisstant' for checklist in checklists):
                    print(f"Task '{task['name']}' already has a checklist by AI assistant. Loading...")
                    has_checklist = True
                    subtasks = []
                    for item in checklists[0]['checkItems']:
                        subtasks.append(item['name'])
     
            else:
                # if the card doesn't have a description, generate a description for the task using AI
                # if preview is true, then update the card's description
                description = self.ai_component.generate_description(f"{task['name']}")

                if description is None:
                    print(f"Failed to generate a description for task {task['name']}")
                    continue  # Skip this task and move on to the next one
                has_description = True

                subtasks = self.ai_component.generate_subtasks(task['name'], task['desc'])
                if subtasks is None:
                    print(f"Failed to generate subtasks for task {task['name']}")
                    continue  # Skip this task and move on to the next one
                has_checklist = True

                if not preview:
                    updated_card = self.trello_component.update_card_description(task['id'], description)
                    self.trello_component.create_subtask_checklist_items(task['id'], subtasks)

                    if updated_card is None:
                        print(f"Failed to update the description for card {task['id']}")
                        continue  # Skip this task and move on to the next one

                    return processed_tasks  # Return the processed tasks without saving to Trello

            processed_tasks.append({
                'name': task['name'],
                'preview': preview,
                'has_description': has_description,
                'has_checklist': has_checklist,
                'status': 'Closed' if task['closed'] else 'Open',
                'original_task': task,
                'subtasks': subtasks,
                'description': description
            })       
        print('Finished processing all tasks.')
        return processed_tasks
