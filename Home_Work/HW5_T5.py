pr = [number for number in range(1,10) if number % 2 == 0]
npr = [number for number in range(1,10) if number % 2 == 1]
other = [number for number in range(1,30) if not number %2 == 0 and not number %3 == 0]

print("Parne: ", pr)
print("Neparne", npr)
print("Ne dil 2 and 3: ", other)