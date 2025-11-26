class Router:

    def __init__(self, memoryLimit: int):
        self.packets = deque()
        self.allPackets = set()
        self.timestampsByDest = defaultdict(list)
        self.howManyDeleted = defaultdict(int)
        self.size = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        newPacket = (source,destination,timestamp)
        if newPacket in self.allPackets:
            return False
        if len(self.packets) == self.size:
            oldPacket = self.packets.popleft()
            #self.packetsByDestination[oldPacket[1]].pop(0)
            self.howManyDeleted[oldPacket[1]] += 1
            self.allPackets.remove(oldPacket)
        self.packets.append(newPacket)
        self.allPackets.add(newPacket)
        self.timestampsByDest[destination].append(timestamp)
        return True

        

    def forwardPacket(self) -> List[int]:
        if len(self.packets) == 0:
            return []
        toReturn = self.packets.popleft()
        self.allPackets.remove(toReturn)
        self.howManyDeleted[toReturn[1]] += 1

        return list(toReturn)
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.timestampsByDest[destination]


        leftIndex = bisect.bisect_left(timestamps,startTime, lo=self.howManyDeleted[destination])
        rightIndex = bisect.bisect_right(timestamps,endTime, lo=self.howManyDeleted[destination])

        return rightIndex-leftIndex
