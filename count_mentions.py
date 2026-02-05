#KN
class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        Count how many times each user gets mentioned across all events.
        Users who are OFFLINE don't receive HERE mentions.
        
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """
        # Track mention count for each user
        mention_count = [0] * numberOfUsers
        
        # Track offline users: {user_id: time_went_offline}
        offline_users = {}
        
        # Sort events by time, with MESSAGE events before OFFLINE at same time
        events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE"))
        
        current_time = 0
        
        for event in events:
            event_type = event[0]
            time = int(event[1])
            
            # Update current time and clean up stale offline entries
            if time > current_time:
                current_time = time
                # Remove users who've been offline for 60+ minutes
                for user_id in list(offline_users.keys()):
                    if current_time - offline_users[user_id] >= 60:
                        del offline_users[user_id]
            
            if event_type == "OFFLINE":
                # Mark user as offline
                user_id = int(event[2])
                offline_users[user_id] = current_time
                
            else:  # MESSAGE event
                message_text = event[2]
                
                if message_text == "ALL":
                    # ALL mentions everyone
                    for i in range(numberOfUsers):
                        mention_count[i] += 1
                        
                elif message_text == "HERE":
                    # HERE mentions only online users
                    # First clean up stale offline entries
                    for user_id in list(offline_users.keys()):
                        if current_time - offline_users[user_id] >= 60:
                            del offline_users[user_id]
                    
                    # Mention all users who are NOT offline
                    for i in range(numberOfUsers):
                        if i not in offline_users:
                            mention_count[i] += 1
                            
                else:
                    # Individual mentions (e.g., "id0 id1 id2")
                    for token in message_text.split():
                        if token.startswith("id"):
                            user_id = int(token[2:])
                            mention_count[user_id] += 1
        
        return mention_count
