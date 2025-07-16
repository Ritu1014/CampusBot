from queue import Queue
from agents.admission_agent import AdmissionAgent
from agents.exam_agent import ExamAgent
from agents.library_agent import LibraryAgent
from agents.hostel_agent import HostelAgent

def main():
    agents_registry = {
        "AdmissionAgent": Queue(),
        "ExamAgent": Queue(),
        "LibraryAgent": Queue(),
        "HostelAgent": Queue()
    }

    # Initialize all agents
    admission = AdmissionAgent("AdmissionAgent", agents_registry["AdmissionAgent"], agents_registry)
    exam = ExamAgent("ExamAgent", agents_registry["ExamAgent"], agents_registry)
    library = LibraryAgent("LibraryAgent", agents_registry["LibraryAgent"], agents_registry)
    hostel = HostelAgent("HostelAgent", agents_registry["HostelAgent"], agents_registry)

    # Start agent threads
    admission.start()
    exam.start()
    library.start()
    hostel.start()

    print("\n🌐 Smart Campus Assistant System Started\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        agents_registry["AdmissionAgent"].put(("User", user_input))

if __name__ == "__main__":
    main()