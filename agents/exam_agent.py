from agents.base_agent import BaseAgent

class ExamAgent(BaseAgent):
    def handle_message(self, sender, message):
        if "marksheet" in message.lower():
            reply = "Marksheet will be available after results on 25th July."
        else:
            self.send_message("LibraryAgent", message)
            reply = "Query not related to Exam. Forwarded to Library."
        print(f"[ExamAgent] To {sender}: {reply}")