# 九章算法（四）BFS

标签（空格分隔）： data structure

---

[以前学员的一个笔记](http://www.cnblogs.com/lingli-meng/p/6557349.html)
今天介绍了两个coding style ：
+ 变量无需全部提前定义好，用的时候再来定义。
+ 题目中出现的某些常年最好用有意义的大写字母代替，增加程序的可读性。比如1表示僵尸，2表示墙。可在程序开始时 

        define JS 1
      define WALL 2
      # python可直接赋值
      JS = 1
      WALL = 2

课前你不花大量时间预习练习，课后你将使用更多的时间进行弥补，还不一定能整明白！！！
## 破枪式
能够用BFS解决的问题，一定不要用DFS。题目问最短路径，一般都是BFS.宽搜是算法面试中训练最有效果的一类提醒，面试也常考。是准备算法面试过程中性价比最高的一类题型，模板也相对比较固定，基本已框架化。三步走一般都能完成。

## BFS 试题分类
主要分为两类：**图的遍历**和**最短路径问题**，其中图的遍历又可以细分为三个小点：==层级遍历==、==连通性问题（由点及面，无层级遍历）==、==拓扑排序==

## BFS 框架
+ put start node in queue
+ while queue is not empty
+ level x to level x + 1

### 二叉树上的宽搜
+ **层级遍历** 典型的题目就是二叉树上的按层次遍历。层级遍历一般都需要queue这个数据结构

        # 关键的一段代码 完美的利用了queue的结构性质 这个for循环就是起到了层级遍历的作用
        que_size = len(que)
            for i in range(que_size):
            #for node in que:
                node = que.pop(0)#前出
[example1 二叉树的层次遍历 一种典型的BFS](http://www.lintcode.com/zh-cn/problem/binary-tree-level-order-traversal/) 

[example2 extend zigzag traversal](https://www.lintcode.com/zh-cn/problem/binary-tree-zigzag-level-order-traversal/)

+ **由点及面（连通性问题）** 这种题型一般无层级遍历，也几乎很少用到queue数据结构。

+ 
### 图上的宽搜
一般会用到Hashmap，也即python中的dict。
#### 拓扑排序
[挺好的一个拓扑排序](http://blog.csdn.net/turne/article/details/50165713)
[让我看懂拓扑排序的一篇文章](http://www.acmerblog.com/topological-sorting-5896.html)
[拓扑排序之有向无环图的最长路径](http://blog.csdn.net/u010519432/article/details/26751867)

拓扑排序是对有向无环图的一种排序，非常经典的一种图算法。表示了顶点按边的方向出现的先后顺序。如果有环，则无法表示两个顶点的先后顺序。一个简单的求拓扑排序的算法：首先要找到任意入度为0的一个顶点，删除它及所有相邻的边，再找入度为0的顶点，以此类推，直到删除所有顶点。顶点的删除顺序即为拓扑排序。

**算法流程**
拓扑排序的第一个顶点总是入度为0。
**算法一流程** 每次都选取入度为0的节点，再更新其相邻的节点的入度。

        1.构造空列表 L和S；
        2.把所有没有依赖节点(入度为0)的节点放入L；
        3.当L还有节点的时候，执行下面步骤：
        3.1  	L中拿出一个节点ｎ（从L中remove掉），并放入S
        3.2  		对每一个邻近n的节点m，
        3.2.1 			去掉边（n,m）;（表示加入最终结果集S）
        3.2.2 			如果m没有依赖节点（入度为零），把m放入L;
**算法二DFS**

### 矩阵上的宽搜
矩阵的BFS一般涉及到由点及面和最短路径问题，比如number of island, knight shortest path, zombie in matrix 以及hard级别的build post office II

[build post office 很棒的一个讲解](http://chuansong.me/n/1597875949416)
[思路很特别 代码量有点多](https://zhengyang2015.gitbooks.io/lintcode/build_post_office_573.html)
[dp解题思路](http://blog.csdn.net/find_my_dream/article/details/4931222)
![code for build post office](http://read.html5.qq.com/image?src=forum&q=5&r=0&imgflag=7&imageUrl=http://mmbiz.qpic.cn/mmbiz_png/hK6krTdpF7uN43BFf0Xiba475Q1dB8ciaqc4JibrGdARFE9iaA5SpxiagvkK1h5iacib6zmBxwW7TJI4Hwuj545z4RjVA/0?wx_fmt=png)

[build post office II](http://www.lintcode.com/zh-cn/problem/build-post-office-ii/)

**两个思路**

[solution 1 from house](http://www.itwendao.com/article/detail/278405.html)

[solution2 from empty（my way）](http://note.youdao.com/)

        # 群内sky的代码
        public class Solution {
    /**
     * @param grid a 2D grid
     * @return an integer
     */
    private final int WALL = 2;
    private final int HOUSE = 1;
    private final int EMPTY = 0;
    private class Index {
        public int x;
        public int y;
        public Index(int a, int b) {
            x = a;
            y = b;
        }
    }
    public int shortestDistance(int[][] grid) {
        // Write your code here
        if (grid == null || grid.length == 0) {
            return -1;
        }
        if (grid[0] == null || grid[0].length == 0) {
            return -1;
        }
        int houseCount = 0;
        List<Index> emptys = new ArrayList<>();
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == HOUSE) {
                    houseCount++;
                } else if (grid[i][j] == EMPTY) {
                    emptys.add(new Index(i, j));
                }
            }
        }
        if (houseCount == 0) {
            return -1;
        }
        int smallestDistanceSum = Integer.MAX_VALUE;
        boolean isExists = false;
        for (Index empty : emptys) {
            int distanceSum = bfsGridWithSumofHouse(empty, grid, houseCount);
            if (distanceSum < 0) {
                continue;
            } else {
                isExists = true;
                smallestDistanceSum =
                    smallestDistanceSum < distanceSum ? smallestDistanceSum : distanceSum;
            }
        }
        if (isExists) {
            return smallestDistanceSum;
        } else {
            return -1;
        }
    }
    private int bfsGridWithSumofHouse(Index start,
                                      int[][] grid,
                                      int houseCount) {
        int[] deltaX = {1, 0, 0, -1};
        int[] deltaY = {0, 1, -1, 0};
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        int level = 0;
        int distanceSum = 0;
        Queue<Index> queue = new LinkedList<>();
        queue.offer(start);
        visited[start.x][start.y] = true;
        while (!queue.isEmpty()) {
            level++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Index head = queue.poll();
                for (int j = 0; j < deltaX.length; j++) {
                    Index point = new Index(head.x + deltaX[j], head.y + deltaY[j]);
                    if (isValidPoint(grid, point, EMPTY)) {
                        if (!visited[point.x][point.y]) {
                            queue.offer(point);
                            visited[point.x][point.y] = true;
                        }
                    } else if (isValidPoint(grid, point, HOUSE)) {
                        if (!visited[point.x][point.y]) {
                            distanceSum += level;
                            visited[point.x][point.y] = true;
                            houseCount--;
                        }
                    }
                }
            }
        }
        if (houseCount == 0) {
            return distanceSum;
        } else {
            return -1;
        }
    }
    private boolean isValidPoint(int[][] grid, Index point, int type) {
        if (isInGrid(grid, point) && grid[point.x][point.y] == type) {
            return true;
        }
        return false;
    }
    private boolean isInGrid(int[][] grid, Index point) {
        return 0 <= point.x && point.x < grid.length
            && 0 <= point.y && point.y < grid[0].length;
    }
}

**example 1** [number of island](http://www.lintcode.com/zh-cn/problem/number-of-islands/#http://note.youdao.com/) 

**solution 1** [BFS+queue](http://bookshadow.com/weblog/2015/04/08/leetcode-number-islands/)
[DFS+stack](https://discuss.leetcode.com/topic/25945/simple-dfs-python-code-beat-90)



**example 3** [course-schedule-ii](http://www.lintcode.com/en/problem/course-schedule-ii/) [拓扑排序](https://segmentfault.com/a/1190000003814058)

### 最短路径问题
关于BFS求最短路径问题提，理解的不是很清楚，但这是BFS的一个最主要的问题。最短路径主要包括以下几类
+ 跳棋 计算最少走多少步就可以获胜
+ 拼写检查器 计算至少编辑几个地方就可以将错误的单词变成正确的单词
+ 人际关系中最近的人




