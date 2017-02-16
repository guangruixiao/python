
# 一个简单的正则表达式解释器

def search (pattern,text):
	"return True if pattern appears anywhere in text."
	if pattern.startswith("^"):
		return match(pattern[1:],text)
	else：
		return match(".*"+pattern,text)

def match(pattern,text):
	"return True if pattern appears at the start of text"
	if pattern=="":
		return True
	elif pattern=="$":
		return  (text=="")
	elif len(pattern)>1 and pattern[1] in "*?":
		p, op, pat = pattern[0], pattern[1], pattern[2:]
		if op=="*":
			return match_star(p,pat,text)
		elif op=="?":
			if match1(p,text) and match (pat, text[1:]):
				return True
			else:
				return match (pat,text)
	else:
		return (match1(pattern[0],text)and match(pattern[1:],text[1:]))


def match1(p,text):
	"return true if first character of text matches pattern character p."
	if not text : return False
	return p=="." or p==text[0]


def match_star(p,pattern,text):
	"return true if any number of char p,followed by pattern,matches text."
	return (match(pattern,text) or (match1(p,text)and match_star(p,pattern,text[1:])))





