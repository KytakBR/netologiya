import argparse
import os

def main(tag: str):
    os.system("git checkout prd")
    os.system("git merge dev")
    os.system(f"git tag -a {tag} -m 'created tag'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('tag', type=str, help='Git tag.')
    args = parser.parse_args()
    main(args.tag)