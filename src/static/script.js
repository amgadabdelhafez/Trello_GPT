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

        const statusElement = document.createElement('p');
        statusElement.textContent = task.status;
        taskElement.appendChild(statusElement);

        const previewElement = document.createElement('p');
        if (task.preview) {
            const confirmButton = document.createElement('button');
            confirmButton.textContent = 'Confirm';
            confirmButton.addEventListener('click', function() {
                confirmTask(task.id);
            });
            previewElement.appendChild(confirmButton);

            const cancelButton = document.createElement('button');
            cancelButton.textContent = 'Cancel';
            cancelButton.addEventListener('click', function() {
                cancelTask(task.id);
            });
            previewElement.appendChild(cancelButton);
        } else {
            previewElement.textContent = 'N/A';
        }
        taskElement.appendChild(previewElement);

        const descriptionElement = document.createElement('p');
        descriptionElement.className = 'description';
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

        taskContainer.appendChild(taskElement);
    });
}

function confirmTask(taskId) {
    // Use the unique ID to select the button
    var button = document.getElementById('saveButton' + taskId);
    var description = button.getAttribute('data-description');
    var subtasks = button.getAttribute('data-subtasks');
    // Include the AI response in the POST request
    fetch('/confirm_task/' + taskId, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            description: description,
            subtasks: subtasks,
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Handle the response if needed
    });
}

function saveTask(taskId) {
    fetch('/confirm_task/' + taskId, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Handle the response if needed
    });
}

function discardTask(taskId) {
    fetch('/cancel_task/' + taskId, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Handle the response if needed
    });
}