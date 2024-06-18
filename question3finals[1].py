import time

def typing_challenge(text):
    print("Welcome to the Typing Challenge!")
    print("Type the following text as fast as you can. Press Enter when you're done.")
    print(text)
    
    input("Press Enter to start typing...")
    
    start_time = time.time()
    user_input = input("Your text: ")
    end_time = time.time()
    
    typing_time = end_time - start_time
    accuracy = calculate_accuracy(text, user_input)
    
    print("\nTyping time:", round(typing_time, 2), "seconds")
    print("Accuracy:", accuracy, "%")
    
def calculate_accuracy(text, user_input):
    correct_chars = sum(1 for x, y in zip(text, user_input) if x == y)
    accuracy = (correct_chars / len(text)) * 100
    return round(accuracy, 2)

def main():
    text_to_type = "The quick brown fox jumps over the lazy dog."
    typing_challenge(text_to_type)

if __name__ == "__main__":
    main()