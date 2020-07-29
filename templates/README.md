# Guidelines <!-- omit in toc --> 

The templates intended for Doxygen-based projects are located in the [with_doxygen](with_doxygen) folder. The templates for the projects that do not use Doxygen are located in the [without_doxygen](without_doxygen) folder.

You can also browse [our GitHub Pages](https://outoftardis.github.io/docs/) to see the output of these templates.

- [Functions and Classes](#functions-and-classes)
- [Enumeration Types](#enumeration-types)
- [Doxygen Groups](#doxygen-groups)
- [Main Page](#main-page)
- [Chapters](#chapters)
- [Glossary](#glossary)
- [Usage Guidelines](#usage-guidelines)
  - [The `contents` directive](#the-contents-directive)
  - [RST Headers](#rst-headers)
  - [Descriptions](#descriptions)

## Functions and Classes

Use the following templates to describe a particular function or a class:

- `Function Template` for projects [with Doxygen](with_doxygen/function_description_doxygen.tmpl) and [without Doxygen](without_doxygen/function_description_no_doxygen.tmpl)
- `Class Template` for projects [with Doxygen](with_doxygen/class_description_doxygen.tmpl) and [without Doxygen](without_doxygen/class_description_no_doxygen.tmpl)
- the template to describe a group of functions [with Doxygen](with_doxygen/functions_doxygen.tmpl)

---

An example of topic in the existing API Reference that could be documented using these templates: 

- [`add` function in oneMKL](https://software.intel.com/content/www/us/en/develop/documentation/oneapi-mkl-dpcpp-developer-reference/top/vector-mathematical-functions/vm-mathematical-functions/arithmetic-functions/add.html)

---

## Enumeration Types

If you need to document enumeration types (enums), use the following:

- the template to describe of a single enumeration type [with Doxygen](with_doxygen/enumerated_type_doxygen.tmpl) and [without Doxygen](without_doxygen/enumerated_type_no_doxygen.tmpl)
- the template to describe a list of enumeration types [with Doxygen](with_doxygen/enumerations_doxygen.tmpl) and [without Doxygen](without_doxygen/enumerations_no_doxygen.tmpl)

## Doxygen Groups

Use the [Group Template](with_doxygen/group_description_doxygen.tmpl) for Doxygen groups (modules).

## Main Page

Use the [template for the main page](index.tmpl) to create an overall structure of your API Reference documentation and provide users with clear navigation.

A note on this template:

- Use `:ref:` directive to provide links to chapters:
  
  - In your chapter RST file, you need to have `.. _chapter_name_link:` line at the top of the file.
  - Then you can use the following syntax to refer to that file from anywhere in your documentation:
  
        :ref:`chapter_name_link`

## Chapters

These templates are used to create a chapter of your API Reference documentation. For each template there is an underlying assumption that you already have a folder with RST files that you want to place within the same chapter.

If you want to have a chapter for examples, namespaces, classes, or doxygen groups, refer to the following templates: 

- [a chapter with examples](examples.tmpl) is created from the `examples` folder
- [a chapter with namespaces](namespaces.tmpl) is created from the `namespaces` folder
- [a chapter with Doxygen groups](groups.tmpl) is created from the `groups` folder

---

**Note:** We recommend using these folder names for consistency across libraries.

---


For API chapters that combine topics related to a particlar entity a type of object, use the following templates:

- [a simple one](chapter.tmpl) that only creates a table of contents from all the topics in a particular folder
- [the one with a hidden table of contents](chapter_complex.tmpl) that you can use to provide more information about the chapter's content in a form of a table

---

Examples of topics in existing API References that could be documented using these templates:

- [Iterators in oneTBB Developer Reference](https://www.intel.com/content/www/us/en/develop/documentation/onetbb-documentation/top/intel-174-oneapi-threading-building-blocks-onetbb-developer-reference/iterators.html)
- [VM Mathematical Functions in oneMKL Developer Reference](https://software.intel.com/content/www/us/en/develop/documentation/oneapi-mkl-dpcpp-developer-reference/top/vector-mathematical-functions/vm-mathematical-functions.html)

---

## Glossary

To create a glossary of terms used across your API Reference documentation, choose one of the following templates:

- [a simple glossary](glossary.tmpl) in which all terms are sorted alphabetically within a single list
- [a glossary with multiple sections](glossary_with_sections.tmpl) in which terms are split into thematic groups and sorted alphabetically within each one

These terms could be referenced from other topics in your API documentation using `:term:` directive.

---

## Usage Guidelines


### The `contents` directive

The `contents` directive produces a local table of contents. Omit it if you only have one subsection.

```
.. contents::
    :local:
    :depth: 1
```

### RST Headers

These templates use the following order of RST headers:

```
Level 1
=======

Level 2
*******

Level 3
-------
```

You should use RST Headers consistenly. If in your documentation you follow another order or another style, adjust these templates accordingly.

### Descriptions

If your Doxygen comments already contain extensive descriptions for functions, classes, and other entities, you do not need to copy these descriptions in RST as well.

For example, this is a part of the function template:

```
Description
***********

[The description of the function.]

API
***

.. doxygenfunction:: the name of the function
   :project: the name of the project
```

If `doxygenfunction` produces the description of the function that you find sufficient, omit the "Description" section.

```
API
***

.. doxygenfunction:: the name of the function
   :project: the name of the project
```