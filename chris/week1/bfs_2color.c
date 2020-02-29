#include <stdio.h>
#include <queue>
using namespace std;
const int MAX = 10000;
vector <int> graph[MAX];
int color[MAX];
int n,m;

bool BFS(int x){
  int targetColor = 1;
  color[x]=targetColor;
  queue <int> Queue;
  Queue.push(x);
  while(!Queue.empty()){
    int y = Queue.front();
    Queue.pop();

    targetColor = color[y];
    if(targetColor==1) targetColor=2;
    else targetColor=1;

    for(int i=0;i<graph[y].size();i++){
      int target = graph[y][i];
      if(color[target]==0){
        Queue.push(target);
        color[target] = targetColor;
      }else if(color[target]!=targetColor){
        return false;
      }
    }
  }
  for(int i=0;i<n;i++){
    if(color[i]==0) return false;
  }
  return true;
}

int main() {

  int start=0;
  scanf("%d %d", &n, &m);
  for(int i=0;i<m;i++){
    int a,b;
    scanf("%d %d", &a, &b);
    graph[a].push_back(b);
    graph[b].push_back(a);
    start = b;
  }
  for(int i=0;i<n;i++){
    color[i]=0;
  }
  bool result = BFS(start);
  if(result){
    printf("YES");
  }else{
    printf("NO");
  }

  return 0;
}