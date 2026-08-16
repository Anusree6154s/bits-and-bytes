---
layout: post
date: 19 aug 2024
excerpt: Passport JWT Documentation
permalink: passport-jwt
---

# Passport-jwt Documentaion

## Table of Contents

1. [Overview](#overview)
2. [Features and Usage](#features-and-usage)
   - [Installation and Import](#installation-and-import)
   - [Configuration](#Configuration)
     - [Basic Code Structure](#basic)
     - [Parts of Code in detail](#Parts)
       - [Imports](Imports)
       - [`passport.use(name[optional], strategy)`](#passport)
       - [`new Startegy(options, verifyCallback)`](#Strategy)
   - [Full Code Structure (seperated into modules)](#full-structure)
3. [Authentication](#authentication)
   - [With session support (w/o callback)](#With)
   - [Without session support (w/ callback)](#Without)
4. [Methods to pass JWT Token](#passing-jwt-token)

## Overview

- A middleware for Express.js framework that provides authentication and authorization using JSON Web Tokens (JWT).
- A passport strategy to work with JWT
- This only handles what we can do with a JWT token created using passport. To create a token checkout [Passport](http://passportdocumentation)

## Features and Usage

1.  Installation and Import
    <a id="installation-and-import"></a> - Install: `npm install passport-jwt` - Import: `const { Strategy, ExtractJwt } = require("passport-jwt");` - _passport-jwt is a class with 2 properties - Strategy and ExtractJwt_ - _Strategy is a class with 2 parameters passed to its contructor_ - _ExtractJwt is an object with various sub properties_

2.  Configuration
    <a id="Configuration"></a>

        - Basic Structure:

    <a id="basic"></a>

          ```javascript
          const JwtStrategy = require("passport-jwt").Strategy;
          const ExtractJwt = require("passport-jwt").ExtractJwt;
          const passport = require("passport");

          // Options for the strategy
          const opts = {
            jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(), // Extract token from Authorization header
            secretOrKey: "your_jwt_secret_key", // Secret key for verifying token
          };

          // JWT Strategy
          passport.use(
            new JwtStrategy(opts, (jwtPayload, done) => {
              // Find the user based on the jwtPayload.sub (subject)
              User.findOne({ id: jwtPayload.sub }, (err, user) => {
                if (err) {
                  return done(err, false);
                }
                if (user) {
                  return done(null, user);
                } else {
                  return done(null, false); // User not found
                }
              });
            })
          );
          ```

        - Parts of the configuration:

    <a id="Parts"></a>

          1. Imports:

    <a id="Imports"></a> - `const {Strategy,ExtractJwt} = require("passport-jwt")` - `const passport = require("passport");` 2. passport.use() method to register strategy (2 ways):
    <a id="passport"></a>
    <details>
    <summary>
    <code>passport.use(Strategy)</code> - Default Strategy
    </summary>

             - Registers a strategy directly.
             - Will be treated as the default strategy.
             - Allows you to refer to the strategy by the name _jwt_ later in the *passport* method `passport.authenticate('jwt')`.
             </details>

             <details>
                 <summary>
                 <code>passport.use(name, Strategy)</code> - Named Strategy [optional]
                 </summary>

             - Allows you to refer to the strategy by the name _jwt_ later in the *passport* method `passport.authenticate('name')`.
             </details>
          3. Strategy (has 2 parameters):

    <a id="Strategy"></a> - Has two parameters: `opts` and `verify`

                - Parameters:
                    <details>
                    <summary>
                        <code>`opts`</code> - (object) Options
                    </summary>

                    - This parameter is an object that defines various options for the strategy.

                    - Example:
                        ```js
                        const opts = {
                            jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
                            secretOrKey: "your_jwt_secret_key",
                            issuer: "your_issuer", // optional
                            algorithms: ["HS256"], // optional
                            ignoreExpiration: false, // optional, defaults to false
                        };
                        ```
                    - Properties:

                        1. <details>
                                <summary>
                                <code>jwtFromRequest</code> - (function) To specify method of Jwt extraction
                                </summary>

                            - Specifies how the JWT will be extracted from the incoming request from client using _ExtractJwt_ class.
                            - Example
                                ```javascript
                                const opts = {
                                    jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken();
                                }
                                ```

                            - All options (Properties of ExtractJwt):

                            1. <details>
                                <summary>
                                <code>ExtractJwt.fromAuthHeaderAsBearerToken()</code>
                                </summary>

                                - **Usage**: Extracts the JWT from the Authorization header, assuming the JWT is prefixed by the word Bearer.
                                - **Input parameter**: none
                                - **Example**:

                                ```js
                                jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken();
                                ```

                                </details>

                            2. <details>
                                <summary>
                                <code>ExtractJwt.fromHeader(header_name)</code>
                                </summary>

                                - **Usage**: Extracts the JWT from a custom header in the request.
                                - **Input parameter**: header_name (string) - The name of the custom header containing the JWT.
                                - **Example**:

                                ```js
                                jwtFromRequest: ExtractJwt.fromHeader('auth_token')
                                ```

                                </details>


                            3. <details>
                                <summary>
                                <code>ExtractJwt.fromBodyField(field_name)</code>
                                </summary>

                                - **Usage**:  Extracts the JWT from a specific field in the request body (typically used in form submissions or JSON payloads).
                                - **Input parameter**: field_name (string) - The name of the field in the request body that contains the JWT.
                                - **Example**:

                                ```js
                                jwtFromRequest: ExtractJwt.fromBodyField('token')
                                ```

                                </details>

                            4. <details>
                                <summary>
                                <code>ExtractJwt.fromUrlQueryParameter(param_name)</code>
                                </summary>

                                - **Usage**:  Extracts the JWT from a URL query parameter.
                                - **Input parameter**: param_name (string) - The name of the query parameter in the URL that contains the JWT.
                                - **Example**:

                                ```js
                                jwtFromRequest: ExtractJwt.fromUrlQueryParameter('token')
                                ```
                                </details>

                            5. <details>
                                <summary>
                                <code>fromAuthHeaderWithScheme(auth_scheme) </code>
                                </summary>

                                - **Usage**:  Extracts the JWT from Authorization Header with the specified auth_scheme
                                - **Input parameter**: (string) Auth scheme like Bearer, Token, etc
                                - **Example**:

                                    ```js
                                    jwtFromRequest: ExtractJwt.ExtractJwt.fromAuthHeaderWithScheme('Token')
                                    ```
                                </details>

                            6. <details>
                                <summary>
                                <code>fromExtractors([array of extractor functions]) </code>
                                </summary>

                                - **Usage**:  Lets us define multiple extractors to extract jwt from different sources one after other.
                                - **Input parameter**: (array) Array of extractors
                                - **Example**:

                                    ```js
                                    const extractors = [
                                        ExtractJwt.fromAuthHeaderAsBearerToken(),         // Try the Bearer token from Authorization header
                                        ExtractJwt.fromUrlQueryParameter('auth_token')    // Then try the token from the URL query parameter
                                    ];

                                    const opts = {
                                        jwtFromRequest: ExtractJwt.fromExtractors(extractors),
                                        secretOrKey: 'your_secret_key'
                                    };
                                    ```
                                </details>

                            7. <details>
                                <summary>
                                <code>Custom Extractors</code>
                                </summary>

                                - **Usage**:  Lets us define custom extractoinof tokens from anywhere
                                - **Example**:
                                    ```js
                                    //when extracting from cookies using cookie parser
                                    var cookieParser = require('cookie-parser')
                                    const express = require('express');

                                    const app = express()
                                    app.use(cookieParser())

                                    //custom extractor
                                    var cookieExtractor = function (req) {
                                    var token = null;
                                    if (req && req.cookies) {
                                        token = req.cookies["jwt"];
                                    }
                                    return token;
                                    };

                                    const opts = {
                                        jwtFromRequest: cookieExtractor,
                                        secretOrKey: 'your_secret_key'
                                    };
                                    ```
                                </details>


                            </details>

                        2. <details>
                            <summary>
                                <code>secretOrKey</code> - (string or buffer) Secret key to verify JWT
                            </summary>

                            - The key used to verify the JWT signature. This is essential for validating the authenticity of the token.

                            - **For symmetric algorithms** (e.g., HS256, HS384, HS512), `secretOrKey` will be a shared secret string or buffer used by both the server that signs the JWT and the server that verifies it.
                            - **For asymmetric algorithms** (e.g., RS256, RS384, RS512), `secretOrKey` will be a public key that verifies the JWT, while the corresponding private key is used to sign the JWT.

                            - Examples:
                                - Symmetric key:
                                    ```js
                                    const opts = {
                                        secretOrKey: 'your_jwt_secret_key' //can be any random word
                                    };
                                    ```
                                - Asymmetric key:
                                    ```js
                                    const opts = {
                                        secretOrKey: fs.readFileSync('./path/to/public.key', 'utf8')
                                    };
                                    ```
                                - Note:
                                    - If using symmetric encryption (e.g., HS256), the same secretOrKey must be used for both signing and verifying the token.
                                    - If using asymmetric encryption (e.g., RS256), the secretOrKey should be the public key, while the private key is used to sign the token.
                                    - It is important to securely manage this key, as exposure could compromise the security of your system.

                            </details>

                        3. <details>
                            <summary>
                                <code>secretOrKeyProvider</code> - (function) [optional] Function to get secretOrKey from anywhere
                            </summary>

                            - This function dynamically provides the secret or public key for verifying the JWT. It is useful in cases where the key needs to be determined based on the request, such as in multi-tenant applications or when using different keys for different users.
                            - Do not use both `secretOrKey` and `secretOrKeyProvider`. Use either of them
                            - Parameters:
                                - `request`: The original HTTP request object.
                                - `rawJwtToken`: The raw JWT token extractedfrom the request.
                                - `done`: A function to return the key, with the parameters:
                                    - `err`
                                    - `secretOrKey` (string or buffer)
                            - Example:
                                ```js
                                    const opts = {
                                        secretOrKeyProvider: (request, rawJwtToken, done) => {
                                            // Logic to determine the secret or key dynamically
                                            const secretOrKey = getSecretForTenant(request); // Example function to get the secret key based on tenant
                                            done(null, secretOrKey); // Pass the key to the callback function
                                        }
                                    };
                                ```

                                - Note:
                                    1. If secretOrKeyProvider is provided, it overrides the static secretOrKey option
                                    2. Useful in scenarios where the key might change per request or per user, such as:
                                        - Multi-tenant applications where each tenant has a different key.
                                        - Using different keys for different users or services.
                                    3. If the key cannot be determined (e.g., a database lookup fails), call done(err) to signal an error.
                                    4. When using asymmetric encryption (e.g., RS256), the secretOrKeyProvider would return the public key for verification.

                                - Example for multi-tenant application:
                                    ```js
                                    const opts = {
                                        secretOrKeyProvider: (request, rawJwtToken, done) => {
                                            // Get the tenant's key based on some property of the request (e.g., subdomain or user ID)
                                            const tenantKey = getTenantKeyFromDb(request.tenantId); // Example function to retrieve tenant's key
                                            done(null, tenantKey);
                                        }
                                    };
                                    ```
                                - Use Case:
                                    - Multi-tenant systems where different tenants have different signing keys.
                                    - Dynamic environments where the key cannot be determined statically and must be retrieved or computed based on the incoming request.
                            </details>

                        4. <details>
                                <summary>
                                <code>issuer</code> - (string or array) [optional]  Verifies the issuer (iss) claim of the token.
                                </summary>
                                - Examples:

                                ```js
                                const opts = {
                                            issuer: 'https://accounts.google.com'
                                        };
                                ```
                                ```js
                                const opts = {
                                        issuer: [
                                            'https://accounts.google.com',
                                            'https://your-tenant-name.auth0.com/',
                                            'https://dev-123456.okta.com'
                                        ]
                                    };
                                ```
                                - Use Cases:
                                    - **Single Issuer Application**: If all tokens are issued by your application, you would set the issuer option to your app's identifier.
                                    - **Third-Party Tokens**: If you're working with tokens issued by third parties (e.g., OAuth providers or external identity systems), you would set issuer to the known trusted issuer.
                            </details>

                        5. <details>
                            <summary>
                            <code>algorithms</code> - (array) [optional] List of allowed algorithms for token verification, e.g., ['HS256', 'RS256'].
                            </summary>

                            - **Purpose**: This option helps enforce which algorithms are accepted for signing JWTs, improving security by rejecting tokens signed with algorithms that are not trusted or expected.
                            - **Default Behavior**: If the algorithms option is not provided, the strategy will allow any algorithm,
                            - Examples:
                                ```js
                                const opts = {,
                                    algorithms: ['HS256', 'RS256', 'ES256'] // Accepts JWTs signed with HS256, RS256, or ES256 algorithms
                                };
                                ```
                                ```js
                                const opts = {,
                                    algorithms: ['HS256']
                                };
                                ```
                            </details>

                        6. <details>
                            <summary>
                            <code>audience</code> - (string or array) [optional] To specify the recipients of Jwt
                            </summary>

                            - **Purpose**: To specify the recipients of Jwt. Will be verifiesd against the recipients mentioned in *aud* coming through *jwt_payload*.
                            - Examples:
                                ```js
                                const opts = {,
                                     "aud": "user-service",
                                };
                                ```
                                ```js
                                const opts = {,
                                     "aud": ["user-service", "billing-service", "yoursite.net"]
                                };
                                ```
                            </details>

                        7. <details>
                                <summary>
                                <code>ignoreExpiration</code> - (boolean) [optional] Whether to ignore the token's expiration time during verification.
                                </summary>

                                - **Purpose**:
                                    - When you want to accept tokens even if they have expired.
                                    - Useful in testing environments where you might not want to deal with token expiration.
                                    - The `exp` claim in a JWT specifies the expiration time of the token. Expiry is not set by passport-jwt.
                                - **Default Behavior**: By default, ignoreExpiration is false, meaning that Passport-JWT will check the exp claim to ensure the token is not expired.
                                - Examples:
                                    ```js
                                    const opts = {
                                        ignoreExpiration: true // Accepts expired tokens
                                    };
                                    ```
                                    ```js
                                    const opts = {
                                        ignoreExpiration: false // Enforces expiration check
                                    };
                                    ```
                            </details>

                        8. <details>
                            <summary>
                            <code>passReqToCallback</code> - (boolean) [optional] Whether to pass the request object to the verification callback.
                            </summary>

                            - The `passReqToCallback` option specifies whether the request object should be passed to the `verify` callback function in the `JwtStrategy`.
                            - Useful if you need access to the `req` object for additional logic inside verify callback.
                            - Example:
                                ```js
                                const opts = {
                                    passReqToCallback: true // Passes the request object to the verify callback
                                };
                                ```
                                ```js
                                passport.use(new JwtStrategy(opts, (req, jwtPayload, done) => { //now you can add req as parameter
                                    // Access request object
                                    console.log(req.headers); // Example of accessing headers

                                    User.findById(jwtPayload.sub, (err, user) => {
                                        if (err) return done(err, false);
                                        if (user) return done(null, user);
                                        return done(null, false);
                                    });
                                }));
                                ```
                            </details>

                        9. <details>
                            <summary>
                            <code>jsonWebTokenOptions </code> - (object) [optional + deprecated] To pass options to customise token verification
                            </summary>

                            - **Purpose**: To pass options directly to the underlying jsonwebtoken.verify() and customise token verification.
                            - **Deprecated**: Though deprecated, still allows you to pass audience / issuer / algorithms / ignoreExpiration on the options
                            - **Properties**:
                                - <details><summary><code>algorithms</code>: (array) Specifies allowed signing algorithms.</summary>

                                    - Specifies which algorithms are allowed for verifying the JWT.
                                    - eg: `algorithms: ['HS256']`
                                    </details>
                                - <details><summary><code>audience</code>: (string | RegExp | array) Specifies the expected audience of the JWT.</summary>

                                    -  Specifies the expected audience of the JWT (who the token is intended for). It can be a string, regex, or array of strings/regexes.
                                    - eg: `audience: 'your-app-client-id'`
                                    </details>
                                - <details><summary><code>clockTimestamp</code>: (integer) Sets a fixed time for token validation.</summary>

                                    - The time in seconds since the epoch to use as the current time when verifying the JWT.
                                    ```js
                                    clockTimestamp: Math.floor(Date.now() / 1000) // current time in seconds
                                    ```
                                    </details>
                                - <details><summary><code>clockTolerance</code>: (integer) Helps with clock skew issues.</summary>

                                    - Specifies the allowed clock skew (in seconds) when verifying the exp and nbf claims (useful when different servers have slightly unsynchronized clocks).
                                    - eg: `clockTolerance: 5`
                                    </details>
                                - <details><summary><code>complete</code>: (boolean) Returns `{ payload, header, signature }` if true.</summary>

                                    -  If true, returns an object with the decoded { payload, header, signature } instead of just the payload.
                                    - eg: `complete: true`
                                    </details>
                                - <details><summary><code>issuer</code>: (string | array) Specifies the expected issuer of the JWT.</summary>

                                    - Specifies the expected issuer of the JWT (the entity that issued the token). Can be a string or an array of strings.
                                    - eg: `issuer: 'auth.your-app.com'`
                                    </details>
                                - <details><summary><code>ignoreExpiration</code>: (boolean) Ignores the `exp` claim if true.</summary>

                                    -  If true, ignores the exp claim during verification (useful in development, but not recommended in production).
                                    - eg: `ignoreExpiration: true`
                                    </details>
                                - <details><summary><code>ignoreNotBefore</code>: (boolean) Ignores the `nbf` claim if true.</summary>

                                    - If true, ignores the nbf (Not Before) claim when verifying the token.
                                    - eg: `ignoreNotBefore: true`
                                    </details>
                                - <details><summary><code>jwtid</code>: (string) Validates the token ID (jti) claim.</summary>

                                     - The jti (JWT ID) claim specifies a unique identifier for the token to prevent replay attacks.
                                     - eg: `jwtid: 'unique-jwt-id-12345'`
                                    </details>
                                - <details><summary><code>nonce</code>: (string) Checks the `nonce` claim (used in OpenID Connect).</summary>

                                    -  Used to check the nonce claim in OpenID Connect to prevent replay attacks. The nonce is a string used to associate a client session with an ID token.
                                    - eg: `nonce: 'nonce-value-generated-at-auth-time'`
                                    </details>
                                - <details><summary><code>subject</code>: (string) Specifies the expected `sub` (Subject) claim.</summary>

                                     - Specifies the expected sub (Subject) claim of the JWT, which typically identifies the principal (user) of the token.
                                     - eg: `subject: 'user-id-12345'`
                                    </details>
                                - <details><summary><code>maxAge</code>: (string | number) Limits how old a token can be.</summary>

                                    -  Specifies the maximum allowable age (in seconds or a time string) for the JWT since its iat (Issued At) claim. Used to reject old tokens.
                                    - eg: `maxAge: '24h'`
                                    </details>
                                - <details><summary><code>allowInvalidAsymmetricKeyTypes</code>: (boolean) Allows invalid asymmetric key types if true.</summary>

                                    - When set to true, allows invalid asymmetric key types during verification (not recommended unless necessary).
                                    - eg: `allowInvalidAsymmetricKeyTypes: true`
                                    </details>
                            - Examples:
                                ```js
                                const opts = {
                                    jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
                                    secretOrKey: 'your_secret_key',
                                    jsonWebTokenOptions: {
                                        clockTolerance: 5,  // Allow 5 seconds of clock skew
                                        maxAge: '1d',       // Only accept tokens no more than 1 day old
                                        algorithms: ['HS256'],  // Only accept tokens signed with HS256
                                        ignoreNotBefore: true, // Will ignore token's Not before dates
                                        ignoreExpiration: false // Will validate the 'expiration' claim
                                    }
                                };

                                passport.use(new JwtStrategy(opts, (jwtPayload, done) => {
                                    User.findById(jwtPayload.sub, (err, user) => {
                                        if (err) return done(err, false);
                                        if (user) return done(null, user);
                                        return done(null, false);
                                    });
                                }));
                                ```
                            </details>
                    </details>

                    <details>
                    <summary>
                        <code>`verify`</code> - (function) Verify Callback
                    </summary>

                    - **Purpose**: Callback used in the `JwtStrategy` to validate the JWT and determine if it should be accepted.
                    - **Parameters**:
                        - <details>
                            <summary>
                            <code>payload</code> - (object) Payload for verify callback
                            </summary>

                            - **Purpose**: It is the decoded JWT payload, which contains the claims from the token (e.g., user ID, roles).
                            - It is an object that contains the claims from the decoded JWT. We can only access these claim values and set it. It is set using *jwt.sign()* using [*jsonwebtoken*](http://jwtdocumentation) module.
                            - **Properties**  **(Claims)**:
                                1. `sub`: The **subject** of the token, usually the user ID. This is a standard claim and is often used to identify the user.
                                2. `exp`: The **expiration** time of the token, specified as a Unix timestamp. This is a standard claim used to determine if the token has expired.
                                3. `iat`: The **issued-at** time, specified as a Unix timestamp. This indicates when the token was issued.
                                4. `iss`: The **issuer** of the token, which is a standard claim indicating who issued the token.
                                5. `aud`: The **audience** for which the token is intended. This is a standard claim indicating the recipient(s) of the token.
                                6. `nbf`: **Not Before** - The time before which the token should not be considered valid.
                                7. `jti`: **JWT ID** - A unique identifier for the token, which can be used to prevent replay attacks.

                                > **Note** : we can also have any custom claims. eg: roles, name.
                            - Example:
                                ```js
                                //setting claims in some other file
                                const jwt = require('jsonwebtoken')
                                fucntion signIn(req, res){
                                    const payload = {
                                        sub: user._id,
                                        roles: user.roles,
                                        exp: Math.floor(Date.now() / 1000) + (60 * 60)
                                        //etc
                                    }
                                    const token = jwt.sign(payload, 'your_jwt_secret_key')
                                    res.send({token})
                                }

                                //accessing those claims
                                passport.use(new JwtStrategy(opts, (jwtPayload, done) => {
                                    console.log('User ID:', jwtPayload.sub);
                                    console.log('Token Expiry Time:', jwtPayload.exp);
                                    console.log('User Roles:', jwtPayload.roles);

                                    User.findById(jwtPayload.sub, (err, user) => {
                                        if (err) return done(err, false);
                                        if (user) return done(null, user);
                                        return done(null, false);
                                    });
                                }));

                                ```
                            </details>

                        - <details>
                            <summary>
                            <code>done</code> - (fucntion) To indicate the result of the verification.
                            </summary>

                            - **Purpose**: To indicate the result of the verification.
                            - **Parameters**:
                                - `err`: Error during verification if any
                                - `user`: Any sort of data that comes out after the logic inside verify callback
                                - `info`: [optional] Any message regarding error or user
                            - Example:
                                ```js
                                //without info
                                passport.use(new JwtStrategy(opts, (jwtPayload, done) => {
                                    User.findById(jwtPayload.sub, (err, user) => {
                                        if (err) return done(err, false);
                                        if (user) return done(null, user); // Verification successful
                                        return done(null, false); // No user found, but no error
                                    });
                                }));
                                ```
                                ```js
                                //with info
                                passport.use(new JwtStrategy(opts, (jwtPayload, done) => {
                                    User.findById(jwtPayload.sub, (err, user) => {
                                        if (err) return done(err, false);
                                        if (!user) return done(null, false, { message: 'User not found' });
                                    });
                                }));
                                ```
                              </details>

                            - <details>
                                <summary>
                                <code>req</code> [conditional]
                                </summary>

                                - Only when inside opts, passReqToCallback is true
                                ```js
                                const opts = {passReqToCallback: true}

                                const verify = (req, payload, done)=>{
                                    // handle payload data
                                }
                                ```
                                </details>

                        - Example:
                            ```js
                            const verify = (jwtPayload, done) => {
                                // jwtPayload contains the decoded JWT payload
                                User.findById(jwtPayload.sub, (err, user) => {
                                    if (err) return done(err, false); // Error during user lookup
                                    if (user) return done(null, user); // User found, authentication successful
                                    return done(null, false); // User not found, authentication failed
                                });
                            }

                            passport.use(new JwtStrategy(opts, verify));
                            ```
                     </details>

                - Example:
                    ```js
                    const JwtStrategy = new Startegy(opts, verify)
                    passport.use(JwtStrategy);
                    ```
                - Strategy is of 2 tyes:
                    - <details><summary>With req</summary>

                        - paasing opts with true for passReqToCallback enables us to use `req` in verify callbak
                        ```js
                        const opts = { passReqToCallback:true }

                        const verify = (req, payload, done)=>{

                        }
                        ```
                        </details>
                    - <details><summary>Without req</summary>
                        ```js
                        opts = { passReqToCallback:false }
                        ```
                        </details>


3.  Full Structure (for deafult strategy):
    <a id="full-structure"></a> - Default Strategy:
    ```javascript
    const { Strategy, ExtractJwt } = require("passport-jwt");
    const passport = require("passport"); //to use for passport.use()

                // Options for the strategy
                const opts = {
                    jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
                    secretOrKey: "your_jwt_secret_key",
                    //etc
                };

                //verify callback for strategy
                const verify = (jwtPayload, done) => {
                    User.findOne({ id: jwtPayload.sub }, (err, user) => {
                    if (err) {
                        return done(err, false);
                    }
                    if (user) {
                        return done(null, user);
                    } else {
                        return done(null, false); // User not found
                    }
                    });
                };

                //new jwt-Strategy
                const JwtStrategy = new Strategy(opts, verify)

                //using new jwt-strategy in passport
                passport.use(JwtStrategy);

                //authenticating default jwt-strategy
                passport.authenticate('jwt')
            ```

        - Named Strategy:
            ```javascript
                const { Strategy, ExtractJwt } = require("passport-jwt");
                const passport = require("passport");

                const opts = {
                    jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
                    secretOrKey: "your_jwt_secret_key",
                    //etc
                };

                const verify = (jwtPayload, done) => {
                    User.findOne({ id: jwtPayload.sub }, (err, user) => {
                    if (err) {
                        return done(err, false);
                    }
                    if (user) {
                        return done(null, user);
                    } else {
                        return done(null, false);
                    }
                    });
                };

                const JwtStrategy = new Strategy(opts, verify)

                //using named jwt-strategy in passport
                passport.use('my-jwt', JwtStrategy);

                //authenticating named jwt-strategy
                passport.authenticate('my-jwt')
            ```

## Authenticating jwt after strategy configuration

- Ways:
  - As of understood till date, passport jwt can be authenticated in 2ways:
    - With session support (**without callback**)
    - Without session support (**with callback**)
  - With session support (without callback), one would need to many extar methods like `passport.serializeUser`, `session()`, etc. We would not have to specifically set `req.user` to user. Passport would do it internally for us.
  - Without session support (with callback), we dont need any extra methods. But we would need to set `req.user` to user explicitly by us.

1.  Without session support (**with callback**)
    <a id="Without"></a> - in the [internal code](https://github.com/jaredhanson/passport/blob/217018dbc46dcd4118dd6f2c60c8d97010c587f8/lib/middleware/authenticate.js#L221), if passport.authenticate gets a callback, it doesnt call any other internal function. It just returns that callback with user and err, to handle by ourself.
    ```js
    // Options for JWT strategy, including extractor function and secret key
    const optsJwt = {
    jwtFromRequest: cookieExtractor,
    secretOrKey: constant.secretKey
    }
    // Function to verify JWT token and retrieve user information
    const verifyJwt = async function (jwt_payload, done) {
    if (!jwt_payload.id) return done(null, false);

            try {
                let user = await User.findOne({ _id: jwt_payload.id });

                if (user) return done(null, santizeUser(user));
                else return done(null, false);

            } catch (error) {
                return done(err, false);
            }
        }

        // Options for Local strategy, specifying the field for username
        const optsLocal = { usernameField: "email" }
        // Function to verify local credentials and handle authentication
        const verifyLocal = async function (email, password, done) {
            try {
                const user = await User.findOne({ email: email }).exec();

                if (!user) {
                    return done(null, false, { message: "No such user email" });
                }

                crytpoJwt(user, password, done)

            } catch (error) {
                return done(error);
            }
        }

        // Initialize Passport with JWT strategy
        passport.use("jwt",new JwtStrategy(optsJwt, verifyJwt););

        // Middleware to authenticate requests using JWT strategy
        app.use((req, res, next) => {
            passport.authenticate("jwt", (err, user, info) => {
                if (err || !user)
                    return next(new ApiError(httpStatus.UNAUTHORIZED, "Please authenticate"))

                req.user = user;
                next()
            })(req, res, next)
        })
        ```

2.  With session support (**without callback**)
    <a id="With"></a> - When with callback, internalluy, passport passes many checks and process including - needing a session - needing to use passport.serializeUser atleast once with a callback containing user.id/user - In the latest version, for authenticating using _passport-jwt_ configured strategy, we need to use 2 extra methods from _passport_ package and 1 method from _express-session_ package: - <details>
    <summary>
    <code>passport.authenticate()</code> from passport
    </summary>

                - `passport.authenticate()` is a passport middleware. It has been [customised internally](https://github.com/mikenicholson/passport-jwt/blob/master/lib/strategy.js#L90) to authenticate jwt via passport-jwt package.
                - 3 paramters:
                    - strategy: (string|array)
                    - options
                    - callback [optional]
                - <details>
                    <summary>It is wrapped inside a wrapper as an express middleware to access req, res and next. Without the wrapper it won't pass on to the next function.
                    </summary>

                    ```js
                    app.use((req, res, next)=>{
                        passport.authenticate('jwt')(req, res, next)
                    })
                    ```
                    </details>
                - <details>
                    <summary>
                    In older versions it would itself be placed as a middleware, but not anymore
                    </summary>

                    ```js
                    app.use(passport.authenticate('jwt'))
                    ```
                    </details>

                - Parameters:
                    - <details>
                        <summary>
                            <code>strategy</code>: (string or array)
                        </summary>

                        - **Purpose**: To point to the strategies named during configuration.
                        - **Example**: jwt, my-jwt, [jwt, my-jwt], etc
                        </details>

                    - <details>
                        <summary>
                            <code>options</code>: (object) [optional]
                        </summary>

                        - **Purpose**: Options to control the behavior of the authentication middleware.
                        - It controls the behaviour at individual route/request level in comparison to opts options which controls behaviour at global/strategy level.
                        - If there are conflicting options between opts and authenticateOptions, then authenticateOptions will override for that particular route.
                        - **Properties**:
                            <details>
                            <summary>1. authInfo</summary>
                            <p><strong>Description:</strong> Whether to include additional authentication information.</p>
                            <p><strong>Default:</strong> undefined (additional info is not included).</p>
                            <p><strong>Example:</strong></p>
                            <pre><code>passport.authenticate('strategy', { authInfo: true });</code></pre>
                            </details>

                            <details>
                            <summary>2. assignProperty</summary>
                            <p><strong>Description:</strong> Assigns the object provided by the verify callback to the specified property on the <code>req</code> object.</p>
                            <p><strong>Default:</strong> undefined (the object is assigned to <code>req.user</code>).</p>
                            <p><strong>Example:</strong></p>
                            <pre><code>passport.authenticate('strategy', { assignProperty: 'userAccount' });</code></pre>
                            </details>

                            <details>
                            <summary>3. failureFlash</summary>
                            <p><strong>Description:</strong> True to flash failure messages or a string to use as a flash message for failures.</p>
                            <p><strong>Default:</strong> undefined (failure messages are not flashed).</p>
                            <p><strong>Example:</strong></p>
                            <pre><code>passport.authenticate('strategy', { failureFlash: 'Login failed' });</code></pre>
                            </details>

                            <details>
                            <summary>4. failureMessage</summary>
                            <p><strong>Description:</strong> True to store failure message in <code>req.session.messages</code>, or a string to use as an override message for failure.</p>
                            <p><strong>Default:</strong> undefined (failure messages are not stored).</p>
                            <p><strong>Example:</strong></p>
                            <pre><code>passport.authenticate('strategy', { failureMessage: 'Login unsuccessful' });</code></pre>
                            </details>

                            <details>
                            <summary>5. failureRedirect</summary>
                            <p><strong>Description:</strong> URL to redirect to after a failed login attempt.</p>
                            <p><strong>Default:</strong> undefined (no redirect occurs).</p>
                            <p><strong>Example:</strong></p>
                            <pre><code>passport.authenticate('strategy', { failureRedirect: '/login' });</code></pre>
                            </details>

                            <details>
                            <summary>6. failWithError</summary>
                            <p><strong>Description:</strong> Whether to fail with an error.</p>
                            <p><strong>Default:</strong> undefined (does not fail with error).</p>
                            <p><strong>Example:</strong></p>
                            <pre><code>passport.authenticate('strategy', { failWithError: true });</code></pre>
                            </details>

                            <details>
                            <summary>7. keepSessionInfo</summary>
                            <p><strong>Description:</strong> Whether to keep session information.</p>
                            <p><strong>Default:</strong> undefined (session info is not specifically retained).</p>
                            <p><strong>Example:</strong></p>
                            <pre><code>passport.authenticate('strategy', { keepSessionInfo: true });</code></pre>
                            </details>

                            <details>
                            <summary>8. session</summary>
                            <p><strong>Description:</strong> Save login state in session.</p>
                            <p><strong>Default:</strong> true (session is used by default).</p>
                            <p><strong>Example:</strong></p>
                            <pre><code>passport.authenticate('strategy', { session: false });</code></pre>
                            </details>

                            <details>
                            <summary>9. scope</summary>
                            <p><strong>Description:</strong> Scope of access required.</p>
                            <p><strong>Default:</strong> undefined (no scope is specified).</p>
                            <p><strong>Example:</strong></p>
                            <pre><code>passport.authenticate('strategy', { scope: ['read', 'write'] });</code></pre>
                            </details>

                            <details>
                            <summary>10. successFlash</summary>
                            <p><strong>Description:</strong> True to flash success messages or a string to use as a flash message for success.</p>
                            <p><strong>Default:</strong> undefined (success messages are not flashed).</p>
                            <p><strong>Example:</strong></p>
                            <pre><code>passport.authenticate('strategy', { successFlash: 'Login successful' });</code></pre>
                            </details>

                            <details>
                            <summary>11. successMessage</summary>
                            <p><strong>Description:</strong> True to store success message in <code>req.session.messages</code>, or a string to use as an override message for success.</p>
                            <p><strong>Default:</strong> undefined (success messages are not stored).</p>
                            <p><strong>Example:</strong></p>
                            <pre><code>passport.authenticate('strategy', { successMessage: 'Welcome back!' });</code></pre>
                            </details>

                            <details>
                            <summary>12. successRedirect</summary>
                            <p><strong>Description:</strong> URL to redirect to after a successful login.</p>
                            <p><strong>Default:</strong> undefined (no redirect occurs).</p>
                            <p><strong>Example:</strong></p>
                            <pre><code>passport.authenticate('strategy', { successRedirect: '/dashboard' });</code></pre>
                            </details>

                            <details>
                            <summary>13. successReturnToOrRedirect</summary>
                            <p><strong>Description:</strong> URL to redirect to or return to after a successful login.</p>
                            <p><strong>Default:</strong> undefined (no redirect or return occurs).</p>
                            <p><strong>Example:</strong></p>
                            <pre><code>passport.authenticate('strategy', { successReturnToOrRedirect: '/profile' });</code></pre>
                            </details>

                            <details>
                            <summary>14. state</summary>
                            <p><strong>Description:</strong> State parameter for the request.</p>
                            <p><strong>Default:</strong> undefined (no state is set).</p>
                            <p><strong>Example:</strong></p>
                            <pre><code>passport.authenticate('strategy', { state: 'xyz' });</code></pre>
                            </details>

                            <details>
                            <summary>15. pauseStream</summary>
                            <p><strong>Description:</strong> Pause the request stream before deserializing the user object from the session.</p>
                            <p><strong>Default:</strong> false (stream is not paused).</p>
                            <p><strong>Example:</strong></p>
                            <pre><code>passport.authenticate('strategy', { pauseStream: true });</code></pre>
                            </details>

                            <details>
                            <summary>16. userProperty</summary>
                            <p><strong>Description:</strong> Property on <code>req</code> that will be set to the authenticated user object.</p>
                            <p><strong>Default:</strong> 'user' (authenticated user is set to <code>req.user</code>).</p>
                            <p><strong>Example:</strong></p>
                            <pre><code>passport.authenticate('strategy', { userProperty: 'currentUser' });</code></pre>
                            </details>

                            <details>
                            <summary>17. passReqToCallback</summary>
                            <p><strong>Description:</strong> Whether to pass the request object to the callback.</p>
                            <p><strong>Default:</strong> undefined (request object is not passed to the callback).</p>
                            <p><strong>Overrides:</strong> Overrides passReqToCallback set in opts of strategy configuration</p>
                            <p><strong>Example:</strong></p>
                            <pre><code>passport.authenticate('strategy', { passReqToCallback: true });</code></pre>
                            </details>

                            <details>
                            <summary>18. prompt</summary>
                            <p><strong>Description:</strong> Prompt parameter for the request.</p>
                            <p><strong>Default:</strong> undefined (no prompt is set).</p>
                            <p><strong>Example:</strong></p>
                            <pre><code>passport.authenticate('strategy', { prompt: 'login' });</code></pre>
                            </details>

                        </details>


                    - <details>
                        <summary>
                            <code>callback</code>: (function) [optional]
                        </summary>

                        - **Purpose**: Handles the result of the authentication process and provides feedback or further actions based on the outcome.

                        - **Parameters**:
                            1. <details>
                                <summary>
                                    <code>err</code>: (Error or <code>null</code>)
                                </summary>

                                - **Description**: Contains any error that occurred during the authentication process.
                                - **Type**: err | false
                                - **Example**: An error object if something went wrong, otherwise `null`.
                                </details>

                            2. <details>
                                <summary>
                                    <code>user</code>: (object | string | Array)
                                </summary>

                                - **Description**: The authenticated user object if authentication was successful, or `false` if no user was authenticated.
                                - **Type**: User | false | null
                                - **Example**: The user data retrieved from the database if authentication is successful.
                                </details>

                            3. <details>
                                <summary>
                                    <code>info</code>: (Object or <code>false</code>)
                                </summary>

                                - **Description**: Contains additional information or error messages about the authentication process. This can include details about why authentication failed.
                                - **Type**: object | string | Array
                                - **Example**: An object with a `message` property if authentication fails, or `false` if no additional information is available.
                                </details>

                            4. <details>
                                <summary>
                                    <code>status</code>: (number | Array)
                                </summary>

                                - **Description**: The HTTP status code representing the result of the authentication attempt.
                                - **Type**: number | Array (HTTP status code)
                                - **Example**: `401` for unauthorized access, `200` for successful authentication.
                                </details>
                        </details>




                - Examples:
                    ```js
                    //default strategy without optional parameters
                    app.post("/profile", (req, res, next) => {
                        passport.authenticate("jwt")(req, res, next)
                    });
                    ```
                    <details>
                        <summary>
                        more examples
                        </summary>

                        ```js
                        //custom strategy without optional parameters
                        app.post("/profile", (req, res, next) => {
                            passport.authenticate("my-jwt")(req, res, next)
                        });
                        ```
                        ```js
                        //default strategy with optional parameters
                        app.post("/profile", (req, res, next) => {
                            passport.authenticate("jwt", { session: false }, function(err, user, info, status) {
                                if (err) {
                                    return res
                                            .status(500)
                                            .json({ message: 'An error occurred', error: err });
                                }

                                if (!user) {
                                    return res
                                            .status(401)
                                            .json({ message: 'Unauthorized', info: info });
                                }

                                //in case of callback we need to set req.user=user
                                req.user=user

                                res.send(status).json(user.profile);
                            })(req, res, next)
                        });
                        ```
                        </details>
                </details>
            - <details>
                <summary>
                <code>passport.serializeUser()</code> from passport
                </summary>

                - We need passport.serializeUser() during the process of logIn which happens inside passport.authenticate()
                - <details>
                    <summary>Input parameter: <code>callback function</code>
                    </summary>

                    - <details><summary>input parameters of cb fn: <code>user</code>, <code>done</code></summary>

                        - `user`: The user object returned from the authentication process.
                        - <details><summary><code>done</code>: A callback function that you call after serializing the user, which takes two parameters: <code>err</code>, <code>id</code></summary>

                            - `err`: Any error that occurred during serialization.
                            - `id`: The user ID or any unique identifier that will be stored in the session.
                            ```js
                            passport.serializeUser((user, done)=>{
                                done(err, id)
                            });
                            ```
                            </details>

                        ```js
                        passport.serializeUser((user, done)=>{});
                        ```
                        </details>

                    ```js
                    passport.serializeUser(callback);
                    ```

                    </details>

                ```js
                // structure of serialiseUser
                passport.serializeUser((user, done) => {
                    done(null, user.id);
                });
                //err can be null or err
                //user can be false, user, user.id, or anything related to user
                ```
                </details>
            - <details>
                <summary>
                <code>session()</code> from express-session
                </summary>

                - session() is also necssary to logIn using passport.authenticate()
                - Parameter: `sessionOptions` (object)
                - So structure is `session(sessionOptions)
                - ```js
                    //structure of session
                    const express = require("express");
                    const session = require("express-session");

                    const app = express()

                    app.use(session({
                            secret: process.env.SESSION_SECRET,
                        resave: false,
                            saveUninitialized: false,
                    }))
                    ```

                - Session option keys:
                    <details>
                    <summary><strong>1. secret</strong></summary>
                    <ul>
                        <li><strong>Type:</strong> string | array</li>
                        <li><strong>Default:</strong> N/A</li>
                        <li><strong>Description:</strong> String(s) used to sign the session ID cookie.</li>
                        <li><strong>Example:</strong> <code>secret: 'mySecret'</code></li>
                    </ul>
                    </details>

                    <details>
                    <summary><strong>2. genid(req)</strong></summary>
                    <ul>
                        <li><strong>Type:</strong> function [(req: express.Request) => string]</li>
                        <li><strong>Default:</strong> Uses uid-safe library to generate a unique session ID.</li>
                        <li><strong>Description:</strong> Function to generate session IDs.</li>
                        <li><strong>Example:</strong> <code>genid: () => 'customID'</code></li>
                    </ul>
                    </details>

                    <details>
                    <summary><strong>3. name</strong></summary>
                    <ul>
                        <li><strong>Type:</strong> string </li>
                        <li><strong>Default:</strong> 'connect.sid'</li>
                        <li><strong>Description:</strong> Name of the session ID cookie.</li>
                        <li><strong>Example:</strong> <code>name: 'session_id'</code></li>
                    </ul>
                    </details>

                    <details>
                    <summary><strong>4. store</strong></summary>
                    <ul>
                        <li><strong>Type:</strong> Store </li>
                        <li><strong>Default:</strong> MemoryStore (in-memory session store)</li>
                        <li><strong>Description:</strong> Specifies session store instance.</li>
                        <li><strong>Example:</strong> <code>store: new RedisStore()</code></li>
                    </ul>
                    </details>

                    <details>
                    <summary><strong>5. cookie</strong></summary>
                    <ul>
                        <li><strong>Type:</strong> object </li>
                        <li><strong>Default:</strong> N/A</li>
                        <li><strong>Description:</strong> Options for the session cookie (e.g., maxAge, secure).</li>
                        <li><strong>CookieOptions:</strong>
                        <details>
                            <summary><strong>1. maxAge</strong></summary>
                            <ul>
                                <li><strong>Type:</strong> number </li>
                                <li><strong>Default:</strong> N/A</li>
                                <li><strong>Description:</strong> Specifies the maximum age of the cookie in milliseconds.</li>
                                <li><strong>Example:</strong> <code>maxAge: 3600000</code> (1 hour)</li>
                            </ul>
                            </details>

                    <details>
                        <summary><strong>2. partitioned</strong></summary>
                        <ul>
                            <li><strong>Type:</strong> boolean </li>
                            <li><strong>Default:</strong> false</li>
                            <li><strong>Description:</strong> Specifies the `Partitioned` attribute for the cookie. Not fully standardized yet.</li>
                            <li><strong>Example:</strong> <code>partitioned: true</code></li>
                        </ul>
                        </details>

                    <details>
                        <summary><strong>3. priority</strong></summary>
                        <ul>
                            <li><strong>Type:</strong> "low" | "medium" | "high" </li>
                            <li><strong>Default:</strong> "medium"</li>
                            <li><strong>Description:</strong> Specifies the `Priority` attribute of the cookie (low, medium, or high).</li>
                            <li><strong>Example:</strong> <code>priority: 'high'</code></li>
                        </ul>
                        </details>

                    <details>
                        <summary><strong>4. signed</strong></summary>
                        <ul>
                            <li><strong>Type:</strong> boolean </li>
                            <li><strong>Default:</strong> false</li>
                            <li><strong>Description:</strong> Specifies whether the cookie is signed with the secret.</li>
                            <li><strong>Example:</strong> <code>signed: true</code></li>
                        </ul>
                        </details>

                    <details>
                        <summary><strong>5. expires</strong></summary>
                        <ul>
                            <li><strong>Type:</strong> Date | null </li>
                            <li><strong>Default:</strong> No expiration set (non-persistent cookie).</li>
                            <li><strong>Description:</strong> Specifies the expiration date for the cookie.</li>
                            <li><strong>Example:</strong> <code>expires: new Date(Date.now() + 3600000)</code></li>
                        </ul>
                        </details>

                    <details>
                        <summary><strong>6. httpOnly</strong></summary>
                        <ul>
                            <li><strong>Type:</strong> boolean </li>
                            <li><strong>Default:</strong> true</li>
                            <li><strong>Description:</strong> Specifies whether the cookie is HTTP-only, preventing access from client-side JavaScript.</li>
                            <li><strong>Example:</strong> <code>httpOnly: false</code></li>
                        </ul>
                        </details>

                    <details>
                        <summary><strong>7. path</strong></summary>
                        <ul>
                            <li><strong>Type:</strong> string </li>
                            <li><strong>Default:</strong> '/'</li>
                            <li><strong>Description:</strong> Specifies the path for which the cookie is valid.</li>
                            <li><strong>Example:</strong> <code>path: '/admin'</code></li>
                        </ul>
                        </details>

                    <details>
                        <summary><strong>8. domain</strong></summary>
                        <ul>
                            <li><strong>Type:</strong> string </li>
                            <li><strong>Default:</strong> No domain set.</li>
                            <li><strong>Description:</strong> Specifies the domain for which the cookie is valid.</li>
                            <li><strong>Example:</strong> <code>domain: 'example.com'</code></li>
                        </ul>
                        </details>

                    <details>
                        <summary><strong>9. secure</strong></summary>
                        <ul>
                            <li><strong>Type:</strong> boolean | "auto" </li>
                            <li><strong>Default:</strong> false</li>
                            <li><strong>Description:</strong> Specifies whether the cookie is only sent over HTTPS.</li>
                            <li><strong>Example:</strong> <code>secure: true</code></li>
                        </ul>
                        </details>

                    <details>
                        <summary><strong>10. encode</strong></summary>
                        <ul>
                            <li><strong>Type:</strong> (val: string) => string </li>
                            <li><strong>Default:</strong> Default encoder for cookie values.</li>
                            <li><strong>Description:</strong> Specifies a custom encoding function for the cookie value.</li>
                            <li><strong>Example:</strong> <code>encode: encodeURIComponent</code></li>
                        </ul>
                        </details>

                    <details>
                        <summary><strong>11. sameSite</strong></summary>
                        <ul>
                            <li><strong>Type:</strong> boolean | "lax" | "strict" | "none" </li>
                            <li><strong>Default:</strong> false</li>
                            <li><strong>Description:</strong> Specifies the `SameSite` attribute for cross-site cookie control (strict, lax, or none).</li>
                            <li><strong>Example:</strong> <code>sameSite: 'strict'</code></li>
                        </ul>
                        </details>

                    </li>
                        <li><strong>Example:</strong> <code>cookie: { maxAge: 60000 }</code></li>
                    </ul>


                    </details>

                    <details>
                    <summary><strong>6. rolling</strong></summary>
                    <ul>
                        <li><strong>Type:</strong> boolean </li>
                        <li><strong>Default:</strong> false</li>
                        <li><strong>Description:</strong> Resets session expiration on every response.</li>
                        <li><strong>Example:</strong> <code>rolling: true</code></li>
                    </ul>
                    </details>

                    <details>
                    <summary><strong>7. resave</strong></summary>
                    <ul>
                        <li><strong>Type:</strong> boolean </li>
                        <li><strong>Default:</strong> true (deprecated)</li>
                        <li><strong>Description:</strong> Forces session to be saved on every request, even if unmodified.</li>
                        <li><strong>Example:</strong> <code>resave: false</code></li>
                    </ul>
                    </details>

                    <details>
                    <summary><strong>8. proxy</strong></summary>
                    <ul>
                        <li><strong>Type:</strong> boolean </li>
                        <li><strong>Default:</strong> undefined</li>
                        <li><strong>Description:</strong> Trust reverse proxy when setting secure cookies.</li>
                        <li><strong>Example:</strong> <code>proxy: true</code></li>
                    </ul>
                    </details>

                    <details>
                    <summary><strong>9. saveUninitialized</strong></summary>
                    <ul>
                        <li><strong>Type:</strong> boolean </li>
                        <li><strong>Default:</strong> true (deprecated)</li>
                        <li><strong>Description:</strong> Saves uninitialized sessions. Useful for login sessions.</li>
                        <li><strong>Example:</strong> <code>saveUninitialized: false</code></li>
                    </ul>
                    </details>

                    <details>
                    <summary><strong>10. unset</strong></summary>
                    <ul>
                        <li><strong>Type:</strong> "destroy" | "keep" </li>
                        <li><strong>Default:</strong> 'keep'</li>
                        <li><strong>Description:</strong> Controls behavior when session is deleted.</li>
                        <li><strong>Example:</strong> <code>unset: 'destroy'</code></li>
                    </ul>
                    </details>

                    </details>

        - Complete structure for authentication:
            ```js
            const express = require('express');
            const session = require("express-session");
            const passport = require("passport");

            const app = express()

            app.use(session({ //to be called on top
                secret: process.env.SESSION_SECRET,
            }))

            app.use((req, res, next)=>{ //can be called anywhere
                passport.authenticate('jwt')(req, res, next)
            })

            passport.serializeUser(()=>{

            })
            ```

## Sending jwt from client to server

1.  <details>
    <summary>
    Using Authorisation header (most common)
    </summary>

    - <details>
        <summary>
        Bearer Token: The most common and standard method for JWTs.
        </summary>

      ```js
      // Client-side (e.g., using Axios in JavaScript)
      axios.get("/protected-resource", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      // Server-side (Express with Passport)
      const opts = {
        jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(), // Extract JWT from Bearer Token
        secretOrKey: SECRET_KEY,
      };
      ```

        <details>

    - <details>
        <summary>
        Custom Scheme: Allows custom authentication schemes as needed.
        </summary>

      ```js
      // Client-side (e.g., using Axios in JavaScript)
      axios.get("/protected-resource", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      // Server-side (Express)
      const customSchemeExtractor = (req) => {
        const authHeader = req.headers["authorization"];
        if (authHeader && authHeader.startsWith("customScheme ")) {
          return authHeader.split(" ")[1];
        }
        return null;
      };

      const opts = {
        jwtFromRequest: customSchemeExtractor, // Use custom extractor
        secretOrKey: SECRET_KEY,
      };
      ```

        <details>

    - <details>
        <summary>
        Digest Authentication: Less common for JWTs, used in specific scenarios.
        </summary>

      ```js
      // Client-side (e.g., using Axios in JavaScript)
      axios.get("/protected-resource", {
        headers: {
          Authorization: `Digest ${token}`,
        },
      });

      // Server-side (Express)
      const digestExtractor = (req) => {
        const authHeader = req.headers["authorization"];
        if (authHeader && authHeader.startsWith("Digest ")) {
          return authHeader.split(" ")[1];
        }
        return null;
      };

      const opts = {
        jwtFromRequest: digestExtractor, // Use custom extractor
        secretOrKey: SECRET_KEY,
      };
      ```

        <details>

    - <details>
          <summary>
          Basic Authentication: Typically used for credentials, not recommended for JWTs.
          </summary>

          ```js
          // (Not Recommended for JWTs)
          // Client-side (e.g., using Axios in JavaScript)
          axios.get('/protected-resource', {
               headers: {
                  'Authorization': `Basic ${token}`
              }
          });

          // Server-side (Express)
          const basicExtractor = (req) => {
              const authHeader = req.headers['authorization'];
              if (authHeader && authHeader.startsWith('Basic ')) {
                  return authHeader.split(' ')[1];
              }
              return null;
          };

      const opts = {
      jwtFromRequest: basicExtractor, // Use custom extractor
      secretOrKey: SECRET_KEY,
      }
      ```
      <details>
      </details>

2.  <details>
    <summary>
    Using cookies
    </summary>

    - For client side: - We dont have to do anything. just run both server an dclient on same url (eg: http://localhost:3000), client using build file and server direclty running using node index. - when both run on same server: - cookies sent to client from sever will be stored as Set-Cookies in header and - server itself will read it back when any req is sent from client to server
      ```js
      //client side
      axios.get('/protected-resource')

          // server side
          const cookieParser = require('cookie-parser')
          const express = require('express');

          const app = express()
          app.use(cookieParser())

          //custom extractor
          var cookieExtractor = function (req) {
          var token = null;
          if (req && req.cookies) {
              token = req.cookies["jwt"];
          }
          return token;
          };

          const opts = {
              jwtFromRequest: cookieExtractor,
              secretOrKey: 'your_secret_key'
          };
          ```

      </details>

3.  <details>
    <summary>
    Using URL Query Parameters
    </summary>

    ```js
    // Client-side (e.g., using Axios)
    axios.get("/protected-resource?token=" + token);

    // Custom extractor function for query parameters
    const queryParamExtractor = (req) => {
      return req.query.token; // Extract JWT from query parameter 'token'
    };

    const opts = {
      jwtFromRequest: queryParamExtractor, // Use custom extractor
      secretOrKey: SECRET_KEY,
    };
    ```

    </details>

4.  <details>
    <summary>
    Using Custom Headers
    </summary>

    ```js
    // Client-side (e.g., using Axios)
    axios.get("/protected-resource", {
      headers: {
        "X-Custom-Header": token, // Replace 'X-Custom-Header' with your custom header name
      },
    });

    // Custom extractor function for custom headers
    const customHeaderExtractor = (req) => {
      return req.headers["x-custom-header"]; // Replace 'x-custom-header' with your custom header name
    };

    const opts = {
      jwtFromRequest: customHeaderExtractor, // Use custom extractor
      secretOrKey: SECRET_KEY,
    };
    ```

    </details>
