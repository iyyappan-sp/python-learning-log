
def email_builder(domain):
    def build_email(username):
        return f"{username}@{domain}"
    return build_email

gmail = email_builder("gmail.com")
ymail = email_builder("ymail.com")
hotmail = email_builder("hotmail.com")


print(gmail("ajith"))
print(ymail("abi"))
print(hotmail("dev"))
