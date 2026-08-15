


from functools import partial

def create_email(username, domain):
    return f"{username}@{domain}"

gmail = partial(create_email, domain="gmail.com")
ymail = partial(create_email, domain="ymail.com")

print(gmail("ajith"))
print(ymail("tom"))
