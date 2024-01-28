S = input()
s = [*S]

sub = []
for i in range(1, len(s)+1) :
    for j in range(len(s)-i+1) :
        sub.append(''.join(s[j:(j+i)]))

sub_set = {*sub}
sub = [*sub_set]
print(len(sub))