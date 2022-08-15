# prompts
Repo for journal prompt web app

Project contains:
- Database of prompts
- Python Backend to serve prompts
- Javascript Frontend to show the prompts

# To-Do's
- Collect prompts + create the database - using sqllite
- Write backend to serve prompts (use fastapi or flask)
- Choose frontend framework and build a very simple front end
- 

## Database Schema:
- Prompt Text
- Date added
- Category - annotate by hand for now
- Sub-category - not sure if i need this yet
- Last answered - none if hasn't been answered yet
- Prompt to return to? - whether or not this would be a good one to return to over time
- Feedback - user can rate the prompt as to whether they enjoyed it or not
- Prompt source

## Backend Endpoints
- Serve prompts: sends the top 3 prompts to the user, for now make it random. BE will "shuffle" prompts by category + factor in whether they've been done before.
- Decline prompts: user can decline the 3 prompts they were given and get new ones
- Complete prompt: user marks prompt as complete and can give feedback on the prompt. BE records date completed and feedback.
