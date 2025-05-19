from google.adk.agents import Agent
from .tools.get_data import get_engine_data_json
from .tools.predict_rul import predict_engine_rul
from .tools.stop_engine import stop_engine
from .tools.maintanance import (
    suggest_maintenance_action, 
    schedule_maintenance_task, 
    assign_maintenance_staff, 
    estimate_maintenance_cost
)
from .prompts import (
    root_agent_instruction, 
    root_agent_description,
    data_agent_instruction,
    data_agent_description,
    maintenance_agent_instruction,
    maintenance_agent_description
)


data_agent = Agent(
    name="data_agent",
    model="gemini-2.0-flash",
    instruction=data_agent_instruction(),
    description=data_agent_description(),
    tools=[get_engine_data_json,predict_engine_rul]
)

maintenance_agent = Agent(
    name="maintenance_agent",
    model="gemini-2.0-flash",
    instruction=maintenance_agent_instruction(),
    description=maintenance_agent_description(),
    tools=[
        suggest_maintenance_action,
        estimate_maintenance_cost,
        assign_maintenance_staff,
        schedule_maintenance_task
    ]
)

root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    instruction=root_agent_instruction(),
    description=root_agent_description(),
    tools=[stop_engine],
    sub_agents=[data_agent, maintenance_agent]
)

