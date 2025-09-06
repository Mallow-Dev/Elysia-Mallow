#!/usr/bin/env python3
"""
Example script demonstrating how to execute a Codex Job Spec with the AgentManager.
This is a basic implementation showing the integration between job specs and agents.
"""

import json
import asyncio
from typing import Dict, Any
from pathlib import Path

# Import from our agent management system
from elysia.api.agent_manager import AgentManager
from elysia.api.custom_tools import SafeMath, EnvironmentSummary


class JobExecutor:
    """Simple job executor that integrates with AgentManager."""

    def __init__(self, agent_manager: AgentManager):
        self.agent_manager = agent_manager

    async def execute_job(self, job_spec: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a job based on the provided specification."""

        # Validate job spec
        self._validate_job_spec(job_spec)

        # Get the agent
        agent_name = job_spec["agent"]["name"]
        agent = self.agent_manager.get_agent(agent_name)

        if not agent:
            raise ValueError(f"Agent '{agent_name}' not found")

        # Extract task information
        task = job_spec["task"]
        objective = task["objective"]
        inputs = task.get("inputs", {}).get("data", {})

        # For this example, we'll simulate execution with SafeMath
        if agent_name == "MathAssistant" and "operation" in inputs:
            # Execute the math operation
            result = await self._execute_math_operation(agent, inputs)
            return {
                "job_id": job_spec["job"]["id"],
                "status": "completed",
                "result": result,
                "execution_time": 0.1,
            }
        else:
            return {
                "job_id": job_spec["job"]["id"],
                "status": "completed",
                "result": {"message": f"Executed task: {objective}"},
                "execution_time": 0.05,
            }

    def _validate_job_spec(self, job_spec: Dict[str, Any]):
        """Basic validation of job specification."""
        required_fields = ["job", "agent", "execution", "task"]
        for field in required_fields:
            if field not in job_spec:
                raise ValueError(f"Missing required field: {field}")

        if "id" not in job_spec["job"]:
            raise ValueError("Job must have an ID")

        if "name" not in job_spec["agent"]:
            raise ValueError("Agent must have a name")

    async def _execute_math_operation(
        self, agent, inputs: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Execute a math operation using the SafeMath tool."""
        # Find SafeMath tool in agent's tools
        safe_math_tool = None
        for tool_class in agent.tools:
            if tool_class.__name__ == "SafeMath":
                safe_math_tool = tool_class()
                break

        if not safe_math_tool:
            raise ValueError("Agent does not have SafeMath tool")

        # Mock tree data and other required parameters
        class MockTreeData:
            def __init__(self):
                self.environment = type(
                    "obj", (object,), {"environment": {}, "hidden_environment": {}}
                )()

        tree_data = MockTreeData()

        # Execute the tool
        results = []
        async for result in safe_math_tool(
            tree_data,
            inputs,
            None,  # base_lm
            None,  # complex_lm
            None,  # client_manager
        ):
            results.append(result)

        # Extract the final result
        from elysia.objects import Result

        for result in results:
            if isinstance(result, Result):
                return result.objects[0] if result.objects else {"error": "No result"}

        return {"error": "No result found"}


async def main():
    """Main execution function."""
    # Initialize agent manager
    manager = AgentManager()

    # Register tools
    manager.register_tool(SafeMath)
    manager.register_tool(EnvironmentSummary)

    # Create a sample agent
    manager.create_agent(
        "MathAssistant",
        "An agent specialized in mathematical operations",
        ["SafeMath"],
        "You are a helpful math assistant.",
    )

    # Initialize job executor
    executor = JobExecutor(manager)

    # Load and execute job spec
    job_spec_path = Path("example_job_spec.json")
    if job_spec_path.exists():
        with open(job_spec_path, "r") as f:
            job_spec = json.load(f)

        print("Executing job:", job_spec["job"]["name"])
        result = await executor.execute_job(job_spec)

        print("Job Result:")
        print(json.dumps(result, indent=2))
    else:
        print("example_job_spec.json not found. Please ensure the file exists.")


if __name__ == "__main__":
    asyncio.run(main())
