from vertexai import agent_engines

# list all the deployed agents
for i in agent_engines.list():
    print(i)


# get the deployed agent
remote_agent = agent_engines.get('projects/YOUR_PROJECT_ID/locations/us-central1/reasoningEngines/YOUR_ENGINE_ID')

# query your agent

for event in remote_agent.stream_query(
    user_id="u_456",
    message="whats the weather in new york",
):
    print(event)


#delete your agent
remote_agent.delete(force=True)
