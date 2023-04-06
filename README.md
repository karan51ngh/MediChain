# MediChain
A Consortium Blockchain for maintaining Patient Details across all private and public health facilities of a country.
(Application Of Blockchain in Healthcare)

## Abstract
A blockchain network can be used to connect hospitals, diagnostic labs, drug companies, and doctors, allowing them to securely access and update patient medical records in real time. This decentralized approach not only improves the efficiency and security of data exchange but also ensures the authenticity and integrity of the data through the use of tamper-evident, immutable audit trails.

One potential benefit of using blockchain in the healthcare system is the ability for doctors to
quickly and securely access a patient's medical history in emergency situations. This can greatly
impact the quality of care provided to the patient, as timely access to comprehensive medical
information can inform treatment decisions.

Another benefit of using a decentralized approach is that it prevents any one entity from
controlling or restricting access to patient data. This ensures that authorized healthcare providers
can easily and securely access the information they need to provide the best possible care to
patients.

Additionally, implementing a blockchain-based system for storing and sharing medical data can
improve patient privacy and security. By giving patients control over their personal medical
information, and preventing the sale of this data to third parties, blockchain technology can help
promote trust and transparency within the healthcare system.

## Overview
- To implement a blockchain-based system, called **MediChain** for maintaining the medical records of all patients in a country. 
- We would need to design a distributed database that is composed of interconnected
nodes. 
- Each hospital would act as a node on the network and would be responsible for securely
storing and updating the medical records of its patients. 


## Architecture Explained Briefly
The implementation details of our blockchain system:
1. The **government** will have a node on the blockchain, which will allow it to govern the
addition or removal of hospital nodes from the network. However, the government node
will not have access to or control over the data stored on the blockchain.
2. The **hospital** nodes will be able to add and validate data on the blockchain. This will
allow hospitals to securely store and access their patient's medical records, while also
maintaining the integrity and reliability of the information.
3. The blockchain will use a **permission-based**, or **private model**, where only authorized
hospitals and medical professionals have access to the network. This will ensure that the
data is only accessible to those who are authorized to view it and will help to protect
patient privacy.
4. To ensure the accuracy and authenticity of the data on the blockchain, the hospital nodes
will use **PoS (Proof of Stake) consensus (A Modified Version)** to verify the information.

### Network Architecture

- ![Network Architecture](https://github.com/karan51ngh/MediChain/blob/main/images/networkArchitecture.png)
- There exists one Government Node.
- All the other Nodes are Hospital Nodes.
-Information transfer can only occur between Government Node and Hospital Nodes
- Each Hospital Node has equal voting pow

### Node-Level Architecture
- ![Node Architecture](https://github.com/karan51ngh/MediChain/blob/main/images/nodeArchitecture.png)
- Government Node connects with all the Hospital Nodes
- Hospital Nodes have access to their copy of the database