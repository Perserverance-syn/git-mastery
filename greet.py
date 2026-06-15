def greet(name):
    """Return a friendly greeting."""
    if not name:
        return "Hello, stranger!"
    return f"Hello, {name}! Welcome to Git Mastery."

if __name__ == "__main__":
    print(greet("Synch"))
