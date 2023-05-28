document.getElementById('process-tasks').addEventListener('click', function() {
    fetch('/preview_tasks', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(tasks => {
        // Display tasks and preview UI
        displayTasksPreview(tasks);
    });
});

function displayTasksPreview(tasks) {
    // Clear existing tasks (if any)
    const taskContainer = document.getElementById('task-container');
    taskContainer.innerHTML = '';

    // Loop through the tasks and create the preview UI
    tasks.forEach(task => {
        const taskElement = document.createElement('div');
        taskElement.className = 'task';

        const nameElement = document.createElement('p');
        nameElement.textContent = task.name;
        taskElement.appendChild(nameElement);

        const descriptionElement = document.createElement('p');
        descriptionElement.textContent = task.description;
        taskElement.appendChild(descriptionElement);

        const subtasksElement = document.createElement('p');
        task.subtasks.forEach(subtask => {
            const subtaskElement = document.createElement('span');
            subtaskElement.textContent = subtask;
            subtasksElement.appendChild(subtaskElement);

            const lineBreak = document.createElement('br');
            subtasksElement.appendChild(lineBreak);
        });
        taskElement.appendChild(subtasksElement);

        const confirmButton = document.createElement('button');
        confirmButton.textContent = 'Confirm';
        confirmButton.addEventListener('click', function() {
            confirmTask(task.id);
        });
        taskElement.appendChild(confirmButton);

        const cancelButton = document.createElement('button');
        cancelButton.textContent = 'Cancel';
        cancelButton.addEventListener('click', function() {
            cancelTask(task.id);
        });
        taskElement.appendChild(cancelButton);

        taskContainer.appendChild(taskElement);
    });
}

function confirmTask(taskId) {
    fetch('/confirm_task/' + taskId, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        // Handle confirmation response if needed
        console.log(data);
    });
}

function cancelTask(taskId) {
    fetch('/cancel_task/' + taskId, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        // Handle cancellation response if needed
        console.log(data);
    });
}
