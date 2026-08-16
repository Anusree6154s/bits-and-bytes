---
parent: Typescript learners guide
layout: default
date: 19 jan 2025
title: More about Modules in Typescript
permalink: modules
tags: [typescript, modules]
parent_post: typescript-learners-guide
hidden: true
---


### **1. Exporting Types**

You can export types such as interfaces, type aliases, and enums in addition to functions, classes, and variables.

```typescript
// types.ts
export interface Person {
  name: string;
  age: number;
}

export type ID = string | number;

// main.ts
import { Person, ID } from "./types";

const user: Person = { name: "Alice", age: 30 };
const userId: ID = 123;

console.log(user, userId);
```

<br>
 
### **2. Re-exports**

You can re-export a module's exports without explicitly importing them.

```typescript
// math.ts
export const add = (a: number, b: number) => a + b;
export const subtract = (a: number, b: number) => a - b;

// operations.ts
export * from "./math";

// main.ts
import { add, subtract } from "./operations";

console.log(add(3, 2));       // Output: 5
console.log(subtract(5, 2));  // Output: 3
```

<br>
 

### **3. Import Aliases**

You can use aliases to rename imports for better readability or to avoid conflicts.

```typescript
// utils.ts
export const calculate = (a: number, b: number) => a + b;

// main.ts
import { calculate as add } from "./utils";

console.log(add(5, 3)); // Output: 8
```

<br>
 
### **4. Importing All Exports**

You can import everything from a module as a single object.

```typescript
// math.ts
export const add = (a: number, b: number) => a + b;
export const multiply = (a: number, b: number) => a * b;

// main.ts
import * as MathUtils from "./math";

console.log(MathUtils.add(2, 3));        // Output: 5
console.log(MathUtils.multiply(2, 3));  // Output: 6
```

<br>
 

### **5. Dynamic Imports**

Dynamic imports allow you to load modules at runtime, which is useful for lazy-loading or conditional imports.

```typescript
// file1.ts
export const greet = (name: string) => `Hello, ${name}`;

// main.ts
async function loadGreet() {
  const { greet } = await import("./file1");
  console.log(greet("Alice")); // Output: Hello, Alice
}

loadGreet();
```

<br>
 

### **6. Module Resolution**

TypeScript uses a **module resolution strategy** to locate and import modules. The two strategies are:

#### Node.js (CommonJS) Resolution:
- Used by default when working in a Node.js environment.
- Looks for `.ts`, `.tsx`, `.js`, or `.json` files in the specified path.

#### ES Module (ECMAScript) Resolution:
- Used for modern JavaScript projects with ES Modules.
- Requires setting `module` to `ESNext` or `ESModule` in `tsconfig.json`.

<br>
 

### **7. Configuring Modules in TypeScript**

TypeScript’s module system is configured in the `tsconfig.json` file. Important options include:

#### `module`:
Specifies the output module format (e.g., `CommonJS`, `ESNext`, or `AMD`).

```json
{
  "compilerOptions": {
    "module": "CommonJS"
  }
}
```

#### `moduleResolution`:
Controls how modules are resolved. Can be set to `node` or `classic`.

```json
{
  "compilerOptions": {
    "moduleResolution": "node"
  }
}
```

#### `baseUrl` and `paths`:
Used to define aliases for module paths.

```json
{
  "compilerOptions": {
    "baseUrl": "./",
    "paths": {
      "@utils/*": ["src/utils/*"]
    }
  }
}
```

```typescript
// main.ts
import { calculate } from "@utils/math";
```

<br>
 

### **8. Module Best Practices**

1. **Use Named Exports for Multiple Items**: Default exports can cause confusion in larger projects.
   ```typescript
   export const add = (a: number, b: number) => a + b;
   export const subtract = (a: number, b: number) => a - b;
   ```

2. **Organize Files Logically**: Group related files into folders and avoid long import paths by using aliases.

3. **Avoid Importing from Deep Paths**:
   ```typescript
   // Bad
   import { something } from "../../utils/math";

   // Good
   import { something } from "@utils/math";
   ```

4. **Prefer Type-Only Imports**: Use `import type` for importing only types to reduce runtime overhead.
   ```typescript
   import type { Person } from "./types";
   ```

