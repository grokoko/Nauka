# Turniej wiedzy
# Gra sprawdzająca wiedzę ogólną, odczytująca dane ze zwykłego pliku tekstowego

import sys, shelve

def open_file(file_name, mode):
    """Otwórz plik."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Nie można otworzyć pliku", file_name, "Program zostanie zakończony.\n", e)
        input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Zwróć kolejny wiersz pliku kwiz po sformatowaniu go."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Zwróć kolejny blok danych z pliku kwiz."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    points = next_line(the_file)
        
    explanation = next_line(the_file) 

    return category, question, answers, correct, points, explanation

def welcome(title):
    """Przywitaj gracza i pobierz jego nazwę."""
    print("\t\t Witaj w turnieju wiedzy!\n")
    print("\t\t", title, "\n")
 
def wynik(score):
    if score == 30:
        print("Gratulacje, udało ci się osiągnąć maksymalną liczbę punktów. W nagrodę program zapamięta twoje imię.")
        s = shelve.open("wyniki.dat")
        name = input("Jak masz na imię?")
        s[name] = [str(score)]
        s.sync()
        print(name, ":", s[name])
        s.close

def main():
    trivia_file = open_file("zad4kwiz.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # pobierz pierwszy blok
    category, question, answers, correct, points, explanation = next_block(trivia_file)
    while category:
        # zadaj pytanie
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # uzyskaj odpowiedź
        answer = input("Jaka jest Twoja odpowiedź?: ")

        # sprawdź odpowiedź
        if answer == correct:
            print("\nOdpowiedź prawidłowa!", end=" ")
            score += int(points)
        else:
            print("\nOdpowiedź niepoprawna.", end=" ")
        print(explanation)
        print("Wynik:", score, "\n\n")

        # pobierz kolejny blok
        category, question, answers, correct, points, explanation = next_block(trivia_file)

    trivia_file.close()

    print("To było ostatnie pytanie!")
    print("Twój końcowy wynik wynosi", score)

    wynik(score)
 
main()  
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
