inp = 'CMXXXIV'

def aa(string):
	if not string: return 0
	s = 'IVXLCDM'
	splitter = max(string, key=lambda x: s.index(x))
	index = string.index(splitter)
	x = s.index(splitter)
	return 10**(x//2)*(x%2*4+1) - aa(string[:index]) + aa(string[index+1:])

def a(n):
	if not n:return 0
	s='IVXLCDM'
	m=max(n,key=lambda x:s.index(x))
	i=n.index(m)
	x=s.index(m)
	return 10**(x//2)*(x%2*4+1)-a(n[:i])+a(n[i+1:])

def bb(string):
	if not string: return 0
	s = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	splitter = max(string, key=lambda x: s[x])
	index = string.index(splitter)
	return s[splitter] - bb(string[:index]) + bb(string[index+1:])

def b(n):
	if not n: return 0
	s = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	m = max(n, key=lambda x: s[x])
	i = n.index(m)
	return s[m] - b(n[:i]) + b(n[i+1:])

def c(s):
	if not s:return 0
	l,v=[(s.split(x,1),6-i) for i,x in enumerate('MDCLXVI') if x in s][0]
	return 10**(v//2)*(v%2*4+1)-c(l[0])+c(l[1])

# import re
# def d(string):
# 	s=0
# 	c={'M':1e3,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
# 	re.sub('[MDLV]|C[MD]?|X[CL]?|I[XV]?', lambda x: s+=c[x.group(0)], string)

def e(n):
	t=0
	s={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	for i,c in enumerate(n):
		t+=s[c]
		if s[n[i-1]]<s[c]:t-=s[n[i-1]]*2
	return t

def f(n):
	l=t=0
	s={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	for i,c in enumerate(n):
		v=s[c]
		t+=v
		if l<v:t-=2*l
		l=v
	return t


print(c(inp))