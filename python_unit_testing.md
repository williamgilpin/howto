# Unit Testing and Continuous Integration

*Instructions by William Gilpin for the [Computational Physics course at UT Austin](https://www.wgilpin.com/cphy/)*

The basic idea behind unit testing is to write short commands that check that every single method in your code is behaving as expected. The degree to which different methods are individually tested is the *coverage* of the tests. 

[Here](https://github.com/williamgilpin/exrepo) is an example repository matching the instructions below. Before you begin, you should have a project repository set up with a few functions that you want to test. The tutoral on [creating a repository](https://www.wgilpin.com/howto/howto_github.html) is a good place to start.

1. In your project repository, make a subdirectory `tests` that will hold your test files. My project directory looks like this:

```bash
	exrepo/
	├── exrepo
	│	├── core.py
	│	└── utils.py
	│
	├── tests
	│	├── test_core.py
	│	└── test_utils.py
```

2. The files `core.py` and `utils.py` represent example project files in this example. In your repository, these might represent the algorithm you are implementing, or an API. For example, here's `core.py` from my repository

```python
    #!/usr/bin/env python
    import random

    def random_walk(x0, nsteps=100):
        """
        Generate a random walk with nsteps steps starting at x0.

        Args:
            x0 (float): The starting point of the walk.
            nsteps (int): The number of steps to take.

        Returns:
            list: A list of floats representing the trajectory.
        """
        all_steps = [x0]
        for _ in range(nsteps):
            all_steps.append(all_steps[-1] + random.choice([-1, 1]))
        return all_steps

    def ornstein_uhlenbeck(x0, nsteps=100, theta=0.15, sigma=0.2):
        """
        Generate an Ornstein-Uhlenbeck process with nsteps steps starting at x0.

        Args:
            x0 (float): The starting point of the process.
            nsteps (int): The number of steps to take.
            theta (float): The rate of mean reversion.
            sigma (float): The volatility.

        Returns:
            list: A list of floats representing the trajectory.
        """
        all_steps = [x0]
        for _ in range(nsteps):
            next_step = all_steps[-1] + theta * (0 - all_steps[-1]) + sigma * random.gauss(0, 1)
            all_steps.append(next_step)
        return all_steps
```

3. We pair this file with a matching file in the subdirectory, which individually tests the individual functions within `core.py`. There are several packages in Python that can be used to write tests, but the built-in `unittest` package is a good place to start. Here's an example of a `tests/test_core.py` file that tests the functions in `core.py`.

```python
    #!/usr/bin/env python
    import os
    import unittest

    WORKING_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(WORKING_DIR)

    import sys

    sys.path.insert(1, os.path.join(WORKING_DIR, "exrepo"))
    from exrepo.core import random_walk, ornstein_uhlenbeck


    class TestModels(unittest.TestCase):
        """
        Tests integration and models
        """
        def test_random_walk(self):
            """
            Test generating a trajectory
            """
            traj = random_walk(0.1, 100)
            assert len(traj) == 100, "Generated trajectory has the wrong shape"
            
        def test_ornstein_uhlenbeck(self):
            """
            Test generating a trajectory with stochasticity
            """
            traj = ornstein_uhlenbeck(0.1, 100)
            assert len(traj) == 100, "Generated trajectory has the wrong shape"

    if __name__ == "__main__":
        unittest.main()
```

4. Consider a few properties of the tests we wrote above: We needed to import the `unittest` package, and we needed to import the functions we wanted to test from the `core.py` file. The latter required us to perform a relative import, in which we told the test file exactly where to find the `core.py` file. We then wrote a class that inherits from `unittest.TestCase`, and wrote test functions that start with the word `test`. We then used the `assert` statement to check that the output of the function matched our expectations. If the assertion fails, the test will fail. Another consideration when writing tests is that they should be small and fast. This is because you will want to run your tests frequently, to check that your code is still working as you make changes to your project.

4. From the top-level directory of our project, we can run all of our tests in the Terminal by running

```bash
    python -m unittest
```

If the tests fail, they will usually specify which test function. Otherwise, the tests will report "OK." If your tests depend on an imported package like numpy, then they will fail unless you run the tests in an environment in which the packages are installed.


## Continuous integration

Continuous integration (CI) is the practice of automatically running your unit tests every time you push a commit to your repository. This ensures that your tests are always up-to-date and passing.

In order to perform CI, you need to have a CI service set up. These are cloud-based services that monitor for when you push a commit to your remote repository. Upon detected an update, they clone the code, spin up a new virtual machine, and run your unit tests. If the tests pass, the CI service will report "OK." If the tests fail, the CI service will report the error and output of the failing tests. GitHub now has CI built-in, called GitHub Actions, that we will use for this example.

1. Create a `.github/workflows` directory in your repository. 

2. Within this directory, you can create a `.yml` file that specifies the CI workflow. Here is an example `.yml` file that runs the tests in the `tests` directory every time you push a commit to the `master` branch:

```yaml
    name: Run tests

    on:
      push:
        branches:
          - master

    jobs:
      test:
        runs-on: ubuntu-latest

        steps:
        - uses: actions/checkout@v2
        - name: Set up Python
          uses: actions/setup-python@v2
          with:
            python-version: '3.x'
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
        - name: Run tests
          run: python -m unittest
```

3. Check that the file structure of your repository now looks like this:

```bash
    exrepo/
    ├── exrepo
    │	├── core.py
    │	└── utils.py
    │
    ├── tests
    │	├── test_core.py
    │	└── test_utils.py
    │
    ├── .github
    │	└── workflows
    │		└── test.yml
```

4. 