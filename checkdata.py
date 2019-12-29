import random
with open('trash', 'r') as f:
    comment_hashtags = f.read()
            
        #rint(comment_hashtags)
            
        
filtro = [hashtag for hashtag in comment_hashtags.split() if hashtag.startswith('#')]
filtro = [i for i in filtro if len(i) <= 10]

#print(filtro)
zz = random.choice(filtro)
#print(zz)

with open('processed.byhash', 'a') as h:
    for i in range(len(zz)):
        try:
            h.write(str(zz[i]) + '\n')
        except:
            pass
                
with open('processed.byhash', 'r', encoding='utf-8') as p:
    current_comment = p.read()

current_comment = current_comment.splitlines()
print(current_comment)
indice_comm = random.randint(0, len(current_comment))
next_comment = current_comment[indice_comm]
#print(next_comment)
