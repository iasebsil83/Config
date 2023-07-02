# ***Config : Just a Configuration file format***

**The simplest syntax to manage configuration files.**

&nbsp;

&nbsp;



## Content

This project is divided in different branches :
- [master](https://github.com/iasebsil83/config), general information about the configuration files.
- [command](https://github.com/iasebsil83/config/tree/command), command executable for reading/writing configuration files.
- [python](https://github.com/iasebsil83/config/tree/python), library for reading/writting configuration files in Python (Python3).
- [C     ](https://github.com/iasebsil83/config/tree/c), library for reading/writting configuration files in C.
- [JS    ](https://github.com/iasebsil83/config/tree/javascript), library for reading/writing configuration files in JavaScript.
- [Kotlin](https://github.com/iasebsil83/config/tree/kotlin), library for reading/writting configuration files in Kotlin.
- [Go    ](https://github.com/iasebsil83/config/tree/go), library for reading/writting configuration files in Go.
- [Lua   ](https://github.com/iasebsil83/config/tree/lua), library for reading/writting configuration files in Lua.

We are currently on branch **master**.

&nbsp;

&nbsp;



## I] Objective

This syntax is inspired on the basics of GNU/Linux configuration files.

Almost every GNU/Linux component we currently use nowadays uses its own configuration files with its own format.

&nbsp;

The objective behind Config is to fix **the simplest standard** of configuration files for both computers and users.

That means that the syntax must be **very light** (for user accessibility) and **restrictive** (for faster parsing).

&nbsp;

***NOTE:*** The default Config syntax should work with (almost) all present configuration files by default.

&nbsp;

&nbsp;



## II] Practical handbook

In this section, you will see all you have to know about Config in just a few lines.

### Special Variables

All the interpretation of the syntax is based on 3 special characters defined as follow :
```python
COMMENT    CHARACTER : '#'
LINE_END   CHARACTER : '\n' #line feed
SEPARATION CHARACTER : '\t' #tabulation
```
They are customizable in the settings of all Config programs/libraries.

***WARNING:*** Do not use alphanumerical characters or underscores in these special character sets or you may have surprises ! (a-z, A-Z, 0-9, _)

Also pay attention to the character used, especially because of its encoding.

&nbsp;

### Rules

Here are all the rules of the Config syntax (in 2 parts) :

```
PART 1 : LINES

-  1) Is considerated as a line every serie of character preceding a LINE_END character or EOF (end of file).

-  2) Empty lines are ignored.

-  3) Every COMMENT CHARACTER marks a comment section.
      Every characters from this one until the next LINE_END CHARACTER will be ignored.

-  4) Every line must be composed by a key-value pair as described here :
  - 4.b) The name of the current configuration field (1 byte minimum)
  - 4.c) One or more SEPARATION CHARACTER
  - 4.d) The value of the configuration field (1 byte minimum)



OPTION : ADDITIONAL_SPACES_ALLOWED (enabled by default)
  If enabled, spaces (' ') are tolerated everywhere on lines and they are ignored.
```

Pay attention to those rules : Every non-matching format will raise an error on parsing.

&nbsp;

&nbsp;

### Coloration

Last but not least, the file *config.nanorc* given is a syntax coloration file made for the [nano](https://www.nano-editor.org/) text editor.

To add it to your current nano configuration, use the following command:
```bash
sudo cp config.nanorc /usr/share/nano
```
There you go.

&nbsp;

&nbsp;


*Contact      : i.a.sebsil83@gmail.com*<br>
*Youtube      : https://www.youtube.com/user/IAsebsil83*<br>
*Repositories : https://github.com/iasebsil83*<br>

Let's Code ! &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;By I.A.
