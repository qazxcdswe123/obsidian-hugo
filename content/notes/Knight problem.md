---
title: Knight problem
---
# DFS
```c++
#include <bits/stdc++.h>

using namespace std;

int dir[8][2] = {-1, -2, -2, -1, -2, 1, -1, 2, 1, 2, 2, 1, 2, -1, 1, -2};
int ans[8][8];

struct knight
{
    int x, y, max;
};

knight st, ed;

void dfs(int x, int y, int moves);
void bfs(knight start);

int main()
{
    // freopen("input.in", "r", stdin);

    char m1[3] = {'\0'}, m2[3] = {'\0'};
    while (cin >> m1 >> m2)
    {
        if (strcmp(m1, m2) == 0)
        {
            cout << "To get from " << m1[0] << m1[1] << " to " << m2[0] << m2[1] << " takes 0 knight moves." << '\n';
        }
        else
        {
            memset(ans, 100, sizeof(ans));
            st.max = 0;
            st.x = m1[0] - 'a';
            st.y = m1[1] - '1';
            ed.x = m2[0] - 'a';
            ed.y = m2[1] - '1';
            dfs(st.x, st.y, 0);
            cout << "To get from " << m1[0] << m1[1] << " to " << m2[0] << m2[1] << " takes " << ans[ed.x][ed.y] << " knight moves." << '\n';
        }
    }
}

void dfs(int x, int y, int moves)
{
    if (x < 0 || x > 7 || y < 0 || y > 7 || ans[x][y] <= moves)
        return;
    ans[x][y] = moves;
    for (int i = 0; i < 8; i++)
    {
        int nx = x + dir[i][0];
        int ny = y + dir[i][1];
        dfs(nx, ny, moves + 1);
    }
}
```
每个位置都存放一个步数，当来到该位置时，就可以分析是否为更少的步数
![Uploading file...ngta5]()

# BFS
```c++
int main() {
    // freopen("input.in", "r", stdin);
    char m1[3] = {'\0'}, m2[3] = {'\0'};
    while (cin >> m1 >> m2)
    {
        if (strcmp(m1, m2) == 0)
        {
            cout << "To get from " << m1[0] << m1[1] << " to " << m2[0] << m2[1] << " takes 0 knight moves." << '\n';
        }
        else
        {
            m = 0;
            knight start;
            start.max = 0;
            start.x = m1[0] - 'a';
            start.y = m1[1] - '1';
            ed.x = m2[0] - 'a';
            ed.y = m2[1] - '1';
            bfs(start);
            cout << "To get from " << m1[0] << m1[1] << " to " << m2[0] << m2[1] << " takes " << m << " knight moves." << '\n';
            for (int i = 0; i < 8; i++)
            {
                for (int j = 0; j < 8; j++)
                {
                    ans[i][j] = 0;
                }
            }
        }
    }
}

void bfs(knight start)
{
    queue<knight> k;
    k.push(start);
    while (!k.empty())
    {
        auto temp = k.front();
        k.pop();
        if (temp.x == ed.x && temp.y == ed.y)
        {
            m = temp.max;
            break;
        }
        for (int i = 0; i < 8; i++)
        {
            int x = temp.x + dir[i][0];
            int y = temp.y + dir[i][1];
            if (x >= 0 && x < 8 && y >= 0 && y < 8 && !ans[x][y])
            {
                start.x = x;
                start.y = y;
                start.max = temp.max + 1;
                k.push(start);
                ans[x][y] = 1;
            }
        }
    }
}
```

# PATH
```c++
path[start.x][start.y].x=temp.x;
path[start.x][start.y].y=temp.y;

void PrintPath(int x, int y)
{
    if (x == -1 && y == -1)
        return;
    PrintPath(path[x][y].x, path[x][y].y);
    cout << "(" << char(x + 97) << "," << y + 1 << ") ";
}

```