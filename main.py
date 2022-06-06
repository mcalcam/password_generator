from generator import Generator

def main():
    gen = Generator()
    num_of_passwords = int(input('please enter number of passwords to generate: '))
    i = 0
    while i < num_of_passwords:
        print(gen.generate_passowrd())
        i += 1

if __name__ == "__main__":
    main()