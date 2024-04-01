.. _api_reference:

API Reference for msaqua
=========================

This page provides a comprehensive reference for the functions and classes within the `msaqua` package, designed to empower you with AI-driven automation capabilities.

**Installation**

Ensure you have Python installed (https://www.python.org/downloads/). Then, install `msaqua` using pip:

```bash
pip install msaqua

Core Modules:

agents (msaqua.agents): This module houses various agent implementations for tackling different automation tasks:

    reinforcement_agent.py: Implements a reinforcement learning agent with capabilities for:
        Training through interaction with an environment.
        Employing hyperparameter optimization techniques.
        Leveraging gradient clipping to prevent exploding gradients.
        Integrating with cloud platforms for distributed training.
    supervised_agent.py: Provides a supervised learning agent suitable for:
        Learning from labeled datasets.
        Making predictions based on trained models.


tasks (msaqua.tasks): This module facilitates defining and orchestrating workflows:

    task_registry.py: Manages the registration and lookup of individual tasks.
    workflow_automation.py: Offers functionalities for:
        Creating workflows by chaining tasks and arguments.
        Executing workflows sequentially or in parallel (depending on implementation).


utils (msaqua.utils): This module contains utility functions for common tasks:

    configuration.py: Provides tools for:
        Loading configuration settings from YAML or JSON files.
        Retrieving specific configuration values.
    data_handling.py: Offers functions for:
        Loading data from various formats (CSV, JSON, HDF5).
        Performing basic data preprocessing (implementation details depend on your needs).
    logging.py: Enables logging messages at different levels (e.g., INFO, DEBUG) to a file or console.