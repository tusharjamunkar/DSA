"""
0355. Design Twitter
Difficulty: Medium
Topic: Hash Table / Linked List / Design / Heap (Priority Queue)
LeetCode Link: https://leetcode.com/problems/design-twitter/

Problem Statement:
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
and see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:
- Twitter() Initializes your twitter object.
- void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId.
  Each call to this function will be made with a unique tweetId.
- List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed.
  Each item in the news feed must be posted by users who the user followed or by the user themself.
  Tweets must be ordered from most recent to least recent.
- void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
- void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

Example 1:
Input:
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output:
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation:
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

Constraints:
- 1 <= userId, followerId, followeeId <= 500
- 0 <= tweetId <= 10^4
- All the tweets have unique IDs.
- At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
- A user cannot follow themselves.
"""

from typing import List, Dict, Set, Tuple
from collections import defaultdict
import heapq


class Twitter:
    """
    Optimal Multi-Way Merge with Priority Queue (K-Way Merge):

    Algorithmic Intuition:
    - `follow_map`: Maps `followerId -> Set[followeeId]`.
    - `tweet_map`: Maps `userId -> List[(timestamp, tweetId)]`.
      Since tweets are appended sequentially, each user's tweet list is already sorted by time.
    - When `getNewsFeed(userId)` is called:
      - A user's news feed consists of their own tweets plus tweets from everyone they follow.
      - Instead of gathering all tweets and sorting them (O(Total_Tweets * log(Total_Tweets))),
        we perform a K-Way Merge using a Max-Heap initialized with the *latest* tweet of each followee:
        1. Insert the head/latest tweet of each relevant user into the heap: `(-timestamp, tweetId, followeeId, index)`.
        2. Pop the most recent tweet, append to result feed.
        3. If that followee has older tweets, push the previous tweet `index - 1` into the heap.
        4. Repeat until 10 tweets are gathered or all feeds are exhausted.

    Complexity:
    - Time Complexity:
      - postTweet: O(1) appending to user list.
      - follow:    O(1) hash set insertion.
      - unfollow:  O(1) hash set deletion.
      - getNewsFeed: O(F + 10 log F) where F is the number of followees (F <= 500).
    - Space Complexity:
      - O(T + U * F) to store tweets and follower relationships.
      - O(F) auxiliary heap space during getNewsFeed.
    """

    def __init__(self):
        self.time: int = 0
        self.tweet_map: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        self.follow_map: Dict[int, Set[int]] = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweet_map[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed: List[int] = []
        max_heap: List[Tuple[int, int, int, int]] = []  # (-time, tweetId, followeeId, index)

        # Relevant users: followees + the user themselves
        users = self.follow_map[userId] | {userId}

        # Initialize heap with the latest tweet from each user
        for u_id in users:
            tweets = self.tweet_map[u_id]
            if tweets:
                last_idx = len(tweets) - 1
                t, tweet_id = tweets[last_idx]
                heapq.heappush(max_heap, (-t, tweet_id, u_id, last_idx))

        # K-way merge for up to 10 most recent tweets
        while max_heap and len(feed) < 10:
            neg_time, tweet_id, u_id, idx = heapq.heappop(max_heap)
            feed.append(tweet_id)

            if idx > 0:
                prev_idx = idx - 1
                prev_t, prev_tweet_id = self.tweet_map[u_id][prev_idx]
                heapq.heappush(max_heap, (-prev_t, prev_tweet_id, u_id, prev_idx))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_design_twitter():
    # Test Case 1: Example 1 from LeetCode
    twitter = Twitter()
    twitter.postTweet(1, 5)
    assert twitter.getNewsFeed(1) == [5]

    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    assert twitter.getNewsFeed(1) == [6, 5]

    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [5]

    # Test Case 2: Maximum 10 tweets limit in feed
    tw2 = Twitter()
    for i in range(15):
        tw2.postTweet(1, i)
    assert tw2.getNewsFeed(1) == list(range(14, 4, -1))

    # Test Case 3: Multiple followees interleaving
    tw3 = Twitter()
    tw3.postTweet(1, 101)
    tw3.postTweet(2, 201)
    tw3.postTweet(3, 301)
    tw3.postTweet(1, 102)
    tw3.follow(1, 2)
    tw3.follow(1, 3)
    assert tw3.getNewsFeed(1) == [102, 301, 201, 101]

    # Test Case 4: Cannot follow self or unfollow non-followed
    tw3.follow(1, 1)
    tw3.unfollow(1, 999)  # Should not raise error
    assert tw3.getNewsFeed(1) == [102, 301, 201, 101]


if __name__ == "__main__":
    test_design_twitter()
    print("All Design Twitter unit tests passed successfully!")
