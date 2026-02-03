from abc import ABC, abstractmethod


class LLMProvider(ABC):
    """
    Abstract base class for all LLM providers.
    This allows us to switch LLMs without changing core logic.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass
