def response(hey_bob: str) -> str:

    clean_hey_bob = hey_bob.replace(" ", "").replace("?", "").replace("!", "")

    if clean_hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if hey_bob.strip(" ").endswith("?"):
        return "Sure."
    if clean_hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob.count(" ") == len(hey_bob) or hey_bob.find("\t") >= 0:
        print(hey_bob)
        return "Fine. Be that way!"
    else:
        return "Whatever."