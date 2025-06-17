---
created_date: <% tp.file.creation_date('YYYY-MM-DD') %>
updated_date: <% tp.file.last_modified_date('YYYY-MM-DD') %>
tags:
  - "#task"
---
<%*
  let title = tp.file.title
  if (title.startsWith("Untitled")) {
    title = await tp.system.prompt("Title");
    await tp.file.rename(`${title}`);
  } 
%>
## Weekly Task

- [ ] Task 1: 
- [ ] Task 2:
- [ ] Task 3:

<% tp.file.last_modified_date('DD/MM/YYYY')%>
## Links
- 