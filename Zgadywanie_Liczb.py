import random

def guess_game():
    print("Witaj w grze w zgadywanie liczb!")
    play_again = 't'
    
    while play_again == 't':
        secret_number = random.randint(1, 100)
        attempts = 0
        
        while attempts < 5:
            try:
                guess = int(input("Podaj liczbę od 1 do 100: "))
                
                if guess == secret_number:
                    print("Brawo! Zgadłeś liczbę w", attempts+1, "próbach!")
                    break
                elif guess < secret_number:
                    print("Liczba jest za mała. Spróbuj ponownie.")
                else:
                    print("Liczba jest za duża. Spróbuj ponownie.")
                    
                attempts += 1
                
            except ValueError:
                print("To nie jest liczba. Spróbuj ponownie.")
                
        if attempts == 5:
            print("Niestety, nie udało Ci się odgadnąć liczby. Była to liczba", secret_number, ".")
            
        play_again = input("Czy chcesz zagrać ponownie? (t/n) ")
        
    print("Dziękujemy za grę!")
    
guess_game()
