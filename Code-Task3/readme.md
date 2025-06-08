### 🔷 Task 3: Consensus Mechanism Simulation

**Objective:**  
Simulate and compare **Proof of Work (PoW)**, **Proof of Stake (PoS)**, and **Delegated Proof of Stake (DPoS)** using simple logic in code.

**🧩 Tasks:**
- Create mock objects for 3 validators:
  - `miner = { power: random value }` → used in PoW
  - `staker = { stake: random value }` → used in PoS
  - `voters = [3 mock accounts voting]` → used in DPoS

**🔄 Simulate:**
- For **PoW**: Select the validator with the **highest power**.
- For **PoS**: Select the validator with the **highest stake**.
- For **DPoS**: Randomly choose a delegate who received the **most votes**.

**💡 Output:**
- Print the selected validator and the consensus method used.
- Use `console.log()` or `print()` statements to explain how each selection was made.

**🎯 Goal:**  
Understand and compare the **decision-making processes** used in various blockchain consensus mechanisms such as PoW, PoS, and DPoS.

---

### 📁 Submission Instructions:

Please submit a GitHub repository or folder that includes the following files:

- `blockchain_simulation.py` → basic blockchain with 3 linked blocks  
- `mining_simulation.py` → Proof-of-Work mining simulation  
- `consensus_demo.py` → Consensus mechanism (PoW, PoS, DPoS) logic

### Output:

![alt text](image.png)
