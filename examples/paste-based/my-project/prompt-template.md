# Prompt Template (paste-based LLMs)

For chat tools without a project auto-load mechanism. Paste or attach the blocks in this order.
Replace every `[...]`.

````text
Strictly adhere to these specifications for all code suggestions and Git operations.

[paste the full content of .ai-rules.md here]

Project context:

[paste docs/product.md]
[paste docs/structure.md]
[paste docs/tech.md]

I am now working on the following feature (only this one):

[paste specs/password-reset/requirements.md]
[paste specs/password-reset/design.md]

Implement Task [N] from the task list below. Do not touch other tasks.

[paste specs/password-reset/tasks.md]
````

Tip: attach only ONE feature folder per chat. The model then never sees unrelated specs.
