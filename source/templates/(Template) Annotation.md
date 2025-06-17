---
created_date: <% tp.file.creation_date('YYYY-MM-DD') %>
updated_date: <% tp.file.last_modified_date('YYYY-MM-DD') %>
tags:
  - annotation
annotation-target:
---
---
created_date: 2025-04-16
updated_date: 2025-04-16
tags:
  - "#task"
---

## Weekly Task

- [ ] Task 1: 
- [ ] Task 2:
- [ ] Task 3:

16/04/2025
## Links
- <%*
  let title = tp.file.title
  if (title.startsWith("Untitled")) {
    title = await tp.system.prompt("Title");
    await tp.file.rename(`${title}`);
  } 
%>

## Notes
- 
## Links
- 