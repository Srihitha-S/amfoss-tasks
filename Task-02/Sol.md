I created the Task-02 directory using mkdir -p Task-02 and navigated into it with cd Task-02 to set up a clean workspace.

I cloned the repository with git clone [https://github.com/Rufine777/ghost-in-the-machine.git](https://github.com/Rufine777/ghost-in-the-machine.git) and accessed it using cd ghost-in-the-machine.

I inspected the folder contents and structure using ls -la and find . -maxdepth 2 -type f | sort.

I checked the installed compiler and package manager versions with rustc --version and cargo --version.

I reviewed the project configurations by running cat Cargo.toml and cat Cargo.toml.bak.

I examined the repository history and branch graph using git log --oneline --all --decorate --graph.

I compiled the application and saved all build logs to a file using cargo build 2>&1 | tee initial-build.txt.
