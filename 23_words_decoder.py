def calculate_word_value(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word = word.lower()
    v_sum = sum(alphabet.index(char) + 1 for char in word if char.isalpha())
    return v_sum

def count_words(text):
    words = text.split()
    return len(words)

def main():
    while True:
        print("\nWord Counting and Word Value Calculation Application")
        print("Paste your essay below. Press Enter twice to finish input.")
        print("Type 'exit' to quit the application.")
        print("------------------------------------------------------")

        essay_text = ''
        while True:
            line = input()
            if line.lower() == 'exit':
                print("Exiting the application...")
                return
            if not line:
                break
            essay_text += line + ' '

        word_count = count_words(essay_text.strip())
        words = essay_text.split()
        
        print("\nWord count of the entire essay: {}".format(word_count))
        print("------------------------------------------------------")
        
        print("23rd Word \t Total of characters")
        print("---------------------------------")
        
        for i in range(22, len(words), 23):
            word = words[i]
            value = calculate_word_value(word)
            print(f"{word} \t\t {value}")
        
        print("------------------------------------------------------")

        another_round = input("Press Enter to process another essay or type 'exit' to quit: ").strip().lower()
        if another_round == 'exit':
            print("Exiting the application...")
            break

if __name__ == "__main__":
    main()
