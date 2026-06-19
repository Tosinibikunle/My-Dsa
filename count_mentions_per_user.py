class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
       
        events.sort(key=lambda e: (int(e[1]), e[0] == "MESSAGE"))

        mention_count = [0] * numberOfUsers
        online_users = set(range(numberOfUsers))
        offline_users = []
        all_count = 0

        for event in events:
            curr_time = int(event[1])
            
            split_index = 0
            for i, (user, time_back) in enumerate(offline_users):
                if time_back > curr_time:
                    break
                online_users.add(user)
                split_index = i + 1

         
            offline_users = offline_users[split_index:]

            if event[0] == "MESSAGE":
                if event[2] == "ALL":
                
                    all_count += 1
                elif event[2] == "HERE":
                    
                    for user in online_users:
                        mention_count[user] += 1
                else:
                    
                    for idx in event[2].split():
                        user = int(idx[2:])
                        mention_count[user] += 1
            else:
                
                user = int(event[2])
                online_users.remove(user)
                offline_users.append((user, curr_time + 60))
        
        
        mention_count = [x + all_count for x in mention_count]

        return mention_count
