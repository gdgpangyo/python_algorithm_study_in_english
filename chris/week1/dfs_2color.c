#include <stdio.h>
#include <vector>

using namespace std;

const int MAX=100000;
vector <int> graph[MAX];
int color[MAX];
bool result = true;

void DFS(int x, int targetColor){
                                // targetColor: 1,2
color[x] = targetColor;
int nextColor;
if(targetColor==1) nextColor = 2;
else nextColor = 1;
for(int i=0;i<graph[x].size();i++){
  int y = graph[x][i];

if(color[y] == 0) DFS(y, nextColor);
else if(color[y] != nextColor) result=false;
}
}

int main() {

  int n, m;
scanf("%d %d", &n, &m);
for(int i=0;i<n;i++){
  color[i] = 0;
}
for(int i=0;i<m;i++){
int a, b;
scanf("%d %d", &a, &b);
graph[a].push_back(b);
graph[b].push_back(a);
}
DFS(0, 1);
for(int i=0;i<n;i++){
if(color[i]==0) result=false;
}

if(result) printf("YES");
else printf("NO");
return 0;
}