import numpy as np


class BaseAgent:
    def __init__(self, state_dim, action_dim, memory_capacity=1000, **hyperparameters):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.memory = ReplayBuffer(memory_capacity)  # Assuming ReplayBuffer implementation
        self.hyperparameters = hyperparameters

    def _gradient_clipping(self, gradients, clip_norm):
        """
        Applies gradient clipping to prevent exploding gradients during training.

        Args:
            gradients (list): A list of gradients for model parameters.
            clip_norm (float): The maximum norm for the clipped gradients.

        Returns:
            list: A list of clipped gradients.
        """
        clipped_gradients = []
        for grad in gradients:
            if grad is not None:  # Handle potential None gradients
                norm = np.linalg.norm(grad)
                if norm > clip_norm:
                    clipped_grad = clip_norm * grad / norm
                else:
                    clipped_grad = grad
                clipped_gradients.append(clipped_grad)
        return clipped_gradients

    def _learning_rate_scheduler(self, initial_lr, decay_rate, steps):
        """
        Adjusts the learning rate dynamically throughout training.

        Args:
            initial_lr (float): The initial learning rate.
            decay_rate (float): The decay rate for the learning rate.
            steps (int): The number of training steps.

        Returns:
            float: The current learning rate based on the decay schedule.
        """
        decayed_lr = initial_lr * np.power(1 - decay_rate, steps)
        return decayed_lr

    # ... (other existing methods in BaseAgent)