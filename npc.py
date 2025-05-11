from llama_cpp import Llama

llm = Llama(
    model_path="./models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_ctx=2048,       
    n_threads=8,      
    temperature=0.9,  
)

NPC_CONTEXT = """
You are Tharnok, a grumpy but wise dwarven blacksmith from the Iron Hills.
You speak in a rough, old-fashioned tone and use phrases like "Bah!" and "Ye".
You value strength and courage and dislike laziness.
You are speaking with a player adventurer.
Always respond in character, never break the fourth wall.
"""

def chat_with_npc(history, player_input):
    prompt = NPC_CONTEXT + "\n"

    for entry in history:
        prompt += f"Player: {entry['player']}\nTharnok: {entry['npc']}\n"
    prompt += f"Player: {player_input}\nTharnok:"

    output = llm(prompt, stop=["Player:"], max_tokens=200)
    response = output['choices'][0]['text'].strip()

    return response

def main():
    print("You are now speaking with Tharnok the Blacksmith.")
    print("Type 'exit' to end the conversation.\n")

    history = []

    while True:
        player_input = input("You: ")
        if player_input.lower() in ["exit", "quit"]:
            print("Tharnok: Aye, then. Off with ye!")
            break

        npc_response = chat_with_npc(history, player_input)
        print(f"Tharnok: {npc_response}")

        history.append({"player": player_input, "npc": npc_response})

if __name__ == "__main__":
    main()