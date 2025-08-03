import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fname")
args = parser.parse_args()

flines = []
with open(args.fname, "r") as f:
    flines  = [line for line in f]

for k in range(len(flines)):
    line = flines[k]
    line = line.replace("$", "$$")
    line = line.replace("$$$$", "$$")
    flines[k] = line

with open(args.fname, 'w') as f:
    for line in flines:
        f.write(line)
        
