import random

secret = random.randint(1,10)
attempts = 0

while True:
    guess = int(input("เดาเลข 1-10: "))
    attempts += 1

    if guess < 1 or guess > 10:
        print("❌ ข้อมูลผิดพลาด ใส่เลข 1-10 เท่านั้น")
    elif guess < secret:
        print("⬆️ น้อยไป")
    elif guess > secret:
        print("⬇️ มากไป")
    else:
        print("🎉 ถูกต้อง!")
        print("คุณใช้ไป", attempts, "ครั้ง")
        break
