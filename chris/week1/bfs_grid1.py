"""
문제
아래와 같이 이동할 수 있는 길, 그리고 이동할 수 없는 벽으로 이루어진 크기 N x M 의 지도가 주어진다. 이 때, (N-1, 0) 에서 출발하여 (0, M-1) 까지 도착하는 최단거리를 출력하는 프로그램을 작성하시오. 아래 그림에 대하여 S에서 E까지 가는 최단거리는 22이다.

ec-16



입력
첫째 줄에 지도의 세로 길이 N과 지도의 가로 길이 M이 주어진다. ( 1 ≤ N, M ≤ 1,000 ) 둘째 줄부터 지도의 정보가 주어진다. 0은 이동할 수 있는 부분, 1은 이동할 수 없는 부분을 나타낸다.



출력
(N-1, 0) 에서 출발하여 (0, M-1) 까지 이동하는 데 필요한 최단거리를 출력한다.



예제 입력
copy10 10
0 0 0 0 0 0 1 1 0 0
0 1 1 1 0 0 1 0 1 0
0 1 1 1 0 0 1 0 1 0
0 0 0 0 0 0 0 0 1 0
0 0 1 1 1 1 0 0 1 0
0 0 0 0 0 0 1 1 0 0
0 0 1 1 1 0 1 1 0 0
0 0 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 0 0
0 0 0 0 0 0 0 1 0 0
예제 출력
copy22
"""
## template
from collections import deque, defaultdict

s = input()
n, m = [int(x) for x in s.split()]

matrix = [[0 for x in range(m)] for y in range(n)]
visited = [[0 for x in range(m)] for y in range(n)] # defaultdict(int)

for i in range(n):
  s = input()
  s = list(map(int, s.split()))
  matrix[i] = s
  # for j in range(m):

def bfs(y, x):
  ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  # key = f"{y},{x}"
  visited[y][x] = 1
  queue = deque()
  queue.append((y, x))
  distance = 0
  # print(visited)
  while len(queue)>0:
    item = queue.pop()
    y, x = item
    # key = f"{y},{x}"
    distance = visited[y][x]
    # print("traverse", item, distance)
    distance += 1

    for d in ds:
      # print("dy dx", d)
      dy, dx = d
      x2 = x+dx
      y2 = y+dy

      # key = f"{y2},{x2}"
      # print("y2 x2", y2, x2)
      if x2<0 or x2>=m:
        #print("x2 exceed", x2, m)
        continue
      if y2<0 or y2>=n:
        #print("y2 exceed", y2, n)
        continue

      # valid
      if visited[y2][x2] == 0 and matrix[y2][x2] == 0:
        # print("queue ", y2, x2)
        queue.append((y2, x2))
        visited[y2][x2] = distance
      elif visited[y2][x2] != 0 and visited[y2][x2] >= distance and matrix[y2][x2]==0:
        visited[y2][x2] = distance
        queue.append((y2, x2))

bfs(n-1, 0)
key = f"{0},{m-1}"
# print(visited)
print(visited[0][m-1]-1)
