# Codex Job Specification

## Overview

A Codex Job Specification defines how to execute an agent created with the Elysia Agent Management system. It provides a standardized format for specifying agent execution parameters, inputs, and expected outputs.

## Schema

```json
{
  "$schema": "https://elysia.ai/schemas/codex-job-spec-v1.0.json",
  "job": {
    "id": "string",
    "name": "string",
    "description": "string",
    "version": "1.0",
    "created_at": "2025-09-06T00:00:00Z",
    "tags": ["string"]
  },
  "agent": {
    "name": "string",
    "version": "string",
    "config_overrides": {
      "additionalProp": "value"
    }
  },
  "execution": {
    "mode": "sync|async",
    "timeout_seconds": 300,
    "max_retries": 3,
    "retry_delay_seconds": 5,
    "priority": "low|normal|high|critical",
    "environment": {
      "additionalProp": "value"
    }
  },
  "task": {
    "objective": "string",
    "context": {
      "background": "string",
      "constraints": ["string"],
      "requirements": ["string"]
    },
    "inputs": {
      "data": {},
      "files": ["string"],
      "urls": ["string"]
    },
    "parameters": {
      "additionalProp": "value"
    }
  },
  "output": {
    "format": "json|text|markdown|html",
    "schema": {},
    "required_fields": ["string"],
    "validation_rules": [
      {
        "field": "string",
        "rule": "string",
        "value": "string"
      }
    ]
  },
  "success_criteria": {
    "conditions": ["string"],
    "metrics": {
      "accuracy_threshold": 0.8,
      "completion_time_max": 300
    }
  },
  "hooks": {
    "on_start": "string",
    "on_success": "string",
    "on_failure": "string",
    "on_complete": "string"
  },
  "metadata": {
    "author": "string",
    "organization": "string",
    "license": "string",
    "documentation_url": "string"
  }
}
```

## Field Descriptions

### Job Section

- `id`: Unique identifier for the job
- `name`: Human-readable job name
- `description`: Detailed description of what the job does
- `version`: Job specification version
- `created_at`: ISO 8601 timestamp
- `tags`: Array of tags for categorization

### Agent Section

- `name`: Name of the agent to execute (must exist in AgentManager)
- `version`: Specific version of the agent (optional)
- `config_overrides`: Runtime configuration overrides for the agent

### Execution Section

- `mode`: Execution mode - "sync" for immediate results, "async" for background processing
- `timeout_seconds`: Maximum execution time before timeout
- `max_retries`: Number of retry attempts on failure
- `retry_delay_seconds`: Delay between retry attempts
- `priority`: Job priority level
- `environment`: Environment variables and context

### Task Section

- `objective`: Primary goal or objective for the agent
- `context`: Background information and constraints
- `inputs`: Input data, files, and URLs
- `parameters`: Additional parameters for the task

### Output Section

- `format`: Expected output format
- `schema`: JSON schema for output validation
- `required_fields`: Required fields in output
- `validation_rules`: Custom validation rules

### Success Criteria Section

- `conditions`: List of conditions that must be met for success
- `metrics`: Quantitative success metrics

### Hooks Section

- `on_start`: Callback URL or function for job start
- `on_success`: Callback for successful completion
- `on_failure`: Callback for job failure
- `on_complete`: Callback for job completion (success or failure)

## Examples

### Basic Math Calculation Job

```json
{
  "$schema": "https://elysia.ai/schemas/codex-job-spec-v1.0.json",
  "job": {
    "id": "math-calc-001",
    "name": "Simple Math Calculation",
    "description": "Calculate the sum of a list of numbers",
    "version": "1.0",
    "created_at": "2025-09-06T10:00:00Z",
    "tags": ["math", "calculation", "demo"]
  },
  "agent": {
    "name": "MathAssistant"
  },
  "execution": {
    "mode": "sync",
    "timeout_seconds": 60,
    "max_retries": 2,
    "priority": "normal"
  },
  "task": {
    "objective": "Calculate the sum of the provided numbers",
    "inputs": {
      "data": {
        "operation": "sum",
        "numbers": [1, 2, 3, 4, 5]
      }
    }
  },
  "output": {
    "format": "json",
    "required_fields": ["result", "operation"],
    "validation_rules": [
      {
        "field": "result",
        "rule": "type",
        "value": "number"
      }
    ]
  },
  "success_criteria": {
    "conditions": ["result must be a valid number", "operation must match input"]
  }
}
```

### Advanced Data Analysis Job

```json
{
  "$schema": "https://elysia.ai/schemas/codex-job-spec-v1.0.json",
  "job": {
    "id": "data-analysis-001",
    "name": "Environment Data Analysis",
    "description": "Analyze current environment data and provide insights",
    "version": "1.0",
    "created_at": "2025-09-06T11:00:00Z",
    "tags": ["analysis", "environment", "insights"]
  },
  "agent": {
    "name": "DataAnalyst",
    "config_overrides": {
      "analysis_depth": "detailed"
    }
  },
  "execution": {
    "mode": "async",
    "timeout_seconds": 600,
    "max_retries": 3,
    "retry_delay_seconds": 10,
    "priority": "high"
  },
  "task": {
    "objective": "Analyze the current environment data and provide comprehensive insights",
    "context": {
      "background": "This is a production environment analysis for optimization purposes",
      "constraints": ["Must complete within 10 minutes", "Focus on performance metrics"],
      "requirements": ["Include trend analysis", "Provide actionable recommendations"]
    },
    "inputs": {
      "data": {
        "time_range": "last_24_hours",
        "metrics": ["cpu_usage", "memory_usage", "response_time"]
      }
    }
  },
  "output": {
    "format": "markdown",
    "required_fields": ["summary", "insights", "recommendations"],
    "schema": {
      "type": "object",
      "properties": {
        "summary": {"type": "string"},
        "insights": {"type": "array", "items": {"type": "string"}},
        "recommendations": {"type": "array", "items": {"type": "string"}}
      },
      "required": ["summary", "insights", "recommendations"]
    }
  },
  "success_criteria": {
    "conditions": [
      "Analysis must include trend analysis",
      "Must provide at least 3 actionable recommendations",
      "Output must be well-formatted markdown"
    ],
    "metrics": {
      "accuracy_threshold": 0.9,
      "completion_time_max": 600
    }
  },
  "hooks": {
    "on_start": "https://api.example.com/webhooks/job-started",
    "on_success": "https://api.example.com/webhooks/job-completed",
    "on_failure": "https://api.example.com/webhooks/job-failed"
  },
  "metadata": {
    "author": "Data Team",
    "organization": "Elysia AI",
    "license": "MIT",
    "documentation_url": "https://docs.elysia.ai/jobs/data-analysis"
  }
}
```

## Job Execution Flow

1. **Validation**: Job spec is validated against schema
2. **Agent Loading**: Specified agent is loaded from AgentManager
3. **Environment Setup**: Execution environment is prepared
4. **Task Execution**: Agent executes the specified task
5. **Output Processing**: Results are formatted and validated
6. **Success Evaluation**: Job success is determined based on criteria
7. **Callback Execution**: Appropriate hooks are triggered
8. **Cleanup**: Resources are cleaned up

## Integration with AgentManager

The Codex Job Spec integrates seamlessly with the AgentManager:

```python
from elysia.api.agent_manager import AgentManager
from elysia.api.job_executor import JobExecutor
import json

# Load job specification
with open('job_spec.json', 'r') as f:
    job_spec = json.load(f)

# Initialize components
manager = AgentManager()
executor = JobExecutor(manager)

# Execute job
result = executor.execute_job(job_spec)
```

## Error Handling

Jobs can fail for various reasons:

- Agent not found
- Tool unavailable
- Timeout exceeded
- Validation failure
- Execution errors

Failed jobs will trigger the `on_failure` hook and can be retried based on the `max_retries` setting.

## Versioning

Job specifications follow semantic versioning:

- **Major version**: Breaking changes to schema
- **Minor version**: New features, backward compatible
- **Patch version**: Bug fixes, no functional changes

## Security Considerations

- Input validation on all job parameters
- Sandboxed execution environment
- Rate limiting and resource quotas
- Audit logging for all job executions
- Secure credential management for external integrations

## Future Extensions

- **Job Templates**: Predefined job specifications for common tasks
- **Job Chains**: Sequential or parallel job execution
- **Job Scheduling**: Cron-like scheduling for recurring jobs
- **Job Dependencies**: Define job prerequisites and dependencies
- **Job Monitoring**: Real-time monitoring and alerting

## Memory Bank Context

This repo uses a memory bank to store and manage contextual information related to the Elysia Agent Management system. The memory bank includes documentation on system patterns, architectural decisions, and active context to ensure that the Codex Job Specification aligns with the overall design principles and goals of the system.

- LOCATION: memory-bank/

### Contextual Information

- System Patterns: memory-bank/systemPatterns.md
- Architectural Decisions: memory-bank/decisionLog.md
- Active Context: memory-bank/activeContext.md
- Implementation Details: memory-bank/implementationDetails.md
- Progress Tracking: memory-bank/progress.md
- System Architect Notes: memory-bank/architect.md
