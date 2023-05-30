document.querySelector('#process-tasks').addEventListener('click', async () => {
  try {
    const response = await fetch('/preview_tasks', { method: 'POST' });
    const { tasks } = await response.json();
    displayTasksPreview(tasks);
  } catch (err) {
    console.error(err);
  }
});

function displayTasksPreview(tasks) {
  const taskContainer = document.querySelector('#task-container');
  taskContainer.innerHTML = '';

  tasks.forEach(({ name, status, preview, id, description, subtasks }) => {
    const taskElement = document.createElement('div');
    taskElement.classList.add('task');

    const nameElement = document.createElement('p');
    nameElement.textContent = name;
    taskElement.appendChild(nameElement);

    const statusElement = document.createElement('p');
    statusElement.textContent = status;
    taskElement.appendChild(statusElement);

    const previewElement = document.createElement('p');
    if (preview) {
      const confirmButton = document.createElement('button');
      confirmButton.textContent = 'Confirm';
      confirmButton.addEventListener('click', () => {
        confirmTask(id);
      });
      previewElement.appendChild(confirmButton);

      const cancelButton = document.createElement('button');
      cancelButton.textContent = 'Cancel';
      cancelButton.addEventListener('click', () => {
        cancelTask(id);
      });
      previewElement.appendChild(cancelButton);
    } else {
      previewElement.textContent = 'N/A';
    }
    taskElement.appendChild(previewElement);

    const descriptionElement = document.createElement('p');
    descriptionElement.classList.add('description');
    descriptionElement.textContent = description;
    taskElement.appendChild(descriptionElement);

    const subtasksElement = document.createElement('p');
    subtasks.forEach(subtask => {
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
    var button = document.getElementById(`saveButton${taskId}`);
    var description = button.dataset.description;
    var subtasks = button.dataset.subtasks;
    // Include the AI response in the POST request
    fetch(`/confirm_task/${taskId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            description,
            subtasks,
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Handle the response if needed
    });
}

function saveTask(taskId) {
    fetch(`/confirm_task/${taskId}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Handle the response if needed
    });
}

function discardTask(taskId) {
    fetch(`/cancel_task/${taskId}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Handle the response if needed
    });
}
