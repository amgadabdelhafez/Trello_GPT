# Trello_GPT Roadmap

This roadmap outlines potential future features for the Trello_GPT project. These features aim to enhance the AI's ability to assist a single user in managing personal to-dos.

## Near-Term Objectives
### Task Status Updates
Improve the AI's understanding of the user's workflow by updating it about task and subtask completions.

### Task Prioritization
Implement a feature where the AI assists in prioritizing tasks based on urgency, importance, or due dates.

### Reminder Notifications
Enhance the system to send the user reminder notifications about upcoming tasks or subtasks. These could be integrated into Trello notifications or through the user's preferred communication channel.

## Mid-Term Objectives
### Rescheduling Assistance
Allow the AI to suggest rescheduling of tasks and subtasks based on the user's progress and upcoming tasks, to optimize time management.

### Daily/Weekly Task Summaries
Design the AI to generate daily or weekly task summaries. These summaries would provide an overview of completed tasks, upcoming tasks, and task management suggestions.

## Long-Term Objectives
### Contextual Task Generation
Based on the user's past tasks and subtasks, have the AI suggest new tasks that the user might want to consider.

Note: The order and timing of these features will depend on user feedback and development capacity. We welcome contributions from the community to help us achieve these objectives!

Creating a front-end for this system would be a great idea. This would allow users to visualize and interact with the system and its outputs. A well-designed user interface can greatly enhance the user experience. Here are some steps to design a front-end for this system:

Define the User Interface Components: You'll need to identify what elements the user needs to interact with. These could include:

A display area for the AI-generated content (subtasks and card descriptions)
Buttons or controls to accept, reject or edit the AI-generated content before adding it to Trello
Notifications or alerts for the status of the process (fetching tasks, processing tasks, updating tasks)
A log area to track the history of actions and changes
Design the Layout: Once you have identified the components, you'll need to decide on a layout for your interface. You could use a web design tool or sketch out your design. The layout should be intuitive and user-friendly.

Choose a Front-End Framework: Depending on your preferences and the complexity of your interface, you might want to use a front-end framework like React, Vue.js, or Angular. These frameworks provide powerful tools for building interactive user interfaces.

Implement the Design: Once you have a design and a framework, you can start building the front-end. You'll need to connect your front-end to your existing Python backend, likely through a REST API or similar interface.

Test: Conduct thorough testing to ensure that the front-end works well with the backend and provides a good user experience.

Iterate: Based on user feedback, continue to refine and improve the design.

This is a high-level overview of the process. The specifics will depend on your exact requirements, your skills and experience, and the tools you have available.

Step 1: Define the User Interface Components
Before we can design a UI, we need to understand what functionality it needs to provide. Here's a list of components that we might need for this application:

Task Display: This is a list or table that displays the tasks from Trello that are to be processed. Each task could be a row in the table with columns for task name, task description, and status (processed or not processed).

AI Generated Content Preview: When a task is selected, this area will show the AI generated content such as the task description and subtasks. This should be editable by the user before it is sent back to Trello.

Accept/Reject Buttons: These will be used to accept or reject the AI generated content for each task. Accepting the content will update the task in Trello, while rejecting it will discard the AI generated content.

Notifications/Alerts Area: This will display any important information or status updates about the system's operations. For example, it could display a message when tasks are being fetched from Trello or when an update to a Trello card is successful.

Activity Log: This area will display a history of actions taken by the user and the system. For example, it could show when tasks were fetched, when AI content was generated, and when tasks were updated on Trello.

This is a basic set of components that should cover the system's main functionality. Depending on the specific needs of your users, you might want to add more components or functionality.

Step 2: Design the Layout
The layout of the application determines how the components are organized on the screen. The goal is to create an intuitive and user-friendly layout that allows users to easily navigate and use the application. Here is a basic layout that corresponds to the components we defined:

Task Display: This could be positioned on the left side of the screen. Users can select a task from this list to view and edit the AI generated content.

AI Generated Content Preview: This could be in the middle of the screen, to the right of the Task Display. This is where the AI's generated content for the selected task will be displayed.

Accept/Reject Buttons: These could be located below the AI Generated Content Preview. After reviewing and editing the AI-generated content, users can click these buttons to accept or reject the content.

Notifications/Alerts Area: This could be at the top of the screen, spanning the width of the screen. This would make it highly visible, ensuring that users do not miss any important notifications.

Activity Log: This could be located on the right side of the screen. This allows users to view the history of actions at a glance, without interfering with their current task.

Remember, this is just a basic layout suggestion. The final design should take into account the preferences and needs of your users, as well as the aesthetics of the application.

The next step after this would be to create a mockup or prototype of the layout. You can use a tool like Figma, Sketch, or Adobe XD to create a visual representation of the layout. This will help you to visualize how the application will look and function, and can be used to gather feedback from users before you start building the application.

Create a New Project: Start by creating a new project or file in your chosen tool.

Define the Layout Grid: Set up your layout grid according to the design layout we discussed earlier.

Create the Components: Begin by creating rectangles for each of the components - Task Display, AI Generated Content Preview, Accept/Reject Buttons, Notifications/Alerts Area, and Activity Log. At this stage, focus on the size and position of each component rather than the details.

Add Details to the Components: Once the basic layout is complete, start adding details to each component. For example, in the Task Display, you might add a table with columns for task name, task description, and status. In the AI Generated Content Preview, you might add a text area for displaying and editing the AI-generated content.

Refine the Design: Finally, refine your design by adjusting colors, fonts, and other stylistic elements. Make sure the design is consistent and easy to understand.

Review and Iterate: Review your design and make any necessary adjustments. You might also want to get feedback from potential users at this stage, before you start building the actual application.

Choose a Web Framework: If you haven't already, choose a web framework to build your application. Some popular options for front-end development include React.js, Vue.js, and Angular.js. All of these have a great ecosystem, comprehensive documentation, and a large community.

Setup the Development Environment: Once you've chosen a web framework, set up your development environment according to the framework's documentation. This typically involves installing Node.js and the framework's command line interface (CLI).

Create a New Project: Use the framework's CLI to create a new project. This will set up the basic structure of your application and install any necessary dependencies.

Build the Components: Now start building the components of your application according to your design. Typically, you'll create a separate file or module for each major component (Task Display, AI Generated Content Preview, etc.). Each component will include HTML for the structure, CSS for the style, and JavaScript for the behavior.

Connect to the API: Once your components are built, you'll need to connect them to your backend API. This involves making HTTP requests to fetch, post, and update data. In your case, you would need to connect to the Trello API and OpenAI's GPT-3 API.

Testing: After building your components and connecting them to the API, test your application to ensure it works as expected. This can involve manual testing, automated testing, or ideally a mix of both.

Deployment: Finally, once you're satisfied with your application and all tests are passing, you can deploy your application to a web server.

Install Node.js and npm: If you haven't installed Node.js and npm (Node Package Manager) on your computer yet, please do so. You can download Node.js and npm from this website: https://nodejs.org/. Node.js is a JavaScript runtime that lets you run JavaScript code on your computer, and npm is a package manager for Node.js.

Install Create Next App: Create Next App is a command-line tool that allows you to create a new Next.js application. You can install it globally on your computer by running the following command in your terminal:

lua
Copy code
npx create-next-app@latest
Create a New Next.js App: After installing Create Next App, you can create a new Next.js application by running the following command in your terminal:

perl
Copy code
npx create-next-app@latest my-app
Replace "my-app" with the name of your application.

Start the Development Server: Navigate into your new project directory with cd my-app (replace "my-app" with your application name), and start the development server with npm run dev. This will start the server, and you can view your application by opening http://localhost:3000 in your web browser.

Now that you've created a new Next.js application, you're ready to start building the components of your application. Do you need help with this next step, or do you have any questions about setting up your Next.js application?

To start, we will create a new page that will serve as the main interface for the user. This page will display the task data and the corresponding AI-generated content.

In Next.js, each page is a React component exported from a .js or .ts file in the pages directory.

To fetch and display the task data and AI-generated content, we will need to communicate with the backend. We can do this by making HTTP requests from our Next.js application to our Flask API.

Next.js provides a built-in fetch function that we can use to make these HTTP requests. We can use this fetch function in the getServerSideProps function, which Next.js calls when it needs to render a page on the server.
Once we have the task data displayed, we can start working on the interface for the AI-generated content. We need an interface where users can review, edit, and approve the AI-generated descriptions and subtasks before they are added to Trello.

One way to achieve this is by creating a modal dialog box that displays the AI-generated content for each task. Users can then interact with this modal to review, edit, and approve the content.

In this example, we're using React's useState hook to manage the state of the AI-generated content. When the user clicks the "Approve" button, we call the onApprove function passed in as a prop, passing along the task id and the current state of the AI-generated content.

This is a basic example, and there's much more we could do here. For example, we might want to add a text input for each subtask, so users can edit the AI-generated subtasks as well. We might also want to add some sort of loading state, so users know when the AI is processing a task.

Once we have the modal component, we can integrate it into our page component. We can add a button next to each task that opens the modal with the AI-generated content for that task.
