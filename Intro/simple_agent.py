# pip install pyautogen   (outdated, unnecessary)
# pip install autogen
# pip install python-dotenv
import os
# from autogen_agentchat.agents import AssistantAgent ,UserProxyAgent
from autogen.agentchat import ConversableAgent

from dotenv import load_dotenv

#pip install groq

load_dotenv()

#pip install truststore
import truststore
truststore.inject_into_ssl()

config_list = [
    {
        "model": "llama-3.1-8b-instant",  
        "api_key": os.environ.get("GROQ_API_KEY"),
        "api_type": "groq",
    }
]
#The reason we use a list of dictionaries (config_list = [...]) in 
#autogen instead of a single dictionary is to support multiple model configurations — even if you're only using one model for now.

agent = ConversableAgent(
    name = "simple_agent",
    llm_config = config_list[0],
    code_execution_config = False,
    human_input_mode = "NEVER"
)

response = agent. generate_reply(messages=[{"role":"user", "content":"Tell me a funny joke?"}])  #generally a list is passed
print(response)
print(response['content'])

print("Hello World")