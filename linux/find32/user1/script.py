import os,random,string
def gen_random_string(N):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

for i in range(20):
    folder_name = gen_random_string(8)
    os.mkdir(folder_name)

    for j in range(20):
        file_name = gen_random_string(8)
        f = open(folder_name +'/'+file_name, 'w')
        f.write(gen_random_string(10000))
        f.close()
