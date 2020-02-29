#include <stdio.h>
#include <vector>

using namespace std;

const int MAX = 100;
vector <int> graph[MAX];
bool visited[MAX];

void DFS(int x){
  visited[x]=true;
  for(int i=0;i<graph[x].size();i++){
    int y = graph[x][i];
    if(visited[y]==false) DFS(y);
  }
}

int main() {

  int n, m;
  scanf("%d", &n);
  scanf("%d", &m);
  for(int i=0;i<m;i++){
    int a,b;
    scanf("%d %d", &a, &b);
    graph[a].push_back(b);
    graph[b].push_back(a);
  }
  DFS(1);
  int cnt=0;
  for(int i=1;i<=n;i++){
    // printf("%d %d\n", i, visited[i]);
    if(visited[i]==true) cnt++;
  }
  printf("%d", cnt-1);
  return 0;
}