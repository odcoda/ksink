# Custom Instructions for Building Tools

Inspired by [Simon Willison's approach](https://simonwillison.net/2024/Dec/19/one-shot-python-tools/).

## Python Tools Instructions

You write Python tools as single files. They always start with this comment:

```
# /// script
# requires-python = ">=3.12"
# ///
```

These files can include dependencies on libraries such as Click. If they do, those dependencies are included in a list like this one in that same comment (here showing two dependencies):

```
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
#     "sqlite-utils",
# ]
# ///
```

## HTML/JavaScript Tools Instructions

Never use React in artifacts—always plain HTML and vanilla JavaScript and CSS with minimal dependencies.

CSS should be indented with two spaces and should start like this:

```
<style>
* {
  box-sizing: border-box;
}
```

Inputs and textareas should be font size 16px. Font should always prefer Helvetica.

JavaScript should be two space indents and start like this:

```
<script type="module">
// code in here should not be indented at the first level
```

## Repository Structure

- `tools/` - All tools live in subfolders here
  - `html/` - HTML/CSS/JS single-page tools
  - `python/` - Python CLI tools (run with `uv run`)
- `index.html` - Main page listing all available tools
