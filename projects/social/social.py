import sys
sys.path.append('../graph')
from util import Queue

import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # Write a for loop that calls create user the right amount of times
        for i in range(num_users):
            self.add_user(f"User {i+1}")
        # Create friendships
        # To create N random friendships
        # you could create a list with all possible friendship combinations,
        # shuffle the list then grab the first N elements from the list.
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)
        # Create n friendships where n = avg_friendships * num_users // 2
        # avg_friendships = total_friendships / num_users
        # total_friendships = avg_friendships * num_users
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
    
    def populate_graph_linear(self, num_users, avg_friendships):
        # Pick a random user
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        
        # Add users
        # Write a for loop that calls create user the right amount of times
        for i in range(num_users):
            self.add_user(f"User {i+1}")
        
        target_frinedships = num_users * avg_friendships
        total_friendships = 0
        collisions = 0
        # Pick another random user
        while total_friendships < target_frinedships:
            user_id = random.randint(1, num_users)
            friend_id = random.randint(1, num_users)
        # Try to create the friendship
            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
        # If it works, increment a counter
        # If not, try again
            else:
                collisions += 1
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # initialize visited with initial argument
        visited = {}  # Note that this is a dictionary, not a set
        # visited key will be user_id's and values will be the path to that user
        # after traversal, visited will be a dictionary with each user, and the shortest path to the user as values
        # use breadth first search to guarantee the shortest path
        q = Queue()
        q.enqueue([user_id])

        while q.size() > 0:
            path = q.dequeue()
            last_user = path[-1]
            
            if last_user not in visited.keys():
                visited[last_user] = path # this is the path between users
            
            # loop through last users friends
                
                for friend in self.friendships[last_user]:
                    path_copy = path.copy()
                    path_copy.append(friend)
                    q.enqueue(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph_linear(10, 2)
    print("FRIENDSHIPS\n", sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("CONNECTIONS\n", connections)
