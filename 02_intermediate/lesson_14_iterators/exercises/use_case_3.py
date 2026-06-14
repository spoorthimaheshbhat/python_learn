# since I don't know classes yet I'll create a function instead

def countdown():
    counts = [3, 2, 1]
    display = iter(counts)

    while True:
        try:
            show_counts = next(display)
            print(show_counts)

        except StopIteration:
            print("Done")
            return

def main():
    countdown()

if __name__ == "__main__":
    main()
