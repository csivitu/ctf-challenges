import os
import re
import threading
import yaml

def change_state(waves, state):
    if state not in ['visible', 'hidden']:
        raise Exception("state must be 'visible' or 'hidden'")

    challenge_waves = open('challenge-waves.yml').read()
    challenge_waves = yaml.load(challenge_waves, Loader=yaml.FullLoader)

    visible = {
        "crypto": [],
        "forensics": [],
        "linux": [],
        "miscellaneous": [],
        "osint": [],
        "pwn": [],
        "reversing": [],
        "web": [],
    }

    for wave in waves:
        for category in challenge_waves[wave]:
            for challenge in challenge_waves[wave][category]:
                chall = open(f'{category}/{challenge}/challenge.yml', 'r')

                challenge_yml = yaml.load(chall, Loader=yaml.FullLoader)
                challenge_yml['state'] = state

                if state == 'visible':
                    visible[category].append(challenge_yml['name'])

                chall = open(f'{category}/{challenge}/challenge.yml', 'w')

                yaml.dump(challenge_yml, chall, sort_keys=False)

    return visible

# Initialize ctfcli with the CTFD_TOKEN and CTFD_URL.
def init():
    CTFD_TOKEN = os.getenv("CTFD_TOKEN", default=None)
    CTFD_URL = os.getenv("CTFD_URL", default=None)

    if not CTFD_TOKEN or not CTFD_URL:
        exit(1)

    os.system(f"echo '{CTFD_URL}\n{CTFD_TOKEN}\ny' | ctf init")


# Each category is in it's own directory, get the names of all directories that do not begin with '.'.
def get_categories():
    denylist_regex = r'\..*'

    categories = [name for name in os.listdir(".") if os.path.isdir(name) and not re.match(denylist_regex, name)]
    print("Categories: " + ", ".join(categories))
    return categories


# Synchronize all challenges in the given category, where each challenge is in it's own folder.
def sync(category):
    challenges = [f"{category}/{name}" for name in os.listdir(f"./{category}") if os.path.isdir(f"{category}/{name}")]

    for challenge in challenges:
        if os.path.exists(f"{challenge}/challenge.yml"):
            print(f"Syncing challenge: {challenge}")
            os.system(f"ctf challenge sync '{challenge}'; ctf challenge install '{challenge}'")


# Synchronize each category in it's own thread.
if __name__ == "__main__":
    visible = change_state(['wave1',], 'hidden')

    init()
    categories = get_categories()

    jobs = []
    for category in categories:
        jobs.append(threading.Thread(target=sync, args=(category, )))
    
    for job in jobs:
        job.start()

    for job in jobs:
        job.join()

    print("Synchronized successfully!")
    print("The following challenges are now visible:")

    for category in visible:
        print(f"\n{category}:")
        print('- ' + '\n- '.join([challenge for challenge in visible[category]]))
