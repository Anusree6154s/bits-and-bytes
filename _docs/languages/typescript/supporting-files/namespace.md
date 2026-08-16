---
parent: Typescript learners guide
layout: default
date: 19 jan 2025
title: More about Namespaces in Typescript
permalink: namespace
tags: [typescript, namespace]
parent_post: typescript-learners-guide
hidden: true
---

### **Namespaces in TypeScript**

Namespaces are a TypeScript feature used to organize and group related code together under a common name. They provide a logical structure to the code and avoid naming conflicts by creating an encapsulated scope. While **modules** (ES6 style) are preferred in modern TypeScript, namespaces are still used in some scenarios, particularly in legacy systems or for organizing large codebases.

<br>

### **1. What Are Namespaces?**

A **namespace** is a construct that wraps code (e.g., interfaces, classes, functions, or variables) in a named scope. This allows the code to be accessed without polluting the global scope.

#### **Basic Syntax**

```typescript
namespace MyNamespace {
  export interface User {
    name: string;
    age: number;
  }

  export function greet(user: User): string {
    return `Hello, ${user.name}!`;
  }
}

// Using the namespace
const user: MyNamespace.User = { name: "Alice", age: 25 };
console.log(MyNamespace.greet(user)); // Hello, Alice!
```

- **Keyword `namespace`**: Used to define a namespace.
- **`export` keyword**: Makes members (interfaces, classes, functions, variables) available outside the namespace.

<br>

### **2. Key Features of Namespaces**

#### **Encapsulation**
Namespaces encapsulate related code into a single logical group, preventing naming conflicts in large projects.

```typescript
namespace Physics {
  export const speedOfLight = 299792458; // meters per second
  export const gravitationalConstant = 6.67430e-11;
}

namespace Chemistry {
  export const speedOfLight = "N/A"; // Different interpretation
}

console.log(Physics.speedOfLight); // 299792458
console.log(Chemistry.speedOfLight); // N/A
```

#### **Nested Namespaces**
Namespaces can be nested within one another, creating a hierarchical structure.

```typescript
namespace Geometry {
  export namespace Shapes {
    export class Circle {
      constructor(public radius: number) {}
      area(): number {
        return Math.PI * this.radius ** 2;
      }
    }
  }
}

const circle = new Geometry.Shapes.Circle(5);
console.log(circle.area()); // 78.53981633974483
```

#### **Merging Namespaces**
Multiple declarations of the same namespace are automatically merged, similar to **declaration merging**.

```typescript
namespace MyNamespace {
  export const greeting = "Hello";
}

namespace MyNamespace {
  export function sayHello(): void {
    console.log(greeting);
  }
}

MyNamespace.sayHello(); // Hello
```

<br>

### **3. Namespaces vs. Modules**

In modern TypeScript development, **ES6 modules** (`import`/`export`) are preferred over namespaces. However, namespaces can still be useful in some scenarios.

| **Feature**            | **Namespaces**                                    | **Modules**                        |
|-------------------------|--------------------------------------------------|------------------------------------|
| **Scope**              | Logical grouping within a single file or project. | Based on file structure.           |
| **Usage**              | Used with `<script>` in browsers or older systems.| Preferred for modern JavaScript.   |
| **Import Syntax**      | Accessed using the namespace prefix.              | Explicit `import`/`export`.        |
| **Preferred Use Case** | Legacy projects or internal libraries.            | Most modern TypeScript projects.   |

#### Example of a Module (Modern Syntax):
```typescript
// file1.ts
export interface User {
  name: string;
  age: number;
}

// file2.ts
import { User } from "./file1";

const user: User = { name: "Bob", age: 40 };
```

<br>

### **4. Advanced Features of Namespaces**

#### **Augmenting Built-in Types with Namespaces**
You can extend built-in types like `Array` or `String` using namespaces.

```typescript
namespace ArrayExtensions {
  export function last<T>(arr: T[]): T | undefined {
    return arr[arr.length - 1];
  }
}

const nums = [1, 2, 3];
console.log(ArrayExtensions.last(nums)); // 3
```

#### **Namespace Aliases**
Use `import` to create an alias for a namespace, making it easier to reference deeply nested namespaces.

```typescript
namespace LongNamespaceName {
  export const value = 42;
}

import LNN = LongNamespaceName;
console.log(LNN.value); // 42
```

<br>

### **5. Practical Applications of Namespaces**

1. **Grouping Related Code**:
   - Combine related classes, interfaces, or functions under one namespace.

   ```typescript
   namespace UI {
     export interface Button {
       label: string;
     }

     export function render(button: Button): void {
       console.log(`Rendering button: ${button.label}`);
     }
   }

   const button: UI.Button = { label: "Submit" };
   UI.render(button); // Rendering button: Submit
   ```

2. **Extending External Libraries**:
   - Add custom logic to third-party libraries without modifying their source code.

   ```typescript
   namespace Express {
     export interface Request {
       user?: string;
     }
   }
   ```

3. **Code Organization for Large Projects**:
   - Split namespaces across multiple files for better structure.

   ```typescript
   // file1.ts
   namespace Utils {
     export function log(message: string): void {
       console.log(message);
     }
   }

   // file2.ts
   namespace Utils {
     export function error(message: string): void {
       console.error(message);
     }
   }

   Utils.log("This is a log message.");
   Utils.error("This is an error message.");
   ```

<br>

### **Summary of Key Topics**

| **Topic**                | **Description**                                                                                         | **Example**                                                                                         |
|--------------------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| **Namespaces**           | Logical groups for related code. Encapsulate members and avoid naming conflicts.                       | `namespace Shapes { export interface Circle { radius: number; } }`                                 |
| **Nested Namespaces**    | Namespaces can be nested for hierarchical organization.                                                | `namespace A { namespace B { export const value = 10; } }`                                         |
| **Merging Namespaces**   | Multiple declarations of the same namespace are merged.                                                | `namespace N { export const a = 1; }` and `namespace N { export const b = 2; }`                    |
| **Namespace Aliases**    | Shorten long namespace names using `import`.                                                          | `import Short = LongNamespace;`                                                                    |
| **Namespaces vs Modules**| Namespaces group code logically; modules group code based on files.                                     | `namespace MathUtils {}` vs. `import { add } from './math';`                                       |

Namespaces are still relevant for certain scenarios, particularly in **legacy projects**, **libraries**, or environments where ES6 modules cannot be used. For modern projects, **ES6 modules** are the preferred approach for modularizing code.
😊
