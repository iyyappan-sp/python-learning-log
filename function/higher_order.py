


def build_email(username, provider):
    if provider == "gmail":
        return f"{username}@gmail.com"
    elif provider == "ymail":
        return f"{username}@ymail.com"
    elif provider == "hotmail":
        return f"{username}@hotmail.com"
    else:
        return f"{username}@exmaple.com"

print(build_email("ajith", "gmail"))
print(build_email("abi", "ymail"))
print(build_email("dev", "hotmail"))
print(build_email("tom", "unknown"))
