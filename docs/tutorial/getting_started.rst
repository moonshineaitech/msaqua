.. _getting_started:

Getting Started with msaqua: Automating Workflows with AI
Welcome to msaqua! This guide empowers you to harness the power of AI for automating repetitive tasks and streamlining workflows.

Installation

Install msaqua using pip:

Bash
pip install msaqua
Use code with caution.
(Optional) Install additional dependencies for specific features:

Cloud Integration: ray (https://www.ray.io/)
Hyperparameter Tuning: optuna (https://optuna.org/) or hyperopt (https://github.com/hyperopt)
Basic Usage Example

Let's create a simple workflow that interacts with an environment using a reinforcement learning agent:

1. Import Necessary Modules:

Python
import msaqua.agents as agents
import msaqua.environments as env  # Assuming a custom environment definition
Use code with caution.
2. Define the Environment:

Python
# Replace with your specific environment implementation
my_env = env.MyCustomEnvironment()
Use code with caution.
3. Create the Agent:

Python
agent = agents.ReinforcementAgent(my_env.observation_space.shape[0], my_env.action_space.n)
Use code with caution.
my_env.observation_space.shape[0]: This retrieves the size of the observation space from your environment, which represents the number of features the agent receives in each observation.
my_env.action_space.n: This retrieves the number of possible actions the agent can take in your environment.
4. Train the Agent:

Python
agent.train(my_env, num_episodes=100)  # Adjust num_episodes as needed
Use code with caution.
The train method allows the agent to learn through interaction with the environment over a specified number of episodes.
5. Use the Agent:

Python
observation = my_env.reset()  # Reset the environment to get the initial observation
while True:
    action = agent.act(observation)  # Get the agent's action based on the observation
    observation, reward, done, info = my_env.step(action)  # Take the action and get feedback
    # ... (use reward and info for further processing)
    if done:
        break
Use code with caution.
The act method takes an observation from the environment and returns the action the agent chooses to take.
The environment step method executes the action, returns the next observation, reward for the action, a flag indicating if the episode is done, and additional information.
This is a basic example, and the specific steps will vary depending on your environment and desired workflow. However, it provides a foundation for understanding how to use msaqua for automating tasks.

Key Concepts:

Environments: Represent the tasks or scenarios your agents will interact with. Define custom environments or utilize existing ones.
Agents: AI models trained to interact with environments and make decisions. msaqua provides reinforcement learning and supervised learning agent implementations.
Workflows: Sequences of tasks chained together. Define workflows using the tasks module.
Next Steps:

Explore the msaqua API documentation (refer to docs/api/reference.rst) for detailed information on available modules, classes, and functions.
Delve into the code examples within the package to understand more complex use cases.
Consider customizing this example by:
Defining a more intricate environment.
Implementing a custom agent logic (e.g., reward shaping).
Integrating cloud platforms or hyperparameter tuning libraries.
By leveraging msaqua, you can automate repetitive tasks, improve efficiency, and unlock the power of AI for your workflows.