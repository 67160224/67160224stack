class Graph:
    def __init__(self):
        # ใช้ dictionary เก็บโครงสร้างกราฟ
        self.graph = {}

    def add_edge(self, node, neighbor):
        """เพิ่มเส้นเชื่อม (Edge) ระหว่าง Node"""
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def bfs(self, start):
        """Breadth-First Search (ค้นหาแบบกว้างก่อน)"""
        visited = set()
        queue = [start]
        result = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                result.append(node)
                # เพิ่มเพื่อนบ้านที่ยังไม่เคยเยี่ยมชมเข้าคิว
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result

    def dfs(self, start):
        """Depth-First Search (ค้นหาแบบลึกก่อน)"""
        visited = set()
        result = []
        self._dfs_recursive(start, visited, result)
        return result

    def _dfs_recursive(self, node, visited, result):
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in self.graph.get(node, []):
                self._dfs_recursive(neighbor, visited, result)

# ---------------- ตัวอย่างการใช้งาน ----------------
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('D', 'F')
    g.add_edge('E', 'F')

    print("Graph:", g.graph)
    print("BFS จากจุด A:", g.bfs('A'))
    print("DFS จากจุด A:", g.dfs('A'))
