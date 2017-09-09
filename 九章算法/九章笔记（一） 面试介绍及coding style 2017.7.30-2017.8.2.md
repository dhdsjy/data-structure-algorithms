# 九章笔记（一） 面试介绍及coding style 2017.7.30-2017.8.2

标签（空格分隔）：data structure

---

## 总决式
最容易出卖你的，就是coding style 工程师的代码长什么样比脸长什么样重要。实现一个算法问题应该控制在45分钟以内

## coding style 原则
+ 变量名的命名尽量直观；不要用简单无意义的字母代替
+ 大括号正确使用； python无须担心，注意缩进就行
+ 避免重复代码，不直观逻辑（三段式）
+ 任何程序都要注意异常检测 边界处理
+ 要有测试自己代码的意识

## 面试时注意的问题
+ 不要闷头写代码 要先和面试官充分交流，确定方向和程序架构
+ lintcode刷题可以冲蓝题（easy）开始，重点是绿题（medium），锻炼解题思维，速度；红题（hard）可少做 刷题数量要有200题左右
+ 你可能是面试官的未来同事！你的代码必须让他看起来舒服，他review你的代码要多长时间？所以你一定要能和面试官舒适的进行交流
+ 

## 搞定算法面试的几个建议
+ 在刷题时，总结 归纳相似题目
+ 找出适合同一类题目的模板程序
+ 不要花时间攻关难题，把时间花在如何做到bug free 和如何提高编程速度上，多做medium题
+ 是面试不是考试 和面试官愉快交流 一起合作解决面试问题，证明自己牛逼，但别去证明面试官傻逼
+ 理解而不是单纯的背诵，在课堂中学习的是思维方式和分析技巧而不是某个题的解法
+ 刀要用在刀刃上

## 今天的讲解题型--递归
搞定算法面试就是搞定两个归 ：递归与动归

**关于递归的理解** 递归可以是“有去有回”，也可以是“有去无回”。但其根本是“由大往小地去，由近及远地去”。“递”是必需，“归”并非必需，依赖于要解决的问题，有的需要去的路上解决，有的需要回来的路上解决。==有递无归的递归其实就是我们很容易理解的一种分治思想==。递归的基本思想是广义地把规模大的问题转化为==规模小的相似的子问题==或者==相似的子问题集合==来解决。广义针对规模的，规模的缩小具体可以是指递归函数的参数，也可以是其参数之一。相似是指解决大问题的方法和解决小问题的方法往往是同一个方法，还可以是指解决子问题集的各子问题的方法是同一个方法。解决大问题的方法可以是由解决次规模问题的方法和解决剩余部分的方法组成，也可以是由一系列解决次规模问题的方法组成。

**一个让我茅塞顿开的递归解题思路**

【题 目】输入一个字符串，打印该字符串的所有排列。例如输入字符串abc，输出其全排列为abc，acb，bac，bca，cab，cba。

【思 路】我们想一下，如果不编程，手工做的话，我们的基本考虑是：每次首先固定一个字母，然后让其余的字母全排列；然后换一个字母固定，再全排列其余的字母，==如此循环而已==。换句话说：假设长度为n的字符串排列方式是f(n)==【1.将要解决的问题直接定义为函数】==，那么我们的基本思路是：每次让n个字母中的一个字母“打头阵”，其余的n-1个字母则按f(n-1)的方式排列==【2.递归的拆解 将要解决的问题去掉一个数会怎么样】==。这样我们就明白这明显是递归思路。

　　递归最重要的问题是：结束的条件是什么？或者说，最小子问题是什么==【3.递归的出口】==？还是以上面的abc例子来说明，首先固定a，然后排列bc；排列bc成为一个子问题，同样固定b，排列c；排列c成为子问题，固定c，剩下一个字符串结束符('\0')；碰到结束符，前面的字符已经都排好了，所以我们只需要打印前面所有已经固定的字符就可以了。

**我的总结**
一个递归函数的功能主要通过出口条件和return 决定，不要被函数的递归调用迷惑！碰到递归一般这样想：
+ **Step1：递归的定义** 将递归要解决的问题直接当做一个整体f(n)
+ **Step2: 递归的拆解** 如何将f(n)拆解到f(n-1)或其他更小的子问题（非递推型一般通过一个for循环即可将问题拆解）
+ **Step3： 递归的出口** 找到最小子问题

        def permute(self, nums):
            def backtrack(start, end):
                if start == end:
                    ans.append(nums[:])
                for i in range(start, end):#Step1: bt(0,3) bt(1,3)
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start+1, end)
                    nums[start], nums[i] = nums[i], nums[start]
                        
                ans = []
                backtrack(0, len(nums))
                return ans
### 递归一般解决三类问题
+ 数据的定义是按递归定义的。(Fibonacci函数)
+ 问题解法按递归算法实现。(回溯)
+ 数据的结构形式是按递归定义的。(树的遍历，图的搜索)

[让我恍然大悟的递归思路的博客](http://www.cnblogs.com/python27/archive/2011/12/08/2281352.html)

**递归三要素**
+ **递归的定义** 对应动态规划的状态；接受什么参数？做了什么事？返回什么值？
+ **递归的拆解** 对应动态规划的转移方程；如何将参数变小？
+ **递归的出口** 对应动态规划的初始化；什么时候可以直接return

**递归种类**
+ 有去有回

        recursion(大规模)
        {
             if (end_condition)
             {
                  end;     
             }
             else
             {     //先将问题全部描述展开，再由尽头“返回”依次解决每步中剩余部分的问题
                  recursion(小规模);     //go;
                  solve;                //back;
             }
        }
        # example 求二叉树深度 递推型也是
        int depth(Tree t){
            if(!t) return 0;
            else {
                int a=depth(t.right);
                int b=depth(t.left);
                return (a>b)?(a+1):(b+1);
            }
        }

        
+ 有去无回 （二叉树的前序遍历、dfs）在去的过程中就把问题解决了 所以就不用归了 没有递归出口了亦可

        recursion(大规模)
        {
             if (end_condition)
             {
                  end;     
             }
             else
             {     //在将问题转换为子问题描述的每一步，都解决该步中剩余部分的问题。
                  solve;                //back;
                  recursion(小规模);     //go;
             }
        }
        
        # example
         res = []
        self.dfs(sorted(S), 0, [], res)
        return res
    
        def dfs(self, S, index, path, res):
            res.append(path)
            for i in xrange(index, len(S)):
                self.dfs(S, i+1, path+[S[i]], res)

+ 有去无回（尽头解决，全排列）

其实理解递归可能没有“归”，只有去（分治）的情况后，我们应该想到递归也许可以既不需要在“去”的路上解决问题，也不需要在“归”的路上解决问题，只需在路的尽头解决问题，即在满足停止条件时解决问题。递归的分治思想不一定是要把问题规模递归到最小，还可以是将问题递归穷举其所有的情形，这时通常递归的表达力体现在将无法书写的嵌套循环（不确定数量的嵌套循环）通过递归表达出来。

        recursion()
        {
             if (end_condition)
             {
                  solve;     
             }
             else
             {     //在将问题转换为子问题描述的每一步，都解决该步中剩余部分的问题。
                  for () { recursion();     //go; }
             }
        }
        
    def permute(self, nums):        
        res = []
        self.recursion(nums,[],res)
        return res
    
    def recursion(self,nums,path,res):
        if not nums:
            res.append(path)
            return
        for i,n in enumerate(nums):
            self.recursion(nums[:i]+nums[i+1:],path+[n],res)
        return

#### 境界一 斐波那契型 （递推型）
许多问题都可以转换成这种类型，只要写出前面几个，找找规律分析下，一般都能找到递推式。这种转换为动态规划非常方便，所以这种类型一般不用递归，直接动态规划就行。

练习实战：

[HDOJ for beginner](http://acm.hdu.edu.cn/search.php?field=problem&key=%B5%DD%CD%C6%C7%F3%BD%E2%D7%A8%CC%E2%C1%B7%CF%B0%A3%A8For+Beginner%A3%A9&source=1&searchmode=source)

**Example**
斐波那契数列

        // 求出第x个fib数
        def fib(x):
            // 递归的出口
            if x <= 2:
                return 1
            else:
                // 递归的拆解
                return fib(x-1) + fib(x-2)
                
    // 动态规划解决方案
    def fib(x):
        arr = [1,1]
        for i in range(2,x+1):# 注意这种隐形的越界 arr[i]=arr[i-1]+arr[i-2]
            arr.append(arr[i-1]+arr[i-2])
        return arr[x]
        
#### 境界II 回溯型

### 境界III 树、图的递归

        
#### 递归版二分查找(感觉逻辑就是这样，没验证程序的正确性，有时间可以慢慢研究下)

        def binarySearch(nums, taget):
            if len(nums) == 1 and nums[0] == target:
                return True
            start = 0
            end = len(nums) - 1
            mid = start + (end - start)/2
            if nums[mid] >= target:
                binarySearch(nums[mid:],target)
            else:
                binarySearch(nums[:mid],target)
            return False
            
                
### 递归的理解
[ppt课件](http://www.docin.com/p-472525983.html)

[人脑理解递归](http://zisong.me/post/suan-fa/ren-nao-li-jie-di-gui)
### 排列组合模板总结
+ 适用范围 几乎所有的搜索问题
+ 需要做的改动 什么时候输出，哪些情况要跳过

[令狐冲老师的解决方案](https://discuss.leetcode.com/topic/10885/java-subsets-solution)

[python版模板](https://leetcode.com/problems/subsets/discuss/)

[python版模板2](https://discuss.leetcode.com/topic/72860/backtrack-summary-general-solution-for-10-questions-python-combination-sum-subsets-permutation-palindrome/2)

[java版模板](https://discuss.leetcode.com/topic/46159/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partitioning)

[leetcode 字符串问题总结](http://www.voidcn.com/blog/luoshengkim/article/p-6143156.html)
### leetcode例题
+ permutions
+ unique permutations
+ combination
+ letter combination of a phone number
+ palindrome partitioning
+ restore ip address
+ 


### 额外知识
[python中的动态规划1](http://python.jobbole.com/81465/)

[python中的动态规划2](http://blog.csdn.net/MrLevo520/article/details/75676160)




