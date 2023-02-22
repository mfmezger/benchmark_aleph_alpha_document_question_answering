# Benchmark Suite for Aleph Alpha Document Question Answering

## Prerequisites:
- You need Docker installed on your machine. (https://www.docker.com/) if you want to use the docker variant (recommended), if you want to execute the scripts locally you need to have Python 3.10 installed.


## Installation and preparation:
- Clone this repository
- first create a .env based on the .env.example file, you need to get your token from the aleph alpha api (app.aleph-alpha.com)
- Create a folder named input in the root of the project, and the folders pdf. If you exclusivly have pdfs as input put them in the pdf folder.

```input
├── images
└── pdf
    └── Put your PDFs here
```

- If you have also images please create a folder for images under the input folder, and create for every document a new folder and put it there, images from the same document should be in the same folder.
- In the class files you have to define the classes that you want to use. First define the number and then the aliases you want to accept as correct for the class, this must be the same classes that you name in your prompt files. (See next Point)
- You need to configure your prompt files. You can see some examples in the prompts folder: There you need to define first your prompt to allow for the classification of your documents. Please edit the file `PROMPT_Document_classification.txt`.
- In the other files please insert the concepts you want to be retrieved for the classes by changing the values in the brackets. -1 one is a fallback if non of the classes matched.


Now you have to decide if you want to run it locally in your environment or use the Dockerized Version. I would recommend the Docker Version

### Using Docker
- Run the following command: `docker-compose up --build`
- The output will be in the output folder

### Using your local run environment.
- Install the dependencies using poetry (poetry.org) to do this please do: `pip install poetry`
- then install the dependencies with: `poetry install`
- to run the application do: `poetry run python main.py`
