def gmail_email(username, domain="gmail.com"):
    return f"{username}@{domain}"
def ymail_email(username, domain="ymail.com"):
    return f"{username}@{domain}"
def hotmail_email(username, domain="hotmail.com"):
    return f"{username}@{domain}"


def build_email(username, email_func):
    return email_func(username)


print(build_email("ajith", gmail_email))
print(build_email("abi", ymail_email))
print(build_email("dev", hotmail_email))
