---
parent: Web Dev
layout: default
date: Oct 31, 2024
title: API Documentation Tools
excerpt: Following are the api documentation tools that helps you create api docs in pretty websites.
permalink: api-documentaion
---

## Api Documentaion Tools

Following are the api documentation tools that helps you create api docs in pretty websites.

### 🔨Tools that can be used (Tried so far):

1. Redocs : Free and Good UI
2. Swagger: Free but little confusing UI
3. Postman: Free but bland UI

- #### Common Docs
  - ##### Redoc and Swagger
    - swagger(openapi) specification docs: [https://swagger.io/specification/](https://swagger.io/specification/)
    - example swagger(openapi) yaml code: https://github.com/Redocly/redoc/blob/main/demo/openapi-3-1.yaml
    - example swagger(openapi) json code: https://github.com/Redocly/redoc/blob/main/demo/big-openapi.json
    - exmaple website github: https://github.com/Redocly/redoc/blob/main/demo/museum.yaml
    - example website: https://redocly.github.io/redoc/
    - my own repo: https://github.com/Anusree6154s/qkart-backend-2
  - ##### Postman
    - example api doc: https://www.postman.com/lunar-module-geoscientist-23775876/xflix-backend-api/collection/6wogu2r/xflix?action=share&creator=33572999
    - above example is intuitive. follow it for other postman docs
- #### How to create documentaion right from the server
  - ##### Redoc

    <details>
      <summary>
        <strong>Using CDN</strong>
      </summary>
    - In app.js
      ```js
      const express = require("express");
      const app = express();
      const PORT=8082 // put your port here
      app.use((req, res, next) => {
          // Set Content Security Policy for running redocly via cdn
          res.header("Content-Security-Policy", " script-src-elem 'self' https://cdn.redoc.ly;");
          next();
      app.get('/swagger.json', (req, res) => {
          // will be called when spec-url='/swagger.json' executes in docs.html
          res.sendFile(path.join(__dirname, '/documentation/swagger.json'));
      });
      app.use('/docs', (req, res) => {
          // will be called when this route will be accessed (http://localhost:PORT/docs)
          res.sendFile(path.join(__dirname, 'html-docs.html'));
      });
      app.listen(PORT)
      ```

      - Make a file named swagger.js or openapi.js. In that file create a yaml or json content by referring to these docs:
      - https://swagger.io/specification/
      - https://github.com/Redocly/redoc/blob/main/demo/openapi-3-1.yaml
      - https://github.com/Redocly/redoc/blob/main/demo/big-openapi.json
      - Create a docs.html and copy the code below:
      ```html
      <!DOCTYPE html>
      <html>
        <head>
          <title>API Documentation</title>
        </head>
        <body>
          <redoc spec-url="/swagger.json" suppress-warnings></redoc>
          <script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"></script>
        </body>
      </html>
      ```

      - Run `node app.js` in terminal. Api documentation will be live on url `http://localhost:8082/docs`

    </details>
       <details>
      <summary>
        <strong>Using NPM package</strong>
      </summary>
    - create swagger.js or openapi.js using above mentioned files
    - In app.js
      ```js
      const express = require("express");
      const app = express();
      const PORT = 8082;
      app.use("/docs", (req, res) => {
        // will be called when this route will be accessed (http://localhost:PORT/docs)
        res.sendFile(path.join(__dirname, "docs.html"));
      });
      app.listen(PORT);
      ```
    - in terminal run `npx @redocly/cli build-docs swagger.json --output docs.html` , then `node app.js`.
    - Api documentation will be live on url `http://localhost:8082/docs`

    </details>

- ##### Swagger
  - ###### using npm package
    - in app.js
      ```js
      const express = require("express");
      const app = express();
      const PORT = 8082; // put your port here
      app.get("/swagger.json", (req, res) => {
        // will be called when spec-url='/swagger.json' executes in docs.html
        res.sendFile(path.join(__dirname, "/documentation/swagger.json"));
      });
      app.use("/docs", (req, res) => {
        // will be called when this route will be accessed (http://localhost:PORT/docs)
        res.sendFile(path.join(__dirname, "html-docs.html"));
      });
      app.listen(PORT);
      ```
    - in swagger.json or openapi.json, write content referring to previous docs
    - Api documentation will be live on url `http://localhost:8082/docs`
  - ###### using cdn: dont know yet

> [!NOTE] > **Tips while using redocly**<br>
>
> 1. **authorization error**: add that url into res.header in app.js<br>
> 2. **error adding logo**: add logo to your own repo, create a route for it, place that routed url in img src<br>
>    refer my own docs for eg: https://github.com/Anusree6154s/qkart-backend-2<br>

---

### 📃 Total list of tools from gpt

#### 1. **Postman**

- **Overview**: Postman is widely used for API development and testing, but it also provides features to generate and host API documentation.
- **Key Features**:
  - Auto-generate documentation from collections.
  - Easy collaboration and sharing of documentation with team members.
  - Can publish documentation online or integrate with CI/CD pipelines.
- **Documentation Example**: Postman allows you to document your API requests, responses, and workflows directly within your collections. You can then share the documentation via a public or private URL.
- **Website**: [Postman API Docs](https://learning.postman.com/docs/publishing-your-api/documenting-your-api/)

#### 2. **Redoc**

- **Overview**: Redoc is an open-source tool that renders OpenAPI (Swagger) specifications as rich and customizable HTML documentation.
- **Key Features**:
  - Provides a clean and intuitive UI for API docs.
  - Easy to integrate into existing applications.
  - Supports OpenAPI 2.0 and 3.0.
  - The appearance of the docs can be customized to fit your branding.
- **Use Case**: Often used as a standalone documentation renderer for OpenAPI specs.
- **Website**: [Redoc](https://github.com/Redocly/redoc)

#### 3. **Slate**

- **Overview**: Slate is an open-source tool for generating beautiful, static API documentation.
- **Key Features**:
  - Features three-pane design (navigation, request, and response sections).
  - Static site generator — docs are hosted as simple static HTML.
  - Markdown-based, so easy to write and maintain documentation.
  - Good for read-only API docs.
- **Use Case**: Good for organizations that want static, easy-to-read documentation, and don't need interactive API testing directly in the docs.
- **Website**: [Slate](https://github.com/slatedocs/slate)

#### 4. **Apiary**

- **Overview**: Apiary, now part of Oracle, is a platform for designing, documenting, and testing APIs.
- **Key Features**:
  - Supports API Blueprint (a markdown-like language for describing APIs) and OpenAPI.
  - Provides mock servers, documentation generation, and testing capabilities.
  - Collaborative design features, letting teams work on API specs together.
  - Hosted, so no need for infrastructure setup.
- **Use Case**: Useful for teams who want an all-in-one solution for API design, mockups, and documentation.
- **Website**: [Apiary](https://apiary.io/)

#### 5. **RapiDoc**

- **Overview**: RapiDoc is another OpenAPI renderer, like Redoc, that generates interactive and beautiful API documentation.
- **Key Features**:
  - Fast and simple, optimized for performance.
  - Allows real-time API request testing directly from the documentation.
  - Fully customizable to match the branding of your application.
- **Use Case**: Great for users looking to customize their API documentation with real-time testing capabilities.
- **Website**: [RapiDoc](https://mrin9.github.io/RapiDoc/)

#### 6. **Docusaurus with API Docs Plugin**

- **Overview**: Docusaurus is a static site generator designed for documentation websites. Using plugins, it can also support API documentation.
- **Key Features**:
  - React-based static site generator.
  - Easily extendable with plugins to handle API documentation.
  - Flexible and customizable documentation sites, supporting markdown and custom layouts.
- **Use Case**: Great for companies or projects that need a full documentation website with an API section.
- **Website**: [Docusaurus](https://docusaurus.io/)

#### 7. **Docz**

- **Overview**: Docz is a documentation tool for building beautiful and interactive API docs using MDX (a mix of Markdown and JSX).
- **Key Features**:
  - Highly customizable and developer-friendly.
  - Interactive components (since it supports JSX).
  - Great for documenting components and APIs in React-based projects.
- **Use Case**: Ideal for projects that need interactive documentation, especially in the context of React or component-based libraries.
- **Website**: [Docz](https://www.docz.site/)

#### 8. **Sphinx**

- **Overview**: Sphinx is a Python documentation generator, but it can be extended to document APIs using plugins such as `sphinxcontrib-httpdomain`.
- **Key Features**:
  - Markdown and reStructuredText support.
  - Highly customizable via extensions.
  - Many plugins are available, including ones for API documentation.
- **Use Case**: Often used for documenting Python projects but can be extended to other languages or APIs.
- **Website**: [Sphinx](https://www.sphinx-doc.org/)

#### 9. **ReDocly**

- **Overview**: ReDocly (built on top of Redoc) is a premium solution for API documentation, offering extra features like linting, versioning, and monetization.
- **Key Features**:
  - API documentation hosting with version control.
  - Linter for OpenAPI specifications.
  - Full-text search across API docs.
- **Use Case**: Enterprise-level documentation solution for teams looking for a more comprehensive suite than Redoc.
- **Website**: [ReDocly](https://redocly.com/)

#### 10. **Spectacle**

- **Overview**: Spectacle is an API documentation tool built on top of OpenAPI.
- **Key Features**:
  - Simple and easy to set up.
  - Provides good visualization for OpenAPI documentation.
  - Can be used as a standalone documentation tool or embedded into a project.
- **Use Case**: Good for teams using OpenAPI and looking for an alternative to Swagger UI.
- **Website**: [Spectacle](https://sourcey.com/spectacle/)

#### 11. **Restlet Studio**

- **Overview**: A full-featured API development platform, Restlet Studio offers API design, testing, and documentation.
- **Key Features**:
  - API designer and documentation generator.
  - Automatically generates interactive docs.
  - Supports OpenAPI and RAML.
- **Use Case**: Useful for teams looking for a visual interface to manage API design and documentation.
- **Website**: [Restlet Studio](https://restlet.studio/)
