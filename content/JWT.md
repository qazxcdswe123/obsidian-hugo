---
aliases: [JSON Web Token]
date created: Dec 20th, 2022
date modified: May 21st, 2023
---
## What
JWTs contain encoded JSON objects, including a set of claims, and are signed using a cryptographic algorithm to ensure that the claims cannot be altered after the token is issued.

## How
A JWT consists of three parts: header, payload, and signature, separated by dots
- The header: Contains the type of token — JWT in this case — and the signing algorithm.
- The payload: Contains the claims, which are used to transmit information between two parties. What these claims are depends on the use case at hand. For example, a claim may assert who issued the token, how long it is valid for, or what permissions the client has been granted. This is displayed as a JSON string, usually containing no more than a dozen fields to keep the JWT compact. This information is typically used by the server to verify that the user has permission to perform the action they are requesting.
- The signature: Ensures that the token hasn’t been altered. The party that creates the JWT signs the header and payload with a secret that is known to both the issuer and receiver, or with a private key known only to the sender. When the token is used, the receiving party verifies that the header and payload match the signature.

## Why


## Links
