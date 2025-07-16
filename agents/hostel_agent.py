from agents.base_agent import BaseAgent

class HostelAgent(BaseAgent):
    def handle_message(self, sender, message):
        if "room" in message.lower():
            reply = "Hostel rooms are fully booked for this semester."
        else:
            reply = "Sorry, I don't have an answer to your query."
        print(f"[HostelAgent] To {sender}: {reply}")