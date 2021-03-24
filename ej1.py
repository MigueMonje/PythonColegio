
def main(r):
    last = 0
    current = 1
    print(last)
    for _ in range(r):
        print(current)
        tmplast = current
        current += last
        last = tmplast
if __name__ == "__main__":
    main(1000)