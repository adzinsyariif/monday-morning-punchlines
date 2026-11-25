import os

ENTRY = "My Monday morning alarm doesn't wake me — it opens negotiations, and I always lose to a snooze button with tenure."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
