#include <stdio.h>
#include <vector>

using namespace std;

const int MAX = 1000;
vector <int> graph[MAX];
int color[MAX];
bool result=true;

void DFS(int x, int targetColor){
  // printf("DFS %d %d\n", x, targetColor);
  color[x]=targetColor;
  int nextColor;
  if(targetColor==1) nextColor=2;
  else nextColor=1;
  for(int i=0;i<graph[x].size();i++){
    int y = graph[x][i];
    if(color[y]==0) DFS(y, nextColor);
    else if(color[y]!=nextColor) result=false;
  }
}

int main() {
  int n, m;
  scanf("%d %d", &n, &m);
  int start;
  for(int i=0;i<m;i++){
    int a,b;
    scanf("%d %d", &a, &b);
    graph[a].push_back(b);
    graph[b].push_back(a);
    start = b;
  }
  DFS(start, 1);
  for(int i=1;i<=n;i++){
    // printf("%d %d\n", i, color[i]);
    if(color[i]==0) result=false;
  }
  if(result) printf("Yes");
  else printf("No");

  return 0;
}