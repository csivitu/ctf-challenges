import os
CTFD_TOKEN = os.getenv("CTFD_TOKEN", default=None)
CTFD_URL = os.getenv("CTFD_URL", default=None)
os.system(f"echo '{CTFD_URL}\n{CTFD_TOKEN}\ny' | ctf init")
blacklist = [".git", ".github", ".ctf"]
categories = [name for name in os.listdir(".") if os.path.isdir(name) and name not in blacklist]

print("Categories:")
print("\n".join(categories))

for i in categories:
    challenges = [f"{i}/{name}" for name in os.listdir(f"./{i}") if os.path.isdir(f"{i}/{name}")]
    print(f"Category {i}:")
    print("\n".join(challenges))
    for j in challenges:
        print(f"Syncing challenge {j}")
        if os.path.exists(f"{j}/challenge.yml"):
            os.system(f"ctf challenge sync '{j}'; ctf challenge install '{j}'")
