import csv

messy = [
    "  apple , 3.50",
    "BANANA,2.1",
    " milk ,  1.99 ",
    "Apple , 3.50",
    "bread,",
    "cheese , abc",
]

def clean_prices(lines):
    seen = set()
    clean = []
    skipped = []
    for line in lines:
        parts = line.split(",")
        if len(parts) != 2:
            skipped.append(line)
            continue
        name = parts[0].strip().title()
        try:
            price = round(float(parts[1].strip()), 2)
        except ValueError:
            skipped.append(line)
            continue
        if name in seen:
            continue
        seen.add(name)
        clean.append((name, price))
    clean.sort()
    return clean, skipped

clean, skipped = clean_prices(messy)

with open("/storage/emulated/0/Download/clean_prices.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Price"])
    writer.writerows(clean)

print("Saved", len(clean), "clean rows to clean_prices.csv")
print("Skipped", len(skipped), "bad rows:")
for s in skipped:
    print(" -", s)
print("Total value:", round(sum(p for _, p in clean), 2))
