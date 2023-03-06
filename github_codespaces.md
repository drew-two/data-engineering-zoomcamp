# GitHub Codespaces

Like a VM that GitHub provides
- Not a fully open VM, but does provide some of a VM for everything we do in the course
- 120 free core hours per month (180 for GitHub pro)
    - More than enough for course

Quick start:
- Go to https://github.com/DataTalksClub/data-engineering-zoomcamp while signed in
- Hit the green drop down "Use this template" > Open in a codespace
- Clones the repo into this workspace and opens VS Code window in the browser with bash terminal
    - Docker is installed, so you can run `docker-compose up` in `week_1_basics/2_docker_sql`
    - VS Code will also automatically port forward, so you can use pgadmin locally in the browser

**Remember to shutdown the codespace when you are down**
- Hit 'Codespaces' in the bottom left and run "Close current codespace"

To see all codespaces go to https://github.com/codespaces
- When you edit someone else's repository, you can publish what you've done to a new repository you own

We used a template earlier from the repository.
- You can also use other premade templates (e.g. React, Jupyter) or a blank
- Can make your own repository into codespace by going one of your repository
    - Hit the green button 'Code', hit the Codespaces tab and create a codespace from the main branch
    - Can also make template out of repository for others to use
        - Go to repo Settings > General > Check "Template Repository"