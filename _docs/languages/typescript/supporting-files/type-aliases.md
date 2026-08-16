---
parent: Typescript learners guide
layout: default
date: 19 jan 2025
title: More about Type Aliases
permalink: type-aliases
tags: [typescript, type aliases]
parent_post: typescript-learners-guide
hidden: true
---


### 1. **Advanced Use Cases**

#### 1. Recursive Types:
Type aliases can define recursive types, which are useful for defining data structures like trees or JSON.

Example:
```typescript
type JSONValue = string | number | boolean | null | JSONValue[] | { [key: string]: JSONValue };

const data: JSONValue = {
  name: "Alice",
  age: 30,
  preferences: {
    theme: "dark",
    notifications: true,
  },
  hobbies: ["reading", "gaming"],
};
```

Here, `JSONValue` is a recursive type alias that describes valid JSON values.



#### 2. Conditional Types:
Type aliases can use **conditional types** for more advanced use cases.

Example:
```typescript
type IsString<T> = T extends string ? true : false;

type Test1 = IsString<string>;  // true
type Test2 = IsString<number>;  // false
```

Here, `IsString` is a conditional type that evaluates to `true` if the input type `T` is `string`, and `false` otherwise.

<br>
<br>

### 2. **Best Practices for Type Aliases**

1. **Use Descriptive Names:** Make type alias names clear and meaningful to convey their purpose.
   ```typescript
   type ProductID = string;
   ```

2. **Use for Non-Object Types:** Prefer type aliases when working with primitives, unions, intersections, or complex types.
   ```typescript
   type Coordinate = [number, number];
   ```

3. **Use Interfaces for Objects:** When defining object shapes that might need to be extended or merged, prefer interfaces.
   ```typescript
   interface User {
     name: string;
     age: number;
   }
   ```

4. **Avoid Overusing Aliases:** Don’t alias everything—use them where they improve readability or reduce repetition.

