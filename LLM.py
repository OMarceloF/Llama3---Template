from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the questions.

Here are the Previous Converstaions{context}
Questions: {question}

Answer:
"""

model = OllamaLLM(model="llama3")

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

def handle_conversation():
    context = ""
    print("\n Welcome to the AI Chat bot")
    print("\n Type 'exit' to quit the program")

    while True:
        user_input = input("Enter your question:")

        if user_input=="exit":
            break


        result = chain.invoke({"context":context,"question":user_input})

        print("Bot:", result)

        context = f"\nUser: {user_input}\nAI: {result}"

if __name__=="__main__":
    handle_conversation()