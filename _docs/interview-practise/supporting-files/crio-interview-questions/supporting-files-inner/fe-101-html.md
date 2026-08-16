---
parent: Crio Interview Questions
layout: default
date: 20 feb 2025
title: FE-101 HTML
excerpt: HTML Crio Interview Questions for practise
permalink: crio-interview-questions-fe-101
tags: [crio interview questions, html]
parent_post: crio-interview-questions
---

## **Crio Questions**

1. [How does the browser load HTML and JS files upon visiting a particular website?](#1-how-does-the-browser-load-html-and-js-files-upon-visiting-a-particular-website)
2. [What is the purpose of the 'doctype' declaration in HTML documents?](#2-what-is-the-purpose-of-the-doctype-declaration-in-html-documents)
3. [What are the differences between block elements, inline elements, and inline-block elements?](#3-what-are-the-differences-between-block-elements-inline-elements-and-inline-block-elements)
4. [What are the differences between HTML and HTML5?](#4-what-are-the-differences-between-html-and-html5)
5. [What are the differences between semantic and non-semantic HTML tags?](#5-what-are-the-differences-between-semantic-and-non-semantic-html-tags)
6. [Explain CSS selectors and their types.](#6-explain-css-selectors-and-their-types)
7. [What is CSS selector specificity and how does it work?](#7-what-is-css-selector-specificity-and-how-does-it-work)
8. [What is CSS Box Model?](#8-what-is-css-box-model)
9. [What is the difference between absolute and relative length units in CSS? Provide examples.](#9-what-is-the-difference-between-absolute-and-relative-length-units-in-css-provide-examples)
10. [What is CSS Flexbox?](#10-what-is-css-flexbox)
11. [What is responsive web design?](#11-what-is-responsive-web-design)
12. [What are the differences between CSS Grids and Flexbox?](#12-what-are-the-differences-between-css-grids-and-flexbox)
13. [What is Bootstrap?](#13-what-is-bootstrap)
14. [What are the different CSS position property values?](#14-what-are-the-different-css-position-property-values)
15. [What is z-index in CSS?](#15-what-is-z-index-in-css)

##  **GPT Answers**

### 1. How does the browser load HTML and JS files upon visiting a particular website?
When you visit a website, the browser follows these steps to load HTML and JavaScript files:

1. **DNS Resolution**: The browser resolves the domain name into an IP address using the Domain Name System (DNS).  
2. **Sending HTTP Request**: The browser sends an HTTP request to the server where the website is hosted.  
3. **Server Response**: The server responds by sending the requested HTML document (and any associated assets like CSS, JavaScript, images, etc.).  
4. **Parsing HTML**: The browser begins parsing the HTML document and constructing the DOM (Document Object Model) tree.  
5. **Fetching External Resources**:  
   - The browser identifies external resources like CSS and JavaScript files (linked with `<link>` or `<script>` tags).  
   - It sends additional HTTP requests to fetch those resources.  
   - JavaScript files are executed in the order they appear (unless `async` or `defer` attributes are used).  
6. **Applying Styles**: The browser parses CSS files and applies styles to the DOM elements.  
7. **Rendering**: After the HTML and CSS are parsed and styles are applied, the browser renders the page on the screen.  
8. **Execution of JS**: JavaScript files can manipulate the DOM and CSSOM to update the content and style dynamically (e.g., user interactions, animations, etc.).

<br>

### 2. What is the purpose of the 'doctype' declaration in HTML documents?
The `<!DOCTYPE>` declaration:
- Tells the browser which version of HTML the document is written in, ensuring that the page is rendered correctly.
- In modern web development, `<!DOCTYPE html>` is used to declare the document type as HTML5, instructing the browser to render the document in **standards mode**.
- Without a doctype declaration, browsers may switch to **quirks mode**, which can lead to inconsistent rendering across different browsers.

<br>

### 3. What are the differences between block elements, inline elements, and inline-block elements?

- **Block Elements**:  
  - Occupy the entire width of their parent container.  
  - Always start on a new line (stacked vertically).  
  - Examples: `<div>`, `<p>`, `<h1>`, `<ul>`.

- **Inline Elements**:  
  - Do not start on a new line and only occupy the width necessary for their content.  
  - Can be placed inside block elements and other inline elements.  
  - Examples: `<span>`, `<a>`, `<strong>`, `<em>`.

- **Inline-block Elements**:  
  - Behave like inline elements (do not start on a new line), but they can have set widths and heights like block elements.  
  - Examples: `<button>`, `<img>`, `<input>`.

<br>

### 4. What are the differences between HTML and HTML5?

HTML5 is the latest version of HTML and includes new features and improvements over previous versions of HTML.

#### Key Differences:
1. **New Semantic Elements**: Tags like `<article>`, `<section>`, `<nav>`, `<header>`, `<footer>` improve the structure and meaning of web content.  
2. **Audio and Video**: HTML5 has native support for embedding audio and video using the `<audio>` and `<video>` tags, without third-party plugins like Flash.  
3. **Local Storage**: Introduces `localStorage` and `sessionStorage` for storing data on the client side.  
4. **Geolocation API**: Allows websites to access the user's location.  
5. **Forms**: Adds new input types (e.g., `email`, `date`, `range`) and attributes (e.g., `placeholder`, `required`).  
6. **Deprecated Tags**: Tags like `<font>`, `<center>`, and `<marquee>` have been deprecated.

<br>

### 5. What are the differences between semantic and non-semantic HTML tags?

- **Semantic HTML Tags**:  
  - These tags describe the meaning of the content enclosed within them, providing context for developers and search engines.  
  - Examples: `<article>`, `<section>`, `<header>`, `<footer>`, `<nav>`, `<main>`.  
  - They improve **accessibility** and **SEO** (Search Engine Optimization).

- **Non-Semantic HTML Tags**:  
  - These tags do not convey any meaning about their content; they are used mainly for structuring or styling the page.  
  - Examples: `<div>`, `<span>`.  
  - These elements require additional context or class names to define their purpose.

<br>

### 6. Explain CSS selectors and their types.

CSS selectors are patterns used to select and style elements in an HTML document. Common types include:

- **Universal Selector (`*`)**: Selects all elements.  
  ```css
  * {
    color: red;
  }
  ```

- **Type Selector (Element Selector)**: Selects all elements of a specific type.  
  ```css
  p {
    font-size: 16px;
  }
  ```

- **Class Selector (`.`)**: Selects all elements with a specific class.  
  ```css
  .my-class {
    background-color: yellow;
  }
  ```

- **ID Selector (`#`)**: Selects a specific element with an ID.  
  ```css
  #my-id {
    border: 1px solid black;
  }
  ```

- **Attribute Selector**: Selects elements with a specific attribute.  
  ```css
  a[href] {
    color: blue;
  }
  ```

- **Pseudo-classes (`:`)**: Selects elements based on their state.  
  ```css
  a:hover {
    text-decoration: underline;
  }
  ```

- **Pseudo-elements (`::`)**: Selects parts of an element.  
  ```css
  p::first-letter {
    font-size: 2em;
  }
  ```

<br>

### 7. What is CSS selector specificity and how does it work?

CSS specificity determines which CSS rule is applied when multiple rules target the same element. The more specific the selector, the higher its priority.

#### Specificity Hierarchy:
1. **Inline styles**: `style="color: red;"` (highest specificity).  
2. **IDs**: `#id-name`.  
3. **Classes, attributes, pseudo-classes**: `.class-name`, `[type="text"]`, `:hover`.  
4. **Elements and pseudo-elements**: `div`, `p`, `::before` (lowest specificity).

#### Example:
```css
#header { color: blue; }        /* Specificity: 1 (ID selector) */
.container { color: green; }    /* Specificity: 10 (Class selector) */
div { color: red; }             /* Specificity: 100 (Element selector) */
```

In case of conflicting styles, the rule with higher specificity is applied.

<br>

### 8. What is the CSS Box Model?

The CSS Box Model describes the rectangular boxes generated for elements in the document. It consists of:
- **Content**: The actual content of the box (text, images).  
- **Padding**: Space between the content and the border.  
- **Border**: Surrounds the padding (optional).  
- **Margin**: Space outside the border, separating the element from others.

#### Diagram:
```
| Margin | Border | Padding | Content |
```

#### Total Width and Height:
- **Total Width** = Content Width + Left Padding + Right Padding + Left Border + Right Border + Left Margin + Right Margin.  
- **Total Height** = Content Height + Top Padding + Bottom Padding + Top Border + Bottom Border + Top Margin + Bottom Margin.

<br>

### 9. What is the difference between absolute and relative length units in CSS? Provide examples.

- **Absolute Length Units**: Fixed units that are not affected by other factors (e.g., screen size, parent elements).  
  Examples: `px`, `cm`, `mm`, `in`, `pt`, `pc`.  
  ```css
  width: 200px;
  height: 5in;
  ```

- **Relative Length Units**: Units that are relative to other factors, such as the parent element or viewport size.  
  Examples: `%`, `em`, `rem`, `vw`, `vh`, `ch`.  
  ```css
  width: 50%;
  font-size: 2em;
  height: 100vh;
  ```

Relative units like `em` and `rem` scale dynamically, making them useful for responsive design, while absolute units like `px` are fixed.

<br>

### 10. What is CSS Flexbox?

CSS Flexbox (Flexible Box Layout) is a layout model that allows you to design complex layouts using a one-dimensional space (either horizontally or vertically). It enables more efficient alignment, distribution of space, and resizing of elements within a container.

#### Key Features:
- **Flex container**: The parent element where the flex properties are applied.  
- **Flex items**: The child elements within the flex container.  
- **Flex direction**: Defines the direction of the flex container (row or column).  
- **Justify-content**: Aligns items along the main axis (horizontal or vertical).  
- **Align-items**: Aligns items along the cross axis (perpendicular to the main axis).  
- **Align-self**: Allows individual items to be aligned differently than the others.  
- **Flex

-grow, flex-shrink, and flex-basis**: Control how the items grow, shrink, or maintain their size.

Flexbox is ideal for creating layouts that need to adjust dynamically to different screen sizes and content sizes.

<br>

### 11. What is responsive web design?

**Responsive Web Design** is an approach to web design that makes web pages render well on a variety of devices and screen sizes, from small mobile screens to large desktop monitors.

#### Key Principles:
1. **Fluid grids**: Use relative units like percentages instead of fixed pixel values for layout elements.  
2. **Media queries**: Apply different styles based on the screen size, resolution, or orientation of the device.  
3. **Flexible images**: Images and other media resize to fit different screen sizes using CSS techniques like `max-width: 100%`.

This approach ensures a consistent and optimized experience across devices.

<br>

### 12. What are the differences between CSS Grids and Flexbox?

Both CSS Grid and CSS Flexbox are powerful layout systems, but they serve different purposes:

#### CSS Grid:
- Designed for **two-dimensional layouts** (both rows and columns).  
- Suitable for **complex layouts** with multiple rows and columns.  
- Provides precise control over positioning and sizing.  
- Example:
  ```css
  .grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 10px;
  }
  ```

#### CSS Flexbox:
- Designed for **one-dimensional layouts** (rows or columns).  
- Great for **aligning items along a single axis**.  
- More straightforward for simpler layouts.  
- Example:
  ```css
  .flex-container {
    display: flex;
    justify-content: space-between;
  }
  ```

#### When to Use:
- **Flexbox**: Ideal for linear layouts (e.g., navigation bars or form layouts).  
- **Grid**: Best for complex layouts with control over both rows and columns.

<br>

### 13. What is Bootstrap?

**Bootstrap** is a popular front-end framework for building responsive, mobile-first web applications quickly. It provides:
- **Grid system**: A 12-column responsive grid system.  
- **Pre-styled components**: Includes buttons, forms, navigation bars, modals, and more.  
- **Customizable themes**: Allows customization using Sass variables.  
- **JavaScript components**: Includes interactive elements like carousels, tooltips, and modals.

Bootstrap helps streamline development and ensures consistent styling across browsers.

<br>

### 14. What are the different CSS position property values?

The `position` property in CSS specifies how an element is positioned within its container. Key values include:

- **static**: Default position, follows normal document flow.  
  ```css
  position: static;
  ```

- **relative**: Positioned relative to its normal position.  
  ```css
  position: relative;
  top: 10px;
  ```

- **absolute**: Positioned relative to the nearest positioned ancestor (non-static).  
  ```css
  position: absolute;
  top: 20px;
  left: 10px;
  ```

- **fixed**: Positioned relative to the viewport; stays in place when scrolling.  
  ```css
  position: fixed;
  top: 0;
  left: 0;
  ```

- **sticky**: Treated as relative until a certain scroll threshold, then becomes fixed.  
  ```css
  position: sticky;
  top: 0;
  ```

<br>

### 15. What is z-index in CSS?

The `z-index` property in CSS controls the **stacking order** of elements on the z-axis (perpendicular to the screen). 

#### Key Points:
- Higher `z-index` values appear in front of lower values.  
- Only elements with a position other than `static` can have a `z-index` applied.  

#### Example:
```css
div {
  position: absolute;
  z-index: 10;
}

div.overlay {
  position: absolute;
  z-index: 20; /* The overlay will appear on top of the first div */
}
```

