# Guidelines


## Terminology

To create a glossary of terms used across your API documentation, choose one of the following templates:

- [a simple glossary](terminology.tmpl) in which all terms are sorted alphabetically within a single list
- [a glossary with multiple sections](teminology_with_sections.tmpl) in which terms are split into thematic groups and sorted alphabetically within each one

These terms could be referenced from other topics in your API documentation using `:term:` directive.

## Function, class, and group definition

Use the following templates to describe a particular function, class, or a group:

- Function Template for projects [with Doxygen](function_description_doxygen.tmpl) and [without Doxygen](function_description_no_doxygen.tmpl)
- Class Template for projects [with Doxygen](class_description_doxygen.tmpl) and [without Doxygen](class_description_no_doxygen.tmpl)
- Group Template for projects [with Doxygen](group_description_doxygen.tmpl) and [without Doxygen](group_description_no_doxygen.tmpl)

## Chapters

These templates are used to create a chapter of your API documentation. For each template there is an underlying assumption that you already have a folder with RST files that you want to place within the same chapter.

If you want to have a chapter for examples, namespaces, classes, or doxygen groups, refer to the following templates: 

- [a chapter with examples](examples.tmpl) is created from the `examples` folder
- [a chapter with namespaces](namespaces.tmpl) is created from the `namespaces` folder
- [a chapter with doxygen groups](groups.tmpl) is created from the `groups` folder

**Note:** We recommend using these folder names for consistency across libraries.

For API chapters that combine topics related to a particlar entity a type of object, use the following templates:

- [a simple one](chapter.tmpl) that only creates a table of contents from all the topics in a particular folder
- [the one with a hidden table of contents](chapter_complex.tmpl) that you can use to provide more information about the chapter's content in a form of a table

Examples of topics in existing APIs that could be documented using these templates:

- [Iterators in oneTBB Developer Reference](https://www.intel.com/content/www/us/en/develop/documentation/onetbb-documentation/top/intel-174-oneapi-threading-building-blocks-onetbb-developer-reference/iterators.html)
- [VM Mathematical Functions in oneMKL Developer Reference](https://software.intel.com/content/www/us/en/develop/documentation/oneapi-mkl-dpcpp-developer-reference/top/vector-mathematical-functions/vm-mathematical-functions.html)