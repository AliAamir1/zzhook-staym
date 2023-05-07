# Estate-booking Application on web3.0


## Hardhat Purpose
Hardhat is a software development environment that allows developers to test and deploy their dApps on the Ethereum network. It is an open-source tool that provides a comprehensive suite of testing tools and an easy-to-use interface that makes testing and debugging smart contracts a breeze. 

## Benefits of Using Hardhat:
One of the main benefits of using Hardhat is its simplicity. It provides a clean and easy-to-use interface that allows developers to test their dApps quickly and efficiently. It also provides a comprehensive suite of testing tools that cover everything from unit testing to end-to-end testing, making it an all-in-one solution for Web 3.0 testing.

Another benefit of using Hardhat is its flexibility. It can be used with a wide range of testing frameworks, including Mocha and Chai, making it easy to integrate into existing development workflows. It also provides support for multiple Ethereum networks, including the main Ethereum network, as well as test networks like Rinkeby and Kovan.

Hardhat also supports test automation, allowing developers to automate their testing processes and ensure that their dApps are always functioning as intended. This can save developers time and effort, as well as ensure that their applications are reliable and secure.

## Testing with Hardhat:

Hardhat provides a suite of testing tools that make it easy to test dApps on the Ethereum network. These tools include:

- Hardhat Network: A local Ethereum network that can be used for testing and development purposes.
- Hardhat Ethers: A library that provides a simple and intuitive way to interact with the Ethereum network.
- Hardhat Waffle: A testing framework that makes it easy to write and run tests for smart contracts.
- Hardhat Console: A console that allows developers to interact with their dApps and test them in real-time.

## To test a dApp using Hardhat, developers can follow these steps:

- Install Hardhat and set up a new project.
- Write smart contracts using Solidity.
- Write tests using Hardhat Waffle.
- Run tests using Hardhat.



# Seting up the Estate bookings NFT DApp

## Technology Stack & Tools

- Solidity (Writing Smart Contracts & Tests)
- Javascript (React & Testing)
- [Hardhat](https://hardhat.org/) (Development Framework)
- [Ethers.js](https://docs.ethers.io/v5/) (Blockchain Interaction)
- [React.js](https://reactjs.org/) (Frontend Framework)

## Requirements For Initial Setup
- Install [NodeJS](https://nodejs.org/en/)

## Setting Up
### 1. Clone/Download the Repository

### 2. Install Dependencies:
`$ npm install`

### 3. Run tests
`$ npx hardhat test`

### 4. Start Hardhat node
`$ npx hardhat node`

### 5. Run deployment script
In a separate terminal execute:
`$ npx hardhat run ./scripts/deploy.js --network localhost`

### 7. Start frontend
`$ npm run start`
