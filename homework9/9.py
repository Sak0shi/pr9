import re

def parse_email(email):
    """Разбирает email на имя пользователя и доменное имя."""
    match = re.match(r"^(.+?)@(.+)$", email) 
        username = match.group(1)
        domain = match.group(2)
        return username, domain
    else:
        return None, None 


email = input("Введите email: ")
username, domain = parse_email(email)

if username and domain:
    print(f"Имя пользователя: {username}")
    print(f"Доменное имя: {domain}")
else:
    print("Некорректный формат email.")

