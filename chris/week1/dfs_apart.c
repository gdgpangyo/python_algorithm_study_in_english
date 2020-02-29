#include <stdio.h>

const int MAX = 25;

int n;

int mat[MAX][MAX];
int visited[MAX][MAX];
int counter[MAX*MAX];

void DFS(int i, int j, int idx){
  // printf("%d %d %d\n", i, j, idx);
  visited[i][j] = idx;
  counter[idx]++;

  for(int dx=-1;dx<=1;dx++){
    for(int dy=-1;dy<=1;dy++){
      if(dx==0 && dy==0) continue;
      if(i+dy<0 || i+dy>=n) continue;
      if(j+dx<0 || j+dx>=n) continue;
      if(dx==-1 && dy==-1) continue;
      if(dx==1 && dy==-1) continue;
      if(dx==-1 && dy==1) continue;
      if(dx==1 && dy==1) continue;
      int i2=i+dy;
      int j2=j+dx;
      if(visited[i2][j2]==0 && mat[i2][j2]==1) DFS(i2, j2, idx);
    }
  }
}

void mergeSort(int arr[], int s, int e){
  if(e<=s) return;
  int m = (s+e)/2;
  // 1 3 5 2 3 6
  // s: 0 e: 5
  // m: 2
  // left: 0~2
  // right: 3~5
  // 1 3 5 / 2 3 6
  mergeSort(arr, s, m);
  mergeSort(arr, m+1, e);

  // merging
  int x=s;
  int y=m+1;
  // x: 0~2
  // y: 3~5
  int tmp[MAX*MAX];
  for(int t=s;t<=e;t++){
    if(x<=m && y<=e && arr[x]<=arr[y]) tmp[t]=arr[x++];
    else if(x<=m && y<=e && arr[x]>arr[y]) tmp[t]=arr[y++];
    else if(x<=m && y>e) tmp[t]=arr[x++];
    else if(x>m && y<=e) tmp[t]=arr[y++];
  }
  for(int t=s;t<=e;t++){
    arr[t]=tmp[t];
  }
}

int main() {

  //Please Enter Your Code Here

  scanf("%d", &n);
  for(int i=0;i<n;i++){
    char cs[MAX];
    scanf("%s", cs);
    for(int j=0;j<n;j++){
      // printf("%d", cs[j] - '0');
      mat[i][j]=cs[j] - '0';
      visited[i][j]=0;
    }
  }
  int idx=0;
  // i: row j: col
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
      // printf("%d %d\n", visited[i][j], mat[i][j]);
      if(visited[i][j]==0 && mat[i][j]==1) {
        idx++;
        counter[idx]=0;
        DFS(i, j, idx);
      }
    }
  }
  // for(int i=0;i<n;i++){
  //   for(int j=0;j<n;j++){
  //     printf("%d", mat[i][j]);
  //   }
  //   printf("\n");
  // }
  // for(int i=0;i<n;i++){
  //   for(int j=0;j<n;j++){
  //     printf("%d", visited[i][j]);
  //   }
  //   printf("\n");
  // }
  mergeSort(counter, 1, idx);

  printf("%d\n", idx);

  for(int i=1;i<=idx;i++){
    printf("%d\n", counter[i]);
  }

  return 0;
}