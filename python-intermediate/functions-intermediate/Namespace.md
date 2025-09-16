We saw that every variable is actually an object. In Python, the term name refers to a variable, and therefore, to an object.

A **Namespace** is a collection of names. Different namespaces can co-exist at a given time but are completely isolated.

The outermost namesapce (scope) is a namespace containing all built-in names, created when the interpreter executes.

A more inner namespace (scope) is the global namespace of each module, and the innermost is the namespace (scope) of functions or classes.

As these namespaces are isolated, the same name may exist in different modules (and scopes) without ambiguity.
