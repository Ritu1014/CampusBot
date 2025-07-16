from agents.base_agent import BaseAgent

class AdmissionAgent(BaseAgent):
    def handle_message(self, sender, message):
        if "admission" in message.lower():
            reply = "Admissions are open until 30th July. Apply via college portal."
        else:
            self.send_message("ExamAgent", message)
            reply = "Forwarding your query to Exam Department."
        print(f"[AdmissionAgent] To {sender}: {reply}")