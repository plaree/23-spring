# Problem Seti 2, adamAsmaca.py
# İsim: Ahmet Eralp Demirer
# Ortak çalışanlar: -
# Harcanan zaman: 4-5 saat

# Adam Asmaca Oyunu
#------------------------------------
# Yardımcı kod
# Bu yardımcı kodu anlamanıza gerek yok,
# ama fonksiyonları nasıl kullanacağını bilmeniz gerekecek
# (dökümanları okuduğunuzdan emin olun!)
import random
import string

WORDLIST_FILENAME = "kelimeler.txt"


def load_words():
    """
    Geçerli kelimelerin bir listesini döndürür.
    Kelimeler küçük harf dizileridir.
    
     Kelime listesinin boyutuna bağlı olarak,
     bu fonksiyonun tamamlanması biraz zaman alabilir.
    """
    print("Dosyadan kelime listesi yükleniyor...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "kelime yüklendi.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): kelime listesi(strings)
    
    Kelime listesinden rastgele bir kelime döndürür
    """
    return random.choice(wordlist)

# yardımcı kodun sonu

#------------------------------------

# Programdaki herhangi bir yerden erişilebilmesi için
# kelime listesini değişken kelime listesine yükleyin
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, kullanıcının tahmin ettiği kelime;
    tüm harflerin küçük olduğunu varsayar
    letter_guessed: şimdiye kadar hangi harflerin tahmin edildiği (harflerin listesi);
     tüm harflerin küçük olduğunu varsayar
     returns: boolean, secret_word'ün tüm harfleri letter_guessed içindeyse True;
     Aksi takdirde yanlış
    '''
# BURAYA KODUNUZU GİRİN VE "pass"ı SİLİN
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
   # pass



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, kullanıcının tahmin ettiği kelime
    letter_guessed: şimdiye kadar hangi harflerin tahmin edildiği (harflerin listesi)
    returns: harflerden, alt çizgilerden (_) ve şu ana kadar secret_word
     içindeki hangi harflerin tahmin edildiğini gösteren boşluklardan oluşan dize.
    '''
# BURAYA KODUNUZU GİRİN VE "pass"ı SİLİN
    guessed_word = ""  

    
    for letter in secret_word: 
        if letter in letters_guessed:   
            guessed_word += letter  
        else:
            guessed_word += "_"  

    return guessed_word
    

    #pass



def get_available_letters(letters_guessed):
    '''
    letter_guessed: şimdiye kadar hangi harflerin tahmin edildiği (harflerin listesi)
    returns: dize (harfler), hangi harflerin henüz tahmin edilmediğini temsil eden harflerden oluşur.
    '''
# BURAYA KODUNUZU GİRİN VE "pass"ı SİLİN
    all_letters = string.ascii_lowercase
    available_letters = ''
    for letter in all_letters:
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters

    #pass
    
    

def adamAsmaca(secret_word):
    '''
    secret_word: string, tahmin edilecek gizli kelime.
    
     Etkileşimli bir Adam Asmaca oyununu başlatır.
    
     * Oyunun başında, kullanıcıya secret_word'ün kaç harf içerdiğini
        ve kaç tahminle başladığını bildirin.
      
     * Kullanıcı 6 tahminle başlamalıdır

     * Her turdan önce kullanıcıya kaç tahmin kaldığını ve
        kullanıcının henüz tahmin etmediği harfleri göstermelisiniz.
    
     * Kullanıcıdan tur başına bir tahmin vermesini isteyin.
        Kullanıcının bir mektup yazdığından emin olmayı unutmayın!
    
     * Kullanıcı, her tahminden hemen sonra tahminlerinin bilgisayarın
        kelimesinde görünüp görünmediği hakkında geri bildirim almalıdır.

     * Her tahminden sonra, o ana kadar kısmen tahmin edilen kelimeyi
         kullanıcıya göstermelisiniz.
    
     Problem yazımında detaylandırılan diğer sınırlamaları takip eder.
    '''
# BURAYA KODUNUZU GİRİN VE "pass"ı SİLİN
    print("Adam Asmaca oyununa hoşgeldiniz!")
    print("{} harf uzunluğunda bir kelime düşünüyorum" .format(len(secret_word)))
    
    guesses = 6
    warns = 3
    print("{} uyarınız kaldı" .format(warns))
    print("-------------")
    print("{} tahmininiz kaldı" .format(guesses))
    
    letters_guessed = []
                              #baslangic
    while guesses > 0:
        
        print("Mevcut harfler:", get_available_letters(letters_guessed))
        guess = input("Lütfen bir harf tahmin edin: ").lower()
        
        if guess in secret_word and guess not in letters_guessed:
            letters_guessed.append(guess)
            print("İyi tahmin:")
        
        elif guess in letters_guessed:
            print("Hata! Bu harfi zaten tahmin ettiniz. {} uyarınız kaldı." .format(warns))
        
        elif len(guess) != 1 or not guess.isalpha():
            warns -= 1
            print("Hata! Bu geçerli bir harf değil. {} uyarınız kaldı:".format(warns))
            if warns == 0:
                guesses -= 1
        
        else:
            guesses -= 1
            letters_guessed.append(guess)
            print("Hata! O harf bu kelimede yok. {} tahminin kaldı." .format(guesses))
        print(get_guessed_word(secret_word, letters_guessed))
        print("-------------")
        
        if is_word_guessed(secret_word, letters_guessed):
            print("Tebrikler, kazandınız!")
            return
    print("Üzgünüm, tahminleriniz tükendi. Kelime Başkaydı: " + secret_word)

    #pass



# Adam asmaca işlevinizi tamamladığınızda, dosyanın
#en altına gidin ve test edilecek ilk iki satırın yorumunu kaldırın
# (ipucu: kendi testinizi yaparken kendi secret_word'ünüzü
# seçmek isteyebilirsiniz)

# -----------------------------------

'''
ILK KISIM - IKINCI KISIM
'''



def match_with_gaps(my_word, other_word):
    '''
    my_word: _ karakterli dize, gizli kelimenin geçerli tahmini
    other_word: string, normal İngilizce kelime
    returns: boolean, True, eğer my_word'ün tüm gerçek harfleri other_word'ün karşılık gelen harfleriyle eşleşiyorsa veya harf özel sembol _ ise ve my_word ile other_word aynı uzunluktaysa; Aksi takdirde False:
    '''
# BURAYA KODUNUZU GİRİN VE "pass"ı SİLİN
    if len(my_word) != len(other_word): 
        return False
    for i in range(len(my_word)):
        if my_word[i] == '_': 
            continue
        elif my_word[i] != other_word[i]:  
            return False
    return True  
    #pass



def show_possible_matches(my_word):
    '''
    my_word: _ karakterli dize, gizli kelimenin geçerli tahmini
    returns: hiçbir şey, ancak kelime listesindeki my_word ile eşleşen
        her kelimeyi yazdırmalıdır.
    adamAsmaca ile bir harf tahmin edildiğinde, o harfin gizli kelimede
        geçtiği tüm pozisyonların ortaya çıktığını unutmayın.
    Bu nedenle, gizli harf(_ ) zaten ortaya çıkmış olan kelimedeki
     harflerden biri olamaz.
    '''
# BURAYA KODUNUZU GİRİN VE "pass"ı SİLİN
    possible_matches = []
    for word in wordlist:
        
        if len(word) == len(my_word):
            
            match = True
            for i in range(len(word)):
                if my_word[i] != "_":
                    if my_word[i] != word[i]:
                        match = False
                        break
            
            if  match:
                
                possible_matches.append(word)
    return possible_matches

    #pass



def adamAsmaca_ipuclu(secret_word):
    '''
    secret_word: string, tahmin edilecek gizli kelime.
    
     Etkileşimli bir Adam Asmaca oyunu başlatır.
    
     * Oyunun başında, kullanıcıya secret_word'ün kaç harf içerdiğini ve
        kaç tahminle başladığını bildirin.
      
     * Kullanıcı 6 tahminle başlamalıdır
    
     * Her turdan önce kullanıcıya kaç tahmin kaldığını ve kullanıcının
        henüz tahmin etmediği harfleri göstermelisiniz.
    
     * Kullanıcıdan tur başına bir tahmin vermesini isteyin.
        Kullanıcının bir harf tahmin ettiğini kontrol ettiğinizden emin olun.
      
     * Kullanıcı, her tahminden hemen sonra tahminlerinin bilgisayarın
        kelimesinde görünüp görünmediği hakkında geri bildirim almalıdır.

     * Her tahminden sonra, o ana kadar kısmen tahmin edilen kelimeyi
         kullanıcıya göstermelisiniz.
      
     * Tahmin sembolü * ise, kelime listesindeki mevcut tahmin edilen
        kelimeyle eşleşen tüm kelimeleri yazdırın.
    
     Problem yazımında detaylandırılan diğer sınırlamaları takip eder.
    '''
# BURAYA KODUNUZU GİRİN VE "pass"ı SİLİN

    print("Adam Asmaca oyununa hoşgeldiniz!")
    print("{} harf uzunluğunda bir kelime düşünüyorum. ".format(len(secret_word)))

    guesses = 6
    letters_guessed = []

    print("-------------")
    print("{} tahmininiz kaldı".format(guesses))

    while guesses > 0:
        print("Mevcut harfler:", get_available_letters(letters_guessed))
        guess = input("Lütfen bir harf tahmin edin: ").lower()

        if guess in secret_word and guess not in letters_guessed:
            letters_guessed.append(guess)
            print("İyi tahmin:")

        elif guess == "*":
            print("Olası kelime eşleşmeleri şunlardır: ", show_possible_matches(get_guessed_word(secret_word, letters_guessed)))

        elif guess in letters_guessed:
            print("Hata! Bu harfi zaten tahmin ettiniz.")
    
        elif len(guess) != 1 or not guess.isalpha():
            guesses -= 1
            print("Hata! Bu geçerli bir harf değil.")
            if guesses == 0:
                break

        else:
            guesses -= 1
            letters_guessed.append(guess)
            print("Hata! O harf bu kelimede yok. {} tahmininiz kaldı.".format(guesses))

        print(get_guessed_word(secret_word, letters_guessed))
        print("-------------")

        if is_word_guessed(secret_word, letters_guessed):
            print("Tebrikler, kazandınız!")
            return

    print("Üzgünüm, tahminleriniz tükendi. Kelime Başkaydı: " + secret_word)


    #pass



# adamAsmaca_ipuclu işlevinizi tamamladığınızda, yukarıdaki adam asmaca
# fonksiyonunu çalıştırmak için kullanılan benzer iki satırı yorumlayın ve
# ardından bu iki satırın yorumunu kaldırın ve test etmek için bu dosyayı çalıştırın!
# İpucu: Test ederken kendi secret_word'ünüzü seçmek isteyebilirsiniz.


if __name__ == "__main__":
    #pass

    # 2. bölümü test etmek için yukarıdaki pass satırında # işaretini kullanın ve aşağıdaki iki satırda # işaretini silin
   
    #secret_word = choose_word(wordlist)
    #adamAsmaca(secret_word)

###############
    
# 3. bölümü test etmek için yukarıdaki satırlarlarda yeniden # işaretini kullanın ve aşağıdaki iki satırda # işaretini silin

    secret_word = choose_word(wordlist)
    adamAsmaca_ipuclu(secret_word)
