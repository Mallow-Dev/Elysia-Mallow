import pytest

from elysia.api.custom_tools import (
    SafeMath,
    EnvironmentSummary,
    HiddenStoreWriter,
    HiddenStoreConditionalTool,
)
from elysia.objects import Result, Status, Error


class DummyEnvironment:
    def __init__(self):
        self.environment = {}
        self.hidden_environment = {}


class DummyTreeData:
    def __init__(self):
        self.environment = DummyEnvironment()


@pytest.mark.asyncio
async def test_safe_math_sum():
    tool = SafeMath()
    tree_data = DummyTreeData()
    inputs = {"operation": "sum", "numbers": [1, 2, 3]}
    out = []
    async for o in tool(tree_data, inputs, None, None, None):
        out.append(o)
    assert any(isinstance(o, Status) for o in out)
    result = next(o for o in out if isinstance(o, Result))
    assert result.objects[0]["value"] == 6
    assert result.objects[0]["operation"] == "sum"


@pytest.mark.asyncio
async def test_safe_math_invalid_operation():
    tool = SafeMath()
    tree_data = DummyTreeData()
    inputs = {"operation": "median", "numbers": [1, 2, 3]}
    out = []
    async for o in tool(tree_data, inputs, None, None, None):
        out.append(o)
    assert any(isinstance(o, Error) for o in out)


@pytest.mark.asyncio
async def test_environment_summary_empty():
    tool = EnvironmentSummary()
    tree_data = DummyTreeData()
    out = []
    async for o in tool(tree_data, {}, None, None, None):
        out.append(o)
    result = next(o for o in out if isinstance(o, Result))
    assert result.objects[0]["message"].startswith("Environment empty")


@pytest.mark.asyncio
async def test_hidden_store_write_and_read():
    writer = HiddenStoreWriter()
    reader = HiddenStoreConditionalTool()
    tree_data = DummyTreeData()

    # Initially not available
    assert not await reader.is_tool_available(tree_data, None, None, None)

    # Store the hidden key
    async for _ in writer(
        tree_data, {"key": "unlock", "value": "yes"}, None, None, None
    ):
        pass

    assert await reader.is_tool_available(tree_data, None, None, None)

    out = []
    async for o in reader(tree_data, {}, None, None, None):
        out.append(o)
    result = next(o for o in out if isinstance(o, Result))
    assert result.objects[0]["unlock"] == "yes"
