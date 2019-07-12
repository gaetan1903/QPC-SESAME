f = open('kamo.txt', 'r')
g = open('kamo.new', 'w')
for line in f:
    for i in range(1, 12):
        try:
            line = line.replace(f'self.player{i}', f"self.player['player{i}']")
        except:
            pass
    g.write(line)
g.close()