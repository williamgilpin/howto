# Lab: Unit testing

The basic idea behind unit testing is to write short commands that check that every single method in your code is behaving as expected. The degree to which different methods are individually tested is the *coverage* of the tests. 

[Here](https://github.com/williamgilpin/exrepo) is an example repository matching these instructions

1. In your project repository, make a subdirectory `tests` that will hold your test files.

	repository/
	├── projectname
	│	├── core.py
	│	└── utils.py
	│
	├── tests
	│	├── test_core.py
	│	└── test_utils.py

2. The files `core.py` and `utils.py` represent example project files in this example. In your repository, these might represent the algorithm you are implementing, or an API. For example, here's `core.py`

```python
        #!/usr/bin/env python
        import random

        def random_walk(x0, nsteps=100):
            """
            Generate a random walk with nsteps steps starting at x0.
            """
            all_steps = [x0]
            for _ in range(nsteps):
                all_steps.append(all_steps[-1] + random.choice([-1, 1]))
            return all_steps

        def ornstein_uhlenbeck(x0, nsteps=100, theta=0.15, sigma=0.2):
            """
            Generate an Ornstein-Uhlenbeck process with nsteps steps starting at x0.
            """
            all_steps = [x0]
            for _ in range(nsteps):
                next_step = all_steps[-1] + theta * (0 - all_steps[-1]) + sigma * random.gauss(0, 1)
                all_steps.append(next_step)
            return all_steps
```
3. We pair this file with a matching files `tests/test_core.py` directory, which individually tests the individual functions within the original files. Notice the use of assert statements, which will cause the test to fail of a function does not behave as expected.

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

4. From the top-level directory of our project, we can run all of our tests in the Terminal by running

```
    python -m unittest
```

If the tests fail, they will usually specify which test function. Otherwise, the tests will report "OK." If your tests depend on an imported package like numpy, then they will fail unless you run the tests in an environment in which the packages are installed.