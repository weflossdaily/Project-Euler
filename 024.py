current = 0
for a in range(0,10):
	for b in range(0,10):
		if b == a:
			continue
		for c in range(0,10):
			if c == a or c == b:
				continue
			for d in range(0,10):
				if d==a or d==b or d==c:
					continue
				for e in range(0,10):
					if e==a or e==b or e==c or e==d:
						continue
					for f in range(0,10):
						if f==a or f==b or f==c or f==d or f==e:
							continue
						for g in range(0,10):
							if g==a or g==b or g==c or g==d or g==e or g==f:
								continue
							for h in range(0,10):
								if h==a or h==b or h==c or h==d or h==e or h==f or h==g:
									continue
								for i in range(0,10):
									if i==a or i==b or i==c or i==d or i==e or i==f or i==g or i==h:
										continue
									for j in range(0,10):
										if j==a or j==b or j==c or j==d or j==e or j==f or j==g or j==h or j==i:
											continue
										current += 1
										if current==1000000:
											print str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)
