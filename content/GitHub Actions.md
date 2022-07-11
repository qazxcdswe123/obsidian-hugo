---
aliases: [Action]
tags: [] 
---
Use [[yaml]] as markup language

## Structure
### Events
An event is a specific activity in a repository that triggers a workflow run. For example, activity can originate from GitHub when someone creates a pull request, opens an issue, or pushes a commit to a repository. You can also trigger a workflow run on a schedule, by [posting to a REST API](https://docs.github.com/en/rest/reference/repos#create-a-repository-dispatch-event), or manually.

For a complete list of events that can be used to trigger workflows, see [Events that trigger workflows](https://docs.github.com/en/actions/reference/events-that-trigger-workflows).

### Jobs
A job is a set of _steps_ in a workflow that execute on the same runner. Each step is either a shell script that will be executed, or an _action_ that will be run. Steps are executed in order and are dependent on each other. Since each step is executed on the same runner, you can share data from one step to another. For example, you can have a step that builds your application followed by a step that tests the application that was built.

### Actions
An _action_ is a custom application for the GitHub Actions platform that performs a complex but frequently repeated task.

### Runners
A runner is a server that runs your workflows when they're triggered.
## Templates
### Checkout
[GitHub - actions/checkout: Action for checking out a repo](https://github.com/actions/checkout)
It is an official GitHub Action used to check-out a repository so a workflow can access it. 
