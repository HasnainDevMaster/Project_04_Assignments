# Define a sentence starter
SENTENCE_START: str = "Mastering Python takes creativity. With the right mindset, you can build a "

def main():
    # Get the three inputs from the user
    adjective: str = input("Please type an adjective and press enter: ")  
    noun: str = input("Please type a noun and press enter: ")  
    verb: str = input("Please type a verb and press enter: ")  

    # Construct and print the final sentence
    print(SENTENCE_START + adjective + " " + noun + " that can " + verb + "!") # smart, chatbot, learn

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
