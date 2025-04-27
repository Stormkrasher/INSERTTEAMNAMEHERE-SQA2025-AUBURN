# Project Report

Lessons Learned: <br/>
- Learned that there is a difference between raw git hooks and the pre-commit framework
- Raw git hooks wound up being much more straightforward for us to implement and sort out locally in all operating environments
- You shouldn't hardcode real production Vault tokens in scripts
- After scrubbing the secrets, you have to remember to run a security checking software like bandit to check that your code has no vulnerabilities.
- Managing a shared GitHub repo helped improve our team collaboration skills, especially around resolving conflicts and maintaining project structure.

Activities: <br/>
- Initially went on a learning path trying to understand the pre-commit python package and how to set that up for our repository hook
- Working with different software like Vault and bandit to learn more about scrubbing secrets
- Developed a fuzz.py script that fuzzes five selected Python methods
- Randomized input was injected automatically to test for unexpected crashes
- forensics-style logging to five selected methods across the project
- 

