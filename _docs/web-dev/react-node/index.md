---
parent: Web Dev
layout: default
title: React-Node App
date: Aug 19, 2024
excerpt: Concepts related to React-Node Web App
permalink: react-node
---

# Concepts related to React-Node Web App

<br>

## Table of Contents

1. [Approx File Organisation Template for React-Node Web App](#1-approx-file-organisation-template-for-react-node-web-app)
2. [CI](#2-ci)
3. [How to Set Up CI](#3-how-to-set-up-ci)
4. [Why Do We Need CI](#4-why-do-we-need-ci)
5. [Writing JSDocs for backend and frontend](#5-JSDocs)


<br>

## Approx File Organisation Template for React-Node Web App
Organizing a project with both client-side and server-side code requires a structured approach to ensure maintainability, scalability, and clarity. Here’s a comprehensive folder structure for a project that includes client-side (React) and server-side (Node.js/Express) code, with folders for services, utilities, middlewares, and tests.

### Suggested Folder Structure

```plaintext
project-root/
│
├── client/                 # React frontend application
│   ├── public/              # Public assets
│   ├── src/                 # Source files
│   │   ├── assets/          # Images, fonts, etc.
│   │   ├── components/      # Reusable components
│   │   ├── pages/           # Page components or views
│   │   ├── services/        # API service functions
│   │   ├── utils/           # Utility functions
│   │   ├── hooks/           # Custom React hooks
│   │   ├── contexts/        # React context providers
│   │   ├── styles/          # Global styles and CSS modules
│   │   ├── App.js           # Main application component
│   │   ├── index.js         # Entry point for React app
│   │   └── ...              # Other frontend-specific files
│   ├── .env                 # Environment variables for frontend
│   ├── package.json         # Frontend dependencies and scripts
│   └── README.md            # Frontend documentation
│
├── server/                 # Node.js/Express backend application
│   ├── config/             # Configuration files (e.g., database, JWT)
│   ├── controllers/        # Route handlers
│   ├── middlewares/        # Express middlewares (e.g., authentication, logging)
│   ├── models/             # Database models
│   ├── routes/             # API route definitions
│   ├── services/           # Business logic and external service integration
│   ├── utils/              # Utility functions
│   ├── validators/         # Request validation schemas
│   ├── tests/              # Unit and integration tests
│   │   ├── unit/           # Unit tests
│   │   ├── integration/    # Integration tests
│   │   └── ...             # Other test types or configurations
│   ├── app.js              # Main application entry point
│   ├── server.js           # Server setup and initialization
│   ├── .env                # Environment variables for backend
│   ├── package.json        # Backend dependencies and scripts
│   └── README.md           # Backend documentation
│
├── .gitignore              # Git ignore file
├── docker-compose.yml      # Docker Compose configuration (if using Docker)
└── README.md               # Project overview and setup instructions
```

### Explanation

#### Client Folder (`client/`)
- **`public/`**: Contains static assets like `index.html`, favicon, and static images.
- **`src/`**:
  - **`assets/`**: For static files like images and fonts.
  - **`components/`**: Reusable UI components.
  - **`pages/`**: Components representing pages or views.
  - **`services/`**: Functions for making API calls and interacting with backend services.
  - **`utils/`**: Utility functions and helpers.
  - **`hooks/`**: Custom React hooks.
  - **`contexts/`**: React context providers for state management.
  - **`styles/`**: Global styles, CSS modules, and theme settings.
  - **`App.js`**: Main component that wraps the entire application.
  - **`index.js`**: Entry point for the React application.

#### Server Folder (`server/`)
- **`config/`**: Configuration files for database connections, environment variables, and other settings.
- **`controllers/`**: Functions that handle requests and responses.
- **`middlewares/`**: Custom Express middleware (e.g., for authentication or logging).
- **`models/`**: Database schemas and models.
- **`routes/`**: Definitions of API routes and their associated controllers.
- **`services/`**: Business logic and integrations with external services.
- **`utils/`**: Utility functions and helpers.
- **`validators/`**: Request validation schemas using libraries like Joi.
- **`tests/`**:
  - **`unit/`**: Unit tests for individual components or functions.
  - **`integration/`**: Integration tests that involve multiple components or services.
- **`app.js`**: Main application logic.
- **`server.js`**: Server initialization and startup script.

### Additional Considerations

- **Testing**: You might also include separate folders for different types of tests (unit, integration) and potentially mock data if required.
- **Docker**: If using Docker, you can include a `docker-compose.yml` file for defining multi-container applications.
- **Documentation**: Each section should include its own `README.md` for specific instructions and details.

This structure will help maintain a clean separation between client-side and server-side code, making it easier to manage and scale your application.

<br>

## 2. CI
Continuous Integration (CI) is a development practice where code changes are automatically tested and integrated into the shared repository multiple times a day. This practice helps in maintaining the quality and consistency of the codebase throughout the development process. Here’s a breakdown of CI:

### Key Aspects of Continuous Integration (CI)

1. **Frequent Integration**:
   - Developers regularly merge their code changes into a shared repository, often multiple times a day.
   - This frequent integration helps in identifying issues early, reducing integration problems.

2. **Automated Testing**:
   - Every code change triggers automated tests to verify that the new code does not break existing functionality.
   - Tests can include unit tests, integration tests, and end-to-end tests.

3. **Automated Builds**:
   - CI systems automatically build the application with every code change.
   - This ensures that the application compiles and runs correctly in an automated environment.

4. **Immediate Feedback**:
   - Developers receive immediate feedback about the health of the application after integrating their changes.
   - CI tools provide reports on test results, build status, and potential issues.

5. **Version Control Integration**:
   - CI systems are integrated with version control systems (e.g., Git) to monitor code changes and trigger automated processes.

6. **Consistency**:
   - CI helps maintain a consistent codebase by ensuring that all code changes are tested and built in the same environment.

### Benefits of Continuous Integration

- **Early Detection of Issues**: Bugs and integration problems are identified and fixed early in the development process.
- **Improved Code Quality**: Regular testing and integration ensure that code quality remains high.
- **Faster Development Cycle**: Automated processes streamline the development cycle, leading to faster releases.
- **Enhanced Collaboration**: Regular integration helps developers stay aligned and reduces conflicts between code changes.

### Popular CI Tools

- **Jenkins**: An open-source automation server that supports building, deploying, and automating any project.
- **Travis CI**: A cloud-based CI service that integrates with GitHub and automates testing and deployment.
- **CircleCI**: A cloud-based CI/CD platform that automates the build, test, and deployment processes.
- **GitHub Actions**: Integrated into GitHub, it allows automation of workflows directly within the repository.
- **GitLab CI**: Part of GitLab, providing integrated CI/CD pipelines within the GitLab ecosystem.

### Example Workflow

1. **Code Commit**: A developer commits code changes to the version control system.
2. **CI Trigger**: The CI system detects the commit and triggers an automated build and test process.
3. **Build and Test**: The CI system builds the application and runs tests to verify the code changes.
4. **Feedback**: The CI system provides feedback on the build and test results, highlighting any issues.
5. **Integration**: If the tests pass, the code changes are integrated into the main codebase. If issues are found, the developer is notified to address them.

By incorporating CI into your development process, you can enhance the quality, reliability, and efficiency of your software projects.

<br>

## 3. How to setup CI
Setting up Continuous Integration (CI) involves configuring a CI tool to automatically build, test, and sometimes deploy your application whenever changes are made to the codebase. Here’s a general guide on how to set up CI using a popular CI tool, such as GitHub Actions, Jenkins, Travis CI, or CircleCI:

### 1. **Choose a CI Tool**

Choose a CI tool that best fits your needs. Popular options include:

- **GitHub Actions**: Integrated into GitHub repositories.
- **Jenkins**: An open-source automation server.
- **Travis CI**: Cloud-based and integrates well with GitHub.
- **CircleCI**: Cloud-based with extensive integration capabilities.

### 2. **Set Up Your CI Tool**

#### **GitHub Actions**

1. **Create a Workflow File**:
   - In your GitHub repository, create a directory named `.github/workflows/`.
   - Inside this directory, create a YAML file (e.g., `ci.yml`) for defining your CI workflow.

2. **Define the Workflow**:
   - Here’s an example of a basic GitHub Actions workflow for a Node.js application:

   ```yaml
   name: CI

   on:
     push:
       branches:
         - main
     pull_request:
       branches:
         - main

   jobs:
     build:
       runs-on: ubuntu-latest

       steps:
         - name: Checkout code
           uses: actions/checkout@v2

         - name: Set up Node.js
           uses: actions/setup-node@v2
           with:
             node-version: '14'

         - name: Install dependencies
           run: npm install

         - name: Run tests
           run: npm test
   ```

3. **Push Changes**:
   - Commit and push the workflow file to your repository. GitHub Actions will automatically pick it up and run the defined tasks.

#### **Jenkins**

1. **Install Jenkins**:
   - Follow the instructions on the [Jenkins website](https://www.jenkins.io/download/) to install Jenkins on your server or use a Jenkins cloud service.

2. **Create a New Job**:
   - Open Jenkins and click on “New Item.”
   - Choose “Freestyle project” or “Pipeline” depending on your needs.

3. **Configure the Job**:
   - **Source Code Management**: Configure your repository URL and credentials.
   - **Build Triggers**: Set up triggers like “GitHub hook trigger for GITScm polling” for automatic builds.
   - **Build Steps**: Add build steps to execute commands (e.g., shell commands for testing).

4. **Add Post-Build Actions**:
   - Configure actions like archiving test results or deploying artifacts.

5. **Save and Build**:
   - Save the configuration and start a build. Jenkins will execute the configured steps and provide feedback.

#### **Travis CI**

1. **Create a `.travis.yml` File**:
   - In the root of your repository, create a `.travis.yml` file.

2. **Define the Build Process**:
   - Here’s an example configuration for a Node.js application:

   ```yaml
   language: node_js
   node_js:
     - "14"

   script:
     - npm install
     - npm test
   ```

3. **Enable Travis CI**:
   - Sign in to Travis CI with your GitHub account and enable the repository.

4. **Push Changes**:
   - Commit and push the `.travis.yml` file to your repository. Travis CI will automatically start the build process.

#### **CircleCI**

1. **Create a `.circleci/config.yml` File**:
   - In the root of your repository, create a `.circleci/config.yml` file.

2. **Define the Configuration**:
   - Here’s an example configuration for a Node.js application:

   ```yaml
   version: 2.1

   jobs:
     build:
       docker:
         - image: circleci/node:14
       steps:
         - checkout
         - run:
             name: Install dependencies
             command: npm install
         - run:
             name: Run tests
             command: npm test

   workflows:
     version: 2
     build:
       jobs:
         - build
   ```

3. **Sign Up and Configure**:
   - Sign up for CircleCI and link your repository.

4. **Push Changes**:
   - Commit and push the configuration file to your repository. CircleCI will automatically start the build process.

### 3. **Monitor and Maintain**

- **Review Build Status**: Monitor the CI dashboard for build results and issues.
- **Update Configuration**: Adjust your CI configuration as needed for new dependencies, test cases, or deployment steps.
- **Fix Failures**: Address any build or test failures promptly to maintain code quality.

By following these steps, you can set up a CI pipeline that will automate the testing and integration process, improving the reliability and efficiency of your development workflow.

<br>

## 4. Why do we need CI
Continuous Integration (CI) is essential for several reasons, particularly in modern software development practices. Here’s why CI is important:

### 1. **Early Detection of Issues**

- **Frequent Testing**: CI automates the process of testing code changes as soon as they are committed, which helps in catching issues early. This reduces the likelihood of bugs accumulating over time and being discovered late in the development cycle.

### 2. **Improved Code Quality**

- **Consistent Testing**: Regular and automated testing ensures that new code does not break existing functionality, leading to a more stable and reliable codebase.
- **Code Review**: CI systems often include linting and formatting checks, ensuring code quality and consistency.

### 3. **Faster Development Cycle**

- **Automated Builds and Tests**: CI automates the build and test processes, which speeds up development and allows developers to focus on writing code rather than manually managing builds and tests.
- **Quick Feedback**: Immediate feedback on code changes helps developers address issues faster and iterate more quickly.

### 4. **Reduced Integration Problems**

- **Frequent Integration**: By integrating code changes multiple times a day, CI reduces the risk of integration problems that often arise when integrating large changes at the end of a development cycle.

### 5. **Increased Confidence in Code**

- **Automated Testing**: CI ensures that code changes are tested against a set of predefined tests, which increases confidence that the code is functioning as expected.
- **Consistent Environment**: CI pipelines often run in consistent environments, reducing the risk of environment-specific issues.

### 6. **Enhanced Collaboration**

- **Team Alignment**: CI encourages frequent integration of code changes, keeping all team members aligned and reducing the likelihood of conflicts between different developers’ code.
- **Transparency**: CI systems provide visibility into the build and test processes, making it easier for teams to collaborate and understand the current state of the project.

### 7. **Efficient Deployment**

- **Automated Deployment**: Many CI systems include Continuous Deployment (CD) capabilities, automating the deployment of code changes to staging or production environments. This streamlines the release process and reduces manual intervention.

### 8. **Documentation and Metrics**

- **Build History**: CI systems maintain a history of builds and test results, which helps in tracking the progress and identifying trends or recurring issues.
- **Test Reports**: CI provides detailed reports on test results, code coverage, and other metrics, aiding in maintaining and improving code quality.

### 9. **Scalability**

- **Handling Multiple Changes**: CI systems can handle changes from multiple developers simultaneously, ensuring that all code changes are integrated and tested efficiently.
- **Scaling Teams**: As teams grow, CI helps manage the complexity of integrating and testing code from multiple contributors.

In summary, CI enhances the development process by ensuring that code changes are continuously tested and integrated, leading to higher quality software, faster development cycles, and better collaboration among team members.

<br>

## Where do we place CI in code
In a typical project folder structure, CI-related files and configurations are usually placed in specific directories to keep them organized and easily accessible. Here's where you might place CI-related files in your folder organization:

### Project Folder Structure with CI

```
/project-root
├── /src
│   ├── /client       # Client-side code (React, etc.)
│   └── /server       # Server-side code (Node.js, Express, etc.)
│
├── /config           # Configuration files
│   ├── /ci           # CI-related configurations
│   │   ├── github-actions.yml  # GitHub Actions workflow file
│   │   ├── travis.yml          # Travis CI configuration file
│   │   └── circleci.yml         # CircleCI configuration file
│   ├── /database    # Database configuration
│   └── /server      # Server configuration
│
├── /scripts         # Helper scripts
│   ├── build.sh     # Build scripts
│   └── deploy.sh    # Deployment scripts
│
├── /tests           # Test files and configurations
│   ├── /unit        # Unit tests
│   ├── /integration # Integration tests
│   └── /e2e         # End-to-end tests
│
├── /public          # Public assets (e.g., images, static files)
├── /docs            # Documentation
│   └── README.md    # Project documentation
│
├── .gitignore       # Git ignore file
├── package.json     # Node.js package configuration
├── .eslintrc.json   # ESLint configuration
└── .prettierrc      # Prettier configuration
```

### Detailed Explanation

- **`/config/ci`**: This directory contains CI-related configuration files for different CI tools like GitHub Actions, Travis CI, CircleCI, etc. It's a central place to keep all CI configurations.

  - **`github-actions.yml`**: For GitHub Actions workflows.
  - **`travis.yml`**: For Travis CI configurations.
  - **`circleci.yml`**: For CircleCI configurations.

- **`/scripts`**: Contains helper scripts for various tasks such as building and deploying the application. Although not directly related to CI, these scripts are often used in CI pipelines.

- **`/tests`**: Includes all test files and configurations. This is where you would place your unit tests, integration tests, and end-to-end tests that CI will execute.

### Placing CI Files

- **GitHub Actions**: Create `.github/workflows/` in the root of your project. Files within this directory define the workflows and jobs for GitHub Actions.

- **Travis CI**: Place the `.travis.yml` file in the root directory of your project.

- **CircleCI**: Place the `config.yml` file in the `.circleci/` directory in the root of your project.

By organizing your project with a dedicated folder for CI configurations and placing other related files in appropriate directories, you ensure that your project remains organized and maintainable. This setup makes it easier to manage and update CI configurations as needed.


## 5. JSDocs
When creating JSDoc comments for functions, it's useful to follow a consistent blueprint to ensure that the documentation is clear, comprehensive, and helpful. Here’s a general blueprint you can follow:

### Blueprint for JSDoc Comments

1. **Function Description**:
   - Provide a concise description of what the function does. Explain the purpose and functionality.

2. **Function Name**:
   - Use the `@function` tag to specify the function name.

3. **Parameters**:
   - Use the `@param` tag to describe each parameter:
     - **Type**: The type of the parameter (e.g., `Object`, `string`, `number`).
     - **Name**: The name of the parameter.
     - **Description**: A description of what the parameter represents and any constraints or details.

4. **Returns**:
   - Use the `@returns` or `@return` tag to describe what the function returns:
     - **Type**: The type of the return value (e.g., `Promise<void>`, `Object`).
     - **Description**: A description of the return value and what it represents.

5. **Errors**:
   - Use the `@throws` tag to describe any errors or exceptions that the function might throw, including:
     - **Type of Error**: The type or name of the error (e.g., `ApiError`).
     - **Description**: Conditions under which the error is thrown.

6. **Example** (Optional):
   - Provide an example of how the function can be used if it adds value.

### Example JSDoc Comments

Here’s how you might use this blueprint to create JSDoc comments for your functions:

```js
const { Product } = require('../model/Product.js');
const catchAsync = require("../utils/catchAsync.util.js");
const status = require('http-status');
const ApiError = require('../utils/ApiError.util.js');

/**
 * Creates a new product.
 * 
 * @function
 * @name createProduct
 * @memberof module:controllers/productController
 * @param {Object} req - Express request object.
 * @param {Object} req.body - The product data to be created.
 * @param {Object} res - Express response object.
 * @returns {Promise<void>} Responds with the created product and status code 201 (Created).
 * @throws {Error} Forwards any errors to the error-handling middleware.
 */
exports.createProduct = catchAsync(async (req, res) => {
    const product = new Product(req.body);
    const data = await product.save();
    res.status(status.CREATED).json(data);
});

/**
 * Fetches products based on query parameters for filtering, sorting, and pagination.
 * 
 * @function
 * @name fetchAllQuery
 * @memberof module:controllers/productController
 * @param {Object} req - Express request object.
 * @param {Object} req.query - Query parameters for filtering and sorting:
 *   - `role` (optional): Role-based filtering (e.g., 'user' or 'admin').
 *   - `_sort` (optional): Field to sort by.
 *   - `_order` (optional): Sort order, 'asc' or 'desc'.
 *   - `category` (optional): Filter by category.
 *   - `brand` (optional): Filter by brand.
 *   - `_page` (optional): Page number for pagination.
 * @param {Object} res - Express response object.
 * @returns {Promise<void>} Responds with the filtered, sorted, and paginated list of products and status code 200 (OK).
 * @throws {Error} Forwards any errors to the error-handling middleware.
 */
exports.fetchAllQuery = catchAsync(async (req, res) => {
    let productQuery = null;

    // Filtering and sorting logic
    if (req.query.role === 'user') {
        productQuery = Product.find({ deleted: { $ne: true } });
    } else if (req.query.role === 'admin') {
        productQuery = Product.find();
    }

    if (req.query._sort && req.query._order) {
        productQuery = productQuery.sort({ [req.query._sort]: req.query._order });
    }
    if (req.query.category) {
        const categories = req.query.category.includes(',') ? req.query.category.split(',') : req.query.category;
        productQuery = productQuery.find({ category: { $in: categories } });
    }
    if (req.query.brand) {
        const brands = req.query.brand.includes(',') ? req.query.brand.split(',') : req.query.brand;
        productQuery = productQuery.find({ brand: { $in: brands } });
    }
    if (req.query._page) {
        const pageSize = 10;
        const page = req.query._page;
        productQuery = productQuery.skip(pageSize * (page - 1)).limit(pageSize);
    }

    const data = await productQuery.exec();
    res.status(status.OK).json(data);
});

/**
 * Fetches a product by its ID.
 * 
 * @function
 * @name fetchProductsById
 * @memberof module:controllers/productController
 * @param {Object} req - Express request object.
 * @param {Object} req.params - URL parameters including the `id` of the product.
 * @param {Object} res - Express response object.
 * @returns {Promise<void>} Responds with the product data and status code 200 (OK).
 * @throws {ApiError} Throws a 404 (Not Found) error if the product is not found.
 * @throws {Error} Forwards any other errors to the error-handling middleware.
 */
exports.fetchProductsById = catchAsync(async (req, res) => {
    const { id } = req.params;
    const data = await Product.findById(id);
    if (!data) {
        throw new ApiError(status.NOT_FOUND, "Product not found");
    }
    res.status(status.OK).json(data);
});

/**
 * Updates a product by its ID with the data provided in the request body.
 * 
 * @function
 * @name updateProduct
 * @memberof module:controllers/productController
 * @param {Object} req - Express request object.
 * @param {Object} req.params - URL parameters including the `id` of the product to update.
 * @param {Object} req.body - The updated product data.
 * @param {Object} res - Express response object.
 * @returns {Promise<void>} Responds with the updated product data and status code 200 (OK).
 * @throws {ApiError} Throws a 404 (Not Found) error if the product is not found.
 * @throws {Error} Forwards any other errors to the error-handling middleware.
 */
exports.updateProduct = catchAsync(async (req, res) => {
    const { id } = req.params;
    const data = await Product.findByIdAndUpdate(id, req.body, { new: true });
    if (!data) {
        throw new ApiError(status.NOT_FOUND, "Product not found");
    }
    res.status(status.OK).json(data);
});
```

### Summary of the Blueprint:

- **Function Description**: Provide a brief overview of what the function does.
- **Function Name**: Use `@function` and `@name` tags to specify the function's name and its purpose.
- **Parameters**: Use `@param` tags to document each parameter's type, name, and description.
- **Returns**: Use `@returns` or `@return` to describe what the function returns.
- **Errors**: Use `@throws` to document any errors that the function may throw and under what conditions.

This blueprint ensures that your JSDoc comments are thorough and consistent, making your code easier to understand and maintain.
