import pytest
import os
import json
from elysia.api.agent_manager import AgentManager, Agent
from elysia.api.custom_tools import SafeMath, EnvironmentSummary


@pytest.fixture
def manager(tmp_path):
    # Use a temporary file for storage
    storage_path = tmp_path / "agents.json"
    manager = AgentManager(str(storage_path))
    manager.register_tool(SafeMath)
    manager.register_tool(EnvironmentSummary)
    return manager


def test_create_agent(manager):
    agent = manager.create_agent(
        "TestAgent", "A test agent", ["SafeMath"], "You are a test agent."
    )
    assert agent.name == "TestAgent"
    assert agent.description == "A test agent"
    assert len(agent.tools) == 1
    assert agent.tools[0] == SafeMath
    assert agent.system_prompt == "You are a test agent."


def test_list_agents(manager):
    manager.create_agent("Agent1", "Desc1", ["SafeMath"])
    manager.create_agent("Agent2", "Desc2", ["EnvironmentSummary"])
    agents = manager.list_agents()
    assert len(agents) == 2
    assert agents[0]["name"] == "Agent1"
    assert agents[1]["name"] == "Agent2"


def test_get_agent(manager):
    manager.create_agent("TestAgent", "Desc", ["SafeMath"])
    agent = manager.get_agent("TestAgent")
    assert agent is not None
    assert agent.name == "TestAgent"
    assert manager.get_agent("NonExistent") is None


def test_update_agent(manager):
    manager.create_agent("TestAgent", "Desc", ["SafeMath"])
    updated = manager.update_agent(
        "TestAgent", description="Updated desc", tools=["EnvironmentSummary"]
    )
    assert updated.description == "Updated desc"
    assert len(updated.tools) == 1
    assert updated.tools[0] == EnvironmentSummary


def test_delete_agent(manager):
    manager.create_agent("TestAgent", "Desc", ["SafeMath"])
    assert "TestAgent" in manager.agents
    manager.delete_agent("TestAgent")
    assert "TestAgent" not in manager.agents


def test_persistence(manager):
    manager.create_agent("PersistentAgent", "Desc", ["SafeMath"])
    # Simulate reload by creating new manager with same path
    new_manager = AgentManager(manager.storage_path)
    new_manager.register_tool(SafeMath)
    agent = new_manager.get_agent("PersistentAgent")
    assert agent is not None
    assert agent.name == "PersistentAgent"
