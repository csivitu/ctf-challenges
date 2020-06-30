import os
TOKEN = os.getenv("TOKEN", default=None)
URL = os.getenv("URL", default=None)
os.system(f"echo '{URL}\n{TOKEN}\ny' | ctf init")
blacklist = [".git", ".github", ".ctf"]
categories = [name for name in os.listdir(".") if os.path.isdir(name) and name not in blacklist]
for i in categories:
    challenges = [f"{i}/{name}" for name in os.listdir(f"./{i}") if os.path.isdir(f"{i}/{name}")]
    for j in challenges:
        if os.path.exists(f"{j}/challenge.yml"):
            os.system(f"ctf challenge sync {j}; ctf challenge install {j}")