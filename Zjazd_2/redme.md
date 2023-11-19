Scenariusz Testu 1/a:    

Uruchomienie przeglądarki:
    Uruchom przeglądarkę Firefox.

Otwarcie strony logowania:
    Przejdź do strony logowania, używając linku "https://1login.wp.pl/zaloguj/dodaj?client_id=wp-backend&login_challenge=Cj4KJDExZTc5M2IyZjQxNDg0NDA4OTI3NzYyZTI4Mjc2NTVmOGIzZhDC3-eqBhoQCgp3cC1iYWNrZW5kEgJ2MhIgQw-ucRfu4d1kzKDURpdpE4j1PSK_eHh2T1pIE-S1YGg".

Wprowadzenie danych logowania:
    Wpisz poprawny adres e-mail w polu "login".
    Wpisz poprawne hasło w polu "password".
    Naciśnij klawisz "Enter" w polu hasła.

Oczekiwanie:
    Poczekaj 3 sekundy, aby dać systemowi czas na przetworzenie logowania.

Sprawdzenie wyniku:
    Jeśli w kodzie źródłowym strony widnieje komunikat "Nieprawidłowy adres e‑mail lub hasło", to uznaj, że logowanie zakończyło się błędem.
        Wypisz w konsoli: "Błąd logowania!"
    W przeciwnym razie uznaj, że logowanie się powiodło.
        Wypisz w konsoli: "Zalogowano".

Zamknięcie przeglądarki:
    Zamknij przeglądarkę.

Scenariusz Testu 2/b:

Uruchomienie przeglądarki:
        Uruchom przeglądarkę Chrome.

Otwarcie kalkulatora kosztów paliwa:
    Przejdź do strony kalkulatora kosztów paliwa, używając linku "https://www.calculator.net/fuel-cost-calculator.html".

Wprowadzenie danych:
    Wpisz odległość podróży jako 600 km w polu "tripdistance".
        Wypisz w konsoli: "Ustawiono odległość na 600 km".
    Wpisz efektywność paliwa jako 7 litrów na 100 km w polu "fuelefficiency".
        Wypisz w konsoli: "Ustawiono efektywność paliwa na 7 litrów na 100 km".
    Wpisz cenę paliwa jako 5 dolarów za litr w polu "gasprice".
        Wypisz w konsoli: "Ustawiono cenę paliwa na 5 dolarów za litr".

Obliczenia:
    Naciśnij przycisk "x" w celu wykonania obliczeń.
        Wypisz w konsoli: "Obliczanie...".

Oczekiwanie:
    Poczekaj 3 sekundy, aby dać systemowi czas na przetworzenie obliczeń.

Sprawdzenie wyniku:
    Pobierz wynik z pola o klasie "verybigtext".
    Jeśli wynik jest równy "This trip will require 42 liters of fuel, which amounts to a fuel cost of $210.", to uznaj, że obliczenia są poprawne.
        Wypisz w konsoli: "Wynik jest poprawny".
    W przeciwnym razie uznaj, że obliczenia są niepoprawne.
        Wypisz w konsoli: "Wynik jest niepoprawny".

Zamknięcie przeglądarki:
    Zamknij przeglądarkę.