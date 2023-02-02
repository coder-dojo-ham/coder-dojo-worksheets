# File types

Markdown is used to create the files.

Each project is a folder.

PDF's are created from the markdown files.
Github actions can create and store the generated PDF's.

## Project folder structure

Each project has a folder with the following structure:

```text
project_folder
├── <project-name>.md # main markdown file
├── <project-name>.py # main project python file - end point
├── <project-name>-<part number>.py # Files for intermediate steps. Should all be runnable.
├── screenshots # folder for screenshots
    ├── <screenshot-name>.png
├── <project-name>.pdf # generated pdf - do not check into git
├── licenses.md # licenses for any used libraries
├── requirements.txt # python requirements (try to stick to the coder dojo libraries)
```

## Writing style

- Use the [sheet template](./sheet_template.md) as a starting point.
    - A heading 2 (##) is used for each section. This will also paginate the PDF.
- Write in the first person. Use the words "we" or "you" to refer to the reader.
- Go step by step, with examples the reader can type. Don't get too mired in theory, aim for working fun examples that build on each other, with a little theory to explain what is happening after.
- Use screenshots or output to show what is happening.
- Drop a checkpoint after a few steps, so the reader can check they are on the right track. this should include:
    - A screenshot of the output
    - The code at that point
- Near the end of the sheet should be ideas/extensions to try out. These should be things that are not too hard to do, but will require some thinking. They should be things that the reader can do on their own, or with a little help from a mentor. Some code snippets and hints can be provided, but the reader should be able to work out the rest.
- The last page can be reference material - functions, libraries, etc. that are used in the sheet.

## Code swaps

Normally we should use the triple backtick for code sections. But where code will have deleted/replaced lines, use the following html embedded in the markdown:

```html
<pre><code>t.shape("circle")
t.color("blue")

<del>t.goto(0, 0)
t.stamp()
</del></code></pre>
```

## Creating PDF's with VS Code

Use the Markdown PDF extension to create PDF's from markdown files. This can be configured to Paginate, by going to the extension in the extensions tab, and clicking on the cog icon.
Look for the footer and header settings, and set the footer to:

```html
<div style="font-size: 9px; margin: 0 auto;"> <span class='pageNumber'></span> / <span class='totalPages'></span></div>
```

Then right click on the Markdown file and select "Markdown PDF: Export (pdf)".

## Creating PDF's with Pandoc
