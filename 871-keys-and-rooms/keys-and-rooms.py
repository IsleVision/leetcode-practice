class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys=rooms[0]
        room_un = {0}
        while keys:
            key = keys.pop()
            if key not in room_un:
                room_un.add(key)    
                keys += rooms[key]
        if len(room_un)==len(rooms):
            return True
        else:
            return False
        