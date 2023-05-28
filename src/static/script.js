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
    fetch('/confirm_task/' + taskId, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Handle the response if needed
    });
}

function cancelTask(taskId) {
    fetch('/cancel_task/' + taskId, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Handle the response if needed
    });
}
