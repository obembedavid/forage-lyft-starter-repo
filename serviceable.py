from abc import ABC, abstractmethod


class Seviceable(ABC):
    @abstractmethod 
    def needs_service(self):
        pass