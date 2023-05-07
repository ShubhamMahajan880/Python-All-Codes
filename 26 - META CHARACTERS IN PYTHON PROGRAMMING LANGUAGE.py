# Metacharacters in Python
Metacharacters are a very important concept of the regular expression that helps us to solve programming tasks using the Python regex module. In this tutorial,
we will learn about the metacharacters in Python or how we can use them. We will explain each metacharacter along with their short and simple example.
The prerequisite of learning metacharacters is that you should be familiar with the Python regular expression. If not, visit our Python regular expression tutorial.

# What are Metacharacters in Python?
Metacharacters are part of regular expression and are the special characters that symbolize regex patterns or formats.
Every character is either a metacharacter or a regular character in a regular expression. However, metacharacters have a special meaning.
They are not used to match any patterns but to define some rules to find the specific pattern in the statement.
Metacharacters are also known as operators, signs, or symbols.

Below is the list of regex metacharacters that we can use in Python.

Metacharacter	Description	Example
[] It represents the set of characters.	"[a-z]"
\  It represents the special sequence.	"\r"
.  It signals that any character is present at some specific place.	"Ja.v."
^  It represents the pattern present at the beginning of the string.	"^Java"
$  It represents the pattern present at the end of the string.	"point"
*  It represents zero or more occurrences of a pattern in the string.	"hello*"
+  It represents one or more occurrences of a pattern in the string.	"hello+"
{} The specified number of occurrences of a pattern the string.	"java{2}"
|  It represents either this or that character is present.	"java|point"
() Capture and group	(javatpoint)

[0-5] - It is same as the [012345].
[A-E] - It is same as the [ABCDE].
[a-d] - It is same as the [abcd].

# The \ Backslash Metacharacter
The backslash is used to escape the various characters including the metacharacters. It can also use to represent the special sequence.
For example - \d is used to find the any digit from 0-9.

Let's see another example - Suppose we want to search the match #a, where a is a characters followed by the # special character.

Below is the table of some special characters which is used with the \.

Characters	Description
\s	It is used to match a one white space character.
\S	It is used to match one non-white space character.
\0	It is used to match a NULL character.
\a	It is used to match a bell or alarm.
\d	It is used to match one decimal digit, which means from 0 to 9.
\D	It is used to match any non-decimal digit.
\n	It helps a user to match a new line.
\w	It is used to match the alphanumeric [0-9a-zA-Z] characters.
\W	It is used to match one non-word character
\b	It is used to match a word boundary.

"" The . Dot Metacharacter
The . dot metacharacter represents any string character apart from the newline character (\n). It can consist of any letters of uppercase or lowercase,
symbols such as dollar ($), pound (#), mark (!), question mark (?) or colons (:), digits 0 to 9, including whitespace.

"" The ^ Carrot Character
The carrot character returns the matching characters from beginning. For example - We want first five words from the string, we would use the caret (^) metacharacter. Let's understand the following example.

"" The caret ( ^ ) to match a pattern at the beginning of each new line
We can use the caret metacharacter only at the beginning of a string in a single line as it is not used in multiline matching.

However, with the help of the re.M flag, we can use caret with each new line.

"" The $ Dollor Metacharacter
This metacharacter is just opposite to the dollor ($) metacharacter. It matches at the end of the string. In the following example, we will match the ice-cream,
which is a present at the last of the string.

"" The * asterisk/star Metacharacter
It is one of the most popular and widely used metacharacters in regular expression patterns. The * asterisk represents the repetition 0 or more times as possible,
meaning it is a greedy repetition. The following example demonstrates the match of all the numbers using the asterisk (*) metacharacter.

"" The + Plus Metacharacter
It is another popular and widely used metacharacter in regular expression patterns. It represents the repetition of one or more times with as many repetitions.
It means it is a greedy repetition. In other words, there are 1 or more repetitions of the preceding expression.

"" The ? Question mark Metacharacter
The question mark ? metacharacter shows preceding character or expression to repeat either zero or one time only. The repetition is restricted to both ends.
In the following example, we will compare the ? with the * and + metacharacter.

The pattern to be matched is /d/d/d/d?. We include the four which means the match should be having at least four digits.

"" The Pipe (|) Metacharacter
The pipe (|) metacharacter represents the alternative option of matching characters.


