---
created_date: <% tp.file.creation_date('YYYY-MM-DD') %>
updated_date: <% tp.file.last_modified_date('YYYY-MM-DD') %>
tags:
  - "#note"
---
<%*
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