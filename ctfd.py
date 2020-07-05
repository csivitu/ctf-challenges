import os
import re

CTFD_TOKEN = os.getenv("CTFD_TOKEN", default=None)
CTFD_URL = os.getenv("CTFD_URL", default=None)

if not CTFD_TOKEN or not CTFD_URL:
    exit(1)

os.system(f"echo '{CTFD_URL}\n{CTFD_TOKEN}\ny' | ctf init")

denylist_regex = r'\..*'
categories = [name for name in os.listdir(".") if os.path.isdir(name) and not re.match(denylist_regex, name)]

print("Categories: " + ", ".join(categories))

for category in categories:
    challenges = [f"{category}/{name}" for name in os.listdir(f"./{category}") if os.path.isdir(f"{category}/{name}")]
    print(f"\nCategory {category}:")
    if challenges != []:
        print("\n".join(challenges))
    else:
        print("None")

    for challenge in challenges:
        if os.path.exists(f"{challenge}/challenge.yml"):
            print(f"Syncing challenge: {challenge}")
            os.system(f"ctf challenge sync '{challenge}'; ctf challenge install '{challenge}'")
