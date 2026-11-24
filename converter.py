"""Simple unit converter: length, weight and temperature."""

LENGTH = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000, "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344}
WEIGHT = {"g": 0.001, "kg": 1, "oz": 0.028349523125, "lb": 0.45359237}
TO_C = {"c": lambda v: v, "f": lambda v: (v - 32) * 5 / 9, "k": lambda v: v - 273.15}
FROM_C = {"c": lambda v: v, "f": lambda v: v * 9 / 5 + 32, "k": lambda v: v + 273.15}

convert_length = lambda v, a, b: v * LENGTH[a] / LENGTH[b]
convert_weight = lambda v, a, b: v * WEIGHT[a] / WEIGHT[b]
convert_temperature = lambda v, a, b: FROM_C[b](TO_C[a](v))

CATEGORIES = {"length": (convert_length, LENGTH), "weight": (convert_weight, WEIGHT), "temperature": (convert_temperature, TO_C)}


def ask(prompt, options):
    while (choice := input(f"{prompt} ({', '.join(options)}): ").strip().lower()) not in options:
        print("  Invalid choice, try again.")
    return choice


def main():
    while True:
        func, units = CATEGORIES[ask("\nCategory", CATEGORIES)]
        try:
            value = float(input("Value: "))
        except ValueError:
            print("  Please enter a valid number.")
            continue
        a, b = ask("From", units), ask("To", units)
        print(f"{value:g} {a} = {func(value, a, b):.4g} {b}")
        if input("Convert another? (y/n): ").lower() != "y":
            break


if __name__ == "__main__":
    main()
