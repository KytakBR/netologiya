import os

def main():
    os.system("git clean -f")
    os.system("git stash")

if __name__ == "__main__":
    main()