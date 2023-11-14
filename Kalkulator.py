def calculator():
    print("Witaj w kalkulatorze!")
    while True:
        print("Wybierz rodzaj operacji matematycznej:")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print("5. Wyjście")
        
        choice = input("\nWybierz opcję (1/2/3/4/5): ")
        
        if choice == '5':
            print("Dziękujemy za korzystanie z kalkulatora!")
            break
        
        try:
            num1 = float(input("\nPodaj pierwszą liczbę: "))
            num2 = float(input("Podaj drugą liczbę: "))
            
            if choice == '1':
                print(num1, "+", num2, "=", num1 + num2)
            elif choice == '2':
                print(num1, "-", num2, "=", num1 - num2)
            elif choice == '3':
                print(num1, "*", num2, "=", num1 * num2)
            elif choice == '4':
                if num2 == 0:
                    print("Nie można dzielić przez zero!")
                else:
                    print(num1, "/", num2, "=", num1 / num2)
            else:
                print("Nieprawidłowa opcja!")
                
        except ValueError:
            print("Błędne dane! Spróbuj ponownie.")
            
calculator()