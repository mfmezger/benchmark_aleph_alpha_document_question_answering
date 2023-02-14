# Benchmark Suite

Prerequisites:
- You need Docker installed on your machine. (https://www.docker.com/)

How to use:
- Clone this repository
- first create a .env based on the .env.example file, you need to get your token from the aleph alpha api (app.aleph-alpha.com)
- Create a folder named input in the root of the project
input
├── images
│   └── Create a folder for your image
│       └── put each page of your document in the folder
└── pdf
    └── Put your PDFs here
- Put your PDFs in the data folder
- Run the following command: `docker-compose up --build`
- The output will be in the output folder
