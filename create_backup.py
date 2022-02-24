"""file to create backups of README.md"""

def main():
    with open("./README.md", "r") as to_copy, open("./README_COPY.md", "w") as to_write:
        for line in to_copy:
            to_write.write(line)
            
if __name__ == "__main__":
    main()
