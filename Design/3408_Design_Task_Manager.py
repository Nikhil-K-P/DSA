"""
3408. Design Task Manager
Level: Medium
Topics: Hash Table, Design, Sorted Set, Priority Queue
Link: https://leetcode.com/problems/design-task-manager?envType=daily-question&envId=2025-09-18
Time Complexity: O(log N) for add, edit, rmv, and execTop
Space Complexity: O(N)
"""
from sortedcontainers import SortedSet


class TaskManager:

    def __init__(self, tasks: list[list[int]]):
        self.taskMap = {}
        self.taskQueue = SortedSet()
        for task in tasks:
            userId = task[0]
            taskId = task[1]
            priority = task[2]
            taskProfile = (userId, priority)
            self.taskMap[taskId] = taskProfile
            self.taskQueue.add((-priority, -taskId, userId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskMap[taskId] = (userId, priority)
        self.taskQueue.add((-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, priority = self.taskMap[taskId]
        self.taskQueue.remove((-priority, -taskId, userId))
        self.taskMap[taskId] = (userId, newPriority)
        self.taskQueue.add((-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        userId, priority = self.taskMap[taskId]
        del self.taskMap[taskId]
        self.taskQueue.remove((-priority, -taskId, userId))

    def execTop(self) -> int:
        if not self.taskQueue:
            return -1
        taskProfile = self.taskQueue[0]
        self.taskQueue.remove(taskProfile)
        return taskProfile[2]
