import threading

class BaseAgent(threading.Thread):
    def __init__(self, name, inbox, agents_registry):
        super().__init__()
        self.name = name
        self.inbox = inbox
        self.agents_registry = agents_registry
        self.daemon = True

    def run(self):
        while True:
            sender, message = self.inbox.get()
            self.handle_message(sender, message)

    def handle_message(self, sender, message):
        raise NotImplementedError("Define in subclass.")

    def send_message(self, receiver, message):
        if receiver in self.agents_registry:
            print(f"[{self.name}] Sending to {receiver}: {message}")
            self.agents_registry[receiver].put((self.name, message))
        else:
            print(f"[{self.name}] Error: Agent '{receiver}' not found.")