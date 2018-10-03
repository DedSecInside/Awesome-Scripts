import rrdtool as rt
import sys
result = rt.fetch(sys.argv[1], "AVERAGE")
start, end, step = result[0]
legend = result[1]
rows = result[2]
endTime = end - 600
#while i <= end - 600:



for i in range(10,0,-1):
    print(endTime,rows[len(rows)-(3+i)][0] + rows[len(rows)-(3+i)][1])
    endTime = endTime - 300
