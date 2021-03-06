# My Useful Scripts

Tiny little scripts I find useful for things I don't always remember how to do.

## Getting Started

Clone the repository.

```sh
git clone https://github.com/jmanuel1/useful-scripts
```

All scripts are in the `src` folder. They're separated into sub-folders by
operating system/platform. You should be able to run each script in its
respective OS without any extra dependencies. If that's not the case, extra
instructions will appear at the top of the script.

### Prerequisites

Windows scripts in `src/windows` will run on Windows. Linux scripts are in
`src/linux`.

Scripts for working with git are under `src/git`.

### Running a script

Largely, you should be able to just run a script from your terminal!

```
rem Windows example
src\windows\battery-report
rem A battery-report.html file appears in your current working directory.
```

Some scripts are written in Python.

## Support

To report issues, report them on
[Github](https://github.com/jmanuel1/useful-scrips/issues). Questions should
also be directed to the issue page.

## Roadmap

* Develop tests for scripts
* Add documentation for each script
* Remove unnecessary dependencies from scripts

## Contributing

If you edit or add a script, please help out and add tests and documentation.
New scripts should come with a justification of their usefulness. Remember to
keep scripts separated by OS, with as few dependencies as reasonably possible.

Mypy should be used for type checking of Python scripts. pycodestyle should be
used to check Python files, too.

## Authors

* **Jason Manuel** - *Initial work* - [jmanuel1](https://github.com/jmanuel1)

See also the list of
[contributors](https://github.com/jmanuel1/useful-scripts/contributors) who
participated in this project.

## Acknowledgments

* [Billie Thompson](https://github.com/PurpleBooth) for the [readme
  template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#file-readme-template-md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE)
file for details.
