Title: Table Styles and Alignment in Markdown
Date: 2020-08-20 18:33
Category: Features
Tags: Markdown, styles, tables
Summary: Using the Docutils styles for table styling & alignment in Markdown

[The table styles that kbits-theme supports for reStructuredText
tables]({filename}table-styles.rst) can also be applied to tables in Markdown
documents, but it takes some extra work.  You might expect to be able to attach
classes to tables with the [attribute list
extension](https://python-markdown.github.io/extensions/attr_list/), but
unfortunately, the syntax does not work with tables, and the author of the
Python Markdown package has no interest in fixing this ([see this
issue](https://github.com/Python-Markdown/markdown/issues/312)).  Instead, if
you want to create a table with a class in Markdown, you have to write out the
table in HTML.

So, if you want to create a table with the "booktabs" class, you have to write
out:

```html
<table class="booktabs">
    <thead>
        <!-- The header row needs to be placed in a thead so that the body rows
        are shaded appropriately. -->
        <tr>
            <th>Color</th>
            <th>Element</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Blue</td>
            <td>Water</td>
        </tr>
        <tr>
            <td>Green</td>
            <td>Earth</td>
        </tr>
        <tr>
            <td>Red</td>
            <td>Fire</td>
        </tr>
        <tr>
            <td>Yellow</td>
            <td>Air</td>
        </tr>
    </tbody>
</table>
```

and that gets you:

<table class="booktabs">
    <thead>
        <tr>
            <th>Color</th>
            <th>Element</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Blue</td>
            <td>Water</td>
        </tr>
        <tr>
            <td>Green</td>
            <td>Earth</td>
        </tr>
        <tr>
            <td>Red</td>
            <td>Fire</td>
        </tr>
        <tr>
            <td>Yellow</td>
            <td>Air</td>
        </tr>
    </tbody>
</table>

Changing the class to "borderless" gives you:

<table class="borderless">
    <thead>
        <tr>
            <th>Color</th>
            <th>Element</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Blue</td>
            <td>Water</td>
        </tr>
        <tr>
            <td>Green</td>
            <td>Earth</td>
        </tr>
        <tr>
            <td>Red</td>
            <td>Fire</td>
        </tr>
        <tr>
            <td>Yellow</td>
            <td>Air</td>
        </tr>
    </tbody>
</table>

There are also classes for aligning tables: ``align-left``, ``align-center``
and ``align-right``.  Let's see ``align-center``:

<table class="align-center">
    <thead>
        <tr>
            <th>Color</th>
            <th>Element</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Blue</td>
            <td>Water</td>
        </tr>
        <tr>
            <td>Green</td>
            <td>Earth</td>
        </tr>
        <tr>
            <td>Red</td>
            <td>Fire</td>
        </tr>
        <tr>
            <td>Yellow</td>
            <td>Air</td>
        </tr>
    </tbody>
</table>

Let's combine a border style with an alignment — `class="booktabs align-left"`:

<table class="booktabs align-left">
    <thead>
        <tr>
            <th>Color</th>
            <th>Element</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Blue</td>
            <td>Water</td>
        </tr>
        <tr>
            <td>Green</td>
            <td>Earth</td>
        </tr>
        <tr>
            <td>Red</td>
            <td>Fire</td>
        </tr>
        <tr>
            <td>Yellow</td>
            <td>Air</td>
        </tr>
    </tbody>
</table>

I think you can take it from here.
