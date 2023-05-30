from flask import request, jsonify

class IntegrationComponent:
    def __init__(self, trello_component, ai_component):
        self.trello_component = trello_component
        self.ai_component = ai_component

    def get_task(self, task_id):
        # Parse the AI-generated description and subtasks from the request body
        data = request.get_json()
        description = data.get('description')
        subtasks = data.get('subtasks')

        # trello_task = self.trello_component.get_card(task_id)

        # Update the Trello card with the AI-generated description
        updated_card = self.trello_component.update_card_description(task_id, description)

        if updated_card:
            # Create checklist items for the AI-generated subtasks
            self.trello_component.create_subtask_checklist_items(task_id, subtasks)

            # Return success message
            return jsonify({'message': 'Task confirmed and saved to Trello.'})
        else:
            # Return error message if card update failed
            return jsonify({'message': 'Failed to update Trello card.'}), 500
        
    def process_tasks(self, preview=True):
        print(f'Processing all tasks, Preview: {preview}')
        processed_tasks = []
        tasks = self.trello_component.fetch_tasks()

        for task in tasks:
            aiac = self.get_aiac(task)
            has_description = False
            has_checklist = False
            subtasks = []
            description = None

            if aiac['has_checklist']:
                subtasks = aiac['subtasks']            
                has_description = True
                description = task['desc']
            else:
                description = self.ai_component.generate_description(f"{task['name']}")
                if description:
                    subtasks = self.ai_component.generate_subtasks(task['name'], task['desc'])
                    if subtasks:
                        has_checklist = True
                        has_description = True

            if not preview:
                if has_description:
                    updated_card = self.trello_component.update_card_description(task['id'], description)
                    if updated_card:
                        processed_tasks.append({
                            'name': task['name'],
                            'preview': preview,
                            'has_description': has_description,
                            'has_checklist': has_checklist,
                            'status': 'Closed' if task['closed'] else 'Open',
                            'original_task': task,
                            'subtasks': subtasks,
                            'description': description,
                            'id': task['id']
                        })
                    else:
                        print(f"Failed to update the description for card {task['id']}")     
                else:
                    print(f"Failed to generate a description for task {task['name']}")

        print('Finished processing all tasks.')
        return processed_tasks


    def get_aiac(self, task):
        checklists = self.trello_component.fetch_card_checklists(task['id'])
        has_checklist = any(
            checklists is not None and checklist['name'] == 'Subtasks by AI Assistant'
            for checklist in checklists
        )
        subtasks = [item['name'] for item in checklists[0]['checkItems']] if has_checklist else []
        return {'checklists': checklists, 'has_checklist': has_checklist, 'subtasks': subtasks}
