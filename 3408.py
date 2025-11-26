class TaskManager:
    tasks = List[list[int]]

    def __init__(self, tasks: List[List[int]]):
        self.taskToId = {}
        self.priority = []
        
        for userId,taskId,priority in tasks:
            self.add(userId,taskId,priority)


    def add(self, userId: int, taskId: int, priority: int) -> None:
        heappush(self.priority,(-priority,-taskId,userId))
        self.taskToId[taskId] = (userId,priority)

    

    def edit(self, taskId: int, newPriority: int) -> None:
        self.taskToId[taskId] = (self.taskToId[taskId][0],newPriority)
        heappush(self.priority,(-newPriority,-taskId,self.taskToId[taskId][0]))


    def rmv(self, taskId: int) -> None:
        if taskId in self.taskToId:
            del self.taskToId[taskId]



    def execTop(self) -> int:
        while self.priority:
            priority,taskId,userId = heapq.heappop(self.priority)
            taskId = -taskId
            if taskId in self.taskToId:
                userIdPop,priorityPop = self.taskToId[taskId]
                if priorityPop == -priority:
                    del self.taskToId[taskId]
                    return userId

        return -1   
