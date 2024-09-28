# test_chatbot.py

from voibot.chatbot import VoiAssistant

# Set up the parameters for the assistant

pdf_url = "https://firebasestorage.googleapis.com/v0/b/voiage-67f40.appspot.com/o/pdfs%2Fdemo%2FVoiAssistantKnowledge.pdf?alt=media"  # Replace this with a valid PDF URL
role = "You are an AI virtual assistant for Voi AI. You are tasked with answering questions about Voi AI or VoiBot"
intents = {
    "Company-related": "Questions about the company (Voi AI), the product (VoiBot), etc.",
    "Assistant-related": "Questions about the assistant like 'what do you know?'",
    "Greeting": "Greetings like 'Hello' or 'How are you?'",
    "Other Topic": "Non-related topics",
    "Not Understandable Word/Phrase": "Gibberish like 'ajskdhasd'",
    "Previous chat-related inquiry": "Asking for clarification/additional info/checking on a previously given info by the LLM",
    "Clarification": "Asking the assistant to clarify a previously given answer",
    "Follow-up Inquiry": "Follow-up question based on a previous response",
    "User Feedback (Positive)": "Positive user feedback like 'Thank you!' or 'That was helpful!'",
    "User Feedback (Negative)": "Negative feedback like 'That didn’t help.' or 'I don’t understand.'",
}

replies = {
    "Company-related": "RAG",
    "Assistant-related": "RAG",
    "Greeting": "role_based_llm_reply",  # Custom, human-like greeting based on query
    "Other Topic": "I'm sorry, but I can't help with that topic.",
    "Not Understandable Word/Phrase": "I didn't quite catch that. Did you really mean: {most_recent_query}",
    "Previous chat-related inquiry": "RAG",
    "Clarification": "Let me clarify that for you: {most_recent_response}",
    "Follow-up Inquiry": "Let’s build on what we discussed earlier: {most_recent_response}",
    "User Feedback (Positive)": "I'm glad you found that helpful! If there is anything else you would like me to help with, please let me know!",
    "User Feedback (Negative)": "I'm sorry if that wasn't clear or helpful. If I can help you with anything further, please feel free to ask!",
}

segment_assignments = {
    "Company-related": "unified",
    "Assistant-related": "unified",
    "Greeting": "unified",
    "Other Topic": "unified",
    "Not Understandable Word/Phrase": "unified",
    "Previous chat-related inquiry": "unified",
    "Clarification": "unified",  # Related to the whole document
    "Follow-up Inquiry": "unified",
    "User Feedback (Positive)": "unified",
    "User Feedback (Negative)": "unified",
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

    extra_response = assistant.get_most_recent_query()
    print(extra_response)
    
    # Print the assistant's response
    print(f"Assistant: {response}")
