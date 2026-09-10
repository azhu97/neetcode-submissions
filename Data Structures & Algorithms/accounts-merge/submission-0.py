class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        class Union:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.rank = [0 for i in range(n)]
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                root_x, root_y = self.find(x), self.find(y)
                if root_x == root_y:
                    return False # same set
                
                # merge based on rank
                if self.rank[root_x] < self.rank[root_y]:
                    self.parent[root_x] = root_y
                elif self.rank[root_x] > self.rank[root_y]:
                    self.parent[root_y] = root_x
                else:
                    # same rank
                    self.parent[root_x] = root_y
                    self.rank[root_y] += 1
            
            def connected(self, x, y):
                return self.find(x) == self.find(y)
        u = Union(len(accounts)) # each account is its own
        email_to_account = {} # email -> index of account | to keep track of whats already been tracked for ease of merge and eventually returning solution
        for i, account in enumerate(accounts):
            for e in account[1:]:
                if e in email_to_account:
                    # merge
                    u.union(i, email_to_account[e])
                else:
                    email_to_account[e] = i
        # at this point we have merged u
        emailGroup = defaultdict(list)
        for e, i in email_to_account.items():
            parent = u.find(i)
            emailGroup[parent].append(e)
        res = []
        for i, listing in emailGroup.items():
            print(i, listing)
            temp = [accounts[i][0]] + listing
            print(temp)
            res.append(temp)
        return res