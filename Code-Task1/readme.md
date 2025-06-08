---

### 🔷 Task 1: Block Simulation in Code

**Objective:**  
Build a basic blockchain with 3 linked blocks using code.

**🧩 Tasks:**
- Create a `Block` class with the following attributes:
  - `index`
  - `timestamp`
  - `data`
  - `previousHash`
  - `hash`
  - `nonce`
- Implement a simple hash generator using **SHA-256**.
- Link 3 blocks together by chaining their `previousHash` values.
- Display all blocks with their hash values.

**🛠️ Challenge:**
- Modify the data of Block 1 and **recalculate its hash**.
- Observe how all subsequent blocks become **invalid** unless their hashes are also updated.

**🎯 Goal:**  
Understand how tampering a single block affects the **entire blockchain**, ensuring **data integrity and immutability**.

### Output :

 Block 0:
Data: Genesis Block
Hash: 05aedbc46e49723bde385ea222116e62a5168255996b753035acac8ba82e6c49
Previous Hash: 0

Block 1:
Data: Block 1 data
Hash: d6f55b59cc11f9a70fb12cc8804c8a5a5814c776da32d087bd28cb4e5471fd67
Previous Hash: 05aedbc46e49723bde385ea222116e62a5168255996b753035acac8ba82e6c49

Block 2:
Data: Block 2 data
Hash: 9d0daa013f4bfd8ab605d46d46450cfe37c55baeddf53688a725f566f250d6c0
Previous Hash: d6f55b59cc11f9a70fb12cc8804c8a5a5814c776da32d087bd28cb4e5471fd67

🔧 Tampering Block 1...
🔍 Checking blockchain validity:

Block 0:
Data: Genesis Block
Hash: 05aedbc46e49723bde385ea222116e62a5168255996b753035acac8ba82e6c49
Previous Hash: 0

Block 1:
Data: Hacked Data
Hash: 8c98f0250abe9890204fabe60d874931a0ca0f540266fd64edf927159a6a8a26
Previous Hash: 05aedbc46e49723bde385ea222116e62a5168255996b753035acac8ba82e6c49

Block 2:
Data: Block 2 data
Hash: 9d0daa013f4bfd8ab605d46d46450cfe37c55baeddf53688a725f566f250d6c0
Previous Hash: d6f55b59cc11f9a70fb12cc8804c8a5a5814c776da32d087bd28cb4e5471fd67
