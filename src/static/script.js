document.getElementById('process-tasks').addEventListener('click', function() {
    fetch('/tasks')
        .then(response => response.json())
        .then(tasks => {
            // TODO: display tasks
            console.log(tasks);
        });
});
