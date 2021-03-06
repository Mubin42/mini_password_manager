from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Input Master Password: ")
if master_pwd != "masterpassword":
    print("Wrong Master Password")
else:

    key = load_key() + master_pwd.encode()
    fer = Fernet(key)

    def view():

        with open('password.txt', 'r') as f:
            for line in f.readlines():
                data = (line.rstrip())
                user, mail , passw = data.split("|")
                print("User: ", user,"\nMail: ",
                      fer.decrypt(mail.encode()).decode(), "\nPass: ",
                      fer.decrypt(passw.encode()).decode(),"\n-------------------------")

    def add():
        name = input("Account Name : ")
        mail = input("Mail ID: ")
        pwd = input("Password : ")
        with open('password.txt', 'a') as f: #w=override, r=readmode, a=append
            f.write(name + " | " + fer.encrypt(mail.encode()).decode() + " | " +
                    fer.encrypt(pwd.encode()).decode() + "\n")

    while True:
        mode = input("Press 'add' command to add password \n"
                     "Press 'view' command to view password \n"
                     "press 'q' command to exit \n"
                     "Command: ")
        if mode == "q":
            break

        if mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid Mode")
            continue

