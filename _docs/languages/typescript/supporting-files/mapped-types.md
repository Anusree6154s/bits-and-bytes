---
parent: Typescript learners guide
layout: default
date: 19 jan 2025
title: More about Mapped Types
permalink: mapped-types
tags: [typescript, mapped types]
parent_post: typescript-learners-guide
hidden: true
---


### **Mapped Types in TypeScript**

Mapped types are a powerful feature in TypeScript that allow you to create new types by transforming the properties of existing types. They are especially useful for modifying the shape or behavior of types dynamically, enabling more flexible and reusable code.

<br>

### **1. Syntax of Mapped Types**

The basic syntax for creating a mapped type is:

```typescript
type NewType<T> = { [Key in keyof T]: TransformedType };
```

- **`keyof T`**: Extracts all keys from the type `T` as a union of string or symbol literal types.
- **`[Key in keyof T]`**: Iterates over each key in the type `T`.
- **`T[Key]`**: Accesses the type of the value corresponding to the key `Key` in `T`.
- **Modifiers** (`readonly`, `?`): Used to adjust the properties (e.g., making them `readonly` or optional).

<br>

### **2. Examples of Mapped Types**

#### **2.1 Readonly Type**

Transforms all properties of an object into `readonly` properties, preventing them from being reassigned.

```typescript
type Readonly<T> = { readonly [Key in keyof T]: T[Key] };

interface Person {
  name: string;
  age: number;
}

type ReadonlyPerson = Readonly<Person>;

const person: ReadonlyPerson = { name: "Alice", age: 30 };
// person.name = "Bob"; // Error: cannot assign to 'name' because it is a read-only property.
```

<br>

#### **2.2 Partial Type**

Makes all properties of an object optional.

```typescript
type Partial<T> = { [Key in keyof T]?: T[Key] };

interface Person {
  name: string;
  age: number;
}

type PartialPerson = Partial<Person>;

const person: PartialPerson = { name: "Alice" }; // `age` is optional
```

<br>

#### **2.3 Required Type**

Makes all properties of an object required.

```typescript
type Required<T> = { [Key in keyof T]-?: T[Key] };

interface Person {
  name?: string;
  age?: number;
}

type RequiredPerson = Required<Person>;

const person: RequiredPerson = { name: "Alice", age: 30 }; // All properties are required
```

<br>

#### **2.4 Record Type**

Creates an object type where keys are specified and values have a uniform type.

```typescript
type Record<K extends keyof any, T> = { [Key in K]: T };

type Roles = "admin" | "user" | "guest";
type Permissions = Record<Roles, string>;

const permissions: Permissions = {
  admin: "all",
  user: "read-only",
  guest: "none",
};
```

<br>

#### **2.5 Pick Type**

Extracts a subset of properties from an object.

```typescript
type Pick<T, K extends keyof T> = { [Key in K]: T[Key] };

interface Person {
  name: string;
  age: number;
  address: string;
}

type NameAndAge = Pick<Person, "name" | "age">;

const person: NameAndAge = { name: "Alice", age: 30 }; // Only name and age are allowed
```

<br>

#### **2.6 Omit Type**

Removes specific properties from an object type.

```typescript
type Omit<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>;

interface Person {
  name: string;
  age: number;
  address: string;
}

type WithoutAddress = Omit<Person, "address">;

const person: WithoutAddress = { name: "Alice", age: 30 }; // Address is omitted
```

<br>

### **3. Key Modifiers in Mapped Types**

#### **3.1 `readonly` Modifier**

Applies the `readonly` modifier to all properties, making them immutable.

```typescript
type Readonly<T> = { readonly [Key in keyof T]: T[Key] };
```

#### **3.2 `?` Modifier**

Applies the optional (`?`) modifier to all properties.

```typescript
type Partial<T> = { [Key in keyof T]?: T[Key] };
```

#### **3.3 `-?` Modifier**

Removes the optional modifier from all properties.

```typescript
type Required<T> = { [Key in keyof T]-?: T[Key] };
```

#### **3.4 `-readonly` Modifier**

Removes the `readonly` modifier from all properties.

```typescript
type Mutable<T> = { -readonly [Key in keyof T]: T[Key] };
```

<br>

### **4. Combining Mapped Types with Utility Types**

Mapped types can be combined with other TypeScript features like **utility types**, **union types**, and **conditional types**.

#### **4.1 Combining with Union Types**

You can use mapped types to iterate over a union of keys.

```typescript
type OptionsFlags<T> = { [Key in keyof T]: boolean };

interface Features {
  darkMode: () => void;
  newUser: () => void;
}

type FeatureFlags = OptionsFlags<Features>;

const flags: FeatureFlags = { darkMode: true, newUser: false };
```

#### **4.2 Using Conditional Types**

You can conditionally modify the properties of a mapped type.

```typescript
type Nullable<T> = { [Key in keyof T]: T[Key] | null };

interface User {
  id: number;
  name: string;
}

type NullableUser = Nullable<User>;

const user: NullableUser = { id: null, name: "Alice" }; // Properties can be null
```

<br>

### **5. Advanced Use Cases**

#### **5.1 Deep Readonly**

Make all properties of an object (and its nested objects) `readonly`.

```typescript
type DeepReadonly<T> = {
  readonly [Key in keyof T]: T[Key] extends object ? DeepReadonly<T[Key]> : T[Key];
};

interface NestedObject {
  level1: {
    level2: {
      value: string;
    };
  };
}

const obj: DeepReadonly<NestedObject> = {
  level1: {
    level2: {
      value: "Hello",
    },
  },
};

// obj.level1.level2.value = "New Value"; // Error
```

#### **5.2 Filtering Keys**

Extract keys from an object based on their types.

```typescript
type FilterKeys<T, U> = { [Key in keyof T]: T[Key] extends U ? Key : never }[keyof T];

interface Example {
  name: string;
  age: number;
  isActive: boolean;
}

type StringKeys = FilterKeys<Example, string>; // "name"
```

<br>

### **6. How Mapped Types Relate to Other Topics**

Mapped types build upon foundational TypeScript concepts:

1. **Generics**: Mapped types often use generics to create reusable type transformations.
2. **Type Inference**: TypeScript infers types within mapped types to ensure transformations are type-safe.
3. **Union and Intersection Types**: Mapped types frequently operate on unions or intersecting types to create flexible transformations.

<br>

### **Conclusion**

Mapped types are a cornerstone of TypeScript’s type system, enabling developers to create dynamic, reusable, and type-safe transformations. By leveraging features like key modifiers, utility types, and conditional types, you can write more expressive and maintainable code tailored to your application’s needs. They provide the flexibility to adapt types without losing TypeScript's static type-checking benefits.
