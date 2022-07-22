PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "

folders = {"1": ["13","12","11"],}

print(f"{folders['1'][0]}\n{PIPE}{ELBOW}\n{folders['1'][1]}\n{PIPE}{ELBOW}\n{folders['1'][2]}\n{PIPE}{ELBOW}")