---
layout: default
layout: post                 
title: Takehome Guidelines     
date: Oct 23, 2024         
excerpt: Take home coding challenge template and guide
permalink: takehome-guidelines
---

Take home coding challenge
==========================

Readme
------

Write your README as if it was for a production service. Include the following items:

* Description of the problem and solution.
* Whether the solution focuses on back-end, front-end or if it's full stack.
* Reasoning behind your technical choices, including architectural. 
* Trade-offs you might have made, anything you left out, or what you might do differently if you were to spend additional time on the project.

How we review 
-------------

Your application will be reviewed by at least two of our engineers. We do take into consideration your experience level.

**We value quality over feature-completeness**. It is fine to leave things aside provided you call them out in your project's README. The goal of this code sample is to help us identify what you consider production-ready code. You should consider this code ready for final review with your colleague, i.e. this would be the last step before deploying to production.

The aspects of your code we will assess include:

* **Architecture**: how clean is the separation between the front-end and the back-end?
* **Clarity**: does the README clearly and concisely explains the problem and solution? Are technical tradeoffs explained?
* **Correctness**: does the application do what was asked? If there is anything missing, does the README explain why it is missing?
* **Code quality**: is the code simple, easy to understand, and maintainable?  Are there any code smells or other red flags? Does object-oriented code follows principles such as the single responsibility principle? Is the coding style consistent with the language's guidelines? Is it consistent throughout the codebase?
* **Security**: are there any obvious vulnerability?
* **Technical choices**: do choices of libraries, databases, architecture etc. seem appropriate for the chosen application?


Bonus point (those items are optional):

* **UX**: is the web interface understandable and pleasing to use? Is the API intuitive?
* **Scalability**: will technical choices scale well? If not, is there a discussion of those choices in the README? 
* **Production-readiness**: does the code include monitoring? logging? proper error handling?

## My personal notes on this
### Format
- Project Name
  - Description
     - Problem Description
     - Solution Description (backend, frontend, or full-stack) 
  - Approach
    - Technology Stack (and reasons for choosing them)
    - Architecture
    - Features Implemented
  - Trade-offs & Improvements
  - Future Improvements
  - How to run
  - Demo image/gif/video
 
### Format in detail
- **Project Name**
  - **Description**
    - **Problem Description**: This project solves [problem description] by addressing [specific pain points], such as improving [performance, scalability, user experience, etc.].
    - **Solution Description**: This is a [backend, frontend, or full-stack] solution using [technology stack] to tackle the identified problem.
  - **Approach**
    - **Technology Stack** (and Reasons for Choosing Them)
      - **Front-end**: [React, Vue, etc.] - Chosen for its scalability and reusable components.
      - **Back-end**: [Node.js, Python, etc.] - Selected for its asynchronous processing capabilities.
      - **Database**: [PostgreSQL, MongoDB, etc.] - Picked for [structured/unstructured] data handling.
      - **Tools**: [Docker, CI/CD tools, etc.] - Used for deployment and containerization to ensure consistency across environments.
    - **Architecture**
      - The solution uses a [RESTful/Microservice] architecture with:
        - **API Layer**: Routes requests to services.
        - **Business Logic**: Processes core operations like authentication, payments, etc.
        - **Database Layer**: Manages data storage and retrieval.
    - **Features Implemented**
      - **User Authentication**: Secure sign-up, login, and session management.
      - **Product Listings**: Display dynamic product data from the database.
      - **Shopping Cart**: Add, remove, and view items in a cart with real-time updates.
      - **Checkout Process**: Integration with payment gateways to complete purchases.
  - **Trade-offs & Improvements**
    - **Performance vs. Flexibility**: Opted for flexibility at the expense of some performance optimization.
    - **Initial Simplicity**: Chose lightweight frameworks to facilitate rapid development, leaving room for future improvements.
    - **Testing**: Focused testing on core logic, with plans to implement more extensive end-to-end tests.
  - **Future Improvements**
    - Expand test coverage to include UI and integration testing.
    - Transition to microservices for improved scalability and fault isolation.
    - Improve CI/CD pipeline with better monitoring and automation tools.
  - **How to Run**
    - Clone the repo: 
      ```js
      git clone https://github.com/yourusername/project.git
      ```
    - Install dependencies:
      ```js
      npm install
      ```
    - Run the server:
      ```js
      npm run dev
      ```
  - **Demo Image/GIF/Video**
    - image

### Example
#### Long version
- # eCommerce Frontend
  - ## Description
    - **Problem Description**: Many online stores lack modern, responsive, and performant user interfaces. This eCommerce application frontend aims to provide users with a seamless and intuitive shopping experience across devices.
    - **Solution Description**: This is a **frontend solution** built using **React** to create a dynamic and responsive user interface. The app improves **user experience**, enhances **performance**, and ensures **scalability** for future feature extensions.
  - ## Approach
      - ### Technology Stack (and Reasons for Choosing Them)
        - **Front-end**: **React** – Chosen for its component-based architecture and excellent support for dynamic, state-driven UIs. React also allows easy integration of third-party libraries for UI elements.
        - **State Management**: **Redux** – Used to manage global state across the application, such as the user's shopping cart, to ensure consistency and performance.
        - **Styling**: **Tailwind CSS** – A utility-first CSS framework that speeds up development while maintaining design consistency.
        - **Routing**: **React Router** – Implemented for navigation between pages, enabling smooth transitions between product listings, cart, and checkout pages.
        - **Tools**: **Webpack & Babel** – Used for bundling and transpiling the JavaScript code for optimized performance in production.
    - ### Architecture
      - The frontend follows a **component-based architecture** where each page and UI element is encapsulated into reusable React components:
      - **Product Listing Page**: Dynamically fetches product data and displays it in a grid layout with filters and sorting options.
      - **Product Detail Page**: Provides detailed information about a selected product, including images, descriptions, and reviews.
      - **Shopping Cart**: Displays the selected items, allowing users to modify quantities or remove items in real-time using state management (Redux).
      - **Checkout Page**: Guides users through the purchase process, integrating payment gateway UI elements.
    - ### Features Implemented
      - **Product Browsing**: Displays a catalog of products with filtering (by category, price) and sorting (by popularity, price).
      - **Product Search**: A search bar allows users to quickly find specific products.
      - **Shopping Cart**: Users can add items to their cart, update quantities, and view a live total of the purchase.
      - **Responsive Design**: The layout adapts seamlessly across desktop, tablet, and mobile devices.
      - **User Authentication**: Integrated login/logout functionality, with access to personalized features like saved shopping carts.
  - ## Trade-offs & Improvements
    - **Performance vs. Features**: Initial focus was on ensuring core eCommerce features like browsing and cart functionality, with performance optimizations to follow.
    - **Custom Design vs. Framework**: Opted for Tailwind CSS to speed up development and ensure design consistency, but custom styling may be introduced in future iterations.
    - **Testing**: Basic unit tests are implemented, but end-to-end testing for the entire user journey is a future goal.
  - ### Future Improvements
    - Improve performance by lazy-loading components and implementing server-side rendering (SSR) with Next.js.
    - Add more comprehensive tests using tools like **Cypress** for end-to-end testing.
    - Integrate with more third-party APIs for recommendations, reviews, and payment processing.
    - Implement localization and internationalization (i18n) to support multiple languages and regions.
  - ## How to Run
    1. **Clone the repo**:
       ```js
       git clone https://github.com/yourusername/ecommerce-frontend.git
       ```
    2. **Install dependencies**:
       ```js
       npm install
       ```
    3. **Run the server**:
       ```js
       npm start
       ```
       The application will run on `http://localhost:3000`.
  - ## Demo Image/GIF/Video
    - Here’s a preview of the eCommerce frontend in action:
      - ![Home Page Screenshot](path/to/screenshot.png)
    - Or a demo of the user adding products to the cart:
      - ![Demo GIF](path/to/demo.mp4)

#### Short version
  - # eCommerce Frontend
    - ## Description
      - **Problem**: Many online stores lack modern, responsive interfaces.
      - **Solution**: A **React**-based frontend that enhances **user experience**, **performance**, and **scalability** for a seamless shopping experience.
    - ## Approach
      - ### Technology Stack
        - **Front-end**: **React** for a dynamic UI.
        - **State Management**: **Redux** for managing the global state.
        - **Styling**: **Tailwind CSS** for rapid, consistent design.
        - **Routing**: **React Router** for smooth page transitions.
        - **Build Tools**: **Webpack & Babel** for optimized performance.
      - ### Architecture
        - **Component-Based**: Each UI element is a reusable component, including:
            - **Product Listing**: Displays products with filters and sorting.
            - **Product Detail**: Detailed view of selected products.
            - **Shopping Cart**: Real-time updates on item quantities and totals.
            - **Checkout Page**: Guides users through the purchase process.
      - ### Features
        - **Product Browsing**: Catalog with filtering and sorting.
        - **Search Functionality**: Quickly find products.
        - **Responsive Design**: Adapts to all devices.
        - **User Authentication**: Login/logout functionality.
    - ## Trade-offs & Improvements
      - Focused on core features over performance; optimizations will follow.
      - Basic testing is in place; end-to-end tests are planned.
    - ### Future Improvements
      - Implement lazy loading and SSR with Next.js.
      - Enhance testing coverage.
      - Add localization support.
    - ## How to Run
      1. **Clone the repo**:
         ```bash
         git clone https://github.com/yourusername/ecommerce-frontend.git
         ```
      2. **Install dependencies**:
         ```bash
         npm install
         ```
      3. **Run the server**:
         ```bash
         npm start
         ```
         Access the application at `http://localhost:3000`.
    - ## Demo
      - ![Home Page Screenshot](path/to/screenshot.png)
      - Or a demo of adding products to the cart:
      - ![Demo GIF](path/to/demo.mp4)

> [!NOTE]
> can take demo and deployemnt urls to the top instead of bottom, just below the title for quicker access
