import random

# Proof of Work
miner = {"id": "Miner1", "power": random.randint(1, 100)}
print(f"⚡ [PoW] {miner['id']} selected with power: {miner['power']}")

# Proof of Stake
staker = {"id": "Staker1", "stake": random.randint(1, 100)}
print(f"💰 [PoS] {staker['id']} selected with stake: {staker['stake']}")

# Delegated Proof of Stake
voters = {
    "User1": "DelegateA",
    "User2": "DelegateA",
    "User3": "DelegateB"
}
votes = {}

# Count votes
for voter, delegate in voters.items():
    votes[delegate] = votes.get(delegate, 0) + 1

selected_delegate = max(votes, key=votes.get)
print(f"🗳️ [DPoS] Delegate selected: {selected_delegate} with {votes[selected_delegate]} votes")
