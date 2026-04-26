---
layout: post
date: 26 apr 2026
title: OOP
excerpt: Learning object oriented programming
permalink: oop
tags: [oop, software design, computer basics]
---

- ## Mental model
  - OOP - thinknig in objects
  - LLD - designing system using OOP
  - HLD - scaling those systems

<br><br>

- ## Thinking in objects
  - Q. Design a library system
  - Steps:
    - Identify **entities**: Book, User, Library, Transaction (\* OOP is not about classes, but rather about modelling real world entities)
    - Develop **Reponsisbilty thinking**:
        - Book: knows title, author, availability
        - User: can borrow books
        - Transaction: tracks borrow/return
        - Library: manages books

- Q. Online food ordering sysytem. List entities and give 1 responsibility per entity
    - Tips:
        - > Keep it modelling-heavy and less of list-heavy
        - > Do not mix levels of abstraction (eg: ingrdients is very low level, orders is core domain, offers is an optional feature, employees is an internal sysytem detail). In interview it will look like candidate is listing everything  instead of structuring the domain
        - Non negotiable core entities: User, Restaurant, Menu, Order, Payment
        - Supporting entities: Delivery Agent, Location, Review, Offer (optional)
        - Reponsibilities: 
          - User: place order, view order
          - Restaurant: manage menu, process order
          - Order: calculate total, update status
          - Payment: handle transaction
          - Menu: provide items
    - > How to identitfy primary actors and itheri associated entities:
      >  - Identify the target users 
      >    - They are teh first class actors
      >    - eg: Customer, Restaurant owner, delivery agent
      >  - Identfy the enitities facing them
      >    - They are the high level entities
      >    - eg: 
      >      - Cutomer -> browse(menu), order, pay
      >      - restaurant -> manage menu, accet orders
      >      - delivery agent -> deliver orders
          
