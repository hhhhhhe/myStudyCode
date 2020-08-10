# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
# 初始化 A 和 B 的元素数量分别为 m 和 n。


class Solution:
    def merge(self, A, m, B, n):
        A[m:] = B
        A.sort()


class Solution1:
    def merge(self, A, m, B, n):
        sorted_ = []
        pa, pb = 0, 0
        while pa < m or pb < n:
            if pa == m:
                sorted_.append(B[pb])
                pb += 1
            elif pb == n:
                sorted_.append(A[pa])
                pa += 1
            elif A[pa] < B[pb]:
                sorted_.append(A[pa])
                pa += 1
            else:
                sorted_.append(B[pb])
                pb += 1
        A[:] = sorted_
