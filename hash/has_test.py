from passlib.context import CryptContext


contexto_senha = CryptContext(schemes=['bcrypt'], deprecated='auto')

target_hash = "$2b$12$XfxESPJe0Fc8jYtBbtJss.nd1/Epv6PfLy7bpHHd0MnK5Uj/3AbQG"

wordlist = [
    "senha",
    "123456",
    "minhasenha",
    "adminadmin",
    "mudar1234"
]

print("--- Starting Hash Cracking ---")
print(f"Target Hash: {target_hash}\n")

password_found = False
for attempt in wordlist:
    if contexto_senha.verify(attempt, target_hash):
        print("✅ **SUCCESS!**")
        print(f"The password for the hash is: **{attempt}**")
        password_found = True
        break
    else:
        print(f"❌ Failed attempt: '{attempt}'")

if not password_found:
    print("\n⚠️ **FAILURE!**")
    print("The password was not found in the provided wordlist.")

print("\n--- Cracking Finished ---")