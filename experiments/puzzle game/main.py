PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "

folders = {"1": ["13","12","11"],
           "2": ["21","22","woo"],}

#print(f"{folders['1'][0]}\n {TEE}\n{folders['1'][1]}\n {TEE}\n{folders['1'][2]}\n {TEE}")
for folder in folders:
    x = folder
    print(x)
    for folder in folders[x]:
        print(f"{TEE}{folder}")