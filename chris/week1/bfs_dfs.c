/*
문제
그래프가 주어질 때, 0번 정점을 시작으로 하여 깊이우선탐색과 너비우선탐색의 결과를 출력하는 프로그램을 작성하시오. 단, 노드를 방문할 때는 노드 번호가 작은 순서대로 방문한다고 하자.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ M ≤ 100,000 ) 둘째 줄부터 간선의 정보가 주어진다. 각 줄은 두 개의 숫자 a, b로 이루어져 있으며, 이는 정점 a와 정점 b가 연결되어 있다는 의미이다. 정점의 번호는 0번부터 N-1번까지이다.

출력
첫 번째 줄에 깊이우선탐색 결과, 두 번째 줄에 너비우선탐색 결과를 출력한다.

Input Example
9 12
0 1
0 2
0 3
1 5
2 5
3 4
4 5
5 6
5 7
5 8
6 7
7 8

Output Example:
0 1 5 2 4 3 6 7 8
0 1 2 3 5 4 6 7 8
*/

#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const int MAX=1000;
int n,m;
vector <int> graph[MAX];
bool dfs_visited[MAX];
bool bfs_visited[MAX];

void mergeSort(vector<int> arr, int s, int e){
  if(e<=s) return;

  int m = (s+e)/2;
  // 5 2 4 3 6
  // s:0 e:4 m:2
  // 5 2 4 / 3 6
  mergeSort(arr, s, m);
  mergeSort(arr, m+1, e);

  int x=s; // s~m
  int y=m+1; // m+1~e
  int tmp[MAX];

  for(int i=s;i<=e;i++){
    if(x<=m && y<=e && arr[x]<=arr[y]) tmp[i]=arr[x++];
    if(x<=m && y<=e && arr[x]>arr[y]) tmp[i]=arr[y++];
    if(x>m && y<=e) tmp[i]=arr[y++];
    if(x<=m && y>e) tmp[i]=arr[x++];
  }
  for(int i=s;i<=e;i++){
    arr[i] = tmp[i];
  }

}

void DFS(int x){
  printf("%d ", x);
  dfs_visited[x] = true;
  sort(graph[x].begin(), graph[x].end());
  for(int i=0;i<graph[x].size();i++){
    // mergeSort(graph[x], 0, graph[x].size()-1);
    int y = graph[x][i];
    if(dfs_visited[y] == false){
      DFS(y);
    }
  }
}

void BFS(int x){
  queue <int> Queue;
  Queue.push(x);
  bfs_visited[x] = true;

  while(!Queue.empty()){
    int y = Queue.front();
    Queue.pop();

    printf("%d ", y);

    // mergeSort(graph[y], 0, graph[y].size()-1);
    sort(graph[y].begin(), graph[y].end());
    for(int i=0;i<graph[y].size();i++){
      int t = graph[y][i];
      if(bfs_visited[t] == false){

        bfs_visited[t] = true;
        Queue.push(t);
      }
    }
  }
}

int main() {

  scanf("%d %d", &n, &m);
  for(int i=0;i<m;i++){
    int a,b;
    scanf("%d %d", &a, &b);
    graph[a].push_back(b);
    graph[b].push_back(a);
  }
  for(int i=0;i<n;i++){
    dfs_visited[i]=false;
    bfs_visited[i]=false;
  }
  DFS(0);
  printf("\n");
  BFS(0);
  return 0;
}
