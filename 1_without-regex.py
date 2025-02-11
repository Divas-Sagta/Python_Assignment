def validate_ipv4_no_regex(ip):
    parts = ip.split(".")

    if len(parts) != 4:
        return "Invalid IP format. IPv4 should be in 'x.x.x.x' format where x is 0-255."

    try:
        octets = [int(part) for part in parts]
    except ValueError:
        return "Invalid IP: Each octet should be a number."

    if any(octet < 0 or octet > 255 for octet in octets):
        return "Invalid IP: Each octet must be between 0-255."

    if octets[0] == 10 or (octets[0] == 172 and 16 <= octets[1] <= 31) or (octets[0] == 192 and octets[1] == 168):
        return f"Valid IPv4: {ip} (Private IP)"
    else:
        return f"Valid IPv4: {ip} (Public IP)"

def validate_gmail_no_regex(email):
    if "@gmail.com" not in email:
        return "Invalid Email: A valid Gmail should contain '@gmail.com'."

    username, domain = email.split("@", 1)

    if domain != "gmail.com":
        return "Invalid Email: Must end with '@gmail.com'."

    allowed_chars = set("abcdefghijklmnopqrstuvwxyz0123456789._%+-")
    
    if any(char not in allowed_chars for char in username):
        return "Invalid Email: Username should contain only lowercase letters, numbers, and allowed symbols."

    return f"Valid Gmail: {email}"


