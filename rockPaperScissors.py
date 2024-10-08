import random

# from menuProjectsPrompt import threeOptionsMenu

# if __name__ == "__main__":
#     threeOptionsMenu("First", "Play Rock-Paper-Scissors", "Play Suit", "keguba", "Suit")


def system(choices, text1):
    playerWins = 0
    computerWins = 0
    print(text1)
    while True:
        try:
            howMany = int(input("Berapa kali Anda ingin bermain (Masukan Angka): "))
            break
        except ValueError:
            print("Tolong jangan memasukkan huruf!\n")
    for x in range(howMany):
        while True:
            try:
                print(
                    f"\nPertandingan Ke-{x+1}\nPilihan:\n1. {choices[0]}\n2. {choices[1]}\n3. {choices[2]}"
                )
                playerChoice = int(input("Silahkan pilih nomor pilihan Anda: "))
                if not 0 < playerChoice < 4:
                    print("Tolong pilih nomor yang telah disediakan")
                else:
                    break
            except ValueError:
                print("Tolong Masukkan Angka!\n")
        computerChoice = random.randrange(1, 4)
        print(
            f"\nPlayer: {choices[playerChoice - 1]} Vs Computer: {choices[computerChoice - 1]}"
        )
        if playerChoice == 1 and computerChoice == 2:
            outcome = 2
        elif playerChoice == 1 and computerChoice == 3:
            outcome = 1
        elif playerChoice == 2 and computerChoice == 1:
            outcome = 1
        elif playerChoice == 2 and computerChoice == 3:
            outcome = 2
        elif playerChoice == 3 and computerChoice == 1:
            outcome = 2
        elif playerChoice == 3 and computerChoice == 2:
            outcome = 1
        else:
            outcome = 0

        match outcome:
            case 0:
                pass
            case 1:
                playerWins += 1
            case 2:
                computerWins += 1
    print()
    print(f"Hasil:\nPlayer: {playerWins} & Computer: {computerWins}")
    if playerWins == computerWins:
        print("Hasilnya adalah seri!!!")
    elif playerWins > computerWins:
        print("Selamat Anda memenangkan permainan ini!!!")
    else:
        print("Anda kalah :(")
    print()


def keguba():
    choicesKeguba = ["Kertas", "Gunting", "Batu"]
    textKeguba = "\n--- Selamat datang di permainan Kertas-Gunting-Batu ---\nAturan Main:\n- Kertas kalah oleh Gunting\n- Gunting kalah oleh Batu\n- Batu kalah oleh Kertas"
    system(choicesKeguba, textKeguba)


def suit():
    choicesSuit = ["Ibu Jari", "Jari Kelingking", "Jari Telunjuk"]
    textsuit = "\n--- Selamat datang di permainan Suit ---\nAturan Main:\n- Ibu Jari kalah oleh Kelingking\n- Jari Kelingking kalah oleh Jari Telunjuk\n- Jari Telunjuk kalah oleh Ibu Jari"
    system(choicesSuit, textsuit)


def main():
    print("=== Selamat Datang di proyek 1 saya!! ===")
    while True:
        match input(
            "Menu:\n1. Kertas-Gunting-Batu\n2. Suit\n3. Keluar Program\nSilahkan pilih nomor menu: "
        ):
            case "1":
                keguba()
            case "2":
                suit()
            case "3":
                break
            case _:
                print("Pilih nomor menu yang telah disediakan!!!\n")


if __name__ == "__main__":
    main()
