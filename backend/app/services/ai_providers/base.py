from abc import ABC, abstractmethod

class BaseAIProvider(ABC):
    """
    Abstract base class for all AI providers in the system.
    """
    
    @abstractmethod
    def generate(self, prompt: str, system_instruction: str = None) -> str:
        """
        Generate content based on a prompt.
        
        Args:
            prompt: The text prompt.
            system_instruction: The system prompt (optional).
            
        Returns:
            The raw text response from the provider.
            
        Raises:
            Exceptions on transient or permanent failures.
        """
        pass
    
    @abstractmethod
    def get_provider_name(self) -> str:
        """Return the identifier for this provider."""
        pass
    
    @abstractmethod
    def get_model_name(self) -> str:
        """Return the model currently configured for this provider."""
        pass
