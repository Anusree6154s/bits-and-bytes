---
parent: Typescript learners guide
layout: default
date: 19 jan 2025
title: More about Conditional Types
permalink: conditional-types
tags: [typescript, conditional types]
parent_post: typescript-learners-guide
hidden: true
---

### **1. Syntax of Conditional Types**

The syntax for a conditional type is:

```typescript
T extends U ? X : Y
```

- **`T`**: The type to evaluate.
- **`U`**: The condition to check (`T extends U`).
- **`X`**: The type returned if the condition is true.
- **`Y`**: The type returned if the condition is false.

<br>

### **2. Example: Basic Conditional Type**

The following example checks if a type `T` is a `string`:

```typescript
type IsString<T> = T extends string ? true : false;

type Test1 = IsString<string>; // true
type Test2 = IsString<number>; // false
```

Here, `Test1` resolves to `true` because `string` extends `string`, while `Test2` resolves to `false` because `number` does not extend `string`.

