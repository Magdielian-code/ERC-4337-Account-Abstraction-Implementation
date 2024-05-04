Description
 Comment
Write a backend service with a language/web framework of your choice to generate an ERC-4337 smart wallet/account. The service should have only one endpoint [GET] /create-account

    Calculate the counterfactual address by interacting with the SimpleAccountFactory contract’s getAddress function
    The address owner parameter should be an address you programmatically generated using a 12-word mnemonic
    Write a util function in your backend service to submit an EIP-4337 user operation from your smart account to a bundler endpoint 

Technical Notes
    Use a testnet node of your choice
    SimpleAccountFactory contract address: 0x9406Cc6185a346906296840746125a0E44976454
    Do not use web3js/ethers.js or any web3 client libraries for interacting with a node or bundler API
    You can use the Bundler API from Stackup.sh 

Resources
    Learn about EIP-4337 -> https://www.youtube.com/watch?v=1pE261Tbjcc
    Original EIP -> https://eips.ethereum.org/EIPS/eip-4337
    Stackup.sh Bundler API Docs -> https://docs.stackup.sh/reference/erc-4337-bundler-api-endpoints
    Ethereum Node API Docs -> https://ethereum.org/en/developers/docs/apis/json-rpc/