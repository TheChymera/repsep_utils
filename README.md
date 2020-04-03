# RepSeP Utilities Package

Utilities for compiling and developing [RepSeP-style](https://youtu.be/WbjQYBuyKdk) articles, such as the [reference implementation](https://github.com/TheChymera/RepSeP).
The package contains generic boilerplate code for PythonTeX-interaction, as used by all RepSeP-style articles, as well as an executable file allowing single-script execution for development and debugging purposes.

## Usage

### Boilerplate Code

The PythonTeX boilerplate code needs to be linked in the document header e.g. by ensuring that the common header of the RepSeP document repository inputs it.

```console
user@host $ cd /path/to/RepSeP/document
user@host $ grep 'repsep/functions.py' common_header.tex
\input{/usr/share/repsep/functions.py}
```

### Development Aid

The executable code script can be used as in the following examples:

```console
user@host $ cd /path/to/RepSeP/document
user@host $ cd scripts
user@host $ repsep pdf myscript.py
```

Which will produce a figure script output named `myscript.pdf` in-place.
Supported scripts for this functionality are currently limited to figure-generating scripts, and supported output formats are `pdf`, `png`, and `pgf`.

## Installation

Depending on your preferred package manager you may choose one of the following methods:

#### Portage (e.g. on Gentoo Linux):
This package is available via Portage (the package manager of Gentoo Linux, derivative distributions, and installable on [any other Linux distribution](https://wiki.gentoo.org/wiki/Project:Prefix), or BSD) via the [Science Overlay](https://github.com/gentoo/sci).
Upon enabling the overlay, the package can be emerged:

```console
user@host $ emerge repsep_utils
```

#### Manual
If your distribution's package manager does not provide this package, you can install it manually, via:

```console
user@host $ git clone git@github.com:TheChymera/repsep_utils.git /home/youruser/repsep_utils
user@host $ su -
root@host # cp -rf /home/youruser/repsep_utils/repsep /usr/share
root@host # cp -rf /home/youruser/repsep_utils/bin/repsep /usr/bin/ 
```
