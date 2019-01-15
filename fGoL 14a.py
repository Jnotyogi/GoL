print('fGoL') # NB click in terminal after starting, before answering question
# good to toggle panel position (to right) via View... Appearance... ; then can toggle it on/off CMD-J
rows = 60; cols = 80
vquiet = False # True prevents one-line print of population-count and step-number when quiet (quiet is set by user input of steps at end of code)
roll = 0 # set to 1 for cyclic field, 0 for dead boundary which is better for large fields re gliders

#seedfile='Grpentomino.txt' # methuselah gives 5 gliders then eg 176 at 751 stabln 110+6 at 1103 with 100R 150C
seedfile='Ggospergun.txt' # good r60 c80 roll=0 right panel. First glider at 15, cycle is 30.
#seedfile='Gspaceship.txt'
#seedfile='Gbeacons.txt'
#seedfile='Gjf.txt' # methuselah produces jplus at top at 41 then 2 gliders & eg 315 at 641 & 290 at 1931 with 100R 150C
#seedfile='Gglider.txt'
#seedfile='Gjplus.txt' # new gliders at 21 and 74 (actually 73) stabiln 128

steps = 0; quiet = True # these are NOT used ! - just initial values re-set by input at end of code
nworld = [[0] * cols for i in range(rows)]
nnext = [[0] * cols for i in range(rows)]
pop=0; tstep=0; stopping=""

with open(seedfile) as f: my_data = f.read()
w=my_data.find('\n'); h=int(round(len(my_data)/w,0))
zc=int(0.5*cols -0.5*w);zr=int(0.5*rows -0.5*h)

for r in range (h):
    for c in range (w+1):
        if (w+1)*r+c+1<=len(my_data):
            if my_data[(w+1)*r+c]=='0': nworld[r+zr][c+zc]=1
            else: nworld[r+zr][c+zc]=0

while stopping=="":
    for nstep in range(steps+1):
        if nstep>0 and not (vquiet and quiet): print('Population',pop,'  Now step',tstep,':') ##
        if tstep==0 or nstep>0:
            tstep+=1; pop=0
            for r in range(rows):
                sm=""
                for c in range(cols):
                    if nstep>0: nworld[r][c]=nnext[r][c]
                    if nworld[r][c]==1: sm+='0'; pop+=1
                    else: sm+='_'
                if nstep==steps or not quiet: print(sm)
    
        for r in range(rows):
            for c in range(cols):
                mesum=0
                for i in (-1,0,1):
                    mlr=1; dr=r+i
                    if dr==-1: mlr=mlr*roll; dr=rows-1
                    if dr==rows: mlr=mlr*roll; dr=0
                    for j in (-1,0,1):
                        mlc=1; dc=c+j
                        if dc==-1:mlc=mlc*roll; dc=cols-1
                        if dc==cols: mlc=mlc*roll; dc=0
                        mesum = mesum+mlr*mlc*nworld[dr][dc]
                if mesum==3 or (nworld[r][c]==1 and mesum==4): nnext[r][c]=1
                else: nnext[r][c]=0

    if nstep==steps or not quiet: print('Population',pop, ' at step', tstep-1)


    if nstep==0:
        ii=input("Keep going? Return=yes, Int=For n steps (-ve is quiet), any other = Stop\nCLICK HERE FIRST ! : ")
    else:
        ii=input("Keep going? Return=yes, Int=For n steps (-ve is quiet), any other = Stop: ")
    try:
        steps = int(ii)
        if steps<0:
            steps=-steps
            quiet = True
        else:
            quiet = False
        ii=""
    except ValueError:
        stopping=ii

print('End')
