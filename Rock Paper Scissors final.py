import random

OPTIONS = ["rock", "paper", "scissors"]

def decide(player, computer):
    if player == computer:
        return "tie"

    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    return "player" if wins[player] == computer else "computer"

def main():
    print("🎮 Rock Paper Scissors — Best of N Rounds 🎮")

    try:
        rounds = int(input("📌 Enter number of rounds (odd number recommended): ").strip())
        if rounds <= 0:
            print("⚠️ Number of rounds must be positive.")
            return
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    player_score = 0
    comp_score = 0
    current_round = 1

    while current_round <= rounds:
        print(f"\n🕹️ Round {current_round} — choose ✊ rock, ✋ paper, or ✌️ scissors:")
        player = input("> ").strip().lower()

        if player not in OPTIONS:
            print("❗ Invalid choice — try again.")
            continue

        computer = random.choice(OPTIONS)
        print(f"🤖 Computer chose: {computer}")

        result = decide(player, computer)

        if result == "tie":
            print("😐 It's a tie!")
        elif result == "player":
            print("🎉 You win this round!")
            player_score += 1
        else:
            print("💻 Computer wins this round!")
            comp_score += 1

        print(f"📊 Score — You: {player_score} | Computer: {comp_score}")
        current_round += 1

    print("\n🏁 Final Result:")
    if player_score > comp_score:
        print("🏆 You won the match! 🎉")
    elif player_score < comp_score:
        print("🤖 Computer won the match!")
    else:
        print("🤝 The match is a tie.")

if __name__ == "__main__":
    main()
