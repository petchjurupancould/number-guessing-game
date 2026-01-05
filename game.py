import random

while True:
    secret = random.randint(1, 10)
    attempts = 0
    max_attempts = 5

    print("🎮 เกมทายเลข 1 - 10")
    print("คุณมี", max_attempts, "ครั้ง")

    while attempts < max_attempts:
        try:
            guess = int(input("เดาเลข: "))
        except:
            print("❌ กรุณาใส่ตัวเลขเท่านั้น")
            continue

        if guess < 1 or guess > 10:
            print("❌ ใส่เลข 1 ถึง 10 เท่านั้น")
            continue

        attempts += 1

        if guess < secret:
            print("⬆ น้อยไป")
        elif guess > secret:
            print("⬇ มากไป")
        else:
            print("🎉 ถูกต้อง! ใช้ไป", attempts, "ครั้ง")
            break

    if guess != secret:
        print("💥 แพ้แล้ว! เลขที่ถูกคือ", secret)

    play_again = input("เล่นอีกไหม? (y/n): ")
    if play_again.lower() != "y":
        print("👋 ขอบคุณที่เล่น!")
        break
