# A simple function call with ollama

This code is taking two **country** names and returns the **distance** between the related **capital cities**. The challenge was to make sure the post request to **ollama** was returning consistently a proper **json** - meeting the defined schema, actually putting a loop to retry if not.

This is a very simple **tinkering** , that fits into the use of functions to compose calls to ollama (llms).

## Output
```bash
main.py italy denmark 
Retrieved city info for italy: {'capital_city': 'Rome', 'latitude': 41.9028, 'longitude': 12.4964}
Retrieved city info for denmark: {'capital_city': 'Copenhagen', 'latitude': 55.6761, 'longitude': 12.5683}
City 1: {'capital_city': 'Rome', 'latitude': 41.9028, 'longitude': 12.4964}
City 2: {'capital_city': 'Copenhagen', 'latitude': 55.6761, 'longitude': 12.5683}
The distance between Rome and Copenhagen is 1530 km
```

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

## Improvements

The code will not recognize capitals and states. For example, run the following:

````bash
python main.py britanny corsica
python main.py tahiti nouvelle-calédonie
````

Have fun !!!


## Aknowledgements & References

Thank you for the guidance!

Matt Williams [https://www.youtube.com/watch?v=RXDWkiuXtG0](https://www.youtube.com/watch?v=RXDWkiuXtG0)
