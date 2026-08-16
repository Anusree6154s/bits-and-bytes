---
parent: Web Dev
layout: default
title: Tailwind styling without inline
date:  3 march 2025
excerpt: Methods to style using tailwind without inline
permalink: tailwing-styling-without-inline
---



### **1️⃣ Use `@apply` in a Global CSS File**  
You can define reusable styles in a CSS file and use `@apply` to apply Tailwind classes.  

🔹 **Steps:**  
- Create a global CSS file (e.g., `globals.css`).  
- Define your reusable styles using `@apply`.  
- Import the CSS file into your project (usually in `_app.js` or `layout.tsx`).  

📌 **Example (`globals.css`):**  
```css
/* Define reusable styles */
.btn-primary {
  @apply bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 transition;
}

.card {
  @apply p-6 shadow-md border border-gray-200 rounded-lg bg-white;
}
```

📌 **Usage in a Component:**  
```tsx
<button className="btn-primary">Click Me</button>
<div className="card">This is a card</div>
```



### **2️⃣ Use Tailwind's Config File (`tailwind.config.js`)**  
If you need custom colors, spacing, or typography, you can extend Tailwind's configuration.

📌 **Example (`tailwind.config.js`):**  
```js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: "#1D4ED8", // Custom primary color
      },
    },
  },
};
```

📌 **Usage in Components:**  
```tsx
<button className="bg-primary text-white px-4 py-2 rounded-md">Click Me</button>
```



### **3️⃣ Use Component-Specific Styling in a `module.css` File**  
If you're using Next.js or a module-based approach, you can create a `module.css` file.

📌 **Example (`Button.module.css`):**  
```css
.btn {
  @apply bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600;
}
```

📌 **Usage in Component:**  
```tsx
import styles from "./Button.module.css";

<button className={styles.btn}>Click Me</button>;
```



### **4️⃣ Use Tailwind with a Component-Based Approach**  
If you're using React/Next.js, you can create reusable styled components.

📌 **Example (`Button.tsx`):**  
```tsx
const Button = ({ children }) => {
  return <button className="bg-blue-500 text-white px-4 py-2 rounded-md">{children}</button>;
};

export default Button;
```

📌 **Usage in a File:**  
```tsx
<Button>Click Me</Button>
```
