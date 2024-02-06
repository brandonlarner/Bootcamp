for num in range(1, 26):
    print(num)

for _ in range(20):
    print("Ik ben hard op weg developer te worden!")

count = 0
total = 625
while total >= 25:
    total -= 25
    count += 1
print(count)

count = 0
total = 625
divisor = 12
while total >= divisor:
    total -= divisor
    count += 1
print(count)

initial_balance = 10000  # Startsaldo
annual_interest_rate = 0.028  # Jaarlijkse rentevoet (2,8%)
years = 5  # Aantal jaren

final_balance = initial_balance * (1 + annual_interest_rate) ** years
print(f"Na {years} jaar heb je {final_balance:.2f} euro.")

years = 15  # Aantal jaren
final_balance = initial_balance * (1 + annual_interest_rate) ** years
print(f"Na {years} jaar heb je {final_balance:.2f} euro.")
