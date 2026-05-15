def process_input(user_input):
    if user_input is None:
        return ""
    return user_input.strip().lower()


if __name__ == "__main__":
    print(process_input(None))