import re

s = "pr$pprtppp{%r%%#(;%rn$;~*s%r%r%;(#(x$p([~(~(r}%=([$[#[~[;~+rr~[r#(n([r%(n%b~;p#rp($;$[,l?(n~p#%$prn~%$r#(~$"
symbols = "abcdefghijklmnopqrstuvwxyz!#$%&\'()*+,-./:;<=>?@[\\]^_{|}~"
number = 9
counter = 0
new_str = []
all_symbols = []
total = 0

for symbol in symbols:
    if symbol in s:
        counter = s.count(symbol)
        all_symbols.append((symbol,counter))
all_symbols = sorted(all_symbols,key = lambda x: (x[1],x[0]),reverse=True)

for symbol, numb in all_symbols:
    if number < 0:
        new_str += [(symbol,0)]
    else:
        new_str += [(symbol,number)]
        number -= 1

for symbol in new_str:
    if symbol[1] == 0:
            s=s.replace(str(symbol[0])," ")
    else:
        s=s.replace(str(symbol[0]),str(symbol[1]))

s = re.split(r'\s|-W', s)
    
for ch in s:
    ch = str(ch)
    if ch.isdigit():
        total += int(ch)

print(total)


