<img width="1236" height="517" alt="image" src="https://github.com/user-attachments/assets/b8b3f6e1-d9a6-4514-8239-b3a69cfafc77" /># Tinker: ByteBits

## Activity Overview

You have joined the development team of ByteBites, a new campus food ordering app that wants to feel fast, personalized, and a little bit smart. The problem is that the current prototype is a mess. The menu structure is inconsistent, orders are unreliable, and the so-called AI recommendations suggest soup as a dessert pairing. No one knows how the system is supposed to fit together.

Your task is to design and build the core architecture of the app using Python classes and simple algorithms. You'll use AI as a design partner, but you must verify and refine everything it produces. By the end, you'll have created a clean and functional version of the system that makes sense to a human engineer.

You'll practice reading vague design requests, turning them into clear system components, generating UML-style diagrams with AI, translating those diagrams into code, and testing your work with small examples. You'll also learn how to guide an AI tool into producing helpful scaffolds rather than over-engineered solutions.

## Goals
By completing this activity, you will be able to...

- Use object-oriented design to break a feature request into core components.
- Represent and manipulate structured data using simple Python classes and containers.
- Apply algorithmic reasoning to tasks such as sorting, filtering, and validation.
- Use UML-style diagrams to think about system structure before writing code.
- Incorporate AI-produced code and diagrams as inputs to your workflow.

# Summary and Results
Add a short summary to the README (5–7 sentences) covering:
 [x] The core concept students needed to understand
 [x] Where students are most likely to struggle
 [x] Where AI was helpful vs misleading
 [x] One way you would guide a student without giving away the answer

The goal of this assignment was to help students get their first full experience of creating a small scale project with AI-assisted workflow. Students should understand that the goal of using AI is to enhance your workflow rather than replace it fully, by which I mean students should not simply tell the AI to do everything from the start with no knowledge of the structure of the program. Students are most likely to struggle with having the AI assist them in each phase of the plan and having the agent stay within the confines of what the requirements and phases are. What may end up happening is the agent doing more work that is outside the scope, or not following instructions properly. The AI was very helpful when it came to creating the scaffolding for the various different methods, as well as the actual creation of the UML design, it was very useful in that form. However, where it was misleading was even with the given context and prompt, for instance during the planning phase it implemented certain methods in the order that didn't make sense (child classes first before setting up the parent classes) which made the plan unclear at times. One way I would guide the student to completing this problem would be via telling them to make sure to use the AI in the proper mode for the phase thay they are in, and to refine their prompts to clearly state what it is that has to be done and what the agent should NOT be doing, such as working ahead without the student having a clear understanding of the foundation and structure of the program. 

Running initial tests with random objects to verify:
<img width="608" height="193" alt="image" src="https://github.com/user-attachments/assets/290afc2b-dd85-4dd8-b12f-9c8eddb2043f" />
Running tests using pytest:
<img width="1236" height="517" alt="image" src="https://github.com/user-attachments/assets/0d466236-f6e5-4de3-99e7-2f4f23d4fdd6" />
