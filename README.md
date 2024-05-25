# A simple function call with ollama

This code is taking two **country** names and returns the **distance** between the related **capital cities**. The challenge was to make sure the post request to **ollama** was returning consistently a proper **json** - meeting the defined schema, actually putting a loop to retry if not.

This is a very simple **tinkering** , that fits into the use of functions to compose calls to ollama (llms).

## Check ollama

[https://ollama.com/](https://ollama.com/)

## Get ollama running on your machine (mac in my case)

Or using the docker image to run it almost anywhere.

### Install it

```bash
brew install ollama
```

### Run it

```bash
ollama serve
```

Now ollama runs on localhost:11434 , you can design any client to call on it

### Pull a model (my favorite one : mistral)

```bash
ollama pull mistral
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Try it

### With VS Code
Use the debug launch.json : you will get the invite to enter the first country, and the second.

### Command Line
**Examples:**

```bash
python main.py france italy
```

```bash
python main.py malawi people-republic-of-china
```

## Aknowledgements & References

Thank you for the guidance!

Matt Williams [https://www.youtube.com/watch?v=RXDWkiuXtG0](https://www.youtube.com/watch?v=RXDWkiuXtG0)
