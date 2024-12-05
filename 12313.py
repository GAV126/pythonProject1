filenames = ["cats.txt", "dogs.txt"]
for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
       with open(filename) as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
          print(f"Sorry, I can't find {filename}.")

print("--------------------------------------------------")