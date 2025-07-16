from agents.base_agent import BaseAgent

class LibraryAgent(BaseAgent):
    def handle_message(self, sender, message):
        if "book" in message.lower():
            reply = "You can borrow 2 books per week. Library open 9am-5pm."
        else:
            self.send_message("HostelAgent", message)
            reply = "Forwarding to Hostel Department."
        print(f"[LibraryAgent] To {sender}: {reply}")