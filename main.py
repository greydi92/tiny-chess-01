import json,os,urllib.request as u
V=[0,50,160,165,250,450,0]
S={1:"dddd}}}}iinsffipdddnfb_dfiiZdddd",2:"KPUUPZddUdikUfknUdknUfikPZdfKPUU",4:"ddddfiiibdddbdddbdddbdddbddddddf",6:"UPPKUPPKUPPKUPPKZUUP_ZZZnnddnsid"}
T=[[0]*128 for _ in range(7)]
for p,t in S.items():
 for i,c in enumerate(t):T[p][112-i//4*16+i%4]=T[p][119-i//4*16-i%4]=ord(c)-100
T[3]=T[2];T[5]=T[4]
U=[];KL=0
KN=[31,33,14,18,-31,-33,-14,-18];KI=[1,15,16,17,-1,-15,-16,-17];BI=[15,17,-15,-17];RO=[1,16,-1,-16];QU=BI+RO;D=[0,0,KN,BI,RO,QU,KI]
CK={4:12,0:13,7:14,116:3,112:7,119:11}
CR={6:(7,5),2:(0,3),118:(119,117),114:(112,115)}
Z=Exception
def A(s,o):
 v=2*o-1
 for d in KN:
  t=s+d
  if not t&136 and B[t]==2*v:return 1
 for d in (15,17):
  t=s-d*v
  if not t&136 and B[t]==v:return 1
 for d in KI:
  t=s+d
  if not t&136 and B[t]==6*v:return 1
  while not t&136 and not B[t]:t+=d
  if not t&136 and B[t] in ((3 if abs(d) in (15,17) else 4)*v,5*v):return 1
 return 0
def G(c):
 ms=[]
 for s,x in enumerate(B):
  if not x or (x>0)^W:continue
  a=abs(x);r=s>>4
  if a==1:
   d=32*W-16;pr=7*W
   for t,fl in ((s+d,0),(s+d-1,1<<17),(s+d+1,1<<17)):
    if t&136:continue
    y=B[t]
    if fl:
     if t==E:fl|=1<<19
     elif not y or (y>0)==W or abs(y)==6:continue
    elif y:continue
    if t>>4==pr:ms.append(s|t<<7|5<<14|fl)
    elif fl:ms.append(s|t<<7|fl)
    elif not c:
     ms.append(s|t<<7)
     if r==6-5*W and not B[s+2*d]:ms.append(s|(s+2*d)<<7|1<<18)
  else:
   if a==6 and not c:
    for b,e,f,t in ((1,(5,6),4,6),(2,(1,2,3),4,2),(4,(117,118),116,118),(8,(113,114,115),116,114)):
     if C&b and not any(B[q] for q in e) and not any(A(q,not W) for q in (f,)+e[-2:]):ms.append(f|t<<7|1<<20)
   for o in D[a]:
    t=s+o
    while not t&136:
     y=B[t]
     if not y:
      if not c:ms.append(s|t<<7)
      if a%4==2:break
      t+=o
     else:
      if (y>0)^W and abs(y)!=6:ms.append(s|t<<7|1<<17)
      break
 return ms
def Mk(m):
 global C,E,W
 f=m&127;t=m>>7&127;p=m>>14&7
 cp=B[t]
 if m&1<<19:cp=B[t-32*W+16]
 U.append((m,cp,C,E,K[0],K[1]))
 x=B[f];B[f]=0;B[t]=x if not p else p*(2*W-1)
 if m&1<<19:B[t-32*W+16]=0
 if m&1<<20:a,b=CR[t];B[b]=B[a];B[a]=0
 C&=CK.get(f,15)&CK.get(t,15);E=f+32*W-16 if m&1<<18 else -1
 if abs(x)==6:K[not W]=t
 W=not W
def Um():
 global C,E,W
 m,cp,C,E,K[0],K[1]=U.pop()
 W=not W
 f=m&127;t=m>>7&127;p=m>>14&7
 x=B[t]
 if m&1<<20:a,b=CR[t];B[a]=B[b];B[b]=0
 if m&1<<19:B[t]=0;B[t-32*W+16]=cp
 else:B[t]=cp
 B[f]=2*W-1 if p else x
def Ev():
 e=sum((V[abs(x)]+T[abs(x)][s^(112*(x<0))])*(x//abs(x)) for s,x in enumerate(B) if x)
 return e*(2*W-1)
def OS(m):
 if m&1<<17:
  y=B[m>>7&127]
  return (V[abs(y)] or 50)*16-V[abs(B[m&127])]+10000
 return 8000 if m==KL else 0
def S(d,a,b,p):
 global N,KL
 N+=1
 if N>99999:raise Z
 ms=G(d<=0)
 if d<=0:
  s=Ev()
  if s>=b:return b
  if s>a:a=s
  if p>24:return a
 ms.sort(key=lambda m:-OS(m))
 n=0
 for m in ms:
  Mk(m)
  if A(K[W],W):Um();continue
  n+=1
  try:s=-S(d-1,-b,-a,p+1)
  finally:Um()
  if s>a:a=s
  if a>=b:
   if d>0 and not m&1<<17:KL=m
   break
 if d>0 and not n:return -9999+p if A(K[W^1],W^1) else 0
 return a
def Uci(m):
 f=m&127;t=m>>7&127;p=m>>14&7
 return f"{chr(97+(f&7))}{f//16+1}{chr(97+(t&7))}{t//16+1}{'nbrq'[p-2] if p else ''}"
def Rt(lg):
 cand=[m for m in G(0) if Uci(m) in lg]
 if not cand:return min(lg)
 cand.sort(key=lambda m:-OS(m))
 bm=cand[0]
 for d in range(1,13):
  try:
   a=-9999;cur=bm
   for m in cand:
    Mk(m)
    try:s=-S(d-1,-9999,-a,1)
    finally:Um()
    if s>a:a=s;cur=m
   bm=cur
   cand.remove(bm);cand.insert(0,bm)
  except Z:break
 return Uci(bm)
def post(p,b):
 return json.load(u.urlopen(os.getenv("MAKEFUN_ENV_URL")+p,json.dumps(b).encode()))
CG=0;NA=0
while True:
 g=post("/game",{})
 if g["status"]=="done":break
 if g["game"]!=CG:
  B=[0]*128;C=15;E=-1;W=1;K=[4,116];U.clear()
  for i,v in enumerate(map(int,"42356324")):B[i]=v;B[i+16]=1;B[i+96]=-1;B[i+112]=-v
  CG=g["game"];NA=0
 while g["status"]=="your_move":
  for v in g["moves"][NA:]:
   Mk(next(m for m in G(0) if Uci(m)==v))
   NA+=1
  N=0
  g=post("/move",{"game":g["game"],"move":Rt(g["legal_moves"])})
