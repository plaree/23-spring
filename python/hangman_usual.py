import random
import string

WORDLIST_FILENAME = "kelimeler.txt"

def load_words():
    print("Dosyadan kelime listesi yükleniyor...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "kelimeler yüklendi.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

# ----------------------------------------------------

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ""  

    for letter in secret_word: 
        if letter in letters_guessed:   
            guessed_word += letter + " "  
        else:
            guessed_word += "_ "  

    return guessed_word

def get_available_letters(letters_guessed):
    all_letters = string.ascii_lowercase
    available_letters = ''
    for letter in all_letters:
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters

def adamAsmaca(secret_word):
    print("Adam Asmaca'ya Hoşgeldiniz!")
    print("Ben bir kelime seçeceğim ve sizin tahmin etmenizi isteyeceğim.")
    print("Kelimenin uzunluğu:", len(secret_word))
    print("Tahmin hakkınız: 6")
    print("Başlıyoruz!")
    print("-------------")
    guesses = 6
    letters_guessed = []

    while guesses > 0:
        print("Kalan tahmin sayısı:", guesses)
        print("Henüz tahmin edilmemiş harfler:", get_available_letters(letters_guessed))
        guess = input("Bir harf tahmin edin: ").lower()
        if guess in secret_word and guess not in letters_guessed:
            letters_guessed.append(guess)
            print("Tebrikler! Tahmininiz doğru.")
        elif guess in letters_guessed:
            print("Üzgünüm, bu harfi zaten tahmin ettiniz. Lütfen başka bir harf deneyin.")
        else:
            guesses -= 1
            letters_guessed.append(guess)
            print("Üzgünüm, tahmininiz yanlış.")
        print(get_guessed_word(secret_word, letters_guessed))
        print("-------------")
        if is_word_guessed(secret_word, letters_guessed):
            print("Tebrikler, kazandınız!")
            return
    print("Maalesef, kaybettiniz. Doğru kelime: " + secret_word)

if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    adamAsmaca(secret_word)