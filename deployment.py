import vertexai
from agent1 import root_agent



PROJECT_ID = "YOUR_PROJECT_ID"
LOCATION = "us-central1"
STAGING_BUCKET = "gs://YOUR_BUCKET"

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
)


from vertexai import agent_engines

remote_app = agent_engines.create(
    agent_engine=root_agent,
    requirements=[
        "google-cloud-aiplatform[adk,agent_engines]"   
    ],
    extra_packages=["agent1"]
)

remote_app.resource_name


remote_session = remote_app.create_session(user_id="u_456")
remote_session