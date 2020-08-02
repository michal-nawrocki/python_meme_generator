# python_meme_generator
Generate memes using Python

<p align="center">
  <img src="https://imgflip.com/s/meme/Futurama-Fry.jpg"/>
</p>

## Start guide

### How do I run this?
1. Make a `virutalenv` for this project:

        mkvirtualenv python_meme_generator

2. Install all requirements using `pip`:

        pip install -r requirements.txt

3. `cd` into the `meme_generator` direcotry:

        cd meme_generator

4. Run the program by running:

        python generator.py

### How to change the meme template?
To change the `meme template` you need to change the `MemeTemplate` enum
in `generator.py` to one that is available.

### How to change the text?
To change the `TOP TEXT` and `BOTTOM TEXT` you can do that in `generator.py`
by changing the `meme.write_text()` function.
 