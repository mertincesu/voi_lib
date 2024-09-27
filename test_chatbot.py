# test_chatbot.py

from voi_lib.chatbot import VoiAssistant

# Set up the parameters for the assistant

pdf_url = "https://firebasestorage.googleapis.com/v0/b/voiage-67f40.appspot.com/o/pdfs%2Fdemo%2FVoiAssistantKnowledge.pdf?alt=media"  # Replace this with a valid PDF URL
role = "You are an AI virtual assistant for Voi AI. You are tasked with answering questions about Voi AI or VoiBot"
intents = {
    "Company-related": "Questions about the company (Voi AI), the product (VoiBot), etc.",
    "Assistant-related": "Questions about the assistant like 'what do you know?'",
    "Greeting": "Greetings like 'Hello' or 'How are you?'",
    "Other Topic": "Non-related topics",
    "Not Understandable Word/Phrase": "Gibberish like 'ajskdhasd'"
}
replies = {
    "Company-related": "RAG",
    "Assistant-related": "RAG",
    "Greeting": "role_based_llm_reply",
    "Other Topic": "I'm sorry, but I can't help with that topic.",
    "Not Understandable Word/Phrase": "I didn't quite catch that. Could you rephrase it?"
}
segment_assignments = {
    "Company-related": "unified",
    "Assistant-related": "unified",
    "Greeting": "unified",
    "Other Topic": "unified",
    "Not Understandable Word/Phrase": "unified"
}
dont_know_response = "I'm not sure if I have that information right now..."

# Initialize the assistant
assistant = VoiAssistant(
    openai_key=openai_key,
    pdf_url=pdf_url,
    role=role,
    intents= intents,
    replies=replies,
    segment_assignments=segment_assignments,
    dont_know_response = dont_know_response
)

# Initialize the assistant (this will load the PDF and prepare the index)
assistant.initialize_assistant()

while True:
    # Get user input
    query = input("You: ")

    # Check if user wants to exit
    if query.lower() == "exit":
        print("Conversation ended.")
        break

    # Get the assistant's response
    response = assistant.get_response(query)
    
    # Print the assistant's response
    print(f"Assistant: {response}")
