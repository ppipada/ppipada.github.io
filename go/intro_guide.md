# Golang introductory primer

- [Getting started links](#getting-started-links)
- [Project layout](#project-layout)
- [Naming conventions](#naming-conventions)
- [Code comments](#code-comments)
- [Generic guidelines](#generic-guidelines)
- [Testing](#testing)

## Getting started links

- [Installation](https://golang.org/doc/install)
- [How to Write Go code](https://golang.org/doc/code.html)
- [Tour of Go](https://tour.golang.org/welcome/1)
- [Effective Go](https://golang.org/doc/effective_go.html)
- [Reference documentation](https://golang.org/ref/spec)

## Project layout

- [Package Oriented Design](https://www.ardanlabs.com/blog/2017/02/package-oriented-design.html)
- [Style guide](https://rakyll.org/style-packages/)
- [Standard project layout](https://github.com/golang-standards/project-layout)

## Naming conventions

- [Standard](https://golang.org/doc/effective_go.html#names)
- [Package names go blog](https://blog.golang.org/package-names)
- [Go Talk](https://talks.golang.org/2014/names.slide#1)
- Few important rules:
  - Package names are singular, short, clear, lower case, with NO under_scores or mixedCaps.
  - Package content: Avoid stutter, simplify function names.
  - **Avoid** meaningless package names such as util, lib, common, or misc.
  - Function and variable names: The convention in Go is to use MixedCaps or mixedCaps rather than underscores to write multiword names.
  - Keep local variables short. Common variable/type combinations can use really short names. E.g: ‘i’ - for index, ‘r’ for reader, ‘b’ for buffer.
  - Acronyms should be all capitals: E.g: ServeHTTP and IDProcessor
- Validation:
  - Use [gofmt](https://golang.org/cmd/gofmt/) for autoformatting your code.
  - Use [golint](https://github.com/golang/lint). It would provide warnings related to naming and styling of go code.

## Code comments

- [Standard](https://golang.org/doc/effective_go.html#commentary)
- [Go Blog](https://blog.golang.org/godoc-documenting-go-code)
- Few important rules:
  - The convention is simple: to document a type, variable, constant, function, or even a package, write a regular comment directly preceding its declaration, with no intervening blank line. Godoc will then present that comment as text alongside the item it documents.
  - The comment is a complete sentence that begins with the name of the element it describes.
  - Comments on package declarations should provide general package documentation.
  - Use doc.go for packages that need large amount of introductory documentation.
- Swagger documentation for APIs: Can use code annotations as described at [GoSwagger](https://goswagger.io/use/spec.html)

## Generic guidelines

- Writing clear idiomatic Go code: [Effective Go](https://golang.org/doc/effective_go.html)
- Few important rules:
  - Dependencies should be passed explicitly. E.g: Pass logger explicitly.
  - Do NOT keep unused functions, constants, variables, types.
  - Do NOT use panics/recover as exception catching mechanism.
  - Avoid blanket error handling.
  - Avoid Misusing errors.
  - Avoid long functions. A function should not exhibit split personality.
  - Avoid global objects.
- Validation:
  - [Static check](https://github.com/dominikh/go-tools/tree/master/cmd/staticcheck)
  - [Race detector](https://golang.org/doc/articles/race_detector.html)
  - [Vet](https://golang.org/cmd/vet/)
  - CI: [GolangCI-Lint](https://github.com/golangci/golangci-lint)

## Testing

- Guidelines:
  - Go provides command `go test` for running tests in `\*\_test.go` files. It also has support for benchmarking.
  - `go test` has support for race detector using `- race`. Use it while running tests.
  - Test file containing component tests should specify the build constraints so that files can be identifiable whether it has Unit or Component or Integration test. The build constraints will be helpful to exclusively run only UT or Component tests or Integration tests. Command “go test ./… -tags UT” will only run unit test file and will exclude file component_test.go as it as define build constraint “!UT”
    - E.g File component_test.go `// +build !UT … some tests`
- Tools:
  - Package for boiler plate test code generation: [gotests](https://github.com/cweill/gotests)
    - This is available as a plugin in VSCode and other major IDEs.
  - Package for generating mocks for interfaces: [mock](https://github.com/golang/mock)
  - Package for mocking SQL: [go-sqlmock](https://github.com/DATA-DOG/go-sqlmock)
  - Test helpers: [testing](https://golang.org/pkg/testing/)
- Measuring code coverage
  - Go test can be configured `-cover` to collect code coverage information.
  - It does not have support to find code coverage in workflow testing. But can be [tweaked](https://www.elastic.co/blog/code-coverage-for-your-golang-system-tests) to collect coverage information by writing test for entry point function of binary.
