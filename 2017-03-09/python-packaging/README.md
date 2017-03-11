Included are the raw Jupyter Notebook slides and the built slides.

To build the slides, first install jupyter:

        pip install --user jupyter

Remember, don't run with escalated privileges (admin, sudo, etc)

Then run:

        jupyter nbconvert --to slides --post serve python_packaging.ipynb
