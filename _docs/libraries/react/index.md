---
layout: default
date: 22 jan 2025
title: React Concepts Guide
excerpt: To study basic and advanced React
permalink: react
tags: [react]
parent: Libraries
---

## Table of Concepts

- Basic React
  1. Core Concepts
  2. Rendering
  3. Handling Events
  4. Forms
  5. Styling
  6. State Management (Basic)
  7. Routing
  8. Error Handling
  9. Working with APIs
  10. Performance Optimization (Introductory)
- Advanced React 
  1. Hooks (Advanced)
  2. State Management (Advanced)
  3. Code Splitting and Lazy Loading
  4. Server-Side Rendering (SSR)
  5. Testing
  6. Performance Optimization (Advanced)
  7. TypeScript with React
  8. Animations
  9. Patterns and Architecture
  10. GraphQL Integration
  11. WebSockets and Real-Time Updates
  12. Custom Rendering
  13. Advanced Routing
  14. Accessibility
  15. Internationalization (i18n)


Certainly! Here's an explanation of the key React topics you mentioned. React is a JavaScript library for building user interfaces, particularly for single-page applications. Below, I'll break down the basics of each topic:

---

### **Core Concepts**

#### **JSX (JavaScript XML)**
- JSX is a syntax extension for JavaScript that looks similar to HTML.
- It allows you to write HTML elements and components directly in your JavaScript code.
- Example:
  ```jsx
  const element = <h1>Hello, world!</h1>;
  ```
- JSX gets transpiled into standard JavaScript using tools like Babel.

#### **Components (Functional and Class)**
- **Functional Components**: These are simple JavaScript functions that return JSX.
  ```jsx
  const Greeting = () => <h1>Hello, World!</h1>;
  ```
- **Class Components**: ES6 classes that extend `React.Component` and include a `render` method.
  ```jsx
  class Greeting extends React.Component {
    render() {
      return <h1>Hello, World!</h1>;
    }
  }
  ```

#### **Props and State**
- **Props**: Short for "properties," they are inputs passed to components.
  ```jsx
  const Welcome = (props) => <h1>Hello, {props.name}</h1>;
  ```
- **State**: A component's internal data that changes over time, used with `useState` (functional components) or `this.state` (class components).

#### **Component Lifecycle (Class Components)**
Lifecycle methods manage what happens at different stages of a component's life:
- `componentDidMount()`: Runs after the component is mounted.
- `componentDidUpdate()`: Runs after the component updates.
- `componentWillUnmount()`: Runs before the component is removed.

---

### **Rendering**

#### **Conditional Rendering**
- Rendering elements based on conditions.
  ```jsx
  const isLoggedIn = true;
  return isLoggedIn ? <h1>Welcome back!</h1> : <h1>Please sign in.</h1>;
  ```

#### **Lists and Keys**
- Rendering a list of items with the `map` method.
- Keys help React identify which items have changed.
  ```jsx
  const items = ['Item 1', 'Item 2'];
  return items.map((item, index) => <li key={index}>{item}</li>);
  ```

---

### **Handling Events**

#### **Event Handling**
- React uses camelCase for event names (e.g., `onClick`).
  ```jsx
  const handleClick = () => alert('Clicked!');
  <button onClick={handleClick}>Click Me</button>;
  ```

#### **Synthetic Events**
- A cross-browser wrapper around the browser’s native event.

---

### **Forms**

#### **Controlled vs. Uncontrolled Components**
- **Controlled**: Component controls form input values using `state`.
  ```jsx
  const [value, setValue] = useState('');
  return <input value={value} onChange={(e) => setValue(e.target.value)} />;
  ```
- **Uncontrolled**: Use `ref` to access DOM elements directly.

#### **Form Handling and Validation**
- Handle form submissions and validate input values programmatically.
  ```jsx
  const handleSubmit = (e) => {
    e.preventDefault();
    if (value.trim() === '') alert('Value required');
  };
  ```

---

### **Styling**

#### **Inline Styles**
- Define styles directly in JSX.
  ```jsx
  const style = { color: 'blue', fontSize: '20px' };
  return <h1 style={style}>Styled Text</h1>;
  ```

#### **CSS Modules**
- Locally scoped CSS classes by importing CSS files as modules.
  ```css
  /* styles.module.css */
  .header { color: red; }
  ```
  ```jsx
  import styles from './styles.module.css';
  <h1 className={styles.header}>Hello</h1>;
  ```

#### **Styled-Components (Optional)**
- CSS-in-JS library to style components.
  ```jsx
  import styled from 'styled-components';
  const StyledButton = styled.button`background: blue; color: white;`;
  ```

---

### **State Management (Basic)**

#### **Using the `useState` Hook**
- Manages state in functional components.
  ```jsx
  const [count, setCount] = useState(0);
  ```

#### **Context API (Introduction)**
- Provides a way to pass data through the component tree without props.
  ```jsx
  const ThemeContext = React.createContext('light');
  ```

---

### **Routing**

#### **React Router Basics (v6+)**
- Define routes for navigation.
  ```jsx
  import { BrowserRouter, Routes, Route } from 'react-router-dom';
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Home />} />
    </Routes>
  </BrowserRouter>;
  ```

#### **Navigation and Link Components**
- Use `Link` to navigate between routes without refreshing.
  ```jsx
  <Link to="/about">About</Link>;
  ```

---

### **Error Handling**

#### **Error Boundaries (Class Components)**
- Catch errors in a component tree using `componentDidCatch` and `getDerivedStateFromError`.
  ```jsx
  class ErrorBoundary extends React.Component {
    componentDidCatch(error, info) { console.error(error); }
    render() { return this.props.children; }
  }
  ```

---

### **Working with APIs**

#### **Fetching Data (Using Fetch or Axios)**
- Use `fetch` or `axios` to get data.
  ```jsx
  useEffect(() => {
    fetch('https://api.example.com/data')
      .then((res) => res.json())
      .then((data) => setData(data));
  }, []);
  ```

#### **Handling Promises and Async/Await**
- Prefer async/await for cleaner asynchronous code.
  ```jsx
  const fetchData = async () => {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    setData(data);
  };
  ```

---

### **Performance Optimization (Introductory)**

#### **React.memo**
- Prevents unnecessary re-renders by memoizing components.
  ```jsx
  const MemoizedComponent = React.memo(MyComponent);
  ```

#### **`useCallback` and `useMemo` (Basic Use Cases)**
- **`useCallback`**: Memoizes functions.
  ```jsx
  const memoizedCallback = useCallback(() => { doSomething(); }, [dependencies]);
  ```
- **`useMemo`**: Memoizes values.
  ```jsx
  const computedValue = useMemo(() => computeExpensiveValue(), [dependencies]);
  ```

---

This overview provides a foundation for React. Let me know if you'd like a deeper dive into any specific topic!
