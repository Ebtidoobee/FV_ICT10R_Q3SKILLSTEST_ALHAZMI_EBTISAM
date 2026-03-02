from pyscript import document

def verify_account(event):
    # Get values from the webpage
    n = document.querySelector("#name").value
    u = document.querySelector("#user").value
    p = document.querySelector("#pass").value
    out = document.querySelector("#output")

    # Reset color to dark for errors
    out.style.color = "black"

    # 1. Check Correct format of the name (first letter capitalized)
    if not n.istitle():
        out.innerHTML = "Name is not in the correct format. Please try again!"
        return

    # 2. Username length check
    if len(u) < 7:
        out.innerHTML = "Username must contain at least 7 characters. Try again!"
        return

    # 3. Password length check
    if len(p) < 10:
        diff = 10 - len(p)
        out.innerHTML = f"Your password is too short. Add at least {diff} more character/s to proceed.<br>Try again!"
        return

    # 4. Password complexity check
    has_letter = any(char.isalpha() for char in p)
    has_number = any(char.isdigit() for char in p)
    has_capital = any(char.isupper() for char in p)

    if not (has_letter and has_number and has_capital):
        out.innerHTML = "Password must contain at least one capital letter, one letter, and one number.<br>Try again!"
        return

    # Success!
    out.style.color = "green"
    out.innerHTML = "<b>Account Created Successfully!</b>"