---
title: Using Bootstrap Icons
date:  4 march 2025
layout: post
excerpt: How to use bootstrap icons in react or NextJS
permalink: bootstrap-icons-usage
---



### **1. Install Bootstrap Icons (Recommended - I use this)**
If you're using a package manager like npm or yarn, install Bootstrap Icons:  

```sh
npm install bootstrap-icons
```
or  
```sh
yarn add bootstrap-icons
```

Then, import the CSS in your **index.js** or **App.js**:  

```js
import 'bootstrap-icons/font/bootstrap-icons.css';
```

Now, you can use icons like this in your components:  
```jsx
<i className="bi bi-heart"></i>
```



### **2. Use Bootstrap Icons via CDN (Alternative)**
If you don’t want to install the package, add this **CDN link** in your `index.html` (inside `<head>`):  

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css">
```

Then, you can use icons directly in your components:  
```jsx
<i className="bi bi-heart"></i>
```



### **3. Using Icons as React Components (For Better Performance)**
Instead of `<i>` tags, you can import SVG icons directly:  
```jsx
import { ReactComponent as HeartIcon } from 'bootstrap-icons/icons/heart.svg';

const MyComponent = () => {
  return <HeartIcon width="24" height="24" fill="red" />;
};
```
