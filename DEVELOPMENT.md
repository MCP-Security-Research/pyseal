# Development TODOs

- code docs and reamde
- create a finalized readme file
- hook up to pypi for first release and set up github actions for publishing / releasing

- make it be able to work with multiple files at once
- ensure tool works with recursive functions and classes. basic test cases using pytest, and also cargo test???
- would a different approach other than ast be faster/more reliable/better?
- start adding tests to make sure tool continues to work
- remove code duplication (consider having one file processing tool, one parser, etc)
- also start to measure the performance of the tool
- use git api to track diffs? (other option is using my own .vurze metadata file)
- create test cases that ensure that code runs the same after the decorators have been added
- can my tool be attacked by adding soooooo many decorators? like should i create a limit?
- does my tool remove decorators that are automatically created? like does it clean up after itself properly?
- add .env to gitignore automatically???, check if a gitignore exists
- update to use ruff to lint python code
- make the tool conform to ruff linting standards
- update to use ____ to lint rust code
- have a code review from professor
