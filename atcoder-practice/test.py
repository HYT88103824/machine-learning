n = int(input())

point = []
points = []

def findPoint(points):
    for i in range(n):
    # Write your code here
      r_x = 2*(points[i][2]-points[i][0])+points[i][0]
      r_y = 2*(points[i][3]-points[i][1])+points[i][1]
    
      print(r_x,r_y)

for i in range(n):
    point = list(map(int,input().split()))
    points.append(point)


findPoint(points)
