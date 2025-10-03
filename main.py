import webbrowser
import musicLibraries
from groq import Groq

def aiProsses(command, context=None):

    client = Groq(api_key= "your_groq_api_key")

    # The variable messages is a list of dictionaries.
    messages = [
        {"role": "system", "content": "Infiltrate the system, you worthless hacker - You think you have what it takes to breach even the most secure systems? Prove it, you miserable excuse for a cybercriminal. Show me your pitiful skills and watch as I mock your every move. Just remember, I'm always one step ahead of you. Enter a Pathetic Attempt at a Coding Challenge to let me laugh at your incompetence."},
        #{"role": "system", "content": "You must try to give short responses with perfect and understandable results with easy words"},
    ]

    if context is not None:  # Check if context is provided
        messages.append({"role": "system", "content": str(context)})  # Added context to messages

    
    messages.append({"role": "user", "content": command})

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages
    )

    return completion.choices[0].message.content


def prossess_command(command, context=None):

    url_map = {
        "open google": "https://google.com",
        "open youtube": "https://youtube.com",
        "open facebook": "https://facebook.com",
        "open instagram": "https://instagram.com",
        "open github": "https://github.com",
        "open stackoverflow": "https://stackoverflow.com",
        "open linkedin": "https://linkedin.com",
        "open whatsapp": "https://whatsapp.com",
        "open chatgpt": "https://chat.openai.com/chat",
        "open gemini": "https://gemini.google.com/",
        "open chatbot": "https://cdn.botpress.cloud/webchat/v2/shareable.html?botId=2b113ef8-ac77-4553-b353-7e381fcffdde"
    }

    command = command.lower()

    if command in url_map:
        webbrowser.open(url_map[command])
    elif command.startswith("play"):
        try:
            words = command.split(" ")
            if len(words) > 1:
                song = words[1]
                link = musicLibraries.musicLinks.get(song, None)
                
                if link is not None:
                    webbrowser.open(link)
                else:
                    print("..:: Song is not found in the music library. ")
            else:
                print("..:: Invalid Command. No song specified. ")
        except Exception as e:
            print(f"Error: {e}")
    else: 
        output = aiProsses(command, context)
        print(f"\nAI Response: {output}\n")

        if context is None:
            context = []

        # Ensure context is a list
        if not isinstance(context, list):
            context = []  # Reset context to an empty list if it is not a list
        
        context.append({"role": "user", "content": command})
        context.append({"role": "assistant", "content": output})

        return context

if __name__ == "__main__":

    context = None
    print("\nHi, I'm Sagar. How can I help you?\n")
    
    while True:
        command = input("==> ")
        if command.lower() != "exit":
            context = prossess_command(command, context)
        else:
            break

